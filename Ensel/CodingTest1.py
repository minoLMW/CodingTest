# 파이썬 문법으로 답안 작성
# 함수 인자와 반환 값은 문제에 따라 적절하게 수정하여 제출

# 1부터 n까지 홀수의 합 - 반복문
def solution1(n):
    total = 0
    for i in range(1, n + 1, 2):
        total += i
    return total
# 1부터 n까지 홀수의 합 - 수학 공식
def solution2(n):
    # n 이하의 홀수 개수
    count = (n + 1) // 2
    return count * count

# 1부터 n까지 홀수의 합 - 재귀 호출
def solution3(n):
    if n <= 0:
        return 0
    if n % 2 == 1:
        return n + solution3(n - 2)
    else:
        return solution3(n - 1)

# 인자 값은 지원자가 적절하게 수정하여 제출
# 테스트
n = 10
print(solution1(n))
print(solution2(n))
print(solution3(n))