'''
Помимо метрик из прошлой задачи для регрессии используют метрику R2
— коэффициент детерминации. Метрика показывает, какую долю изменчивости
целевого признака уловила модель. Вот формула для вычислений:
R2 = 1 −∑i=1N(yi −ŷi)2 ∑i=1N(y¯ − yi)2

где y¯ = 1 N ∑i=1Nyi — среднее истинное значение.

Используя только библиотеки numpy и math, реализуйте эту метрику на python.

Функция принимает на вход две выборки — истинные значения целевого признака
и предсказанные. Обратите внимание, что ответ зависит от порядка выборок — среднее вычисляется для истинных значений.
'''

import numpy as np


def R_metric(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)

    SSres = np.sum((y_true - y_pred) ** 2)
    SStot = np.sum((y_true - np.mean(y_true)) ** 2)
    R_metric = 1 - (SSres / SStot)

    return R_metric


y_true = list(map(float, input().split()))
y_pred = list(map(float, input().split()))

R_metric_value = R_metric(y_true, y_pred)
print(f"R2: {R_metric_value:.2f}")