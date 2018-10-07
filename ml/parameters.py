train_in = '../data/input_data/train.csv'
test_in = '../data/input_data/test.csv'

infile = '../data/transformed_data/train_preprocessed.csv'
explore_out = '../data/transformed_data/explore.csv'
model_out = '../data/transformed_data/model.csv'

none_list = [
    'Alley', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'BsmtQual', 'Fence', 'FireplaceQu', 'GarageCond', 'GarageFinish',
    'GarageQual', 'GarageType', 'GarageYrBlt', 'MiscFeature', 'PoolQC',
    'MasVnrType'
]
na_list = ['MasVnrArea']

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1
}

quality_vars = [
    'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtQual',
    'BsmtCond', 'KitchenQual', 'HeatingQC', 'FireplaceQu'
]

features = [
    'Id', 'OverallQual', 'PropertyAge',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr',
    'Neighborhood', 'MSZoning', 'BldgType', 'Remodelled', 'IsNew', 'IsPartial',
    'SalePrice', 'LotArea', 'Functional'
]

scale_list = [
    'OverallQual', 'PropertyAge', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
    'GrLivArea', 'TotalArea', 'LotArea'
]

one_hot_list = [
    'Neighborhood', 'MSZoning', 'BldgType', 'Functional'
]

skew_list = [
    'OverallQual', 'PropertyAge', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF',
    'GrLivArea', 'TotalArea', 'FullBath', 'HalfBath', 'TotalBath',
    'TotRmsAbvGrd', 'BedroomAbvGr', 'SalePrice'
]
