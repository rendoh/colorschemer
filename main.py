import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

from lib.image_colorizer import ImageColorizer


def run():

    def open_dialog():
        fTyp = [('image files', ('.png', '.jpg', '.jpeg', '.gif', '.svg'))]
        filepath = filedialog.askopenfilename(filetypes=fTyp)
        colorizer = ImageColorizer(filepath)
        print(colorizer.get_colors())
        print(colorizer.get_hexes())
        # image = Image.open(filepath)
        # image.thumbnail((500, 500), Image.ANTIALIAS)
        # image = ImageTk.PhotoImage(image)
        # canvas.create_image(
        #     0,
        #     0,
        #     image=image,
        #     anchor=tk.NW,
        # )

    root = tk.Tk()
    root.title('Color Schemer')
    root.geometry('600x400')

    # canvas = tk.Canvas(root, width=600, height=400)
    # canvas.place(x=0, y=0)

    button = tk.Button(root, text='参照', command=open_dialog)
    button.pack()
    root.mainloop()


if __name__ == '__main__':
    run()
