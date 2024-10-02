'''
Используя только библиотеки numpy и math,
реализуйте метрики регрессии на python.
Способ реализации (одна функция на каждую
метрику или все в одной) остается на ваше усмотрение.

Функция принимает на вход две выборки — истинные значения целевого признака и предсказанные.
'''

import numpy as np
import math


def regression_metrics(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    mse = np.mean((y_true - y_pred) ** 2)
    mae = np.mean(abs(y_true - y_pred))
    rmse = math.sqrt(mse)

    return mse, mae, rmse


y_true, y_pred = list(map(float, input().split())), list(map(float, input().split()))

mse, mae, rmse = regression_metrics(y_true, y_pred)
print(f"MSE: {mse:.2f}\nMAE: {mae:.2f}\nRMSE: {rmse:.2f}")