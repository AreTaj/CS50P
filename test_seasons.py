# Seasons of Love
# Problem Set 8

import seasons
from seasons import check_birthday

def main():
    test_check_birthday()


def test_check_birthday():
    assert check_birthday("1999-01-02") == ("1999", "01", "02")
    assert check_birthday("January 1, 1999") == None
    assert check_birthday("1995-1-1") == None


if __name__ == "__main__":
    main()