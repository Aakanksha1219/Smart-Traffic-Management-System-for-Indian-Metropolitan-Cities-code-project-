# main.py

from tkinter import *
from tkinter import messagebox, filedialog
import matplotlib.pyplot as plt
import cv2
from vehicle_detection import detect_vehicles

main = Tk()
main.title("Smart Traffic Management System using YOLOv8")
main.geometry("1000x600")
main.config(bg='magenta3')

filename = None
vehicle_count = 0

def uploadTrafficImage():
    global filename
    filename = filedialog.askopenfilename(initialdir="images", title="Select Image",
                                          filetypes=(("Image files", "*.jpg *.png *.jpeg"), ("all files", "*.*")))
    pathlabel.config(text=filename)

def applyYOLODetection():
    global filename, vehicle_count
    if not filename:
        messagebox.showwarning("Warning", "Please upload an image first.")
        return

    annotated_img, vehicle_count = detect_vehicles(filename)
    output_path = "gray/yolo_detected.png"
    cv2.imwrite(output_path, annotated_img)

    # Display image
    img = cv2.cvtColor(annotated_img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.title(f"Detected Vehicles: {vehicle_count}")
    plt.axis('off')
    plt.show()

    messagebox.showinfo("Detection Result", f"Detected Vehicles: {vehicle_count}")

def allocateSignalTime():
    global vehicle_count
    if vehicle_count == 0:
        messagebox.showwarning("Warning", "Run detection first.")
        return

    if vehicle_count >= 70:
        time = 70  # Extremely heavy traffic
        level = "Extremely Heavy"
    elif vehicle_count >= 60:
        time = 65
        level = "Very Heavy"
    elif vehicle_count >= 50:
        time = 60
        level = "Heavy"
    elif vehicle_count >= 45:
        time = 55
        level = "Medium-Heavy"
    elif vehicle_count >= 40:
        time = 50
        level = "Medium"
    elif vehicle_count >= 35:
        time = 45
        level = "Moderate"
    elif vehicle_count >= 30:
        time = 40
        level = "Light-Moderate"
    elif vehicle_count >= 25:
        time = 35
        level = "Light"
    elif vehicle_count >= 20:
        time = 30
        level = "Very Light"
    elif vehicle_count >= 10:
        time = 25
        level = "Sparse"
    elif vehicle_count >= 5:
        time = 20
        level = "Minimal"
    else:
        time = 15
        level = "Empty or Very Minimal"

    messagebox.showinfo(
        "Green Signal Allocation Time", 
        f"Detected Vehicles: {vehicle_count}\n"
        f"Traffic Level: {level}\n"
        f"Recommended Green Signal Time: {time} seconds"
    )


def exitApp():
    main.destroy()

# UI Widgets
font = ('times', 16, 'bold')
title = Label(main, text='Smart Traffic Management System using YOLOv8', anchor=W, justify=CENTER, bg='yellow4', fg='white', font=font, height=2)
title.pack(fill=X)

font1 = ('times', 14, 'bold')

upload_btn = Button(main, text="Upload Traffic Image", command=uploadTrafficImage, font=font1)
upload_btn.place(x=50, y=100)

pathlabel = Label(main, text="", bg='yellow4', fg='white', font=font1)
pathlabel.place(x=50, y=150)

detect_btn = Button(main, text="Detect Vehicles Using YOLOv8", command=applyYOLODetection, font=font1)
detect_btn.place(x=50, y=200)

signal_btn = Button(main, text="Calculate Green Signal Time", command=allocateSignalTime, font=font1)
signal_btn.place(x=50, y=250)

exit_btn = Button(main, text="Exit", command=exitApp, font=font1)
exit_btn.place(x=50, y=300)

main.mainloop()
