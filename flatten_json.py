import pandas as pd

# Read JSON file
df = pd.read_json(r"C:\Users\uthej\Downloads\PEI_assessment\src\Shipping.json")

# Convert to CSV
df.to_csv("shipping_flatten_output.csv", index=False)

print("CSV created successfully!")