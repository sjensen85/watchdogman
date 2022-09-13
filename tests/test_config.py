from watchdogman import config
from os import path

def test_load_config():
    config.CONFIG = config.load_config()
    assert config.CONFIG is not None
    assert isinstance(config.CONFIG, config.Config)
    assert config.CONFIG.allow_patterns == ["*.py", ".watchdogman"]
    assert config.CONFIG.directory == path.abspath("./")
    assert config.CONFIG.ignore_patterns == [
        "*.whl",
        "*.tar.gz",
        "*.egg-info",
        "watchdogman-*",
        "build",
        "dist"
    ]
    assert config.CONFIG.ignore_dirs == True
    assert config.CONFIG.command == "pip install ./"
