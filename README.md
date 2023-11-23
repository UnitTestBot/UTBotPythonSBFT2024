# Python Tool Competition Implementation Using UTBotPython

Uses the python-tool-competition-2024 to generate tests using the UTBotPython.

For more information see
<https://github.com/ThunderKey/python-tool-competition-2024/>.

## Requirements

* Python 3.11, implementation: CPython
* poetry
* OS: Linux
* Java 17, accessible in command line under name `java`
* glibc>=2.31

## Installation

* Install [poetry](https://python-poetry.org/)
* Run `poetry install`

### Check the installation success
* Run `poetry run check`, this command runs simple test generation and shows error messages
* Successful logger messages should end with the following lines:
```
Exit status: 0
............ | INFO  | GlobalPythonEngine | Symbolic: stop receiver
............ | INFO  | PythonTestCaseGenerator | Collect all test executions for some_method
............ | INFO  | SbftGenerateTestsCommand | Saving tests...
```

## Development

The entry point called by `python-tool-competition-2024` is the `build_test`
method in `utbot_python_sbft_2024/generator.py`.

## Calculating Metrics

Run `poetry run python-tool-competition-2024 run utbot-python`.

With `poetry run python-tool-competition-2024 run -h` you can find out what
generators were detected.
