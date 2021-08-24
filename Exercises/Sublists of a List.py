#Finds every possible sublist in a given list

print("Print sublists of a list.")

usr_input = input("Enter a list: ")

input_list = usr_input.split(',')
new_list = []
counter = 0
in_list = False

for i in input_list:
    new_val = i.replace('[', '').replace(']', '').strip()
    if(len(new_list) == 0):
        new_list.append([new_val])
        continue
    for sublist in new_list:
        if(new_val in sublist):
            in_list = True
            sublist.append(new_val)
            break
    if(not in_list):
        new_list.append([new_val])
    counter += 1

print(new_list)
