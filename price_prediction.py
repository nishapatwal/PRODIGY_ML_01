import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load Dataset
data = pd.read_csv('house_data.csv')
print("\n--- Loaded Data ---")
print(data)

# Split Features and Target
X = data[['Area (sqft)', 'Bedrooms', 'Bathrooms']]
y = data['Price (in Lakhs)']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print(f"\nModel Accuracy: {accuracy:.2f}\n")

# Take User Input
try:
    area = float(input("Enter the area of the house in sqft: "))
    bedrooms = int(input("Enter the number of bedrooms: "))
    bathrooms = int(input("Enter the number of bathrooms: "))

    predicted_price = model.predict([[area, bedrooms, bathrooms]])
    print(f"Predicted Price: ₹{predicted_price[0]:.2f} Lakhs")

except Exception as e:
    print("Invalid input. Please enter valid numbers.")