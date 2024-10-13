import numpy as np


def calculate(products, cook):
    '''
    products - numpy matrix
    cook - list(n, m, k)
    '''

    total = np.dot(cook, products)
    
    total = np.ceil(total).astype(int)
    
    print("Молоко, литры:", total[0])
    print("Яйца, штуки:", total[1])
    print("Мука, кг:", total[2])

