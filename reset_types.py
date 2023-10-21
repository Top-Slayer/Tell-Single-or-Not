import os

for folder in os.listdir("types/"):
    folder_path = os.path.join("types/", folder)
    print(f"[ {folder} ]")
    
    if os.listdir(folder_path) == []:
        print(f"\x1B[32m --> All Clear \x1B[37m")

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        print(f"\x1B[31m --> Delete Image: {file_path} \x1B[37m")
        os.remove(file_path)
