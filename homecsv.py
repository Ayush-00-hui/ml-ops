import os
import random
import pandas as pd
from faker import Faker

fake = Faker(['en_IN', 'en_US'])
Faker.seed(42)
random.seed(42)

base_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(base_dir, "data")
os.makedirs(data_dir, exist_ok=True)
output_path = os.path.join(data_dir, "house_prices_fake.csv")

data = []
num_records = 1000

for _ in range(num_records):
    lot_area = random.randint(2000, 20000)
    overall_qual = random.randint(1, 10)
    overall_cond = random.randint(1, 10)
    year_built = fake.random_int(min=1950, max=2024)
    gr_liv_area = random.randint(500, 5000)
    garage_cars = random.randint(0, 4)

    sale_price = (
        30000
        + lot_area * 3
        + gr_liv_area * 120
        + overall_qual * 25000
        + garage_cars * 12000
        + (year_built - 1950) * 800
        - overall_cond * 500
        + random.randint(-15000, 15000)
    )

    sale_price = max(50000, int(sale_price))

    data.append({
        "LotArea": lot_area,
        "OverallQual": overall_qual,
        "OverallCond": overall_cond,
        "YearBuilt": year_built,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "SalePrice": sale_price
    })

df = pd.DataFrame(data)
df.to_csv(output_path, index=False)

print(df.head())
print(f"\nCSV file '{output_path}' created successfully.")
