import tkinter as tk
from pynput import keyboard, mouse
import pyautogui

# 클릭 정보를 저장하는 클래스
class MouseClick:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"MouseClick(x={self.x}, y={self.y})"

# 클릭할 좌표 설정 (초기값)
click_position = MouseClick(389, 73)

# 현재 상태 추적
key_combination = {keyboard.Key.ctrl_l, keyboard.Key.space}
current_keys = set()

# 최근 클릭과 가장 최근 클릭된 좌표를 저장하기 위한 객체
previous_click = MouseClick()
latest_click = MouseClick()

def show_screen_coordinates(x, y):
    global latest_click, previous_click
    # 최근 클릭된 좌표를 저장하고 업데이트
    if latest_click.x != 0 or latest_click.y != 0:
        # 최근 클릭이 있다면, 그것을 previous_click에 저장
        previous_click.set_position(latest_click.x, latest_click.y)
    # 최신 클릭 위치 업데이트
    latest_click.set_position(x, y)
    # 레이블에 클릭한 위치의 좌표 표시
    coordinate_label.config(text=f"모니터 클릭 좌표: ({x}, {y})")

# 마우스 클릭
def on_click(x, y, button, pressed):
    if pressed:
        # 확인 버튼 영역 제외
        button_x = confirm_button.winfo_rootx()
        button_y = confirm_button.winfo_rooty()
        button_width = 80
        button_height = 56
        if not (button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height):
            show_screen_coordinates(x, y)  # 클릭 시 좌표를 표시하고 업데이트

# 키보드 입력
def on_press(key):
    global current_keys
    if key in key_combination:
        current_keys.add(key)
        if current_keys == key_combination:
            pyautogui.click(click_position.x, click_position.y)

def on_release(key):
    global current_keys
    if key in current_keys:
        current_keys.remove(key)

def confirm_action():
    global click_position
    click_position.set_position(latest_click.x, latest_click.y)
    
    print(f"확인 버튼이 눌렸습니다! 저장된 좌표: {click_position}")
    print(f"최근 클릭 좌표: {previous_click}")

# Tkinter UI 설정
root = tk.Tk()
root.title("마우스 클릭 좌표 및 클릭기")

# 레이블 설정
coordinate_label = tk.Label(root, text="모니터 클릭 좌표는 여기에 나타납니다.", font=("Arial", 14))
coordinate_label.pack(pady=20)

# 확인 버튼 설정, 버튼 크기 : 80 x 56
confirm_button = tk.Button(root, text="확인", font=("Arial", 14), command=confirm_action)
confirm_button.pack(pady=10)

# 마우스 리스너 설정
mouse_listener = mouse.Listener(on_click=on_click)
mouse_listener.start()

# 키보드 리스너 설정
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)
keyboard_listener.start()

# Tkinter main loop
root.mainloop()