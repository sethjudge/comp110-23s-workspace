"""Writing Functions for exercise 8"""


__author__ = "730569838"


from io import TextIOWrapper


DATA_DIRECTORY: str = "../../data"
DATA_FILE_PATH: str = f"{DATA_DIRECTORY}/nc_durham_2015_march_21_to_26.csv"


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Reads a CSV file and says how many rows there are."""
    rows: list[str] = []
    file_handle: TextIOWrapper = open(csv_file, "r")
    for row in file_handle:
        row = row.strip()
        row = row.lower()
        rows.append(row)
    return rows