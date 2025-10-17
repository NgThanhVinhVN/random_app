import tkinter as tk
import random

# Hàm xáo trộn chuỗi theo khoảng trắng
def randomize_words():
    text = entry.get()
    parts = text.split()
    random.shuffle(parts)
    result.set(' '.join(parts))

# Giao diện chính
root = tk.Tk()
root.title("🎲 Randomizer App")
root.geometry("400x250")
root.resizable(False, False)
root.config(bg="#222831")

# Biến lưu kết quả
result = tk.StringVar()

# Tiêu đề
title = tk.Label(root, text="Random Chuỗi Ngẫu Nhiên", 
                 fg="#EEEEEE", bg="#222831", font=("Segoe UI", 14, "bold"))
title.pack(pady=15)

# Ô nhập
entry = tk.Entry(root, font=("Segoe UI", 12), width=30, justify="center", bd=2, relief="solid")
entry.pack(pady=10)

# Nút random
btn = tk.Button(root, text="Random 🎲", font=("Segoe UI", 12, "bold"), 
                bg="#00ADB5", fg="white", relief="raised", bd=3, 
                activebackground="#028C95", activeforeground="white",
                command=randomize_words)
btn.pack(pady=10)

# Kết quả
lbl_result = tk.Label(root, textvariable=result, 
                      fg="#FFD369", bg="#222831", 
                      font=("Consolas", 13, "bold"))
lbl_result.pack(pady=15)

# Chạy ứng dụng
root.mainloop()
