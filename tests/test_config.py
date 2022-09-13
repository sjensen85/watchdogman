from src.watchdogman.config import Config, CONFIG, load_config

def test_load_config():
    CONFIG = load_config()
    assert CONFIG is not None
    assert isinstance(CONFIG, Config)
    assert CONFIG.allow_patterns == ["*.py", "watch.json", "*.yaml"]
    assert CONFIG.directory == "./"
    assert CONFIG.ignore_patterns == [
        "*.whl",
        "*.tar.gz",
        "*.egg-info",
        "watchdogman-*",
        "build",
        "dist"
    ]
    assert CONFIG.ignore_dirs == True
    assert CONFIG.command == "python3 setup.py sdist bdist_egg bdist_wheel"
