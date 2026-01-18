import sys
import pandas as pd
print("arguments", sys.argv)

month = int(sys.argv[1])
print(f"Running pipeline for month {month}\n")

df = pd.DataFrame({"day": [1, 2], "number_of_passengers": [3, 4]})
df.set_index("day", inplace=True)
print(df.head())

df.to_parquet(f"output_day_{sys.argv[1]}.parquet")