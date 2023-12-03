# Development Guidelines

In order to improve the code maintainace some practices should be followed:

## Always use Pylint and Black
To use both applications you should you the commands:
```shell
python -m black src
python -m pylint --recursive=y src
```

Or you could use from the root directory:
```shell
python ./tools/format_check.py --path path/to/be/analyzed
```
