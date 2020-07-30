import tkinter as tk
from PIL import Image, ImageTk

# create instance
window = tk.Tk()
# set default window size
window.geometry("500x400")
# set min window size
#window.minsize(300, 200)
# set max window size
#window.maxsize(700, 600)
# add a title
window.title("ranjan")

# Add header(label)
tk.Label(window, compound=tk.TOP, text='Image Gallery').pack()

# Add aframe
image_frame = tk.Frame()
image_frame.pack()

image_list = ['image1.png', 'image2.png', 'image3.png', 'image4.png', 
            'image5.png', 'image6.png']
current = 0

# Add an image-label
image_label = tk.Label(window, compound=tk.BOTTOM)
image_label.pack()

button_frame = tk.Frame()
button_frame.pack()

tk.Button(button_frame, text='Previous', command=lambda: move(-1)).grid(row=1, column=1)
tk.Button(button_frame, text='Next', command=lambda: move(+1)).grid(row=1, column=3)
tk.Button(text='Quit', command=window.quit, fg='red').pack(side=tk.BOTTOM)


def goTO(text):
    global current
    current = 0
    move(int(text) -1 )

def move(pos):
    global current, image_list
    if not (0 <= current + pos < len(image_list)):
        # Out-Of-Range: no image to display
        return
    current += pos
    image = Image.open(image_list[current])
    photo = ImageTk.PhotoImage(image)
    image_label['text'] = str(current+1) +". "+ image_list[current]
    image_label['image'] = photo
    image_label.photo = photo

# start GUI
move(0)
window.mainloop() 