output_lines = []  

keywords = [
    "apiKey", "secret", "token", "accessToken", "auth", "authorization", "bearer", "key",
    "password", "pwd", "pass", "user", "username", "login", "email", "credentials", "auth",
    "config", "db_password", "db_username", "database", "connectionString", "mongoUri", "redisUri",
    "privateKey", "publicKey", "env", "process.env", "NODE_ENV", "REACT_APP", "VUE_APP", "NEXT_PUBLIC",
    "url", "endpoint", "path", "directory", "uploadPath", "downloadPath",
    "encryption", "decrypt", "hash", "salt", "md5", "sha1", "sha256", "crypto",
    "debug", "console.log", "alert", "print", "error", "stackTrace",
    "session", "csrf", "xsrf", "otp", "secret_key", "jwt", "bearer", "cookie", "header"
]
with open("C:/Users/youss/OneDrive/Desktop/python/jsfile.txt", "r") as file:
    for line in file:
        if any(word in line for word in keywords):
            output_lines.append(line)  # Store the line in output_lines list

# Write the matched lines to the output file
with open("C:/Users/youss/OneDrive/Desktop/python/out.txt", 'w') as output_file:
    for line in output_lines:
        output_file.write(line)  # Writing each line to the output file

# The output file path is set correctly
output_file_path = 'C:/Users/youss/OneDrive/Desktop/python/out.txt'