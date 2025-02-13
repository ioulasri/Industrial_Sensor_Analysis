import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path, sep=' ', header=None)
    df = df.dropna(axis=1)
    return df

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df_cleaned


file_path = "data/test_FD004.txt"
df = load_data(file_path)
df_cleaned = remove_outliers(df)
df_cleaned.to_csv("data/cleaned_data.csv", index=False)
print("Data cleaning complete. Cleaned data saved.")