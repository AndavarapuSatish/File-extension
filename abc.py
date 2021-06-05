import os
split_tuple=os.path.splitext("my_file.python")
print(split_tuple)
file_name=split_tuple[0]
file_extension=split_tuple[1]
print("File Name:",file_name)
print("File Extension:",file_extension)
