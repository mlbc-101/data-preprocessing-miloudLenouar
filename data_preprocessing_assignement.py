""" Do not delete this section, Please Commit your changes after implementing the necessary code.

- The data file called Social_Network_Ads.csv.
- Your Job is to preprocess this data because we gonna use it later one in the course.

The Features of this dataset are:
	- UserID: Which represent id of user in the database.
	- Gender: Can be male or female.
	- EstimatedSalary: The salary of the user.
	- Purchased: An integer number {1 if the user purshased something, 0 otherwise}
	
	The target variable for this data is the purshased status.

Happy coding."""

# Step 0: import the necessary libraries: pandas, matplotlib.pyplot, and numpy.
    import numpy as np
    import pandas as pd 
    import matplotlib.pyplot as plt
    from sklearn.preprocessing import LabelEncoder
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import train_test_split

# Step 1: load your dataset using pandas
    data = pd.read_csv('Social_Network_Ads.csv')
    x = data.drop(['User ID', 'Purchased'], axis = 1)
	y = data['Purchased']

# Step 2: Handle Missing data if they exist.
    X.isnull().sum()

# Step 3: Encode the categorical variables.
    df = pd.get_dummies(data,prefix="",columns=['Gender'])
    encoder = LabelEncoder()
    x['Gender'] = encoder.fit_transform(X['Gender'])
# Step 4: Do Feature Scaling if necessary.
    scaler = StandardScaler()
	x = scaler.fit_transform(X)
# Final Step: Train/Test Splitting.
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 19)
    