# Datapeek

A tool for peeking at data from a variety of different formats.
When you just need to know what's in the file. 

Under the hood, this loads data into a pandas dataframe then inspects the resulting object, 
so it is best suited to flat files (not hierarchical data).

## Supported file types

Datapeek uses the file's extension to determine the file type, so your file must end with one of the
following:

- parquet
- avro
- csv

## Usage

sample output for a file with 3 columns and one row
```
$ datapeek [filepath]

Size:

Number of rows: 2
Number of columns: 3

Pandas preview:

      col1  col2    col3
0       11    15    row1
1       84    28    row2

Columns:
('col1', 'int64')
('col2', 'int32')
('col3', 'object', 'max_length=4')
```

The `-c/--columns` switch shows a description of the columns
(along with the max length of values in any text fields):

```
$ datapeek [filepath] --columns

Columns:
('col1', 'int64')
('col2', 'int32')
('col3', 'object', 'max_length=18')
```

The `-s/--size` switch to shows a description of how big the data is:

```
$ datapeek [filepath] --size
1 rows x 3 columns
```
The `-r/--recursive` switch allows you to pass an entire folder (as long as the folder contains 
files which all have an identical, supported, file extension):

```
$ datapeek [folderpath] --recursive [optionally any other switches]
```

## Getting started as a developer
1. `git clone` the repo

2. `cd /path/to/wherever/you/saved/it`

3. create a virtualenv `mkvirtualenv datapeek -p /usr/local/bin/python3.7`

4. `make requirements`

5. install the package to your virtualenv `pip install --editable .`

Optional step: create a symlink somewhere that's on your path

```
ln -s ~/.virtualenvs/datapeek/bin/datapeek ~/bin/datapeek
```
