# 완전탐색 패턴(Lv.1~2 절반이 이거)

# 예 : 배열에서 두 수의 합이 target인 경우 세게

def solution(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):  # i 다음부터
            if arr[i] + arr[j] == target:
                count += 1
    return count

# -> "모든 경우를 다 해보자" =완전탐색.노베이스한테 제일 중요한 패턴
