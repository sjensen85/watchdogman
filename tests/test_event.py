from src.watchdogman.event import throttle

count = 0
count_fail = 0
count_string = 0

@throttle(1)
def fix(a_string):
    print(a_string)
    global count
    count += 1

@throttle(0.0000000000000000000001)
def fix_fail(a_string):
    print(a_string)
    global count_fail
    count_fail += 1

@throttle("1")
def fix_string(a_string):
    print(a_string)
    global count_string
    count_string += 1

def test_throttle():
    fix("first run")
    fix("second run")
    assert count == 1


def test_throttle_fail():
    fix_fail("first run")
    fix_fail("second run")
    assert count_fail == 2

def test_throttle_string():
    fix_string("first run")
    fix_string("second run")
    assert count_string == 1