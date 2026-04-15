# 문제 - 시계열 (이동 평균 + 개념)
# 다음 시계열 데이터에 대해 3일 이동 평균을 계산하시오.

data = [10, 12, 14, 13, 15, 18]

import pandas as pd

# 시계열 데이터
data = pd.Series([10, 12, 14, 13, 15, 18])

# 3일 이동 평균 계산
moving_avg = data.rolling(window=3).mean()

print(moving_avg)