#Finds the occurences of 'test' in a string

print("Count the occurences of the word 'test' in string.")

string = input("Enter a string: ")
answer = 0

words = string.split(" ")

for word in words:
    if (word.lower() == "test"):
        answer += 1

print(answer)
