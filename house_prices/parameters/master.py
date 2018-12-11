train_in = '../data/input_data/train.csv'
test_in = '../data/input_data/test.csv'
train_test_raw_out = '../data/transformed_data/train_test_raw.csv'
all_model_out = '../data/transformed_data/model_all.csv'
train_model_out = '../data/transformed_data/model_train.csv'
test_model_out = '../data/transformed_data/model_test.csv'

target = 'SalePrice'
uid = 'Id'
''' Pre Processing '''

# Variables to be dropped entirely
drop_vars = [
    'Utilities'
]

# Replace missing values with 'None'
none_vars = [
    'MasVnrType',
    'MSSubClass',
    'GarageType',
    'GarageFinish',
    'GarageQual',
    'GarageCond',
    'PoolQC',
    'MiscFeature',
    'Alley',
    'Fence',
    'FireplaceQu',
    'BsmtQual',
    'BsmtCond',
    'BsmtExposure',
    'BsmtFinType1',
    'BsmtFinType2',
]

# Replace missing values with 0
na_vars = [
    'MasVnrArea',
    'GarageYrBlt',
    'GarageArea',
    'GarageCars',
    'BsmtFinSF1',
    'BsmtFinSF2',
    'BsmtUnfSF',
    'TotalBsmtSF',
    'BsmtFullBath',
    'BsmtHalfBath',
    'MoSold',
]


# Replace missing values with the variable median or the median for the
# particular group
med_vars = [{
    'var': 'LotFrontage',
    'group': 'Neighborhood'
}]

# Replace missing values with the mode
mode_vars = [
    'MSZoning',
    'Electrical',
    'KitchenQual',
    'Exterior1st',
    'Exterior2nd',
    'SaleType',
    'Functional',
    'BldgType',
]

# Convert numeric variables to string
to_string_vars = [
    'MSSubClass',
    'MoSold',
    'YrSold'
]


# Feature Engineering

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1,
    'None': 0
}

quality_vars = [
    'BsmtCond',
    'BsmtQual',
    'ExterCond',
    'ExterQual',
    'FireplaceQu',
    'GarageCond',
    'GarageQual',
    'HeatingQC',
    'KitchenQual'
]

ordinal_vars = [
    'Alley',
    'BldgType',
    'BsmtExposure',
    'BsmtFinType1',
    'BsmtFinType2',
    'CentralAir',
    'Condition1',
    'Condition2',
    'Electrical',
    'Exterior1st',
    'Exterior2nd',
    'Fence',
    'Foundation',
    'Functional',
    'GarageFinish',
    'GarageType',
    'Heating',
    'HouseStyle',
    'LandContour',
    'LandSlope',
    'LotConfig',
    'LotShape',
    'MoSold',
    'MSSubClass',
    'MSZoning',
    'MasVnrType',
    'MiscFeature',
    'Neighborhood',
    'PavedDrive',
    'PoolQC',
    'RoofMatl',
    'RoofStyle',
    'SaleCondition',
    'SaleType',
    'Street',
    'YrSold',
]

one_hot_vars = [
    'Alley',
    'BldgType',
    'BsmtExposure',
    'BsmtFinType1',
    'BsmtFinType2',
    'CentralAir',
    'Condition1',
    'Condition2',
    'Electrical',
    'Exterior1st',
    'Exterior2nd',
    'Fence',
    'Foundation',
    'Functional',
    'GarageFinish',
    'GarageType',
    'Heating',
    'HouseStyle',
    'LandContour',
    'LandSlope',
    'LotConfig',
    'LotShape',
    'MoSold',
    'MSSubClass',
    'MSZoning',
    'MasVnrType',
    'MiscFeature',
    # 'Neighborhood',
    'PavedDrive',
    'PoolQC',
    'RoofMatl',
    'RoofStyle',
    'SaleCondition',
    'SaleType',
    'Street',
    'YrSold',
]

num_exclude_vars = [
    'Train',
    'Test',
    uid,
    target
]

poly_trf_list = []

# Linear
to_ordinal_list = [
    'Neighborhood',
    'MSSubClass',
    'MasVnrType',
    'Foundation',
    'SaleType',
    'SaleCondition'
]
