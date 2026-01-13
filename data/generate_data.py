import pandas as pd
import numpy as np

np.random.seed(42)

rows = 1000

data = pd.DataFrame({
    "monthly_sales": np.random.randint(50, 1000, rows),
    "revenue": np.random.randint(10000, 500000, rows),
    "customer_count": np.random.randint(10, 5000, rows),
    "churn_rate": np.random.uniform(0, 0.5, rows),
    "support_tickets": np.random.randint(0, 200, rows),
    "marketing_spend": np.random.randint(1000, 50000, rows)
})

# failure logic
data["failed"] = (
    (data["churn_rate"] > 0.3) &
    (data["monthly_sales"] < 200)
).astype(int)

data.to_csv("data/raw/business_data.csv", index=False)
print("Dataset generated!")
