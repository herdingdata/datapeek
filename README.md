# Datapeek

A tool for peeking at data from a variety of different formats.
When you just need to know what's in the file.

## Supported file types

- parquet
- avro

## Usage

```datapeek [filepath]```

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
