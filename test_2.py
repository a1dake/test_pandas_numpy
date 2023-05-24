import numpy as np


def find_intervals(intervals_1, intervals_2):
    final_intervals = []

    for interval_1 in intervals_1:
        for interval_2 in intervals_2:
            if interval_1[1] >= interval_2[0] and interval_1[0] <= interval_2[1]:
                final_intervals.append([max(interval_1[0], interval_2[0]), min(interval_1[1], interval_2[1])])

    return np.array(final_intervals)


specialist_1_intervals = np.array([[1, 2], [5, 8], [11, 15], [17, 18]])
specialist_2_intervals = np.array([[3, 6], [10, 15], [16, 21]])
intervals = find_intervals(specialist_1_intervals, specialist_2_intervals)

print(intervals)