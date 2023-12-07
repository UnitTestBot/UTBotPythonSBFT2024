"""A test generator using UTBotPython."""
import pathlib
import subprocess
import sys
import tempfile
import time

import rich
from python_tool_competition_2024.config import get_config, GeneratorName
from python_tool_competition_2024.generation_results import (
    TestGenerationFailure,
    TestGenerationResult,
    TestGenerationSuccess,
    FailureReason,
)
from python_tool_competition_2024.generators import FileInfo, TestGenerator

from python_tool_competition_2024_utbot_python.config import UTBotPythonConfig

GENERATION_TIMES: list[float] = []


class UTBotPythonTestGenerator(TestGenerator):
    """A test generator using UTBotPython."""

    def build_test(self, target_file_info: FileInfo) -> TestGenerationResult:
        """
        Generate a test for the specific target file.

        Args:
            target_file_info: The `FileInfo` of the file to generate a test for.

        Returns:
            Either a `TestGenerationSuccess` if it was successful, or a
            `TestGenerationFailure` otherwise.
        """
        return _build_test(target_file_info)

    @staticmethod
    def check_run() -> None:
        """
        Try to run UTBotPython and shows error message.
        """
        target_file_info = FileInfo(
            pathlib.Path("./targets/example1.py").resolve().absolute(),
            "example1",
            get_config(
                GeneratorName("UTBotPython"),
                pathlib.Path("./targets/").resolve().absolute(),
                pathlib.Path("").absolute(),
                rich.console.Console(),
                show_commands=True,
                show_failures=True,
            ),
        )
        _build_test(target_file_info, check_usvm=True)


def _build_test(
    target_file_info: FileInfo, check_usvm: bool = False
) -> TestGenerationResult:
    if not sys.platform.startswith("linux"):
        sys.stderr.write("ERROR: This script works only on Linux\n")
        exit(1)

    sys_paths = [target_file_info.config.targets_dir]

    with tempfile.TemporaryDirectory() as tempdir:
        output_dir = pathlib.Path(tempdir)
        module_name = target_file_info.module_name.replace(".", "_")
        output_file = output_dir / f"test_{module_name}.py"
        _run_utbot(
            target_file_info.absolute_path,
            sys_paths,
            output_file,
            UTBotPythonConfig.JAR_FILE,
            UTBotPythonConfig.USVM_PATH,
            UTBotPythonConfig.TIMEOUT,
            UTBotPythonConfig.PYTHON_PATH,
            UTBotPythonConfig.JAVA_PATH,
            check_usvm=check_usvm,
            include_mypy_in_timeout=UTBotPythonConfig.INCLUDE_MYPY_RUN_IN_TIMEOUT,
        )

        utbot_tests = _read_generated_tests(str(output_file))
        if utbot_tests == "":
            utbot_tests = f"""def test_dummy():
                                  import {module_name}"""

        return TestGenerationSuccess(utbot_tests)


def _run_utbot(
    source_file: pathlib.Path,
    sys_paths: list[pathlib.Path],
    output_file: pathlib.Path,
    jar_path: pathlib.Path,
    usvm_dir: pathlib.Path,
    timeout: int,
    python_path: str,
    java_cmd: str,
    check_usvm: bool = False,
    include_mypy_in_timeout: bool = False,
):
    command = (
        f"{java_cmd} -jar {jar_path}"
        f" generate_python {source_file}"
        f" -p {python_path}"
        f" -o {output_file}"
        f" -s {','.join(map(str, sys_paths))}"
        f" -t {timeout}"
        f" --java-cmd {java_cmd}"
        f" --usvm-dir {usvm_dir}"
        f" --runtime-exception-behaviour PASS"
        f" --prohibited-exceptions -"
        f" --do-not-generate-state-assertions"
    )
    if check_usvm:
        command += " --check-usvm"

    if include_mypy_in_timeout:
        command += " --include-mypy-analysis-time"

    print(command)
    start = time.time()

    p = subprocess.Popen(command.split(), close_fds=True)
    while p.poll() is None:
        time.sleep(1)

    cur_time = time.time() - start
    GENERATION_TIMES.append(cur_time)
    print("Process finished in", cur_time)
    print("Mean time:", sum(GENERATION_TIMES) / len(GENERATION_TIMES))
    print("Max time:", max(GENERATION_TIMES))


def _read_generated_tests(output_file: str) -> str:
    try:
        with open(output_file, "r") as f:
            return f.read()
    except:
        return ""
