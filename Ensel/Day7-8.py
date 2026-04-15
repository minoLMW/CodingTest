# 문제 - 이미지 분류 (CNN 개념)
# 28x28 흑백 이미지를 입력으로 받아
# 10개 클래스로 분류하는 CNN 모델 구조를 작성하시오.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential ([
    # 특징 추출: 합성곱 층
    Conv2D(32, (3, 3,), activation='relu', input_shape=(28, 28, 1)),

    # 크기 축소
    MaxPooling2D((2, 2)),

    # 2D -> 1D 변환
    Flatten(),

    # 분류
    Dense(10, activation='softmax')
])

model.summary()