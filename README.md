# Industrial Sensor Data Analysis

## 📌 Overview
This project focuses on **industrial sensor data analysis**, where we analyze engine performance over time using various sensors. The goal is to **clean the data, detect anomalies, and visualize trends** to assist in **predictive maintenance and failure detection**.

## 🛠 Features
- **Data Loading & Cleaning**: Handle missing values and remove outliers using the **Interquartile Range (IQR) method**.
- **Sensor Trend Analysis**: Visualize sensor values over time to detect degradation patterns.
- **Correlation Analysis**: Use a heatmap to identify relationships between different sensors.
- **Sensor Distribution**: Histogram visualization for individual sensor readings.
- **Boxplot Analysis**: Identify outliers and assess data spread.
- **Rolling Average**: Apply moving average to smooth data trends.
- **Export Cleaned Data**: Save processed data for further use.

## 📂 Project Structure
```
├── data/                     # Raw and processed datasets
├── visualizations/           # Generated plots and figures
├── scripts/                  # Python scripts for analysis
│   ├── data_cleaning.py      # Handles missing values and outliers
│   ├── visualization.py      # Generates plots and charts
│   ├── main.py               # Main execution script
├── README.md                 # Project documentation
└── Industrial_Sensor_Analysis_Report.pdf  # Final report
```

## 🚀 Installation & Usage
### Prerequisites
Make sure you have the following installed:
- Python 3.7+
- Required libraries: `pandas`, `matplotlib`, `seaborn`, `fpdf`

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/industrial-sensor-analysis.git
   cd industrial-sensor-analysis
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the main script:
   ```sh
   python scripts/main.py
   ```

## 📊 Visualizations
The following visualizations are included in the analysis:
- **Sensor Trends for a Single Engine**: Helps track performance over time.
- **Sensor Correlation Heatmap**: Identifies relationships between different sensors.
- **Sensor Distribution**: Detects abnormalities in sensor readings.
- **Boxplot Analysis**: Highlights outliers and data spread.
- **Rolling Average**: Smoothens data for trend analysis.

## 📝 Report
A detailed PDF report summarizing the findings is available in `Industrial_Sensor_Analysis_Report.pdf`.

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
### 🔗 Connect with Me
- GitHub: [ioulasri](https://github.com/ioulasri)
- Gmail: imad.oulasri01@gmail.com

