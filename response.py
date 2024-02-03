# Response Validation
# Problem Set 7

from validator_collection import validators, checkers, errors
# import validators
# Do not use re library

def main():
    print(validate(input("What's your email address? ")))

def validate(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"




if __name__ == "__main__":
    main()
