word = input("Please insert a word or sentence\n")
if len(word) < 2:
    print("")
else:
    print(word[:2]+word[-2:])