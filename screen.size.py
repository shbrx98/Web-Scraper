
import tkinter as tk
def motion(event):
    x, y = event.x, event.y
    label.config(text=f"Mouse Coordinates: x={x}, y={y}")

root = tk.Tk()
root.title("Mouse Coordinates Tracker")

label = tk.Label(root, text="Mouse Coordinates: ", font=("Arial", 14))
label.pack()

root.bind('<Motion>', motion)

root.mainloop()