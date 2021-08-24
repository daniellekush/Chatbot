#Gets character input and encrypts it with a shift key of value +3

print("Substitute a character with a key of 3.")

character = input("Enter a character: ")

answer = chr(ord(character)+3)

print(answer)
