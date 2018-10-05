import warnings
import pandas as pd
from numpy import log1p
from helper_functions import one_hot_encoder, min_max_scaler
from .transformation_functions import *
warnings.filterwarnings('ignore')


def feature_engineering(
    df, quality_vars, quality_codes, explore_out, model_out, features,
    scale_list, one_hot_list
):
    '''Performs the feature engineering on the dataset'''

    # Convert numeric to categorical
    df['MSSubClass'] = df['MSSubClass'].astype(str)

    # Code the quality variables
    for item in quality_vars:
        df[item].replace(quality_codes, inplace=True)

    # Binning the target into bands for visualisation
    df['SalePriceBand'] = pd.qcut(
        df['SalePrice'],
        q=10,
        labels=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    )

    # Create new variables + remove unneeded ones
    df['HasPorch'] = df.apply(has_porch, axis=1)
    df['Remodelled'] = df.apply(is_remodelled, axis=1)
    df['PropertyAge'] = df.apply(property_age, axis=1)
    df['FullBath'] = df.apply(full_bath, axis=1)
    df['HalfBath'] = df.apply(half_bath, axis=1)
    df['TotalBath'] = df['FullBath'] + df['HalfBath']
    df['HasPool'] = df.apply(has_pool, axis=1)
    df['HasDeck'] = df.apply(has_deck, axis=1)
    df['TotalArea'] = (
        df['TotalBsmtSF'] + df['1stFlrSF'] + df['2ndFlrSF'] + df['GrLivArea']
    )
    df['YrSold'] = df['YrSold'] - 2005
    df['IsNew'] = df.apply(is_new, axis=1)
    df['IsPartial'] = df.apply(is_partial, axis=1)

    # Export a dataset for exploration
    df.to_csv(explore_out, index=False)

    # Limit to appropriate features
    df = df[features]

    # Remove outliers
    df = df[((df['TotalArea'] <= 10000))]

    # Scaling
    df = min_max_scaler(df, scale_list)

    # One-hot encoding
    df = one_hot_encoder(df, one_hot_list)

    # Log Transforms
    df['SalePriceLog'] = log1p(df['SalePrice'])

    # Export a dataset for modelling
    df.to_csv(model_out, index=False)

    return df
