train_in = '../data/input_data/train.csv'
test_in = '../data/input_data/test.csv'

explore_out_linear = '../data/transformed_data/explore_linear.csv'
explore_out_tree = '../data/transformed_data/explore_tree.csv'
train_model_out_linear = '../data/transformed_data/model_train_linear.csv'
train_model_out_tree = '../data/transformed_data/model_train_tree.csv'
test_model_out_linear = '../data/transformed_data/model_test_linear.csv'
test_model_out_tree = '../data/transformed_data/model_test_tree.csv'

none_list = [
    'Alley', 'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2',
    'BsmtQual', 'Fence', 'FireplaceQu', 'GarageCond', 'GarageFinish',
    'GarageQual', 'GarageType', 'GarageYrBlt', 'MiscFeature', 'PoolQC',
    'MasVnrType'
]
na_list = ['MasVnrArea']

med_list = [
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'BsmtFullBath',
    'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'YearBuilt',
    'GarageCars'
]

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1
}

simple_codes = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 3,
    10: 4
}

story_codes = {
    '1Story': '1',
    '1.5Fin': '1',
    '1.5Unf ': '1',
    '2Story': '2',
    '2.5Fin': '2',
    '2.5Unf': '2',
    'SFoyer': 'S',
    'SLvl': 'S',
}

exterior_codes = {
   'AsbShng': 'Shingle',
   'AsphShn': 'Shingle',
   'BrkComm': 'BrkFace',
   'BrkFace': 'BrkFace',
   'CBlock': 'Shingle',
   'CemntBd': 'CemntBd',
   'HdBoard': 'HdBoard',
   'ImStucc': 'Stucco',
   'MetalSd': 'MetalSd',
   'Other': 'Other',
   'Plywood': 'Plywood',
   'PreCast': 'Other',
   'Stone': 'BrkFace',
   'Stucco': 'Stucco',
   'VinylSd': 'VinylSd',
   'Wd Sdng': 'Wd Sdng',
   'WdShing': 'WdShing'
}

foundation_codes = {
    'BrkTil': 'BrkTil',
    'CBlock': 'CBlock',
    'PConc': 'PConc',
    'Slab': 'Other',
    'Stone': 'Other',
    'Wood': 'Other'
}

quality_vars = [
    'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtQual',
    'BsmtCond', 'KitchenQual', 'HeatingQC', 'FireplaceQu'
]

# Linear (and maybe Tree)
linear_features = [
    'Id',
    # Num Variables
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr',
    'KitchenAbvGr', 'SimpleOverallQual', 'SimpleOverallCond',
    'Neighborhood_ordinal', 'MSSubClass_ordinal', 'GarageCars',

    # Cat Variables
    'Neighborhood', 'MSZoning', 'BldgType', 'Functional', 'MSSubClass',
    'Condition1', 'LotConfig', 'MasVnrType', 'SaleType', 'SaleCondition',
    'Stories', 'Foundation',

    # Binary Variables
    'IsRemodelled', 'IsNew', 'IsCulDeSac', 'IsPartial'
]

tree_features = [
    'Id',
    # Num Variables
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr',
    'KitchenAbvGr', 'SimpleOverallQual', 'SimpleOverallCond',

    # Cat Variables
    'Neighborhood_label', 'MSZoning_label', 'BldgType_label',
    'Functional_label', 'MSSubClass_label', 'Condition1_label',
    'LotConfig_label', 'MasVnrType_label', 'SaleType_label',
    'SaleCondition_label',

    # Binary Variables
    'IsRemodelled', 'IsNew'

]

target = 'SalePrice'

# Linear
scale_list = [
    'OverallQual', 
    'PropertyAge', 
    'OverallGrade', 
    'ExterGrade', 
    'CoreArea',
    'TotalBsmtSF', 
    '1stFlrSF', 
    '2ndFlrSF', 
    'GrLivArea', 
    'TotalArea', 
    'LotArea',
    'FullBath',
    'HalfBath', 
    'TotalBath', 
    'TotRmsAbvGrd', 
    'BedroomAbvGr',
    'KitchenAbvGr', 
    'SimpleOverallQual', 
    'SimpleOverallCond',
    'Neighborhood_ordinal', 
    'MSSubClass_ordinal', 
    'GarageCars',
]

# Linear
one_hot_list = [
    'SaleCondition', 'Stories', 'Foundation'
]

# Linear
to_ordinal_list = [
    'Neighborhood', 'MSSubClass', 'MasVnrType', 'Foundation'
]

# Linear
log_trf_list = [
    'OverallQual', 'PropertyAge', 'OverallGrade', 'ExterGrade', 'CoreArea',
    'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'GrLivArea', 'TotalArea', 'LotArea',
    'FullBath', 'HalfBath', 'TotalBath', 'TotRmsAbvGrd', 'BedroomAbvGr',
    'KitchenAbvGr', 'SimpleOverallQual', 'SimpleOverallCond',
    'Neighborhood_ordinal', 'MSSubClass_ordinal', 'GarageCars'
]

# Tree
label_list = [
     'Neighborhood', 'MSZoning', 'BldgType', 'Functional', 'MSSubClass',
     'Condition1', 'LotConfig', 'MasVnrType', 'SaleType', 'SaleCondition'
]
