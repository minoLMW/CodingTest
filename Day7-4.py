# 문제
# 정수 배열 arr가 주어질 때,
# 가장 많이 등장한 숫자를 반환하시오.
# 단, 등장 횟수가 같다면 더 큰 숫자를 반환한다.

arr = [1, 3, 2, 3, 4, 2, 4, 4]

from collections import Counter

def most_frequent_numbers(arr):
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x:(-x[1], -x[0]))
    return sorted_items[0][0]