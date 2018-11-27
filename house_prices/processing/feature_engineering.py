import warnings
import pandas as pd
from helper_functions import (
    one_hot_encoder, min_max_scaler, log_transform, to_ordinal_med,
    get_ordinal_values, label_encoder
)
from .transformation_functions import *
warnings.filterwarnings('ignore')


def feature_engineering_linear(
    df, data, features, target,
    scale_list, one_hot_list, log_trf_list, to_ordinal_list,
    train_model_out_linear, test_model_out_linear
):
    '''
    Performs feature engineering specific to linear models
    '''

    if data == 'Train':

        # Convert Categorical to Ordinal
        for feature in to_ordinal_list:
            to_ordinal_med(df, feature, target)
            df['{}_ordinal'.format(feature)] = (
                df['{}'.format(feature)].replace(get_ordinal_values(feature))
            )

    if data == 'Test':

        # Apply Categorical to Ordinal Conversion
        for feature in to_ordinal_list:
            df['{}_ordinal'.format(feature)] = (
                df['{}'.format(feature)].replace(get_ordinal_values(feature))
            )

    df = min_max_scaler(df, scale_list)
    df = one_hot_encoder(df, one_hot_list)
    df = log_transform(df, log_trf_list)

    if data == 'Train':
        df.to_csv(train_model_out_linear, index=False)
        print('Train model dataset created: {}'.format(train_model_out_linear))

    if data == 'Test':
        df.to_csv(test_model_out_linear, index=False)
        print('Test model dataset created: {}'.format(test_model_out_linear))

    return df


def feature_engineering_tree(
    df, data, features,
    label_list,
    train_model_out_tree, test_model_out_tree
):
    '''
    Performs feature engineering specific to tree models
    '''

    # Label encoding
    df = label_encoder(df, label_list)

    if data == 'Train':
        df.to_csv(train_model_out_tree, index=False)
        print('Train model dataset created: {}'.format(train_model_out_tree))

    if data == 'Test':
        df.to_csv(test_model_out_tree, index=False)
        print('Test model dataset created: {}'.format(test_model_out_tree))

    return df


def feature_engineering(
    df, data, features, target,
    quality_vars, quality_codes, med_list, story_codes, exterior_codes,
    foundation_codes,
    scale_list, one_hot_list, log_trf_list, to_ordinal_list, label_list,
    train_model_out_linear, test_model_out_linear, train_model_out_tree,
    test_model_out_tree
):
    '''
    Wrapper function for feature engineering
    '''

    # Limit to useful features only
    df = df[features]

    # Convert numeric to categorical
    df['MSSubClass'] = df['MSSubClass'].astype(str)

    # Code the quality variables
    for item in quality_vars:
        df[item].replace(quality_codes, inplace=True)

    # Fills na with median values
    for item in med_list:
        df[item].fillna(df[item].median(), inplace=True)

    # Code the HouseStyle variable
    df['Stories'] = df['HouseStyle'].replace(story_codes)

    # Create new variables
    df['HasPorch'] = df.apply(has_porch, axis=1)
    df['IsRemodelled'] = df.apply(is_remodelled, axis=1)
    df['PropertyAge'] = df.apply(property_age, axis=1)
    df['FullBath'] = df.apply(full_bath, axis=1)
    df['HalfBath'] = df.apply(half_bath, axis=1)
    df['TotalBath'] = df['FullBath'] + (df['HalfBath'] * 0.5)
    df['HasPool'] = df.apply(has_pool, axis=1)
    df['HasDeck'] = df.apply(has_deck, axis=1)
    df['YrSold'] = df['YrSold'] - 2005
    df['IsNew'] = df.apply(is_new, axis=1)
    df['IsPartial'] = df.apply(is_partial, axis=1)
    df['IsCulDeSac'] = df.apply(is_cul_de_sac, axis=1)

    # Combination Variables
    df['OverallGrade'] = df['OverallQual'] * df['OverallCond']
    df['ExterGrade'] = df["ExterQual"] * df["ExterCond"]
    df['TotalArea'] = (
        df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF'] + df['GrLivArea']
    )
    df['CoreArea'] = df['GrLivArea'] + df['TotalBsmtSF']

    df_l = df.copy()
    df_t = df.copy()

    df_l = feature_engineering_linear(
        df_l, data, features, target,
        scale_list, one_hot_list, log_trf_list, to_ordinal_list,
        train_model_out_linear, test_model_out_linear
    )

    df_t = feature_engineering_tree(
        df_t, data, features,
        label_list,
        train_model_out_tree, test_model_out_tree
    )

    return df_l, df_t
