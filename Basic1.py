# 리스트/딕셔리

# 연습문제 1 (Easy)
# 숫자 리스트가 주어졌을 때, 가장 많이 등장한 숫자를 출력하세요.
# [1, 2, 2, 3, 3, 3] -> 3

from collections import Counter

arr = [1, 2, 2, 3, 3, 3]

def most_frequent_numver(arr):
    freq = Counter(arr)
    