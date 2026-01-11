import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import pygetwindow as gw
import keyboard
import time

root = tk.Tk()
root.title("GD Auto Rate")
root.geometry("300x225")
root.resizable(True, True)

# macro vars
no_transition = tk.BooleanVar()
interval = 0.5

running = False

scroll_attempts = 0
rate_attempts = 0

def start_macro():
    global running
    running = True
    no_transition_checkbox.config(state=tk.DISABLED)
    interval_button.config(state=tk.DISABLED)
    status_label.config(text="Macro running")
    threading.Thread(target=macro_loop).start()

def stop_macro():
    global running
    running = False
    no_transition_checkbox.config(state=tk.NORMAL)
    interval_button.config(state=tk.NORMAL)
    status_label.config(text="Macro stopped")

def macro_loop():
    global running
    while running:
        windows = gw.getWindowsWithTitle("Geometry Dash")

        if windows:
            window = windows[0]
            if window.isActive:
                if no_transition.get():
                    rate_noTransition()
                else:
                    rate()
            else:
                print("Geometry Dash is not active")
        else:
            print("Geometry Dash is not open")

        time.sleep(interval)

def no_transition_hint():
    tk.messagebox.showinfo("No Transition", "Enable this if you have the 'No Transition' hack enabled in Mega Hack or any other mod menu. \n\nThe macro won't wait for menu transitions with this enabled making it faster.")

def set_interval():
    global interval
    try:
        value = float(interval_typebox.get())

        if value < 0.1 or value > 60:
            tk.messagebox.showerror("Interval", "Enter a value between 0.1 and 60.")
        else:
            interval = value
            print(f"Set interval: {interval}s")
    except ValueError:
        tk.messagebox.showerror("Interval", "Enter a valid value.")

def rate():
    global scroll_attempts
    global rate_attempts

    if scroll_attempts >= 5 or rate_attempts > 10:
        scroll_attempts = 0
        rate_attempts = 0
        pyautogui.moveTo(1803, 548) # next page
        pyautogui.leftClick()

    try:
        location = pyautogui.locateOnScreen("get_it_button.PNG", confidence=0.5)
    except:
        scroll_attempts += 1
        print("GET IT button not found")
        for _ in range(5):
            pyautogui.scroll(-900)
    else:
        scroll_attempts = 0
        rate_attempts += 1
        print(f"GET IT button found at: {location.left}, {location.top}")
        pyautogui.moveTo(location) ## get it button
        pyautogui.leftClick()
        time.sleep(0.5)
        pyautogui.moveTo(1789, 954) ## rate button
        pyautogui.leftClick()
        pyautogui.moveTo(1212, 611) ## 10* button
        pyautogui.leftClick()
        pyautogui.moveTo(1167, 765) ## submit button
        pyautogui.leftClick()
        pyautogui.moveTo(957, 678) ## ok button (in case load error occurs)
        pyautogui.leftClick()
        pyautogui.press("esc") ## exits level page
        time.sleep(0.5)

def rate_noTransition():
    global scroll_attempts
    global rate_attempts

    if scroll_attempts >= 5 or rate_attempts > 10:
        scroll_attempts = 0
        rate_attempts = 0
        pyautogui.moveTo(1803, 548) # next page
        pyautogui.leftClick()

    try:
        location = pyautogui.locateOnScreen("get_it_button.PNG", confidence=0.5)
    except:
        scroll_attempts += 1
        print("GET IT button not found")
        for _ in range(5):
            pyautogui.scroll(-900)
    else:
        scroll_attempts = 0
        rate_attempts += 1
        print(f"GET IT button found at: {location.left}, {location.top}")
        pyautogui.moveTo(location) ## get it button
        pyautogui.leftClick()
        pyautogui.moveTo(1789, 954) ## rate button
        pyautogui.leftClick()
        pyautogui.moveTo(1212, 611) ## 10* button
        pyautogui.leftClick()
        pyautogui.moveTo(1167, 765) ## submit button
        pyautogui.leftClick()
        pyautogui.moveTo(957, 678) ## ok button (in case load error occurs)
        pyautogui.leftClick()
        pyautogui.press("esc") ## exits level page

keyboard.add_hotkey("f1", start_macro)
keyboard.add_hotkey("f2", stop_macro)

# UI
frame1 = tk.Frame(root)
frame1.pack(pady=10)

no_transition_checkbox = tk.Checkbutton(frame1, text="No Transition", variable=no_transition)
no_transition_checkbox.pack(side=tk.LEFT, padx=5)

no_transition_hint_button = tk.Button(frame1, text="?", command=no_transition_hint, width=2)
no_transition_hint_button.pack(side=tk.LEFT)

frame2 = tk.Frame(root)
frame2.pack(pady=10)

interval_label = tk.Label(frame2, text="Interval")
interval_label.pack(side=tk.LEFT, padx=5)

interval_typebox = tk.Entry(frame2, width=5)
interval_typebox.insert(0, "0.5")
interval_typebox.pack(side=tk.LEFT)

interval_secLabel = tk.Label(frame2, text="sec")
interval_secLabel.pack(side=tk.LEFT)

interval_button = tk.Button(frame2, text="Set", command=set_interval)
interval_button.pack(side=tk.LEFT, padx=5)

tk.Button(root, text="Start (F1)", command=start_macro).pack(pady=10)
tk.Button(root, text="Stop (F2)", command=stop_macro).pack(pady=10)

status_label = tk.Label(root, text="Macro stopped")
status_label.pack(pady=10)

root.mainloop()
