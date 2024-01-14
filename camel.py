# Problem Set 2
# camelCase

text = input("Input in camel case: ")
new_text = ""

for char in text:
    if char.isupper():
        new_text += "_" + char.lower()
    else:
        new_text += char

print(new_text)




"""
def main():
    text = input("Input in camel case: ")
    new_text = ""
    convert(text)
    print(new_text)

def convert(text):
    for char in text:
        if char.isupper():
            new_text += "_" + char.lower()
        else:
            new_text += char

main()
"""