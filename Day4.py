# Day 4 목표
# CNN이 왜 필요한지 말할 수 있게
# CNN의 구조 흐름을 머릿속에 고정
# 이미지 분류 기본 코드 틀을 재현 가능

# 오늘 미리 결론
# "모델 선능 튜닝" X
# "레이어 하나하나 수학적 의미" X
# "Conv -> Pool -> Flatten -> Dense" 흐름만 정확히 이해 O

# CNN이 필요한 이유(제일 중요)

# X: 이미지에 일반 선형회귀/ML을 쓰면?
# 픽셀 하나하나가 독립변수
# 공간 정보(위치 관계) 전부 깨짐

# CNN을 쓰는 이유
# 이미지의 '공간적 특징'을 유지하면서 특징을 자동으로 뽑아내기 위해서

# "모서리 -> 패턴 -> 형태"를 단계적으로 학습

# 시험용 한 줄
# "CNN은 이미지의 공간적 정보를 유지하면 특징을 추출하기 때문에 이미지 분류에 적합합니다."

# 입력 이미지
#   ↓
# Conv2D (특징 추출)
#   ↓
# ReLU (비선형성)
#   ↓
# MaxPooling (크기 축소)
#   ↓
# Flatten (1차원 변환)
#   ↓
# Dense (분류)

# 각 단계 역할
# Conv2D: 이미지에서 특징(엣지, 패턴) 추출
# ReLU: 음수를 제거해 비선형성 추가
# MaxPooling: 중요한 정보만 남기고 크기 축소
# Flatten: 2D 이미지를 1D 벡터로 변환
# Dense + Softmax: 클래스별 확률 출력

# 문제 - CNN 모델 구조 작성
# 28x28 흑백 이미지를 입력으로 받아 10개 클래스로 분류하는 CNN 모델을 작성하시오

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# CNN 모델 생성
model = Sequential([
    # 1) 특징 추출: 합성곱 층
    Conv2D(32, (3, 3,), activation='relu', input_shape=(28, 28, 1)),

    # 2) 크기 축소
    MaxPooling2D((2, 2)),

    # 3) 2D -> 1D 변환
    Flatten(),

    # 4) 분류
    Dense(10, activation='softmax')
])

model.summary()

# 코드 해설
# Conv2D(32, (3,3))
# -> 3x3 필터 32개로 특징 추출
# input_shape=(28,28,1)
# -> 흑백 이미지
# Faltten()
# -> Dense 층에 넣기 위한 변환
# softmax
# -> 다중 분류 확률 출력

# 시험용 한 줄 설명
# "합성곱 층으로 특징을 추출하고, 풀링으로 크기를 줄인 뒤 Flatten 후 Dense 층으로 분류했습니다."

# 자주 나오는 함정 질문

# 왜 CNN을 쓰나요?
# "이미지의 공간적 구조를 유지하며 특징을 자동으로 학습할 수 있기 때문입니다."

# Flatten은 왜 필요한가요?
# "Dense 층에 입력하기 위해 2차원 이미지를 1차원 벡터로 변환합니다."

# softmax는 언제 쓰나요?
# "클래스가 여러 개인 분류 문제에서 각 클래스의 확률을 출력할 때 사용합니다."

# 셀프 체크

# CNN 전체 흐름을 말할 수 있나?
# "입력 이미지를 합성곱 층에서 특징을 추출하고, 풀링 층에서 크기를 줄인 뒤 Flatten으로 1차원으로 변환해서 Dense 층에서 분류합니다."

# Conv / Pool / Flatten 역할 설명 가능?
# "Conv는 이미지에서 특징을 추출하고, Pooling은 중요한 정보만 남기면서 크기를 줄이며, Flatten은 2차원 특징 맵을 1차원 벡터로 변환합니다."

# softmax 쓰는 이유 말할 수 있나?
# "다중 클래스 분류에서 각 클래스에 대한 확률을 출력하기 위해 softmax를 사용합니다."

