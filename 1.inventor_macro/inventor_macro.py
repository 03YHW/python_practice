import tkinter as tk
from pynput import keyboard, mouse
import pyautogui

# 클릭할 좌표 설정
click_position = (389, 73)

# 현재 상태 추적
key_combination = {keyboard.Key.ctrl_l, keyboard.Key.space}
current_keys = set()

def show_screen_coordinates(x, y):
    # 모니터에서 클릭한 좌표를 레이블에 표시
    coordinate_label.config(text=f"모니터 클릭 좌표: ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        show_screen_coordinates(x, y)

def on_press(key):
    global current_keys
    if key in key_combination:
        current_keys.add(key)
        if current_keys == key_combination:
            # Ctrl + Space 조합이 감지되면 클릭 수행
            pyautogui.click(click_position)

def on_release(key):
    global current_keys
    if key in current_keys:
        current_keys.remove(key)

# Tkinter UI 설정
root = tk.Tk()
root.title("마우스 클릭 좌표 및 클릭기")

# 레이블 설정
coordinate_label = tk.Label(root, text="모니터 클릭 좌표는 여기에 나타납니다.", font=("Arial", 14))
coordinate_label.pack(pady=20)

# 마우스 리스너 설정
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 키보드 리스너 설정
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# Tkinter main loop
root.mainloop()