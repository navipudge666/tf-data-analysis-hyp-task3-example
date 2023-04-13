import pandas as pd
import numpy as np
import scipy.stats as st

chat_id = 475225606 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    alpha = 0.04
    t_statistic, p_value = st.ttest_1samp(x, 500, alternative="two-sided")
    return p_value < 2*alpha and x.mean() > 500
