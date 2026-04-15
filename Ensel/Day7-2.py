arr = [4, 1, 2, 2, 3, 3, 3, 4, 4]

from collections import Counter

def most_frequent_numbers(arr):
    count = Counter(arr)

    sorted_items = sorted(count.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[0][0]

print(most_frequent_numbers(arr))

arr = [5, 3, 1, 3, 5, 2]

def unique_sorted_list(arr):

    unique_numbers = set(arr)

    sorted_numbers = sorted(unique_numbers)

    return sorted_numbers

print(unique_sorted_list(arr))

s = "Hello123World"

def analyze_string(s):
    digit_count = 0
    lower_count = 0
    upper_count = 0

    for ch in s:
        if ch.isdigit():
            digit_count += 1
        elif ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1

    print("숫자:", digit_count)
    print("소문자:", lower_count)
    print("대문자:", upper_count)

analyze_string(s)

arr = [1, 2, 3, 4, 5]

def transform_numbers(arr):
    result = []

    for num in arr:
        if num % 2 == 0:
            result.append(num)
        else:
            result.append(num * 2)

    return result

print(transform_numbers(arr))

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 예측
pred = model.pridict(X)

print("예측값:", pred)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, pred)

r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential[(
    # 특징 추출: 합성곱
    Conv2D(32, (3, 3,), activation='relu', input_shape=(28, 28, 1)),
    
    # 크기 축소
    MaxPooling2D((2, 2)),

    # 2D -> 1D 변환
    Flatten(),

    # 분류
    Dense(10, activation='softmax')
)]

model.summary()

data = [10, 12, 14, 13, 15, 18]

import pandas as pd

data = pd.Series([10, 12, 14, 13, 15, 18])

moving_avg = data.rolling(window=3).mean()

s = "Hello! AI_Developer2025"

def keep_alpha_to_lower(s: str) -> str:
    result_chars= []

    for ch in s:
        if ch.isalpha():
            result_chars.append(ch.lower())

    return "".join(result_chars)

print(keep_alpha_to_lower(s))