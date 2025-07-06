# House Price Prediction

A simple machine learning project that predicts house prices based on area, number of bedrooms, and bathrooms using Linear Regression.

## 📋 Project Description

This project uses a Linear Regression model to predict house prices in Lakhs (Indian currency) based on three key features:
- **Area (sqft)**: Total area of the house in square feet
- **Bedrooms**: Number of bedrooms
- **Bathrooms**: Number of bathrooms

The model is trained on a dataset of 15 house samples and provides an interactive interface for users to input house specifications and get price predictions.

## 🚀 Features

- **Machine Learning Model**: Uses scikit-learn's LinearRegression for price prediction
- **Interactive Input**: Command-line interface for user input
- **Data Visualization**: Displays loaded dataset information
- **Model Evaluation**: Shows model accuracy on test data
- **Error Handling**: Graceful handling of invalid user inputs

## 📁 Project Structure

```
house_prediction/
├── price_prediction.py    # Main prediction script
├── house_data.csv         # Training dataset
└── readme.md             # Project documentation
```

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Dependencies

Install the required packages:

```bash
pip install pandas scikit-learn
```

Or install all dependencies at once:

```bash
pip install -r requirements.txt
```

## 📊 Dataset

The project uses a sample dataset (`house_data.csv`) containing 15 house records with the following features:

| Feature | Description | Range |
|---------|-------------|-------|
| Area (sqft) | House area in square feet | 500 - 4000 |
| Bedrooms | Number of bedrooms | 1 - 6 |
| Bathrooms | Number of bathrooms | 1 - 5 |
| Price (in Lakhs) | House price in Lakhs (₹) | 25 - 230 |

## 🎯 Usage

1. **Run the prediction script:**
   ```bash
   python price_prediction.py
   ```

2. **Follow the prompts:**
   - Enter the area of the house in square feet
   - Enter the number of bedrooms
   - Enter the number of bathrooms

3. **Get the prediction:**
   The model will output the predicted house price in Lakhs (₹).

### Example Output

```
--- Loaded Data ---
    Area (sqft)  Bedrooms  Bathrooms  Price (in Lakhs)
0           500         1          1               25
1           750         2          1               35
...

Model Accuracy: 0.99

Enter the area of the house in sqft: 1200
Enter the number of bedrooms: 3
Enter the number of bathrooms: 2
Predicted Price: ₹62.50 Lakhs
```

## 🔧 How It Works

1. **Data Loading**: The script loads the house dataset from `house_data.csv`
2. **Feature Selection**: Extracts area, bedrooms, and bathrooms as features
3. **Data Splitting**: Splits data into training (80%) and testing (20%) sets
4. **Model Training**: Trains a Linear Regression model on the training data
5. **Model Evaluation**: Calculates and displays model accuracy
6. **User Input**: Takes user input for house specifications
7. **Prediction**: Predicts house price using the trained model

## 📈 Model Performance

The Linear Regression model typically achieves high accuracy (around 99%) on the provided dataset, indicating good fit for the sample data.

## 🤝 Contributing

Feel free to contribute to this project by:
- Adding more features to the dataset
- Implementing different machine learning algorithms
- Improving the user interface
- Adding data visualization capabilities

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created as a machine learning project for house price prediction.

---

**Note**: This is a demonstration project using sample data. For real-world applications, consider using larger, more diverse datasets and additional features for more accurate predictions.
