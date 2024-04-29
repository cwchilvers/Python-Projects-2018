import os, operator

def count_words(x):

    all_words = {}
    
    x = x.splitlines()
    x = ''.join(x)
    
    x = x.replace(".", "")
    x = x.replace("?", "")
    x = x.replace("!", "")
    x = x.replace(":", "")
    x = x.replace(";", "")
    x = x.replace("\"", " ")
    x = x.replace("(", "")
    x = x.replace(")", "")
    x = x.replace("/", " ")
    x = x.replace(",", "")
    x = x.replace("-", " ")
    
    x = x.lower()
    x_list = x.split(" ")
    
    for word in x_list:
        if word not in all_words:
            all_words[word] = 1
        else:
            all_words[word] += 1

    for key in all_words: 
        all_words[key] = all_words.get(key, 0) + 1

    sorted_words = sorted(all_words.items(), key = lambda x: x[1], reverse = True)

    for tup in sorted_words:
        item = tup[0]
        num = str(tup[1])
        print(( item+ "\t" + num).expandtabs(28))


def line():
    print("==============================================================================================================")


script_path = os.path.dirname(os.path.realpath(__file__))
path = script_path[:]
path =  path + "\Files"


for file in os.listdir(path):
    line()
    file_path = path + "\\" + file
    print("\n\n" + file_path + "\n\n")
    read_file = open(file_path, "r")
    file_words = (read_file.read())
    count_words(file_words)

print("\n\n DONE")
input("")
