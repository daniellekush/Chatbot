import json

movie_lines = []
data = {}
data['intents'] = []
tag = 0

with open('movie_lines.txt', 'r', encoding='iso-8859-1') as file:
    for r in file.readlines():
        temp_list = r.split(' +++$+++ ')
        movie_lines.append(temp_list)

def fileInsertion(parent, child):
    global tag
    tag += 1
    data['intents'].append({
        'tag': tag,
        'parent': parent,
        'child': child,
                        })
    #print("data appended", tag)
    #print(data, "\n")

def pairing(row):
    conversation_texts = []
    position = -1
    new_list = row.split(' +++$+++ ')
    if len(new_list) > 4:
        return
    lines = new_list[3]
    if len(lines) == 1:
        return
    else:
        line_ids = lines.split(',')
        for line_id in line_ids:
            position += 1
            formatted_id = line_id.replace("[", "").replace("]", "").replace("'", "").replace(" ", "")
            for line_data in movie_lines:
                if formatted_id == line_data[0]:
                    if position == 0:
                        conversation_texts.append(line_data[4].replace("\n", ""))
                    elif position == len(line_ids)-1:
                        child = line_data[4]
                        parent = conversation_texts[position-1]
                        fileInsertion(parent, child)
                        #print("parent:" + parent + "child:" + child)
                        #print(conversation_texts)
                    else:
                        conversation_texts.append(line_data[4].replace("\n", ""))
                        child = line_data[4].replace("\n", "")
                        parent = conversation_texts[position-1]
                        fileInsertion(parent, child)
                        #print("parent:" + parent + "child:" + child)
                        #print(conversation_texts)

with open('movie_conversations.txt', 'r', encoding='iso-8859-1' as f:
          for row in f.readlines():
          pairing(row)

with open('intents.json', 'w') as outfile:
          json.dump(data, outfile)
#print("File creation complete")
