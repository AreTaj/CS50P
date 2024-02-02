# Back to the Bank
# Problem Set 5

from bank import value


def main():
    test_bank_0()
    test_bank_20()
    test_bank_100()

def test_bank_0():
    assert value("Hello") == 0
    assert value(" Hello ") == 0
    assert value(" hello ") == 0
    assert value("hello") == 0

def test_bank_20():
    assert value("hi") == 20
    assert value("help") == 20
    assert value("How are you doing?") == 20

def test_bank_100():
    assert value("What's up?") == 100
    assert value("Weather") == 100

if __name__ == "__main__":
    main()