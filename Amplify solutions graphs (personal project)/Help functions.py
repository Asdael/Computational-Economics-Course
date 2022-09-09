import numpy as np
#import matplotlib.pyplot as plt
import pandas as pd
#from compecon import NLP

def chart_range_generator(x1_initial, x1_final, x2_initial, x2_final, x1_density=100, x2_density=100):

    x1 = x1_initial

    epsilon_1 = abs(x1_initial-x1_final)/x1_density
    epsilon_2 = abs(x2_initial-x2_final)/x2_density

    df = pd.DataFrame([x1, x2_initial])
    df = pd.DataFrame(columns=['x_1', 'x_2'])

    for i in range(x1_density):

        x1 = x1 + epsilon_1

        x2 = x2_initial

        for j in range(x2_density):
            x2 += epsilon_2
            df.loc[len(df), df.columns] = x1, x2
    return df

a=chart_range_generator(0, 1, 0, 1)
print(a)