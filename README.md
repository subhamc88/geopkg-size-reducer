# GeoPackage Reducer

This Python package provides utilities for handling GeoPackage (GPKG) files, including compression, decompression, file retrieval, merging, and splitting.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [File Retrieval](#file-retrieval)
  - [Splitting Geopackage Files ](#splitting-geopackage-files)
  - [Compression](#compression)
  - [Decompression](#decompression)
  - [Merging GeoPackage Files](#merging-geopackage-files)
- [License](#license)

## Installation

Ensure you have Python 3.x installed. Install dependencies using pip:

```python
pip install py7zr geopandas pandas
```

## Dependencies

- py7zr: For compressing and decompressing files using the .7z format.
- geopandas: For reading, writing GeoPackage files, and performing spatial operations.
- pandas: For handling data structures and data analysis in Python.

## Usage

### File Retrieval

Retrieve files with a specific extension from a directory and its subdirectories:

```python

from geopackage_utils import get_files

file_list = get_files("/directory/path", file_extension=".gpkg")
```

### Splitting GeoPackage Files

Split a large GeoPackage file into smaller parts:

```python
from geopackage_utils import split_files

split_files("/large/gpkg/file.gpkg", number_of_division=4)
```

### Compression

Compress files in a directory to .7z format:
```python

from geopackage_utils import compress_files

compress_files("/path/to/files")
```


### Decompression

Decompress .7z files into a specified directory:

```python

from geopackage_utils import decompress_files

decompress_files("/path/to/compressed/file.7z", "/output/path")
```

### Merging GeoPackage Files

Merge multiple .gpkg files into a single GeoPackage file:

```python

from geopackage_utils import merge_files

merge_files("/directory/with/gpkg/files", "/output/merged.gpkg")
```

## License

This project is licensed under the GNU General Public License v3.0 (GNU GPLv3).
