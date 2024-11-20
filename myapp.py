import time
import threading
from pynput.mouse import Controller, Listener

# Create a mouse controller
mouse = Controller()
# Get the current position of the mouse


# from pynput.mouse import Listener


# Function to handle mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        if button.name == "left":
            print(f"Left click at ({x}, {y})")
        elif button.name == "right":
            print(f"Right click at ({x}, {y})")
    else:
        print(f"Released at ({x}, {y})")


# Start listening to mouse events


def timer_function():
    # print(f"ahmed Function called at {time.strftime('%H:%M:%S')}")'
    position = mouse.position
    print(f"Current mouse position: {position}")


def listen_function():
    listener_thread = threading.Thread( target=lambda: Listener(on_click=on_click).start() )
    listener_thread.daemon = (True)# Make sure the listener thread exits when the main program exits)  
    listener_thread.start()
