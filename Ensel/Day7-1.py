# 문제 1 알고리즘 (문자열 + 구현)
# 문자열 주어질 때, 알파벳 문자만 남기고 모두 제거한 뒤, 소문자로 변환하여 문자열로 반환하시오.
s = "Hello! AI_Developer2025"

def keep_alpha_to_lower(s: str) -> str:
    result_chars = []   # 알파벳만 모아둘 리스트

    for ch in s:
        if ch.isalpha():    #  알파벳이면  True
            result_chars.append(ch.lower()) # 소문자로 바꿔서 저장

    # 리스트에 모은 문자들을 하나의 문자열로 합침
    return "".join(result_chars)

s = "Hello! AI_Developer2025"
print(keep_alpha_to_lower(s))   # helloaideveloper

# 문제 2 알고리즘(빈도 + 정렬)
# 정수 배열이 주어질 때, 가장 많이 등장한 숫자를 반환하시오.(등장 횟수가 같아면 더 큰 숫자 반환)

arr = [1, 3, 2, 3, 4, 2, 4, 4]

from collections import Counter

def most_frequent_numbers(arr):
    # Counter는 숫자의 등장 횟수를 자동으로 계산해준다.
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (x[1], x[0]))

    return sorted_items[0][0]

print(most_frequent_numbers(arr))

# 문제 3 머신러닝(회귀 + 평가)
# 다음 데이터로 단순 선형회귀 모델을 학습하고 MSE와 R2를 출력하시오
X = [[1], [2], [3], [4]]
y = [3, 5, 7, 9]


from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 입력 데이터 2차원 유지
X = [[1], [2], [3], [4]]
y = [3, 5, 7, 9]

# 모델 생성
model = LinearRegression()

# 모델 학습(x와 y의 관계)
model.fit(X, y)

# 예측
pred = model.predict(X)

mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)
print("예측값:", pred)