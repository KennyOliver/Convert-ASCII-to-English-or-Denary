def intoASCII():
  reply = "y"
  input_char = input("Enter a character to be converted to ASCII: ")
  print(f"\"{input_char}\" in Unicode is {ord(input_char)}")
#====================
def intoEnglish():
  reply = "y"
  input_code = int(input("Enter ASCII to be converted into characters: "))
  print(f"\"{input_code}\" in Unicode is {chr(input_code)}")
  reply = input("Do you want to convert more ASCII?\n--> ").lower()
  if reply == "y":
    intoEnglish()
#====================
# MAIN PROGRAM
intoASCII()
intoEnglish()