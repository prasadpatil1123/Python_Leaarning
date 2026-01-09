file = open("new_file.txt", 'w')

try:
    file.write("ready")
finally:
    file.close()
    

with open("new_file2.txt",'w') as file:
    file.write("Avatar")