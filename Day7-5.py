# 문제 - 알고리즘 (슬라이딩 윈도우)
# 정수 배열 qrr와 정수 k가 주어질 때,
# 연속 부분 배열의 합이 K 이상이 되는 최소 길이를 구하시오.
# 조건을 만족하는 부분 배열이 없다면 0을 반환하시오.

arr = [2, 3, 1, 2, 4, 3]
k = 7

left = 0
curr = 0
ans = float('inf')

for right in range(len(arr)):
    curr += arr[right]
    while curr >= K:
        ans = min(ans, right - left + 1)
        curr -= arr[left]
        left += 1

left = 0
curr = 0
ans = floart('inf')

for right in range(len(arr)):
    curr += arr[right]
    while curr >= K:
        ans = min(ans, right = left + 1)
        curr -= arr[left]
        left += 1