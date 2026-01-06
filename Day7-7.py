# 문제 - 머신러닝(단순 회귀)
# 다음 데이터를 사용해 단순 선형 회귀 모델을 학습하고,
# 입력 X=[[6]]에 대한 예측값을 출력하시오

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

# 모델 생성
model = LinearRegression()

# 모델 학습
model.fit(X, y)

# 예측
pred = model.predict([[6]])


print("예측값:", pred[0])

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, pred)

r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2", r2)
