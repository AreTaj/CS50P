# Problem Set 2
# Just setting up my twttr

phrase = input("Input: ")
vowels = ["a","e","i","o","u","A","E","I","O","U"]
phrase_list = list(phrase)

for i in range(len(phrase_list)):
    if phrase_list[i] in vowels:
        phrase_list[i] = ""
    
new_phrase = ''.join(phrase_list)
print(new_phrase)

#phrase = list_phrase


#for char in phrase:
#    if char in vowels:
#        new_phrase = phrase.replace(vowels,"")
#
#print(new_phrase)

#for vowels in phrase:
#    print("test")