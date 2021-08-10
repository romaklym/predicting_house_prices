import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = 'C:\\Users\\Roman Klym\\Desktop\\predicting_house_prices\\train.csv'

home_data = pd.read_csv(iowa_file_path)

# print the list of columns in the dataset to find the name of the prediction target
# print(home_data.columns)

y = home_data.SalePrice

# Create the list of features below
feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select data corresponding to features in feature_names
X = home_data[feature_names]

# Review data
# print description or statistics from X
# print(X.describe())

# print the top few lines
# print(X.head())

iowa_model = DecisionTreeRegressor(random_state=1)

# Fit the model
iowa_model.fit(X, y)

predictions = iowa_model.predict(X)
print(predictions)

