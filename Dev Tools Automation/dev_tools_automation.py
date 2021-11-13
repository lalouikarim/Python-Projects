from pywinauto import Application
import ctypes
from ctypes import wintypes
import psutil
import os
import webbrowser
import urllib.parse
from pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button as MouseButton, Controller as MouseController
import time
import subprocess
from tkinter import *
from tkinter import ttk, messagebox
from selenium import webdriver

# returns the current window name
def current_window_name():
    user32 = ctypes.windll.user32
    h_wnd = user32.GetForegroundWindow()
    pid = wintypes.DWORD()
    user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
    return psutil.Process(pid.value).name()

# returns the current chrome tab
def current_chrome_tab():
    app = Application(backend='uia')
    app.connect(title_re=".*Chrome.*", timeout=30)
    element_name="Address and search bar"
    dlg = app.top_window()
    url = dlg.child_window(title=element_name, control_type="Edit").get_value()
    return url

# automate the workflow
def automate():
    if project_folder.get() == "" or project_folder.get() == "":
        messagebox.showinfo(title = "Error", message = "Please enter the project path")
    else:
        # check if the path exists
        if os.path.isdir(r"C:\xampp\htdocs\\" + project_folder.get()):
            # the project folder path in a url 
            project_folder_url = "localhost/" + project_folder.get().replace(" ", "%20").replace("\\", "/")

            # XAMPP
            # start xampp which will automatically start apache and mysql
            os.startfile(r"C:\xampp\xampp-control.exe")
            # wait till xampp is fully loaded to proceed
            while current_window_name() != "xampp-control.exe":
                pass

            # Chrome
            # open the github website
            webbrowser.open("https://github.com/")
            # wait till the tab is created
            while current_chrome_tab() != "github.com":
                pass
            # open the index of the project
            webbrowser.open_new_tab("http://" + project_folder_url)
            # wait till the tab is created
            while current_chrome_tab() != project_folder_url:
                pass
            # simulate a key press to automatically open chrome dev tools
            keyboard = KeyboardController()
            keyboard.press(Key.f12)
            keyboard.release(Key.f12)

            # File Explorer
            # open the file explorer in the project's folder
            subproc = subprocess.Popen(r'explorer /select,"C:\xampp\htdocs\"' + project_folder.get())
            # wait till file explorer is fully loaded to proceed
            while current_window_name() != "explorer.exe":
                pass

            # VS Code
            # open vs code in the project's folder (simulate a right click and then press "i" to trigger "Open with Code")
            time.sleep(1)
            mouse = MouseController()
            mouse.click(MouseButton.right, 1)
            time.sleep(1)
            keyboard.press("i")
            keyboard.release("i")

            # close the window
            window.destroy()
        else:
            messagebox.showinfo(title = "Error", message = "The path doesn't exist")

window = Tk()
window.geometry("400x80")
window.title("Develeopment Tools Automation In Windows")
msg = Message(window, text = "Project Path")
msg.grid(row = 0, column = 0)
project_folder = StringVar()
entr = Entry(window, textvariable = project_folder)
entr.grid(row = 0, column = 1)
btn = Button(window, text = "Automate", width = 10, height = 2, command = automate)
btn.grid(row = 0, column = 2)    
window.mainloop()