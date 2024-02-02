# Problem Set 5
# Just setting up my twttr

def main():
    shorten(input("Input: "))


def shorten(word):
    #word = input("Input: ")
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    word_list = list(word)

    for i in range(len(word_list)):
        if word_list[i] in vowels:
           word_list[i] = ""
    
    new_word = ''.join(word_list)
    print(new_word)


if __name__ == "__main__":
    main()






