import pathlib
import site
import sys


class UTBotPythonConfig:
    JAVA_PATH = "java"
    SITE_DIR = pathlib.Path(site.getsitepackages()[0])
    JAR_FILE = SITE_DIR / "utbot_dist" / "utbot-cli-python-2023.11-SNAPSHOT.jar"
    USVM_PATH = SITE_DIR / "utbot_dist" / "usvm-python"
    PYTHON_PATH = sys.executable
    INCLUDE_MYPY_RUN_IN_TIMEOUT = True
    TIMEOUT = 300_000
