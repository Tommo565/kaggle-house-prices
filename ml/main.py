import pandas as pd
from processing import pre_processing, feature_engineering, import_files
from parameters import (
    train_in, test_in, explore_out, model_out, none_list, na_list,
    quality_codes, quality_vars, features, scale_list, one_hot_list,
    skew_list
)

# Execution

df_train, df_test, df = import_files(train_in, test_in)
df = pre_processing(df_train, none_list, na_list)
df = feature_engineering(
    df, quality_vars, quality_codes, explore_out, model_out, features,
    scale_list, one_hot_list, skew_list
)
print('Execution Complete. Have a nice Day =)')
