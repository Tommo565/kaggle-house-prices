import pandas as pd
from processing.import_files import *
from processing.pre_processing import *
from processing.feature_engineering_linear import *
from processing.feature_engineering_tree import *
from parameters.master import *

data = 'Train'

# Import
df_train, df_test = import_files(train_in, test_in)
df_train = pre_processing(df_train, none_list, na_list)
df_test = pre_processing(df_test, none_list, na_list)

# Train data
if data == 'Train':

    # Linear
    # print('1. Processing Linear Train Data')
    # df_train_linear = feature_engineering_linear(
    #     df_train, data, target, quality_vars, quality_codes, simple_codes,
    #     med_list, explore_out_linear, train_model_out_linear,
    #     test_model_out_linear, linear_features, scale_list, one_hot_list,
    #     log_trf_list
    # )

    # Tree
    print('2. Processing Tree Train Data')
    df_train_tree = feature_engineering_tree(
        df_train, data, target, quality_vars, quality_codes, simple_codes,
        med_list, label_list, explore_out_tree, train_model_out_tree,
        test_model_out_tree, tree_features
    )

# Test data
if data == 'Test':

    print('1. Processing Train Data')
    df_train = pre_processing(df_train, none_list, na_list)
    df_train_linear = feature_engineering_linear(
        df_train, data, target, quality_vars, quality_codes, simple_codes,
        med_list, explore_out_linear, train_model_out_linear,
        test_model_out_linear, linear_features, scale_list, one_hot_list,
        log_trf_list
    )

    print('2. Processing Test Data')

    df_test_linear = feature_engineering_linear(
        df_test, data, target, quality_vars, quality_codes, simple_codes,
        med_list, explore_out_linear, train_model_out_linear,
        test_model_out_linear, linear_features, scale_list, one_hot_list,
        log_trf_list
    )


print('Execution Complete. Have a nice Day =)')
