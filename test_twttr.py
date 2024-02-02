# Problem Set 5
# Testing my twttr

from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("hello") == "hll"

if __name__ == "__main__":
    main()