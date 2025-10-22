import tkinter as tk
from tkinter import messagebox

# ====== Function to Display Greeting ======
def display_greeting():
    name = entry_name.get().strip()
    if name == "":
        messagebox.showwarning("Input Error", "Please enter your name.")
    else:
        label_output.config(text=f"Hello, {name}! Have a good day..!", fg="#046865")

# ====== Hover Effects ======
def on_enter(e):
    submit_btn.config(bg="#0B8E81")

def on_leave(e):
    submit_btn.config(bg="#059C9B")

# ====== Main Window ======
root = tk.Tk()
root.title("Personalized Greeting App")
root.geometry("520x400")
root.configure(bg="#D9F3F1")

# ====== Outer Frame (Rounded Look Simulation) ======
outer_frame = tk.Frame(root, bg="#F9FFFE", bd=2, relief="ridge", highlightthickness=0)
outer_frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=280)

# ====== Title ======
title_label = tk.Label(outer_frame, text="Welcome to Greeting App",
                       font=("Segoe UI", 14, "bold"), bg="#F9FFFE", fg="#046865")
title_label.pack(pady=15)

# ====== Input Section ======
name_label = tk.Label(outer_frame, text="Enter Your Name:", font=("Segoe UI", 11), bg="#F9FFFE", fg="#333333")
name_label.pack(pady=(5, 0))

entry_name = tk.Entry(outer_frame, font=("Segoe UI", 11), relief="solid", justify="center",
                      bd=2, highlightthickness=1, highlightcolor="#059C9B", highlightbackground="#059C9B")
entry_name.pack(pady=8, ipady=5, ipadx=10)

# ====== Submit Button (Gradient Style Look) ======
submit_btn = tk.Button(outer_frame, text="Show Greeting", font=("Segoe UI Semibold", 11), bg="#059C9B",
                       fg="white", activebackground="#0B8E81", activeforeground="white", bd=0,
                       relief="flat", padx=18, pady=8, cursor="hand2", command=display_greeting)
submit_btn.pack(pady=15)

# Hover Bindings
submit_btn.bind("<Enter>", on_enter)
submit_btn.bind("<Leave>", on_leave)

# ====== Output Label ======
label_output = tk.Label(outer_frame, text="", font=("Segoe UI", 12, "bold"), bg="#F9FFFE", fg="#046865")
label_output.pack(pady=10)

# ====== Footer ======
footer_label = tk.Label(root, text="Designed by Aman", font=("Segoe UI", 9), bg="#D9F3F1", fg="#046865")
footer_label.pack(side="bottom", pady=5)

# ====== Run App ======
root.mainloop()
