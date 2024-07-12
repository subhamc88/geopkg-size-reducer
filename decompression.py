import os

from py7zr import SevenZipFile


def decompress_files(file_path, output_path=None):
    if output_path is None:
        output_path = os.path.dirname(file_path)

    if os.path.isdir(file_path):
        for filename in os.listdir(file_path):
            if filename.endswith(".7z"):
                file = os.path.join(file_path, filename)
                with SevenZipFile(file, "r") as archive:
                    archive.extractall(path=output_path)
                    print(f"Extracted {file} to {output_path}")
    if os.path.isfile(file_path):
        with SevenZipFile(file_path, "r") as archive:
            archive.extractall(path=output_path)
            print(f"Extracted {file_path} to {output_path}")
    else:
        print(f"Error: {file_path} is not a valid .7z file or directory")
