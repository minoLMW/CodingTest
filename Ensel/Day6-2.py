arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_numbers(arr):
    # Counter는 각자 숫자 등장 횟수를 자동으로 계산해준다.
    count = Counter(arr)

    # count.items() -> (숫자, 등장횟수)
    sorted_items = sorted(count.items(), key = lambda x: (-x[1], x[0]))
     