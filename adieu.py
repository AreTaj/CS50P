# Adieu, Adieu
# Problem Set 4

import inflect

p = inflect.engine()
# Creates engine of inflect library to allow use of its methods.

text = ["Adieu", "adieu"]
# List with two initial elements, one for each "adieu"; later, names are appended.

while True:
    try:
        n = input("Name: ")
    except EOFError:
        print()
        break           # Allows exit from program with CTRL D.
    text.append(n)      # append() adds a value to a list, in this case, the text[] list.
text[2] = "to " + text[2]

if len(text) == 3:      # Three list elements, one name. Assumes at least one name will be entered.
    new_text = p.join(text, conj = '')
    # By default, conj = 'and', so remove to meet requirement.
elif len(text) == 4:    # Four list elements, two names.
    new_text = p.join(text, final_sep = "")
else:                   # More than four list elements, more than two names.
    new_text = p.join(text)

print(new_text)