# Numb3rs
# Problem Set 7

from numb3rs import validate

def main():
    test_format()
    test_range()
    
# Input must be of format x.x.x.x    
def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1") == False

# Each segment of input must be in range (0,255]
def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"500.255.255.255") == False
    assert validate(r"255.500.255.255") == False
    assert validate(r"255.255.500.255") == False
    assert validate(r"255.255.255.500") == False


if __name__ == "__main__":
    main()