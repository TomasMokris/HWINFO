import platform
import psutil
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Informace o počítači")
root.geometry("1920x1080")
root.configure(bg="#5a5a5a")

bg = ImageTk.PhotoImage(Image.open("HWInfo\Background.gif"))
background_label = tk.Label(root, image=bg)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

hw_label = tk.Label(root, text="HW informace:", bg="#191313", fg="#ffffff")
os_label = tk.Label(root, text="OS informace:", bg="#191313", fg="#ffffff")
cpu_label = tk.Label(root, text="CPU informace:", bg="#191313", fg="#ffffff")
memory_label = tk.Label(root, text="Paměť informace:", bg="#191313", fg="#ffffff")
network_label = tk.Label(root, text="Síťové informace:", bg="#191313", fg="#ffffff")

hw_info = platform.uname()
os_info = platform.platform()
cpu_info = platform.processor()
memory_info = psutil.virtual_memory()
network_info = psutil.net_if_addrs()

hw_info_label = tk.Label(root, text=str(hw_info), bg="#191313", fg="#ffffff")
os_info_label = tk.Label(root, text=str(os_info), bg="#191313", fg="#ffffff")
cpu_info_label = tk.Label(root, text=str(cpu_info), bg="#191313", fg="#ffffff")
memory_info_label = tk.Label(root, text=f"Volná paměť: {memory_info.available / (1024 * 1024):.2f} MB", bg="#191313", fg="#ffffff")
network_info_label = tk.Label(root, text=str(network_info), bg="#191313", fg="#ffffff")

hw_label.place(width=100, height=20, x=0, y=400)
os_label.place(width=100, height=20, x=0, y=420)
cpu_label.place(width=100, height=20, x=0, y=440)
memory_label.place(width=100, height=20, x=0, y=460)
network_label.place(width=100, height=20, x=0, y=480)
hw_info_label.place(width=800, height=20, x=110, y=400)
os_info_label.place(width=800, height=20, x=110, y=420)
cpu_info_label.place(width=800, height=20, x=110, y=440)
memory_info_label.place(width=800, height=20, x=110, y=460)
network_info_label.place(width=800, height=20, x=110, y=480)

root.mainloop()
