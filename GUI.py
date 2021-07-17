from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox


class GUI(Tk):
    BTN = []

    def __init__(self, title="Window", icon=None, width=200, height=200, bg="white", resizableX=0, resizableY=0):
        super().__init__()
        self.title(title)
        self.wm_iconbitmap(icon)
        self.geometry(f"{width}x{height}")
        self.config(bg=bg)
        self.resizable(resizableX, resizableY)

    def start(self):
        self.mainloop()

    def disableButtons(self):
        for item in self.BTN:
            item.config(state=DISABLED)

    def enableButtons(self):
        for item in self.BTN:
            item.config(state=ACTIVE)

    def drawButtons(self, img_func, cam_func, vid_func):
        # Buttons
        img_btn = Button(self, text="Image", width=10, command=img_func)
        cam_btn = Button(self, text="Camera", width=10, command=cam_func)
        vid_btn = Button(self, text="Video", width=10, command=vid_func)
        img_btn.pack(pady=5)
        cam_btn.pack(pady=5)
        vid_btn.pack(pady=5)

        # BTN
        self.BTN = [img_btn, cam_btn, vid_btn]

    @staticmethod
    def openFile(ext):
        return askopenfilename(defaultextension=ext, filetypes=[("All Files", "*.*")])

    @staticmethod
    def giveError(text):
        messagebox.showerror("Error", text)
