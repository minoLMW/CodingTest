# Day 1~6 복습

# 문제 1 (빈도 계산 - 최빈값)
# 정수 배열이 주어질 때 가장 많이 등장한 숫자를 반환하시오. (등장 횟수가 같다면 더 작은 숫자 반환)

arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_number(arr):
    # Counter는 각자 숫자 등장 횟수를 자동으로 계산해준다.
    count = Counter(arr)

    # count.items() -> (숫자, 등장횟수)
    # 정렬기준:
    # (1) 등장횟수는 내림차순 (-x[1])
    # (2) 숫자는 오름차순 (x[0])
    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))

    # 가장 앞에 있는 값의 숫자만 반환
    return sorted_items[0][0]

print(most_frequent_number(arr))

# 문제 2 (리스트 전처리 - 중복 제거 + 정리)
# 정수 배열에서 중복을 제거하고 오름차순으로 정렬된 리스트를 반환하시오.

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):
    # set은 중복을 자동으로 제거해준다
    unique_numbers = set(arr)

    # set은 순서가 없기 때문에 정렬이 필요
    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))

# 문제 3 - 문자열 분석
# 문자열이 주어질 때 숫자/소문자/대문자의 개수를 각각 출력하시오.

s = "Hello123World"

def analyze_string(s):
    digit_count = 0     # 숫자 개수
    lower_count = 0     # 소문자 개수
    upper_count = 0     # 대문자 개수

    # 문자열은 한 글자씩 순회 가능
    for ch in s:
        if ch.isdigit():        # 숫자인 경우
            digit_count += 1
        elif ch.islower():      # 소문자인 경우
            lower_count += 1
        elif ch.isupper():      # 대문자인 경우
            upper_count += 1

    print("숫자:", digit_count)
    print("소문자:", lower_count)
    print("대문자:", upper_count)

analyze_string(s)

# 문제 4 - 조건 구현
# 정수 배열이 주어질 때 짝수는 그대로, 홀수는 2배로 만든 새 리스트를 반환하시오

arr = [1, 2, 3, 4, 5]

def transform_numbers(arr):
    result = []     # 결과를 저장할 리스트

    for num in arr:
        if num % 2 == 0:     # 짝수
            result.append(num)
        else:                # 홀수
            result.append(num * 2)
    
    return result

print(transform_numbers(arr))

# 문제 5 - 단순 회귀 모델 학습
# 다음 데이터로 단순 선형회귀 모델을 학습하시오.

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

from sklearn.linear_model import LinearRegression

# 입력 데이터 (2차원 형태 유지)
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# 1) 모델 생성
model = LinearRegression()

# 2) 모델 학습 (X와 y의 관계 학습)
model.fit(X, y)

# 3) 예측
pred = model.predict(X)

print("예측값:", pred)

# 문제 6 - 모델 평가
# 위 모델의 MSE와 R2를 계산하시오

from sklearn.metrics import mean_squared_error, r2_score

# MSE 계산
mse = mean_squared_error(y, pred)

# R2 계산
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)

# 문제 7 - CNN 모델 구조 작성
# 28x28 흑백 이미지를 입력으로 받아 10개 클래스로 분류하는 CNN 모델을 작성하시오

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# CNN 모델 생성
model = Sequential([
    # 1) 특징 추출 : 합성곱 층
    Conv2D(32, (3, 3,), activation='relu', input_shape=(28, 28, 1)),

    # 2) 크기 축소
    MaxPooling2D((2, 2)),

    # 3) 2D -> 1D 변환
    Flatten(),

    # 4) 분류
    Dense(10, activation='softmax')
])

model.summary()

# 문제 8 - 이동 평균(가장 기본)
# 다음 시계열 데이터에 대해 3일 이동 평균을 계산하시오.
data = [10, 12, 14, 13, 15, 18]

import pandas as pd

# 시계열 데이터
data = pd.Series([10, 12, 14, 13, 15, 18])

# 3일 이동 평균 계산
moving_avg = data.rolling(window=3).mean()

print(moving_avg)