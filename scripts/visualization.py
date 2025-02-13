import matplotlib.pyplot as plt
import seaborn as sns

def plot_sensor_trends(df, unit_id, sensors=[2, 3, 4]):
    """Plots sensor trends over time for a specific engine unit."""
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
    """Plots a heatmap of sensor correlations."""
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.iloc[:, 5:].corr(), annot=False, cmap='coolwarm')
    plt.title("Sensor Correlation Heatmap")
    plt.show()

def plot_sensor_distribution(df, sensor=2):
    """Plots the distribution of a specific sensor's readings."""
    plt.figure(figsize=(12, 6))
    sns.histplot(df[f'sensor_measurement_{sensor}'], bins=50, kde=True)
    plt.title(f"Distribution of Sensor {sensor} Readings")
    plt.xlabel(f"Sensor {sensor} Values")
    plt.ylabel("Frequency")
    plt.show()
