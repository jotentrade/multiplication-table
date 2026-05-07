#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk

def generate_table():
    # Clear previous content
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Header
    for j in range(1, 10):
        lbl = ttk.Label(frame, text=str(j), font=('Arial', 10, 'bold'))
        lbl.grid(row=0, column=j, padx=5, pady=5)
    
    # Rows
    for i in range(1, 10):
        # Row header
        lbl = ttk.Label(frame, text=str(i), font=('Arial', 10, 'bold'))
        lbl.grid(row=i, column=0, padx=5, pady=5)
        
        for j in range(1, 10):
            product = i * j
            lbl = ttk.Label(frame, text=str(product), font=('Arial', 10))
            lbl.grid(row=i, column=j, padx=5, pady=5)

# Main window
root = tk.Tk()
root.title("9 x 9 乘法表 - GUI 版本")
root.geometry("600x500")
root.resizable(False, False)

# Title label
title = ttk.Label(root, text="9 × 9 乘法表", font=('Arial', 16, 'bold'))
title.pack(pady=10)

# Frame for table
frame = ttk.Frame(root)
frame.pack(pady=10, padx=20)

generate_table()

# Copy button
def copy_to_clipboard():
    result = "9 x 9 乘法表\n"
    for i in range(1, 10):
        row = []
        for j in range(1, 10):
            row.append(f"{i}×{j}={i*j}")
        result += "  ".join(row) + "\n"
    root.clipboard_clear()
    root.clipboard_append(result)
    status.config(text="已複製到剪貼簿！")

btn = ttk.Button(root, text="複製到剪貼簿", command=copy_to_clipboard)
btn.pack(pady=10)

status = ttk.Label(root, text="", foreground="green")
status.pack()

root.mainloop()