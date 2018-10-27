train_in = '../../data/input_data/train.csv'
test_in = '../../data/input_data/test.csv'

explore_out = '../../data/transformed_data/explore.csv'
train_model_out = '../../data/transformed_data/model_train.csv'
test_model_out = '../../data/transformed_data/model_test.csv'

none_list = [
    'Alley', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'BsmtQual', 'Fence', 'FireplaceQu', 'GarageCond', 'GarageFinish',
    'GarageQual', 'GarageType', 'GarageYrBlt', 'MiscFeature', 'PoolQC',
    'MasVnrType'
]
na_list = ['MasVnrArea']

med_list = [
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath', 
    'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'YearBuilt'
]

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1
}

simple_codes = {
    1 : 1, # poor
    2 : 1, # poor
    3 : 1, # poor
    4 : 2, # average
    5 : 2, # average 
    6 : 2, # average
    7 : 3, # good
    8 : 3, # good 
    9 : 3, # good 
    10 : 4 # outstanding                                         
}

quality_vars = [
    'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtQual',
    'BsmtCond', 'KitchenQual', 'HeatingQC', 'FireplaceQu'
]

features = [
    'Id', 
    # Num Variables
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr', 'KitchenAbvGr',
    'SimpleOverallQual', 'SimpleOverallCond',

    # Cat Variables
     'Neighborhood', 'MSZoning', 'BldgType', 'Functional', 'MSSubClass', 'Condition1', 
     'LotConfig', 'MasVnrType', 'SaleType', 'SaleCondition',

    # Binary Variables
    'IsRemodelled', 'IsNew'
]

target = 'SalePrice'

scale_list = [
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr', 'KitchenAbvGr',
    'SimpleOverallQual', 'SimpleOverallCond'
]

one_hot_list = [
     'Neighborhood', 'MSZoning', 'BldgType', 'Functional', 'MSSubClass', 'Condition1', 
     'LotConfig', 'MasVnrType', 'SaleType', 'SaleCondition'
]

log_trf_list = [
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr', 'KitchenAbvGr',
    'SimpleOverallQual', 'SimpleOverallCond'
]


