import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Defining column names
column_names = [
    'unit_number', 'time_in_cycles',
    'operational_setting_1', 'operational_setting_2', 'operational_setting_3',
    'sensor_measurement_1', 'sensor_measurement_2', 'sensor_measurement_3',
    'sensor_measurement_4', 'sensor_measurement_5', 'sensor_measurement_6',
    'sensor_measurement_7', 'sensor_measurement_8', 'sensor_measurement_9',
    'sensor_measurement_10', 'sensor_measurement_11', 'sensor_measurement_12',
    'sensor_measurement_13', 'sensor_measurement_14', 'sensor_measurement_15',
    'sensor_measurement_16', 'sensor_measurement_17', 'sensor_measurement_18',
    'sensor_measurement_19', 'sensor_measurement_20', 'sensor_measurement_21',
    'sensor_measurement_22', 'sensor_measurement_23', 'sensor_measurement_24',
    'sensor_measurement_25', 'sensor_measurement_26',
]

def load_data(file_path):
    df = pd.read_csv(file_path, sep=' ', header=None, names=column_names)
    df = df.dropna(axis=1)
    return df

def remove_outliers(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    df_cleaned = df[~((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df_cleaned

def plot_sensor_trends(df, unit_id, sensors=[2, 3, 4]):
    df_unit = df[df['unit_number'] == unit_id]
    plt.figure(figsize=(12, 6))
    for sensor in sensors:
        plt.plot(df_unit['time_in_cycles'], df_unit[f'sensor_measurement_{sensor}'], label=f'Sensor {sensor}')
    plt.xlabel("Time in Cycles")
    plt.ylabel("Sensor Readings")
    plt.title(f"Sensor Trends for Engine {unit_id}")
    plt.legend()
    plt.show()

def plot_correlation_heatmap(df):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.iloc[:, 5:].corr(), annot=False, cmap='coolwarm')
    plt.title("Sensor Correlation Heatmap")
    plt.show()

def plot_sensor_distribution(df, sensor=2):
    plt.figure(figsize=(12, 6))
    sns.histplot(df[f'sensor_measurement_{sensor}'], bins=50, kde=True)
    plt.title(f"Distribution of Sensor {sensor} Readings")
    plt.xlabel(f"Sensor {sensor} Values")
    plt.ylabel("Frequency")
    plt.show()

def plot_boxplot(df, sensor=2):
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df[f'sensor_measurement_{sensor}'])
    plt.title(f"Boxplot for Sensor {sensor}")
    plt.show()

def plot_rolling_average(df, unit_id, sensor=2, window=5):
    df_unit = df[df['unit_number'] == unit_id]
    df_unit[f'rolling_avg_{sensor}'] = df_unit[f'sensor_measurement_{sensor}'].rolling(window=window).mean()
    plt.figure(figsize=(12, 6))
    plt.plot(df_unit['time_in_cycles'], df_unit[f'rolling_avg_{sensor}'], label=f'Rolling Avg Sensor {sensor}', color='red')
    plt.xlabel("Time in Cycles")
    plt.ylabel(f"Sensor {sensor} Readings (Rolling Avg)")
    plt.title(f"Rolling Average for Sensor {sensor} (Unit {unit_id})")
    plt.legend()
    plt.show()

# Main Execution
file_path = 'test_FD004.txt'
df = load_data(file_path)
print("Original Data:")
print(df.describe())

df = remove_outliers(df)
print("Cleaned Data:")
print(df.describe())

# Saving cleaned data
df.to_csv("cleaned_data.csv", index=False)

# Visualizations
plot_sensor_trends(df, unit_id=1)
plot_correlation_heatmap(df)
plot_sensor_distribution(df, sensor=2)
plot_boxplot(df, sensor=2)
plot_rolling_average(df, unit_id=1, sensor=2, window=10)
