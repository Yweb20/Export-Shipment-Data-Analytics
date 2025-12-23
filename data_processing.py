import pandas as pd

df = pd.read_csv("input_data.csv")

df.columns = df.columns.str.strip()

df["SB_Year"] = pd.to_datetime(df["SB date"], errors="coerce").dt.year

df.to_csv("processed_output.csv", index=False)

print("processed_output.csv created")