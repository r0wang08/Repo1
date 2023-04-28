import pandas as pd
import statsmodels.api as sm

# Load data into a Pandas dataframe
data = pd.DataFrame({
    'healthier_premium': [0, 1, 1, 1, 3, 2, 2, 2, 3, 3, 2, 2, 2, 1, 0, 2, 1, 2, 2, 2, 2, 1, 0, 1, 3, 1, 2, 2, 1, 3, 1, 1, 2, 0, 1, 0, 3, 0, 2, 4, 4, 1, 1, 1, 2, 1, 1, 3, 1, 1, 2, 3, 1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 2, 4, 2, 4, 4, 1, 1, 1, 0, 2, 2, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1],
    'household_income': [20000, 35000, 100000, 20000, 20000, 87500, 45000, 100000, 100000, 20000, 20000, 20000, 100000, 100000, 20000, 25000, 62500, 20000, 25000, 20000, 62500, 25000, 20000, 62500, 20000, 62500, 25000, 25000, 20000, 25000, 25000, 20000, 45000, 87500, 20000, 20000, 100000, 25000, 20000, 62500, 20000, 35000, 20000, 35000, 20000, 35000, 35000, 45000, 25000, 20000, 45000, 35000, 35000, 45000, 87500, 62500, 45000, 45000, 87500, 62500, 62500, 62500, 45000, 62500, 62500, 100000, 62500, 62500, 87500, 100000, 87500, 62500, 87500, 87500, 20000, 87500, 87500, 20000, 20000, 62500]
})

# Add a constant column to the data to fit an intercept term
data = sm.add_constant(data)

# Fit the linear regression model
model = sm.OLS(data['healthier_premium'], data[['const', 'household_income']])
results = model.fit()

# Print the regression results summary
print(results.summary())
