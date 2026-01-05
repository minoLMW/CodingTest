arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_number(arr):
    
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[0][0]

print(most_frequent_number(arr))

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):
    unique_numbers = set(arr)

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))

arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_number(arr):
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[0][0]

print(most_frequent_number(arr))

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):
    unique_numbers = set(arr)

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))

arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_number(arr):
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[0][0]

print(most_frequent_number(arr))

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):
    unique_numbers = set(arr)

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))

arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_number(arr):
    count =Counter(arr)
    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    return sorted_items[0][0]

print(most_frequent_number(arr))

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):
    unique_numbers = set(arr)
    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))