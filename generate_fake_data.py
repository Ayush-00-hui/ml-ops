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

def generate_house_prices(num_records=1000):
    records = []
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

        records.append({
            "LotArea": lot_area,
            "OverallQual": overall_qual,
            "OverallCond": overall_cond,
            "YearBuilt": year_built,
            "GrLivArea": gr_liv_area,
            "GarageCars": garage_cars,
            "SalePrice": sale_price
        })

    df = pd.DataFrame(records)
    out_path = os.path.join(data_dir, "house_prices.csv")
    df.to_csv(out_path, index=False)
    print(f"✅ Generated {num_records} house price records -> {out_path}")
    return df

def generate_raw_customer_data(num_records=500):
    records = []
    for _ in range(num_records):
        name = fake.first_name()
        age = None if random.random() < 0.10 else float(random.randint(20, 65))
        salary = random.randint(25000, 150000)
        purchased = "Yes" if random.random() > 0.5 else "No"

        records.append({
            "Name": name,
            "Age": age,
            "Salary": salary,
            "Purchased": purchased
        })

    df = pd.DataFrame(records)
    out_path = os.path.join(data_dir, "raw.csv")
    df.to_csv(out_path, index=False)
    print(f"✅ Generated {num_records} raw customer records -> {out_path}")
    return df

if __name__ == "__main__":
    generate_house_prices(1000)
    generate_raw_customer_data(500)
