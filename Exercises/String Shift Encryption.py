print("Encrypt a string with a key of 7.")

string = input("Enter a string: ")
answer = ""

for char in string:
    answer += chr(ord(char)+7)

print(answer)