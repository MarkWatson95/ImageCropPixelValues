# ImageCropPixelValues
Mouse select sections of an image, instantly sending the values of the crop region in pixels to the clipboard, using XML format. 


This program is designed to calculate the position, height, and width of rectangles drawn on an image using the mouse. 
--Created by Mark Watson 12/6/2023


- Install latest version of python (3.12)
- Run the following commands in cmd or powershell
py -m pip install --upgrade Pillow
py -m pip install --upgrade tk

- Run the Python file using the command `py image_selector.pyw` in your terminal, or double-click the icon.
- Select the image file from the browser window
- A window will pop up with your image displayed on a canvas widget.
- Use your mouse to draw a rectangular selection around the region of interest in your image.
- The pixel data of the selected region will be copied to your clipboard as XML format.
- You can paste the pixel data to any text editor or application that supports XML.
- Use Escape to close the window, and Delete to remove all rectangular markings.

