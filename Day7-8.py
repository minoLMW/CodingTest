# 문제 - 이미지 분류 (CNN 개념)
# 28x28 흑백 이미지를 입력으로 받아
# 10개 클래스로 분류하는 CNN 모델 구조를 작성하시오.

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

