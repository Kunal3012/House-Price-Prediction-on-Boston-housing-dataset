## Linear Regression Overview

### What is Linear Regression?

Linear Regression is a statistical method used to model the relationship between one or more independent variables and a dependent variable. It assumes a linear relationship between the variables.

### Simple Linear Regression

#### Overview

Simple Linear Regression models the relationship between a single independent variable and a dependent variable.

#### Equation

The equation of a simple linear regression model:
```
Y = β₀ + β₁X + ε
```
- **Y:** Dependent variable (target).
- **X:** Independent variable (predictor).
- **β₀:** Intercept term (constant).
- **β₁:** Coefficient for the independent variable (slope).
- **ε:** Error term accounting for unexplained variation.

#### Model Training and Evaluation

1. **Data Preparation:** Split the dataset into X and Y variables.
2. **Model Fitting:** Learn the relationship between X and Y to minimize the difference between predicted and actual values.
3. **Predictions:** Predict Y values for new X values using the learned equation.
4. **Evaluation:** Measure performance using metrics like R-squared and Mean Squared Error (MSE).

### Multiple Linear Regression

#### Overview

Multiple Linear Regression extends simple regression to model the relationship between multiple independent variables and a dependent variable.

#### Equation

The equation of a multiple linear regression model:
```
Y = β₀ + β₁X₁ + β₂X₂ + ... + βᵢXᵢ + ε
```
- **Y:** Dependent variable (target).
- **X₁, X₂, ..., Xᵢ:** Independent variables (predictors).
- **β₀:** Intercept term (constant).
- **β₁, β₂, ..., βᵢ:** Coefficients for the independent variables (slopes).
- **ε:** Error term accounting for unexplained variation.

#### Model Training and Evaluation

1. **Data Preparation:** Split the dataset into X variables (multiple predictors) and the target variable Y.
2. **Model Fitting:** Learn the relationship between multiple X variables and Y to minimize the difference between predicted and actual values.
3. **Predictions:** Predict Y values for new observations based on their X values.
4. **Evaluation:** Measure performance using metrics like R-squared and Mean Squared Error (MSE).

### Conclusion

Linear Regression methods, whether simple or multiple, provide valuable tools for understanding and predicting relationships between variables. They are widely used across various domains for prediction and analysis.

----
