import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Tkinter App")

label = tk.Label(master=root, text="Tkinter App", bg="lightblue", fg="black")
label.pack(pady=20)

enrty = tk.Label(master=root, width=30, bg="lightblue", fg="navy")
enrty.pack(pady=20)

button = tk.Button(master=root, text="Click")
button.pack(pady=20)

root.mainloop()
