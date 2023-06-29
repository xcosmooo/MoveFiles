import os
import time


folder_path = r"C:\Users\ARowland\Desktop\folder4"
filename = "testfax.txt"
log_file_path = r"C:\Users\ARowland\PycharmProjects\MoveFiles\log.txt"

def create_log_entry(file_path):
    with open(log_file_path, "a") as log_file:
        log_file.write(f"{file_path} entered folder4 at {time.ctime()}\n")
        print(f"logged")

def check_folder():
    files = os.listdir(folder_path)
    for file in files:
        if file == filename:
            file_path = os.path.join(folder_path, file)
            create_log_entry(file_path)


while True:
    check_folder()
    time.sleep(10)
