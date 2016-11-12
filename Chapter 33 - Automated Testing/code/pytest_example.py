# execute command : py.test pytest_example.py

def func(x):
    return x + 1


def test_answer_correct():
    assert func(3) == 4


def test_answer_wrong():
    assert func(3) == 5