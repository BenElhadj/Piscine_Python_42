# load_csv.py

import pandas as pd


def load(path: str) -> None:
    """
    Load a dataset from a CSV file, display its dimensions,
    and print the first two rows.

    Parameters:
    path (str): The path to the CSV file.

    Returns:
    None: The function does not return anything.
    """
    try:
        # Load the dataset from the CSV file
        dataset = pd.read_csv(path)

        # Print the dimensions of the dataset
        print(f"Loading dataset of dimensions {dataset.shape}")

        # Return None to avoid printing the dataset in tester.py

        if dataset is not None:
            # # Extract the column names and first row
            # columns = list(dataset.columns)
            # first_row = dataset.iloc[0].values
            # first_col = f"{' '.join(map(str, columns[1:5]))}"
            # last_col = f"{' '.join(map(str, columns[-5:]))}"

            # # Format the header
            # header = f"{columns[0]} {first_col} ... {last_col}"

            # # Format the first row
            # row = f"{first_row[0]} {first_col} ... {last_col}"
            # to_print = f"{header}\n{row}\n  ..."
            # return to_print
            return dataset
        return None

    except FileNotFoundError:
        return "FileNotFoundError: The file was not found."
    except pd.errors.EmptyDataError:
        return "EmptyDataError: The file is empty."
    except pd.errors.ParserError:
        return "ParserError: The file is not a valid CSV file."
    except TypeError as e:
        return f"TypeError: {e}"
    except ValueError as e:
        return f"ValueError: {e}"
    except Exception as e:
        return f"Exception: An unexpected error occurred: {e}"


# Example usage
if __name__ == "__main__":
    print(load("life_expectancy_years.csv"))
