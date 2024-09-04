import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load and prepare data
data = pd.read_csv('ml_data_3188.csv')

# Print column names for debugging
print("Columns in data:", data.columns)

# Use 'caracter' as the label column
X = data.drop('caracter', axis=1)
y = data['caracter']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
print('Accuracy:', accuracy_score(y_test, predictions))

# Save model
joblib.dump(model, 'model.pkl')
