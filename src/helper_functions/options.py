import warnings
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def options():
    '''
    Sets my preferred options for Jupyter
    '''

    warnings.filterwarnings('ignore')
    sns.set_style("whitegrid")
    pd.set_option('display.max_rows', 100)
    pd.set_option('display.max_columns', 100)
    pd.set_option('display.width', -1)
