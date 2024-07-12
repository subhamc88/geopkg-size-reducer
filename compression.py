import os

from py7zr import SevenZipFile


def compress_files(file_path, output_path=None):
    if output_path is None:
        output_path = os.path.dirname(file_path)

    for filename in os.listdir(file_path):
        file = os.path.join(file_path, filename)
        if os.path.isfile(file):
            output_filename = os.path.join(output_path, f"{filename}.7z")
            with SevenZipFile(output_filename, "w") as archive:
                archive.write(file, arcname=filename)
                print(f"Compressed {file} to {output_filename}")
