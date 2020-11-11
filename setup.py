import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='knox-source-data-io',
    packages=setuptools.find_packages(),
    description='Package for important and exporting JSON files generated based on the source data for the Knox project',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='0.0.6',
    url='https://repos.libdom.net/knox_source_data_io',
    author='Niels F. S. Vistisen, Thomas G. Lorentzen',
    author_email='nvisti18@student.aau.dk, tglo18@student.aau.dk',
    keywords=['Knox', 'I/O', 'JSON'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
