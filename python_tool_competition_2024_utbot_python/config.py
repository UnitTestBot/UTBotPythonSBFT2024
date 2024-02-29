import pathlib
import site
import sys
from enum import Enum


class Mode(Enum):
    BOTH = "both"
    SYMBOLIC = "symbolic"
    FUZZING = "fuzzing"


class UTBotPythonConfig:
    JAVA_PATH = "java"
    SITE_DIR = pathlib.Path(site.getsitepackages()[0])
    JAR_FILE = SITE_DIR / "utbot_dist" / "utbot-cli-python.jar"
    USVM_PATH = SITE_DIR / "utbot_dist" / "usvm-python"
    PYTHON_PATH = sys.executable
    INCLUDE_MYPY_RUN_IN_TIMEOUT = True
    TIMEOUT = 60_000
    MODE = Mode.SYMBOLIC
    ONLY_TOPLEVEL = False
    PATH_SELECTOR = "BaselinePriorityDfs"
