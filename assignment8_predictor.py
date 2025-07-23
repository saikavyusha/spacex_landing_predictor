import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, roc_auc_score

# Step 1: Load dataset
df = pd.read_csv('cleaned_api_dataset.csv')

# Step 2: Feature selection
# Drop columns not useful for prediction
X = df.drop(columns=['LandingOutcome'])  # Features
y = df['LandingOutcome']                # Target

# Step 3: Encode categorical variables
X_encoded = pd.get_dummies(X, drop_first=True)

# Step 4: Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_encoded, y, test_size=0.2, random_state=42
)

# Step 5: Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Utility function to train and evaluate models
def evaluate_model(model, X_train, X_test, y_train, y_test, model_name):
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n {model_name} Results:")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    try:
        y_prob = model.predict_proba(X_test)[:, 1]
        print("ROC AUC Score:", roc_auc_score(y_test, y_prob))
    except:
        print("ROC AUC Score: Not available (no predict_proba method)")

# Step 6: Train and evaluate models
evaluate_model(LogisticRegression(max_iter=1000), X_train_scaled, X_test_scaled, y_train, y_test, "Logistic Regression")
evaluate_model(RandomForestClassifier(n_estimators=100, random_state=42), X_train, X_test, y_train, y_test, "Random Forest")
evaluate_model(SVC(kernel='linear', probability=True), X_train_scaled, X_test_scaled, y_train, y_test, "Support Vector Machine")

