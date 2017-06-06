import pytest


if __name__ == "__main__":
    pytest.main(["test_sample_pytest.py", '-s', '-v', "--alluredir=test"])