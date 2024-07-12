import os
import shutil

import geopandas as gpd


def split_files(file_path, number_of_division=4):

    print(f"Processing file: {file_path}")

    # Determine output directory for split files
    dataset_path = os.path.dirname(file_path)
    print(dataset_path)
    split_files_path = os.path.join(dataset_path, "split_files")
    print(split_files_path)

    # Delete and recreate split_files directory if it exists
    if os.path.exists(split_files_path):
        shutil.rmtree(split_files_path)
        print(f"Deleted existing split files directory: {split_files_path}")
    os.makedirs(split_files_path)
    print(f"Created split files directory: {split_files_path}")

    # Read the GeoPackage file
    gdf = gpd.read_file(file_path)
    total_features = len(gdf)
    print(f"Total features in {os.path.basename(file_path)}: {total_features}")

    # Calculate features per chunk
    features_per_chunk = total_features // number_of_division

    # Split the GeoDataFrame and save to files
    for each_division in range(number_of_division):
        starting_index = each_division * features_per_chunk
        ending_index = (each_division + 1) * features_per_chunk
        if each_division == number_of_division - 1:
            ending_index = total_features
        split_gdf = gdf.iloc[starting_index:ending_index]
        split_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}_part{each_division + 1}.gpkg"
        split_filepath = os.path.join(split_files_path, split_filename)
        split_gdf.to_file(split_filepath, driver="GPKG")
        print(
            f"Split {each_division + 1}/{number_of_division} saved to: {split_filepath}"
        )

    print(f"Splits saved in: {split_files_path}")
