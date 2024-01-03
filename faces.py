# Making Faces
# Problem Set 0

def main():
    emojicon = input()
    emojicon = convert(emojicon)
    print(emojicon)

def convert(emojicon):
    emojicon = emojicon.replace(":)","🙂")
    emojicon = emojicon.replace(":(","🙁")
    return emojicon

main()