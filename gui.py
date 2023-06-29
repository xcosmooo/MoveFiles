import subprocess
import tkinter as tk

def run_script1():
    subprocess.Popen(['python', r'C:\Users\ARowland\PycharmProjects\MoveFiles\main.py'])
    print(f"Script 1 has started")
def run_script2():
    subprocess.Popen(['python', r'C:\Users\ARowland\PycharmProjects\MoveFiles\test.py'])
    print(f"Script 2 has started")
def stop_script1():
    subprocess.call(['pkill', '-f', r'C:\Users\ARowland\PycharmProjects\MoveFiles\main.py'])
def stop_script2():
    subprocess.call(['pkill', '-f', r'C:\Users\ARowland\PycharmProjects\MoveFiles\test.py'])


window = tk.Tk()
window.title("Script Control GUI")

run_button = tk.Button(window, text="Run Script 1", command=run_script1)
run_button.pack()

stop_button = tk.Button(window, text="Stop Script 1", command=stop_script1)
stop_button.pack()

run_button = tk.Button(window, text="Run Script 2", command=run_script2)
run_button.pack()

stop_button = tk.Button(window, text="Stop Script 2", command=stop_script2)
stop_button.pack()

window.mainloop()
