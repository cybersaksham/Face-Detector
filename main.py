import cv2
import os
from PIL import Image, ImageTk
from threading import Thread
import process

from GUI import GUI


def video(file, subtitle):
    root.disableButtons()
    vid = cv2.VideoCapture(file)

    while vid.isOpened():
        _, frame = vid.read()
        frame = process.process(frame)
        cv2.imshow(f"{TITLE} - {subtitle}", frame)
        if cv2.waitKey(1) == 27:
            break

    root.enableButtons()
    cv2.destroyAllWindows()
    vid.release()


def camera():
    th_cam = Thread(target=video, args=[0, "Camera"])
    th_cam.daemon = 1
    th_cam.start()


def vid_file():
    file = root.openFile(".mp4")
    if file == "":
        root.giveError("Empty File")
        return
    try:
        vid = cv2.VideoCapture(file)
        _, f1 = vid.read()
        ret, f2 = vid.read()
        if not ret:
            root.giveError("Incorrect file")
            return
        video(file, os.path.basename(file))
    except Exception as e:
        root.giveError(e)


def photoThread(img, fileName):
    root.disableButtons()
    img = process.process(img)
    cv2.imshow(f"{TITLE} - {fileName}", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    root.enableButtons()


def photo():
    file = root.openFile(".png")
    if file == "":
        root.giveError("Empty File")
        return
    try:
        img = cv2.imread(file)
        pic = Image.open(file)
        image = ImageTk.PhotoImage(pic)
        th_pic = Thread(target=photoThread, args=[img, os.path.basename(file)])
        th_pic.daemon = 1
        th_pic.start()
    except Exception as e:
        root.giveError(e)


if __name__ == '__main__':
    TITLE = "Face Detector"
    root = GUI(title=TITLE, icon="icon.ico", width=300, height=200)
    root.drawButtons(photo, camera, vid_file)
    root.start()
    exit()
