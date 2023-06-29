import os
import shutil
import time
import threading

sourceFile = "testfax.txt"
desktopPath = os.path.expanduser("~/Desktop")
destination = ["folder1", "folder2", "folder3", "folder4"]
sourcePath = os.path.join(desktopPath, sourceFile)
currentIndex = 0
is_running = False

def start_script():
    global is_running
    is_running = True
    script_thread = threading.Thread(target=script_loop)
    script_thread.start()

def script_loop():
    global currentIndex, is_running, sourcePath
    while is_running:
        destinationFolder = destination[currentIndex]
        destinationFolderPath = os.path.join(desktopPath, destinationFolder)

        if not os.path.exists(destinationFolderPath):
            os.makedirs(destinationFolderPath)

        destinationFilePath = os.path.join(destinationFolderPath, sourceFile)
        shutil.move(sourcePath, destinationFilePath)
        print(f"File {sourceFile} has moved to {destinationFolderPath}")

        sourcePath = destinationFilePath
        currentIndex = (currentIndex + 1) % len(destination)
        time.sleep(2)

def stop_script():
    global is_running
    is_running = False
    print(f"Script has been stopped")

# Start the script
start_script()
