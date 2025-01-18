# aff_pop.py

import matplotlib.pyplot as plt
from load_csv import load


def convert_population(population: str) -> float:
    """
    Convert a population string with suffix (k, M, B, T) to a float.
    """
    suffixes = {"k": 1e3, "M": 1e6, "B": 1e9, "T": 1e12}
    for suffix, multiplier in suffixes.items():
        if suffix in population:
            return float(population.replace(suffix, "")) * multiplier
    return float(population)  # No suffix, assume raw number


def extract_population(dataset, country, years_range=(1800, 2050)):
    """
    Extract years and population for a specific country within a year range.

    Parameters:
    dataset (pd.DataFrame): The dataset to extract from.
    country (str): The country name to filter.
    years_range (tuple): Range of years to filter (default: 1800 to 2050).

    Returns:
    tuple: Filtered years and population values.
    """
    country_data = dataset[dataset["country"] == country]
    if country_data.empty:
        raise ValueError(f"Error: Data for {country} not found.")

    # Convert year columns to integers
    years = list(map(int, country_data.columns[1:]))
    population = [
        convert_population(value) for value in country_data.values[0][1:]
    ]  # Convert population

    # Filter by year range
    filtered = [
        (year, pop)
        for year, pop in zip(years, population)
        if years_range[0] <= year <= years_range[1]
    ]
    return zip(*filtered)  # Unpack years and populations as separate lists


def main(
        country1="France", country2="Belgium", csv_path="population_total.csv"
        ):
    """
    Main function to compare the population of two countries over time.
    """
    try:
        dataset = load(csv_path)
        if dataset is None:
            raise FileNotFoundError("Dataset could not be loaded.")

        # Extract data for both countries
        years1, pop1 = extract_population(dataset, country1)
        years2, pop2 = extract_population(dataset, country2)

        # Plot the data
        # Country 2 in blue
        plt.plot(years2, pop2, label=country2, color="blue")
        # Country 1 in green
        plt.plot(years1, pop1, label=country1, color="green")

        # Customize the plot
        # plt.title(f"{country1} vs {country2} Population Projections")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(ticks=range(1800, 2041, 40))
        plt.ylabel("Population")
        plt.yticks(ticks=[20e6, 40e6, 60e6], labels=["20M", "40M", "60M"])
        plt.legend(loc="lower right")

        plt.show()

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main("France", "Belgium", "population_total.csv")
