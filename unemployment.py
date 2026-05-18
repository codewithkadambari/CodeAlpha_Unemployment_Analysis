import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================================
# CODEALPHA DATA SCIENCE INTERNSHIP
# TASK 2 : UNEMPLOYMENT ANALYSIS
# =========================================
def main():
    print("\n======================================")
    print(" UNEMPLOYMENT ANALYSIS PROJECT ")
    print("======================================\n")
    
    # -----------------------------------
    # FILE PATH
    # -----------------------------------

    file_path = "C:\\Users\\HP\\Downloads\\Unemployment in India.csv"

    # -----------------------------------
    # CHECK FILE EXISTS
    # -----------------------------------

    if not os.path.exists(file_path):

        print(" ERROR : Dataset file not found")
        print("\nCheck your file path.")
        return

    # -----------------------------------
    # LOAD DATASET
    # -----------------------------------

    df = pd.read_csv(file_path)

    print(" Dataset Loaded Successfully\n")

    # -----------------------------------
    # DISPLAY DATASET
    # -----------------------------------

    print("First 5 Rows:\n")

    print(df.head())

    print("\n-----------------------------------")
    print("Dataset Information")
    print("-----------------------------------\n")

    print(df.info())

    print("\n-----------------------------------")
    print("Statistical Summary")
    print("-----------------------------------\n")

    print(df.describe())

    print("\n-----------------------------------")
    print("Missing Values")
    print("-----------------------------------\n")

    print(df.isnull().sum())

    # -----------------------------------
    # REMOVE MISSING VALUES
    # -----------------------------------

    df.dropna(inplace=True)

    # -----------------------------------
    # VISUALIZATION
    # -----------------------------------

    sns.set_style("whitegrid")

    # Get last numeric column
    numeric_column = df.select_dtypes(include='number').columns[-1]

    # -----------------------------------
    # HISTOGRAM
    # -----------------------------------

    plt.figure(figsize=(8,6))

    sns.histplot(df[numeric_column], kde=True)

    plt.title("Unemployment Distribution")

    plt.savefig("histogram.png")

    plt.show()

    # -----------------------------------
    # LINE GRAPH
    # -----------------------------------

    plt.figure(figsize=(12,6))

    plt.plot(df[numeric_column])

    plt.title("Unemployment Trend")

    plt.xlabel("Index")

    plt.ylabel("Rate")

    plt.savefig("lineplot.png")

    plt.show()

    # -----------------------------------
    # BOXPLOT
    # -----------------------------------

    plt.figure(figsize=(8,6))

    sns.boxplot(x=df[numeric_column])

    plt.title("Boxplot")

    plt.savefig("boxplot.png")

    plt.show()

    # -----------------------------------
    # HEATMAP
    # -----------------------------------

    plt.figure(figsize=(10,6))

    correlation = df.corr(numeric_only=True)

    sns.heatmap(
        correlation,
        annot=True,
        cmap="coolwarm"
    )

    plt.title("Correlation Heatmap")

    plt.savefig("heatmap.png")

    plt.show()

    # -----------------------------------
    # BAR GRAPH
    # -----------------------------------

    plt.figure(figsize=(10,6))

    df[numeric_column].head(10).plot(kind='bar')

    plt.title("Top 10 Records")

    plt.savefig("bargraph.png")

    plt.show()

    # -----------------------------------
    # FINAL MESSAGE
    # -----------------------------------

    print("\n======================================")
    print(" PROJECT COMPLETED SUCCESSFULLY ")
    print("======================================\n")

    print("Generated Graph Files:\n")

    print("1. histogram.png")
    print("2. lineplot.png")
    print("3. boxplot.png")
    print("4. heatmap.png")
    print("5. bargraph.png")


# =========================================
# MAIN FUNCTION
# =========================================

if __name__ == "__main__":
    main()