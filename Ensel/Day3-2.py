X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()

model.fit(X, y)

pred = model.predict(X)

print("예측값:", pred)

from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y, pred)

r2 = r2_score(y, pred)

print("MSE:", mse)
print("R2:", r2)
