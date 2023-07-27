import os

def split_file_path(file_path):
    folder_path, full_file_name = os.path.split(file_path)
    file_name, file_extension = os.path.splitext(full_file_name)
    return folder_path, file_name, file_extension

file_path = "/home/user/documents/example.txt"
path, name, extension = split_file_path(file_path)
print("Путь к папке:", path)
print("Имя файла:", name)
print("Расширение файла:", extension)
