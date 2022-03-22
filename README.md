# cfc - cfc 

Comunidad Familia Cristiana

## Usage

####  Environment variables

Add if needed

#### Correct usage

With the virtual env activated, run: 

```
python cfc.py --fill-me-in
```

#### Incorrect usage

Add if needed


## Getting Started

### Python Dependencies

See the `requirements` directory for required Python modules for building, testing, developing etc.
They can all be installed in a [virtual environment](https://docs.python.org/3/library/venv.html) 
using the follow commands:

```
python3 -m venv venv
source venv/bin/activate
pip install -r ./requirements/dev.txt -r ./requirements/prod.txt -r ./requirements/test.txt
```

There's also a bin script to do this:

```
./tools/create_venv.sh
```


## Developer Guide

The following is documentation for developers that would like to contribute
to cfc.

### Pycharm Note

Make sure you mark `cfc` and `./test` as source roots!

### Testing

This project uses pytest to manage and run unit tests. Unit tests located in the `test` directory 
are automatically run during the CI build. You can run them manually with:

```
./tools/run_tests.sh
```

### Local Linting

There are a few linters/code checks included with this project to speed up the development process:

* Black - An automatic code formatter, never think about python style again.
* Isort - Automatically organizes imports in your modules.
* Pylint - Check your code against many of the python style guide rules.
* Mypy - Check your code to make sure it is properly typed.

You can run these tools automatically in check mode, meaning you will get an error if any of them
would not pass with:

```
./tools/run_checks.sh
```

Or actually automatically apply the fixes with:

```
./tools/apply_linters.sh
```

There are also scripts in `./tools/` that include run/check for each individual tool.


