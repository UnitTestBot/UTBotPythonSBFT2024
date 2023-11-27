# Python Tool Competition Implementation Using UTBotPython

Uses the python-tool-competition-2024 to generate tests using the UTBotPython.

For more information see
<https://github.com/ThunderKey/python-tool-competition-2024/>.

## Requirements

* Python 3.11, implementation: CPython
* OS: Linux
* Java 17, accessible in command line under name `java`
* glibc>=2.31

## Installation

* Install [poetry](https://python-poetry.org/)
* Run `poetry install`

### Check the installation
* Run `poetry run check`.
* Successful logger messages should end with the following lines:
```
VenvConfig: VenvConfig(basePath=..., libPath=..., binPath=...)
Exit status: 0 (Success)
............ | INFO  | GlobalPythonEngine | Symbolic: stop receiver
............ | INFO  | PythonTestCaseGenerator | Collect all test executions for some_method
............ | INFO  | SbftGenerateTestsCommand | Saving tests...
Process finished in ...
Mean time: ...
Max time: ...
```

If you get a message `No VenvConfig`, virtual environment in our interpreter was not activated for some reason.

If you get a message `Exit status: ... (Failure)`, `usvm-python` could not be run for some reason.

## Configuration

Configuration is set in `python_tool_competition_2024_utbot_python/config.py`.

You can specify the time budget with the option `TIMEOUT`. Now it is set to 300 seconds. The tool will probably spend all given time.

## Development

The entry point called by `python-tool-competition-2024` is the `build_test`
method in `python_tool_competition_2024_utbot_python/generator.py`.

## Calculating Metrics

Run `poetry run python-tool-competition-2024 run utbot-python`.

With `poetry run python-tool-competition-2024 run -h` you can find out what
generators were detected.
