import pandas as pd
from transformation import has_porch

# Variables & Parameters

infile = './data/transformed_data/train_preprocessed.csv'
explore = './data/transformed_data/explore.csv'
final = './data/transformed_data/final.csv'

quality_codes = {
    'Ex': 5,
    'Gd': 4,
    'TA': 3,
    'Fa': 2,
    'Po': 1
}
quality_vars = [
    'ExterQual', 'ExterCond', 'BsmtQual', 'BsmtQual', 'BsmtCond',
    'KitchenQual', 'HeatingQC', 'FireplaceQu'
]

# Processing

df = pd.read_csv(infile)

# Categorical Cleaning
df['MSSubClass'] = df['MSSubClass'].astype(str)
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

df.drop(porch_vars, axis=1, inplace=True)
df.drop('YearRemodAdd', axis=1, inplace=True)
df.drop('YearBuilt', axis=1, inplace=True)
df.drop('BsmtFullBath', axis=1, inplace=True)
df.drop('BsmtHalfBath', axis=1, inplace=True)
df.drop(pool_vars, axis=1, inplace=True)
df.drop(garage_vars, axis=1, inplace=True)
df.drop('WoodDeckSF', axis=1, inplace=True)

# Export for exploratory analysis
df.to_csv(explore, index=False)


