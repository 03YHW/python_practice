from pynput import keyboard, mouse
import pyautogui

# 클릭할 좌표 설정
click_position = (100, 100)

# 현재 상태 추적
key_combination = {keyboard.Key.ctrl_l, keyboard.Key.space}
current_keys = set()

def on_press(key):
    if key in key_combination:
        current_keys.add(key)
        if current_keys == key_combination:
            # Ctrl + Space 조합이 감지되면 클릭 수행
            pyautogui.click(click_position)

def on_release(key):
    if key in current_keys:
        current_keys.remove(key)

def on_click(x, y, button, pressed):
    if pressed:
        print(f"클릭한 위치: ({x}, {y})")

# 키보드 리스너 설정
with keyboard.Listener(on_press=on_press, on_release=on_release) as key_listener:
    # 마우스 리스너 설정
    with mouse.Listener(on_click=on_click) as mouse_listener:
        print("Ctrl + Space로 클릭하고, 클릭하면 마우스 좌표를 확인하세요.")
        key_listener.join()
        mouse_listener.join()