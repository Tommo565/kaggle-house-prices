import pandas as pd
from processing.import_files import *
from processing.pre_processing import *
from processing.feature_engineering import feature_engineering
from parameters.master import *

data = 'Test'

# Import
df_train, df_test = import_files(train_in, test_in)

# Pre Processing
df_train = pre_processing(df_train, none_list, na_list)
df_test = pre_processing(df_test, none_list, na_list)

# Feature Engineering

# Train data
if data == 'Train':
    print('Processing Train Data')
    feature_engineering(
        df_train, data, features, target,
        quality_vars, quality_codes, med_list, story_codes, exterior_codes,
        foundation_codes,
        scale_list, one_hot_list, log_trf_list, to_ordinal_list, label_list,
        train_model_out_linear, test_model_out_linear, train_model_out_tree,
        test_model_out_tree
    )

# Test data
if data == 'Test':
    df_test['SalePrice'] = 0
    print('Processing Test Data')
    feature_engineering(
        df_test, data, features, target,
        quality_vars, quality_codes, med_list, story_codes, exterior_codes,
        foundation_codes,
        scale_list, one_hot_list, log_trf_list, to_ordinal_list, label_list,
        train_model_out_linear, test_model_out_linear, train_model_out_tree,
        test_model_out_tree
    )


print('Execution Complete. Have a nice Day =)')
