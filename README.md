# kaggle-house-prices

Repo to hold my code for the [Kaggle House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques) challenge.

## Notes

### General Notes & Ideas

* Housing price crash from 2008 onwards. Is this significant? Maybe variables to indicate the stage of the crisis based upon month / year?
* Variable to indicate number of floors (including basement)?
* Dimensionality Reduction on Basement, Garage variables?
* Has Basement / Garage variables?

### Correlations

Highly correlated variables: 
    `OverallQual` Rates the overall material and finish of the house **0.8**
    `GrLivArea` Above grade (ground) living area square feet **0.7**
    
Correlated variables
    `1stFlrSF` First Floor square feet **0.6**
    `TotalBsmtSF` Total square feet of basement area **0.6**
    `FullBath` Full bathrooms above grade **0.6**
    `YearBuilt` Year Built **0.5**
    `YearRemodAdd` Year Remodelled **0.5** (note - this is the same as the construction date if no remodelling or additions)
    `MasVnrArea` Masonry veneer area in square feet **0.5**
    
