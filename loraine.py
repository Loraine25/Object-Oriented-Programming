#Anonuevo, Loraine N.
#BSCPE 1-4
#Problem 1

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mAyooo! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mYnah\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm proud of you!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, and i'll share some knowledge today!\033[0m")

print("")
print("\033[;45;1;3m*\033[0m" * 70)
print("\033[;1;3mChill and do amazing stuff with me!\033[0m".center(81))
print("\033[;45;1;3m*\033[0m" * 70)

#Instruct the user to enter the encrypted message.
encrypted_message = input(f"\n\033[45;1;3mInput your encrypted message: \033[0m")
decrypted_message = ""

#Count the number of letters you input.
characters_counter = len(encrypted_message)
print(f"\n\033[1mThe count of the characters you have entered is", characters_counter)

#Turn the encrypted to decrypted message
for encrypted in encrypted_message: 

#   If this symbol "*" is/are in the message, change it to letter a
    if "*" in encrypted:
        decrypted_message += "a"

#   If this symbol "&" is/are in the message, change it to letter e
    elif "&" in encrypted:
        decrypted_message += "e"

#   If this symbol "#" is/are in the message, change it to letter i
    elif "#" in encrypted:
        decrypted_message += "i"

#   If this symbol "+" is/are in the message, change it to letter o
    elif "+" in encrypted:
        decrypted_message += "o"

#   If this symbol "!" is/are in the message, change it to letter u
    elif "!" in encrypted:
        decrypted_message += "u"
    else:
        decrypted_message += encrypted

#Print the output
print(f"\n\033[96;1;3mEncrypted Message: \033[0m" + encrypted_message)
print("\033[96;1;3mDecrypted Message: \033[0m" + decrypted_message)

print("")
print("\033[;33;1;3mJob well done, it's nice to meet you!\033[0m".center(84, "~"))
