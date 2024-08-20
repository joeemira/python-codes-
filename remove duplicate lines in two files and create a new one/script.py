with open("C:/Users/youss/OneDrive/Desktop/python/file.txt", "w") as f:
    f.write("Hello, World!\n")
    f.write("This is file\n\n")
    f.write("Hello, zerosploit!\n")
    
with open("C:/Users/youss/OneDrive/Desktop/python/file2.txt", "w") as t:
    t.write("Hello, secound World!\n")
    t.write("This is file \n\n")
    t.write("Hello, zerosploit!\n")
    
newlines= [] 
with open("C:/Users/youss/OneDrive/Desktop/python/file.txt", "r") as file:
    for line in file :
        line=line.strip()
        if line not in newlines:
            newlines.append(line)
with open("C:/Users/youss/OneDrive/Desktop/python/file2.txt", "r") as file:
    for line in file :
        line=line.strip()
        if line not in newlines:
            newlines.append(line)
with open("C:/Users/youss/OneDrive/Desktop/python/merged_output.txt", 'w') as output:
        for line in newlines:
            output.write(line + '\n')
            

output_file = 'merged_output.txt'