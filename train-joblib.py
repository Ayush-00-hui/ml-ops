import os
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

data_path = os.path.join(os.path.dirname(__file__), "data", "house_prices.csv")
df = pd.read_csv(data_path)

X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, prediction))
print("R2 :", r2_score(y_test, prediction))

joblib.dump(model, "model.joblib")
print("Saved model to model.joblib")
