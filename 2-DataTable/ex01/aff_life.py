# aff_life.py

import matplotlib.pyplot as plt
from load_csv import load


# def main():
def main(country: str, dataset_path: str = "life_expectancy_years.csv"):
    # Load the dataset
    dataset = load(dataset_path)

    if dataset is None:
        print("Error: Failed to load the dataset.")
        return

    # Extract data for country
    country_data = dataset[dataset["country"] == country]

    if country_data.empty:
        print(f"Error: Data for {country} not found.")
        return

    # Extract years and life expectancy values
    years = country_data.columns[1:]  # Skip the 'country' column
    life_expectancy = country_data.values[0][1:]  # Skip the 'country' value

    # Convert years to integers and life_expectancy to floats
    years = [int(year) for year in years]
    life_expectancy = [float(value) for value in life_expectancy]

    # Plot the data
    plt.plot(years, life_expectancy, label=country)

    # Add title and labels
    plt.title(f"{country} Life Expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life Expectancy")

    # Add a legend
    plt.legend()

    # Show the plot
    plt.show()


if __name__ == "__main__":
    main("France", "life_expectancy_years.csv")
