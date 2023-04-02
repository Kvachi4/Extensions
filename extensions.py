file_name = input("File name: ")
if "." in file_name:
    file_extension = file_name.split(".")
    last_index = len(file_extension)-1
    print(f"image/{file_extension[last_index]}")
else:
    print("Please enter file name with some extension ")