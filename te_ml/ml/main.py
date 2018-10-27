import pandas as pd
from processing import pre_processing, feature_engineering, import_files
from parameters import (
    train_in, test_in, explore_out, train_model_out,
    test_model_out, none_list, na_list, quality_codes, simple_codes, 
    quality_vars, med_list, features, target, scale_list, one_hot_list,
    log_trf_list
)

data = 'Train'

# Import
df_train, df_test = import_files(train_in, test_in)

# Train data
if data == 'Train':
    print('Processing Train Data')
    df_train = pre_processing(df_train, none_list, na_list)
    df_train = feature_engineering(
        df_train, data, target, quality_vars, quality_codes, simple_codes, med_list, 
        explore_out, train_model_out, test_model_out, features, scale_list, 
        one_hot_list, log_trf_list
    )

# Test data
if data == 'Test':
    print('Processing Test Data')
    df_test = pre_processing(df_test, none_list, na_list)
    df_test = feature_engineering(
        df_test, data, target, quality_vars, quality_codes, simple_codes, med_list, 
        explore_out, train_model_out, test_model_out, features, scale_list, 
        one_hot_list, log_trf_list
    )

print('Execution Complete. Have a nice Day =)')
