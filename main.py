import polars as pl
from typing import List
import os
import json

csvs_folder = "/home/alejoseed/Projects/hyper-table/front-end/src/dummy_data"

name_jsons = {
    "first_name": csvs_folder + "/first_name.json",
    "last_name": csvs_folder + "/last_name.json"
}

def load_polars_table():
    return 0


def convert_jsons_to_csv() -> List[str]:
    if not os.path.exists(csvs_folder):
        print("No csvs folders exists. Please verify path...")
        return []
    
    try:
        created_csv_files : List[str] = []
        for name_type, folder in name_jsons.items():
            name_type_df = pl.read_json(source=folder).explode(name_type)
            
            name_type_df = name_type_df.shrink_to_fit()
            file_to_write_path = f'{csvs_folder}/{name_type}.csv'
            name_type_df.write_csv(file=file_to_write_path)
            created_csv_files.append(file_to_write_path)
        return created_csv_files
    except Exception as e:
        print(e)
        return []
    
def main():
    csvs = convert_jsons_to_csv()

    if csvs is None:
        print("No CSVs were creating, verify JSONs path, exiting...")
        exit(1)

    print(csvs)

if __name__ == "__main__":
    main()
