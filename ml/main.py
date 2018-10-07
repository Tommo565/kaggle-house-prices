import pandas as pd
from processing import pre_processing, feature_engineering
from parameters import (
    infile, explore_out, model_out, none_list, na_list, quality_codes,
    quality_vars, features, scale_list, one_hot_list, skew_list
)

# Execution

df = pd.read_csv(infile)
df = pre_processing(df, none_list, na_list)
df = feature_engineering(
    df, quality_vars, quality_codes, explore_out, model_out, features,
    scale_list, one_hot_list, skew_list
)
print('Execution Complete. Have a nice Day =)')
