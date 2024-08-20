import re

emails = []
pattern = re.compile(r"[^@]+@[^@]+\.[a-zA-Z]{2,}")

with open("C:/Users/youss/OneDrive/Desktop/python/file.txt", "r") as file:
    for line in file:
        line = line.strip()
        if pattern.match(line) and line not in emails:
            emails.append(line)

with open(r"C:/Users/youss/OneDrive/Desktop/python/emails.txt", 'w') as output:
    for email in emails:
        output.write(email + '\n')

output_file = 'C:/Users/youss/OneDrive/Desktop/python/emails.txt'
