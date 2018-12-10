import pandas as pd
from parameters.master import *
from helper_functions import build_ordinal, get_ordinal
from processing.pre_processing import *
from processing.feature_engineering import feature_engineering


# Import
df_train = pd.read_csv(train_in)
df_train['Train'] = 1
df_test = pd.read_csv(test_in)
df_test['Test'] = 1

# Concat the datasets & export
df = pd.concat([df_train, df_test])
df.to_csv(train_test_raw_out, index=False)

# Pre-processing
df = pre_processing(
    df, drop_vars, none_vars, na_vars, mode_vars, med_vars, to_string_vars
)

# Feature Engineering
df = feature_engineering(
    df, target, quality_vars, quality_codes, med_vars, get_ordinal,
    ordinal_vars, num_exclude_vars, one_hot_vars,
    train_model_out, test_model_out, all_model_out
)

print('Execution Complete. Have a nice Day =)')
