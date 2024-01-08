# File Extensions
# Problem Set 1

filename = input("File name: ")
filename = filename.lower()

# gif
if(filename.__contains__(".gif")):
    print("image/gif")

# jpg jpeg
elif(filename.__contains__(".jpg") or filename.__contains__(".jpeg")):
    print("image/jpeg")

# png
elif(filename.__contains__(".png")):
    print("image/png")

# pdf
elif(filename.__contains__(".pdf")):
    print("application/pdf")

# txt
elif(filename.__contains__(".txt")):
    print("text/plain")

# zip
elif(filename.__contains__(".zip")):
    print("application/zip")

else:
    print("application/octet-stream")