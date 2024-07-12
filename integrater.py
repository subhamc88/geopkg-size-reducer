import geopandas as gpd
import pandas as pd

from get_files import get_files


def merge_files(input_directory, output_file):
    file_list = get_files(input_directory, file_extension=".gpkg")
    gdf_list = []

    for file in file_list:
        gdf = gpd.read_file(file)
        gdf_list.append(gdf)

    merged_gdf = pd.concat(gdf_list, ignore_index=True)

    crs = gdf_list[0].crs
    merged_gdf = gpd.GeoDataFrame(merged_gdf, crs=crs)

    merged_gdf.to_file(output_file, driver="GPKG")
    print(f"Merged GPKG file saved to: {output_file}")
