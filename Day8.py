# 알고리즘 (문자열 + 구현)
# 문자열 주어질 때, 알파벳 문자만 남기고 모두 제거한 뒤, 소문자로 변환하여 문자열로 반환하시오.
s = "Hello! AI_Developer2025"

def keep_alpha_to_lower(s: str) -> str:
    result_chars = []    # 알파벳만 모아둘 리스트

    for ch in s:
        if ch.isalpha():
            result_chars.append(ch.lower())
            # 소문자로 바꿔서 저장

    # 리스트에 모은 문자들을 하나의 문자열로 합침
    return "".join(result_chars)

# 문제 알고리즘(빈도 + 정렬)
# 정수 배열이 주어질 때, 가장 많이 등장한 숫자를 반환하시오.(등장 횟구가 같다면 더 큰 숫자 반환)

arr = [1, 3, 2, 3, 4, 2, 4, 4]

from collections import Counter

def most_frequent_numbers(arr):
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], -x[0]))

    return sorted_items[0][0]

# 문제 머신러닝(회귀 + 평가)
# 다음 데이터로 단순 선형회귀 모델을 학습하고 MSE와 R2를 출력하시오
X = [[1], [2], [3], [4], [5]]
y = [3, 5, 7, 9]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 예측
pred = model.predict(X)

mse = mean_squared_error(y, pred)
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)
print("예측값", pred)

# 문제 - 이미지 분류(CNN 개념)
# 28x28 흑백 이미지를 입력으로 받아
# 10개 클래스로 분류하는 CNN 모델 구조를 작성하시오

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential [(
    #특징추출
    Conv2D(32, (3, 3,), activation='relu', input_shape=(28, 28, 1)),

    # 크기 축소
    MaxPooling2D((2, 2)),

    # 2D -> 1D 변환
    Flatten(),

    # 분류
    Dense(10, activation='softmax')
)]

model.summary()

# 문제 - 시계열 (이동 평균 + 개념)
# 다음 시계열 데이터에 대해 3일 이동 평균을 계산하시오.

data = [10, 12, 14, 13, 15, 18]

import pandas as pd

# 시계열 데이터
data = pd.Series([10, 12, 14, 13, 15, 18])

# 3일 이동 평균
moving_avg = data.rolling(window=3).mean()

print(moving_avg)

# 문제 - 시계열 (이동 평균 + 개념)
# 다음 시계열 데이터에 대해 3일 이동 평균을 계산하시오.

data = [10, 12, 14, 13, 15, 18]

import pandas as pd

# 시계열 데이터
data = pd.Series([10, 12, 14, 13, 15, 18])

# 3일 이동 평균
moving_avg = data.rolling(window=3).mean()

print(moving_avg)