def has_porch(row):
    '''Determines if the property has a porch'''
    if row['OpenPorchSF'] > 0:
        return 1
    else:
        return 0


def is_remodelled(row):
    '''Determines if the property has been remodelled'''
    if row['YearBuilt'] == row['YearRemodAdd']:
        return 1
    else:
        return 0


def property_age(row):
    '''Determines the property age'''
    return int(row['YrSold'] - row['YearBuilt'])


def is_new(row):
    '''Flag to indicate if a house is new'''
    if row['PropertyAge'] == 0:
        return 1
    else:
        return 0


def is_partial(row):
    '''Flag to indicate if a salwe is partial'''
    if row['SaleCondition'] == 'Partial':
        return 1
    else:
        return 0


def full_bath(row):
    '''Adds basement full baths to full baths'''
    return row['FullBath'] + row['BsmtFullBath']


def half_bath(row):
    '''Adds basement half baths to half baths'''
    return row['HalfBath'] + row['BsmtHalfBath']


def has_pool(row):
    '''Determines if the property has a pool'''
    if row['PoolArea'] > 0:
        return 1
    else:
        return 0


def has_deck(row):
    '''Determines if the property has a deck'''
    if row['WoodDeckSF'] > 0:
        return 1
    else:
        return 0