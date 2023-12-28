import pickle
import pandas as pd

# Load the trained model
model = pickle.load(open(r'Practical_Implementaion\Linear_Regression_boston-housing-dataset', 'rb'))

# Get user input for housing details
CRIM = float(input("Enter the per capita crime rate by town: "))
ZN = float(input("Enter the proportion of residential land zoned for lots over 25,000 sq. ft.: "))
INDUS = float(input("Enter the proportion of non-retail business acres per town: "))
CHAS = int(input("Enter the Charles River dummy variable (1 if tract bounds river; 0 otherwise): "))
NOX = float(input("Enter the nitric oxides concentration (parts per 10 million): "))
RM = float(input("Enter the average number of rooms per dwelling: "))
AGE = float(input("Enter the proportion of owner-occupied units built prior to 1940: "))
DIS = float(input("Enter the weighted distances to five Boston employment centers: "))
RAD = float(input("Enter the index of accessibility to radial highways: "))
TAX = float(input("Enter the full-value property tax rate per $10,000: "))
PTRATIO = float(input("Enter the pupil-teacher ratio by town: "))
B = float(input("Enter the proportion of Black residents by town: "))
LSTAT = float(input("Enter the percentage of lower status of the population: "))

# Create a DataFrame from user inputs
input_data = {
    'CRIM': [CRIM],
    'ZN': [ZN],
    'INDUS': [INDUS],
    'CHAS': [CHAS],
    'NOX': [NOX],
    'RM': [RM],
    'AGE': [AGE],
    'DIS': [DIS],
    'RAD': [RAD],
    'TAX': [TAX],
    'PTRATIO': [PTRATIO],
    'B': [B],
    'LSTAT': [LSTAT]
}

input_df = pd.DataFrame(input_data)

# Make predictions using the model
predicted_MEDV = model.predict(input_df)

# Display the predicted median value of owner-occupied homes
print(f"The predicted median value of owner-occupied homes is: {predicted_MEDV[0]}")