def intoASCII():
    reply = "y"
    inputCharacter = input("Enter a character to be converted to ASCII:")
    resultASCII = ord(inputCharacter)
    print(inputCharacter,"in ASCII Unicode is",resultASCII)

#main program
intoASCII()


def intoEnglish():
    reply = "y"
    inputASCII = int(input("Enter ASCII to be converted into characters:"))
    resultCharacter = chr(inputASCII)
    print(inputASCII,"in ASCII Unicode is",resultCharacter)
    reply = input("Do you want to convert more ASCII?").lower()
    if reply == "y":
      intoEnglish()

#main program
intoEnglish()


#Dr. Hughes's work:
def char_to_denary():
    print("Program to convert a Unicode character into denary")
    reply = "y"
    while reply == "y":
        char = input("Enter character ? ")
        print(ord(char))

        reply = input("Do you want to continue another character Y or N ?").lower()
        if reply == "y":
          char_to_denary()
char_to_denary()


def denary_to_char():
    print("Program to convert denary value into Unicode character")
    reply = "y"
    while reply == "y":
        char = int(input("Enter denary value? "))
        print(ord(char))

        reply = input("Do you want to continue another character Y or N ?").lower()
        if reply == "y":
          denary_to_char()
denary_to_char()
