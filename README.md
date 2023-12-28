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

# Implementation

### Data Overview

Here we aim to predict the median value of owner-occupied homes in Boston using the **Boston Housing Dataset** from Kaggle . It involves data preprocessing, model building, and evaluation.

| Feature  | Description                                                |
|----------|------------------------------------------------------------|
| CRIM     | Per capita crime rate. Higher values indicate a higher crime rate. |
| ZN       | Proportion of large residential lots. Higher values represent more spacious residential zoning. |
| INDUS    | Proportion of non-retail business acres. Higher values indicate more industrial/commercial land use. |
| CHAS     | Binary variable indicating proximity to Charles River. |
| NOX      | Nitric oxides concentration. Higher values imply higher pollution levels. |
| RM       | Average number of rooms. Higher values suggest larger dwellings. |
| AGE      | Proportion of older housing units (built before 1940). Higher values indicate older infrastructure. |
| DIS      | Distance to employment centers. Higher values suggest more distant locations. |
| RAD      | Accessibility to highways. Higher values indicate better highway access. |
| TAX      | Property tax rate. Higher values represent higher taxes. |
| PTRATIO  | Pupil-teacher ratio. Lower values suggest better-resourced schools. |
| B        | Proportion of Black residents. Higher values may indicate a higher proportion of Black residents. |
| LSTAT    | Percentage of lower-status population. Higher values represent a higher percentage of the population in lower socio-economic status. |
| MEDV     | Median value of owner-occupied homes in $1000s (the target variable). |


### Model Details

The model utilized for prediction is a Linear Regression model. **After preprocessing steps** (handling missing values by replacing them with column means), the data was split into training and testing sets **(80-20 split)**.

The model was trained on the training data and evaluated using R-squared and Mean Squared Error metrics on the test data.

### Model Performance

- **R-squared:** The model achieved an R-squared value of approximately 0.7314.
- **Mean Squared Error:** The MSE obtained was approximately 22.67.

### Conclusion

The model demonstrated a moderate predictive capability, explaining around 73.14% of the variability in the housing prices. Further enhancements could involve feature engineering, exploring different models, or parameter tuning for improved performance.

---
