file_name = "file.txt"
data = "Hello world\n"

with open(file_name, 'a') as files:
    files.write(data)
