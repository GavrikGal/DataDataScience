from typing import List
import random
import tqdm
from scratch.linear_algebra import distance, Vector
from scratch.statistics import mean


def random_point(dim: int) -> Vector:
    return [random.random() for _ in range(dim)]


def random_distances(dim: int, num_pairs: int) -> List[float]:
    return [distance(random_point(dim), random_point(dim))
            for _ in range(num_pairs)]


dimensions = range(1, 101)

avg_distances = []
min_distances = []

random.seed(0)
for dim in tqdm.tqdm(dimensions, desc="Проклятие размерности"):
    distances = random_distances(dim, 10000)    # 10 000 произвольных пар
    avg_distances.append(mean(distances))       # Отследить среднее
    min_distances.append(min(distances))        # Отследить среднее

min_avg_ratio = [min_dist / avg_dist
                 for min_dist, avg_dist in zip(min_distances, avg_distances)]
