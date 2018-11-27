train_in = '../data/input_data/train.csv'
test_in = '../data/input_data/test.csv'

explore_out_linear = '../data/transformed_data/explore_linear.csv'
explore_out_tree = '../data/transformed_data/explore_tree.csv'
train_model_out_linear = '../data/transformed_data/model_train_linear.csv'
train_model_out_tree = '../data/transformed_data/model_train_tree.csv'
test_model_out_linear = '../data/transformed_data/model_test_linear.csv'
test_model_out_tree = '../data/transformed_data/model_test_tree.csv'

none_list = [
    'MasVnrType',
    'MSZoning',
    'Functional',
    'SaleType',
]

na_list = [
    'MasVnrArea',
]

med_list = [
    'TotalBsmtSF',
    '1stFlrSF',
    '2ndFlrSF',
    'GrLivArea',
    'BsmtFullBath',
    'BsmtHalfBath',
    'FullBath',
    'HalfBath',
    'BedroomAbvGr',
    'YearBuilt',
    'GarageCars'
]

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1
}

story_codes = {
    '1Story': '1',
    '1.5Fin': '1',
    '1.5Unf': '1',
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
    'ExterQual', 'ExterCond',
]


target = 'SalePrice'

features = [
    'Id',
    # Target
    'SalePrice',
    # Num Variables
    'OverallQual',
    'ExterQual',
    'ExterCond',
    'OverallCond',
    'TotalBsmtSF',
    '1stFlrSF',
    '2ndFlrSF',
    'GrLivArea',
    'LotArea',
    'BsmtFullBath',
    'BsmtHalfBath',
    'YearBuilt',
    'FullBath',
    'HalfBath',
    'TotRmsAbvGrd',
    'BedroomAbvGr',
    'KitchenAbvGr',
    'HeatingQC',
    'GarageCars',
    'OpenPorchSF',
    'YearRemodAdd',
    'YrSold',
    'PoolArea',
    'WoodDeckSF',
    # Cat Variables
    'Neighborhood',
    'MSZoning',
    'BldgType',
    'Functional',
    'MSSubClass',
    'Condition1',
    'LotConfig',
    'MasVnrType',
    'SaleType',
    'SaleCondition',
    'Foundation',
    'HouseStyle',
]

scale_list = [
    'OverallQual',
    'OverallCond',
    'ExterQual',
    'ExterCond',
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
    'Neighborhood_ordinal',
    'MSSubClass_ordinal',
    'MasVnrType_ordinal',
    'Foundation_ordinal',
    'GarageCars',
    'YearBuilt',
    'YrSold',
]

# Linear
one_hot_list = [
    'SaleCondition',
    'Stories'
]

# Linear
to_ordinal_list = [
    'Neighborhood',
    'MSSubClass',
    'MasVnrType',
    'Foundation'
]

# Linear
log_trf_list = [
    'OverallQual',
    'ExterQual',
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
    'KitchenAbvGr'
]

# Tree
label_list = [
     'Neighborhood',
     'MSZoning',
     'BldgType',
     'Functional',
     'MSSubClass',
     'Condition1',
     'LotConfig',
     'MasVnrType',
     'SaleType',
     'SaleCondition',
     'Foundation'
]
