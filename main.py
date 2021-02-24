def char_to_unicode():
  print("char --> Unicode")
  input_char = input("Enter character: ")
  while len(input_char) != 1:
    input_char = input("Must be 1 character: ")
  print(f"\"{input_char}\" in Unicode is {ord(input_char)}")
#====================
def unicode_to_char():
  print("Unicode --> char")
  input_code = int(input("Enter Unicode: "))
  print(f"{input_code} in Unicode is \"{chr(input_code)}\"")
#====================
def menu():
  print("Choose method:\n\t[1] char --> Unicode\n\t[2] Unicode --> char")
  option = input("\t--> ")
  while int(option) not in [1,2]:
    option = input("\n\t--> ")
  option = int(option) #cast to integer once valid
  
  if option == 1:
    char_to_unicode()
    menu() #recursive
  elif option == 2:
    unicode_to_char()
    menu() #recursive
#====================
# MAIN PROGRAM
menu()