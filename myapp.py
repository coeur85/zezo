import time
import threading
from pynput.mouse import Controller, Listener

# Create a mouse controller
mouse = Controller()
click_start_time = None
click_end_time = None
is_right_click = None


# Function to handle mouse clicks
def on_click(x, y, button, pressed):
    global click_start_time, click_end_time, is_right_click
    if pressed:
        if click_start_time is None:
            click_start_time = time.time()
        if button.name == "left":
            is_right_click = False
        elif button.name == "right":
            is_right_click = True
    else:
        if click_start_time is not None:
            click_end_time = time.time()


# Start listening to mouse events


def timer_function():
    # print(f"ahmed Function called at {time.strftime('%H:%M:%S')}")'
    global click_start_time, click_end_time, is_right_click
    position = mouse.position
    msg = f"Current mouse position: {position}"
    if click_start_time is None and click_end_time is None:
        msg += f" no click found"
    if click_start_time is not None and click_end_time is None:
        msg += f" click started at {click_start_time} but not ended yet"
    if click_start_time is not None and click_end_time is not None:
        msg += f" click started at {click_start_time} and ended at {click_end_time} and it was {'right' if is_right_click else 'left'} click"
        click_end_time = None
        click_start_time = None
        is_right_click = None
    print(msg)


def listen_function():
    listener_thread = threading.Thread(
        target=lambda: Listener(on_click=on_click).start()
    )
    listener_thread.daemon = (
        True  # Make sure the listener thread exits when the main program exits)
    )
    listener_thread.start()
    print("Listener started")
