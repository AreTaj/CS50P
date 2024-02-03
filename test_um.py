# Regular, um, Expressions
# Problem Set 7

from um import count

def main():
    test_case()
    test_word_with_um()
    test_with_spaces()

def test_case():
    assert count("Um, thanks for the album.") == 1
    assert count("Um, um, thanks.") == 2


def test_word_with_um():
    assert count("Album") == 0
    assert count("Penumbra") == 0


def test_with_spaces():
    assert count("Hello um world") == 1
    assert count("Yo um what's up")


if __name__ == "__main__":
    main()