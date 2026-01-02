# Day 3
# 단순 선형회귀가 뭘 하는 모델인지 말할 수 있게
# sklearn(사이킷런) 코드 구조에 익숙해지기
# MSE / R2를 보고 "좋다/나쁘다" 판단 가능

# 오늘 미리 결론(안심부터)
# 오늘 내용은 "이하하면 쉽고, 모르면 막연한" 파트
# 지금부터는 문제 -> 코드 -> 해석 순서로 진행

# 개념 정리(시험에 필요한 만큼만)
# 1) 단순 선형회귀란?
# 하나의 입력(x)으로 하나의 출력(y)을 예측하는 모델

# 형태
# y = wX + b
# X: 입력 데이터, y: 예측 대상, w: 기울기 b: 절편
# "직선을 하나 그ㅡ어서 데이터에 맞춘다"라고 생각하면 충분

# 2) 모델 학습이란?
# w, b를 자동으로 찾는 과정
# 실제 y와 예측 y의 차이가 가장 작아지도록 조정

# 3) 모델 평가란?
# "이 직선, 얼마나 잘 맞았나?"를 숫자로 보는 것
# 오늘 쓸 건 딱 2개

# MSE(Mean Squared Error)
# 오차의 평균
# 작을수록 좋음

# R2 (결정계수)
# 0 ~ 1 사이
# 1에 가까울수록 좋음

# 문제 1 - 단순 회귀 모델 학습
# 다음 데이터로 단순 선형회귀 모델을 학습하시오.
X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# 접근 사고 과정
# 1) 모델 생성
# 2) 데이터로 학습
# 3) 예측

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

# 문제 2 - 모델 평가
# 위 모델의 MSE와 R2를 계산하시오.

# 접근
# 실제 값 vs 예측 값 비교
# sklearn 평가 함수 사용

from sklearn.metrics import mean_squared_error, r2_score

# MSE 계산
mse = mean_squared_error(y, pred)

# R2 계산
r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)

# 결과 해석 (이게 중요
# MSE = 0.0
# R2 = 1.0
# 완벽한 직선 관계

# 시험용 한 줄 해석
# "MSE가 0이고, R2가 1이라서 모델이 데이터를 완벽하게 설명합니다."

# 오늘 반드시 기억할 코드 구조
# 회기 기본 틀(암기수준)
# model = LinearRegression()
# model.fit(X, y)
# pred = model.predict(X)

# 평가 기본 틀
# mean_squared_error(y, pred)
# r2_score(y, pred)

# 셀프 체크
# 1) 단순 선형회귀가 뭘 하는 모델인가?
# 2) fit과 predict의 역할 차이는?
# 3) MSE와 R2는 클수록/작을수록 좋은가?

# 위 코드 안 보고 작성해보기
# 결과 보고 말로 설명해보기 - "이 결과는 왜 이렇게 나왔지?"