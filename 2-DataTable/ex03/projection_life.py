# projection_life.py

import matplotlib.pyplot as plt
from load_csv import load


def main(
    life_expectancy_file: str = "life_expectancy_years.csv",
    income_file: str =
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
    year: str = "1900",
):
    """
    Main function to display the projection of life expectancy
    in relation to the gross national product for a given year.

    Parameters:
    life_expectancy_file (str): The path to the life expectancy
    CSV file (default: "life_expectancy_years.csv").
    income_file (str): The path to the income CSV file (default:
    "income_per_person_gdppercapita_ppp_inflation_adjusted.csv").
    year (str): The year to analyze (default: "1900").
    """
    # Load the life expectancy dataset
    life_expectancy_dataset = load(life_expectancy_file)

    if life_expectancy_dataset is None:
        print("Error: Failed to load the life expectancy dataset.")
        return

    # Load the income dataset
    income_data = load(income_file)

    if income_data is None:
        print("Error: Failed to load the income dataset.")
        return

    # Check if the year exists in both datasets
    if (
        year not in life_expectancy_dataset.columns
        or year not in income_data.columns
    ):
        print(
            f"Error: Data for the year {year} not found in datasets."
        )
        return

    # Extract life expectancy and income data for the specified year
    life_expectancy = life_expectancy_dataset[["country", year]]
    income = income_data[["country", year]]

    # Merge the two datasets on the 'country' column
    merged_data = life_expectancy.merge(
        income, on="country", suffixes=("_life", "_income")
    )

    # Drop rows with missing values
    merged_data = merged_data.dropna()

    # Extract life expectancy and income values
    life_expectancy_values = merged_data[f"{year}_life"]
    income_values = merged_data[f"{year}_income"]

    # Plot the data
    plt.scatter(
        income_values, life_expectancy_values, color="blue", label=year
    )
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=["300", "1k", "10k"])
    plt.title(year)
    plt.xlabel("Gross domestic Product")
    plt.ylabel("Life Expectancy")

    # Show the plot
    plt.show()


if __name__ == "__main__":
    # Example usage with default files and year
    main(
        "life_expectancy_years.csv",
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv",
        "1900",
    )
