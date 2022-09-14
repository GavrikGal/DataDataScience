from typing import List, NamedTuple
from collections import Counter
from scratch.linear_algebra import Vector, distance


def majority_vote(labels: List[str]) -> str:
    """Исходит из того, что метки упорядочены
    от ближайшего до самой удаленной"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner   # уникальный победитель, поэтому вернуть его
    else:
        return majority_vote(labels[:-1])   # попытаться снова без самой удаленной


assert majority_vote(['a', 'b', 'c', 'b', 'a']) == 'b'


class LabeledPoint(NamedTuple):
    point: Vector
    label: str


def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:

    # Упорядочить помеченные точки от ближайшей до самой дальней
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point))
    # Отыскать метки для k ближайших
    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    # И дать им проголосовать
    return majority_vote(k_nearest_labels)
    