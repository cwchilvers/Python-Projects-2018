def encrypt():
    global file
    encrypt_map = {}
    file_map = open('map.txt', 'r')
    for line in file_map:
        encrypt_map[line[0]] = line[2]
    file = list(file)
    print(encrypt_map)
    file_map.close()
    #==================================#

file = input("say something:\n")
encrypt()
