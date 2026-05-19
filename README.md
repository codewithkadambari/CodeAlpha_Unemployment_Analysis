# Unemployment Analysis with Python

## 📌 Project Overview
This project focuses on the exploratory data analysis (EDA) of unemployment trends in India. By leveraging Python's powerful data manipulation and visualization libraries, this analysis uncovers underlying patterns, statistical distributions, and correlations within the labor market data.

## 🎯 Objectives
- **Data Loading & Cleaning**: Ingesting the dataset and resolving any missing values to ensure data integrity.
- **Statistical Profiling**: Generating comprehensive summaries of the dataset's structural and statistical properties.
- **Data Visualization**: Creating a suite of visual representations to better understand the distribution and trends of unemployment rates.

## 🛠️ Technologies & Libraries Used
- **Python 3.x**: The core programming language.
- **Pandas**: Utilized for efficient data manipulation, cleaning, and statistical analysis.
- **Matplotlib & Seaborn**: Employed for generating high-quality, insightful data visualizations.

## 📊 Visualizations Generated
The script automatically generates and saves the following analytical plots:
1.  **`histogram.png`**: Displays the frequency distribution of unemployment rates.
2.  **`lineplot.png`**: Illustrates the chronological trend of unemployment over the dataset's index.
3.  **`boxplot.png`**: Highlights the central tendency and identifies potential outliers in the data.
4.  **`heatmap.png`**: Provides a correlation matrix to identify relationships between different numerical variables.
5.  **`bargraph.png`**: Showcases a localized comparison of the top records in the dataset.

## 🚀 How to Run the Project
1.  **Prerequisites**: Ensure you have the required libraries installed:
    ```bash
    pip install pandas matplotlib seaborn
    ```
2.  **Dataset Configuration**: Update the `file_path` variable in the script to point to the location of your `Unemployment in India.csv` file.
3.  **Execution**: Run the script using Python:
    ```bash
    python unemployment_analysis.py
    ```
4.  **Results**: The script will output statistical summaries to the console and save the generated visualizations in the current directory.

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
