from datetime import datetime
from typing import List, NamedTuple, Dict
from collections import defaultdict
from dateutil.parser import parse
import csv


class StockPrice(NamedTuple):
    symbol: str
    date: datetime.date
    closing_price: float

    def is_high_tech(self) -> bool:
        """Это класс, и поэтому мы также можем добавлять методы"""
        return self.symbol in ['MSFT', 'GOOG', 'FB', 'AMZN', 'AAPL']


data: List[StockPrice] = []

with open('../stocks.csv', 'r') as f:
    colon_reader = csv.DictReader(f, delimiter=',')
    for dict_row in colon_reader:
        date = parse(dict_row["Date"]).date()
        symbol = dict_row["Symbol"]
        closing_price = float(dict_row["Close"])
        data.append(StockPrice(symbol, date, closing_price))


# Собрать цены по символу
prices: Dict[str, List[StockPrice]] = defaultdict(list)

for sp in data:
    prices[sp.symbol].append(sp)

prices = {symbol: sorted(symbol_prices)
          for symbol, symbol_prices in prices.items()}


def pct_change(yesterday: StockPrice, today: StockPrice) -> float:
    return today.closing_price / yesterday.closing_price - 1


class DailyChange(NamedTuple):
    symbol: str
    date: datetime.date
    pct_change: float


def day_over_day_changes(prices: List[StockPrice]) -> List[DailyChange]:
    """Предполагает, что цены только для одной акции и упорядочены"""
    return [DailyChange(symbol=today.symbol,
                        date=today.date,
                        pct_change=pct_change(yesterday, today))
            for yesterday, today in zip(prices, prices[1:])]


all_changes = [change
               for symbol_prices in prices.values()
               for change in day_over_day_changes(symbol_prices)]

max_change = max(all_changes, key=lambda change: change.pct_change)
print(max_change)

min_change = min(all_changes, key=lambda change: change.pct_change)
print(min_change)

changes_by_month: List[DailyChange] = {month: [] for month in range(1, 13)}

for change in all_changes:
    changes_by_month[change.date.month].append(change)

avg_daily_change = {
    month: sum(change.pct_change for change in changes) / len(changes)
    for month, changes in changes_by_month.items()
}


print(avg_daily_change)
print(max(avg_daily_change.values()))
