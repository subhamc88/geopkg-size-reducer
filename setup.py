from setuptools import find_packages, setup

setup(
    name="geopkg-size-reducer",
    version="0.1",
    packages=find_packages(),
    install_requires=["geopandas", "pandas", "py7zr", "shapely"],
    entry_points={
        "console_scripts": [],
    },
    author="subhamc88",
    author_email="subham020304@gmail.com",
    long_description=open("README.md").read(),
    long_description_content_type="markdown",
    url="https://github.com/subhamc88/geopkg-size-reducer.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
