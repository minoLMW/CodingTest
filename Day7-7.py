# 문제 - 머신러닝(단순 회귀)
# 다음 데이터를 사용해 단순 선형 회귀 모델을 학습하고,
# 입력 X=[[6]]에 대한 예측값을 출력하시오

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
pred = model.predict(X)

print("예측값:", pred)