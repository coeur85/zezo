import tkinter as tk
from tkinter import messagebox
import time
from myapp import ahmed


# Function to handle image click
def on_image_click(file_name):
    messagebox.showinfo("Image Clicked", f"You clicked on: {file_name}")


# Create the main window
root = tk.Tk()
root.title("Image Clicker")
root.geometry("600x400")  # Adjust the size of the window

# List of image file paths (must be .png, .gif, .pgm, or .ppm)
image_files = [
    "image1.png",
    "image2.png",
    "image3.png",
    "image4.png",
    "image5.png",
    "image6.png",
]

# List to hold the PhotoImage objects to prevent garbage collection
image_tk_objects = []

# Coordinates for images
positions = [(50, 50), (250, 50), (450, 50), (50, 250), (250, 250), (450, 250)]

# Load and place images
for idx, (file, pos) in enumerate(zip(image_files, positions)):
    try:
        # Load the image
        img_tk = tk.PhotoImage(file=file)
        image_tk_objects.append(img_tk)
        # Create a label for the image
        lbl = tk.Label(root, image=img_tk, cursor="hand2")
        lbl.place(x=pos[0], y=pos[1])

        # Bind click event to the label
        lbl.bind("<Button-1>", lambda e, file_name=file: on_image_click(file_name))
    except Exception as e:
        print(f"Error loading {file}: {e}")


def periodic_function():
    ahmed()
    # Schedule the function to run again after 1000ms (1 second)
    root.after(1000, periodic_function)


periodic_function()
# Start the Tkinter event loop
root.mainloop()
