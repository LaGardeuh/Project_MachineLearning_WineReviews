import pandas as pd
import matplotlib.pyplot as plt

file_path = "../data/raw/winemag-data_first150k.csv"
df = pd.read_csv(file_path)

# Display the first few rows
print(df.head(200))