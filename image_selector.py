#Code by Mark Watson 12/6/2023, for Radiant Communications Corp.

# Import the Pillow and tkinter libraries
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog as fd

# Define the callback function for mouse selection
def onselect(event):
    global window, rect_id, x1, x2, y1, y2
    # Get the mouse position
    x2, y2 = event.x, event.y
    # Calculate the height and width of the selection
    width = x2 - x1
    height = y2 - y1
    

    #If rectangle is backwards, flip the values.
    if (width < 0):
        tempx = x1
        x1 = x2
        x2 = tempx
        width = width * -1

    if (height < 0):
        tempy = y1
        y1 = y2
        y2 = tempy
        height = height * -1

    # Format the pixel data as XML
    xml = f"<Left>{x1}</Left>\n\t  <Top>{y1}</Top>\n\t  <Width>{width}</Width>\n\t  <Height>{height}</Height>"
    
    #Ensure that the box is not a misclick
    if height != 0 and width != 0:
        # Clear the clipboard
        window.clipboard_clear()
        # Append the pixel data to the clipboard
        window.clipboard_append(xml)





# Create the main window
window = tk.Tk()
window.title("Image Selector")

# Open the image file
filename = fd.askopenfilename(title="Select an image file", filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
window.focus_force()
img = Image.open(filename)
window.geometry("{}x{}".format(img.width, img.height))
window.configure(background="grey")

# Create a Tkinter-compatible photo image
img = ImageTk.PhotoImage(img)

# Create a canvas widget to display the image
canvas = tk.Canvas(window, width=img.width(), height=img.height())
canvas.create_image(0, 0, image=img, anchor=tk.NW)
canvas.pack(side="bottom", fill="both", expand="yes")


# Create a variable to store the rectangle ID
rect_id = None
x1, y1, x2, y2 = 0, 0, 0, 0

# Define the callback function for mouse press
def onpress(event):
    # Get the mouse position
    global rect_id, x1, x2, y1, y2
    x1, y1 = event.x, event.y
    # Create a rectangle with zero size
    rect_id = canvas.create_rectangle(x1, y1, x1, y1, outline="red", dash=(2, 2), tag='rect')

# Define the callback function for mouse drag
def ondrag(event):
    global rect_id, x1, x2, y1, y2
    # Get the mouse position
    x2, y2 = event.x, event.y
    # Update the rectangle size
    canvas.coords(rect_id, x1, y1, x2, y2)


# Define the callback function for clearing the canvas
def onclear(event):
    # Delete all the items on the canvas
    canvas.delete('rect')


# Define the callback function for exiting the program
def onexit(event):
    # Close the window and exit the program
    window.destroy()


# Bind the mouse events to the canvas
canvas.bind("<Button-1>", onpress)
canvas.bind("<B1-Motion>", ondrag)
canvas.bind("<ButtonRelease-1>", onselect)
window.bind("<Escape>", onexit)
window.bind("<Delete>", onclear)





window.mainloop()
