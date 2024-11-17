import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from bloom_filter import process_files  # Import the process_files function from bloom_filter.py
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def open_file_dialog():
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    return file_path


def start_process():
    initial_file = open_file_dialog()
    if not initial_file:
        messagebox.showwarning("Warning", "No initial file selected.")
        return

    verify_file = open_file_dialog()
    if not verify_file:
        messagebox.showwarning("Warning", "No verification file selected.")
        return

    false_positive_rate = 0.0000001  # You can set this value dynamically if needed

    try:
        # Call the process_files function from bloom_filter.py
        results = process_files(initial_file, verify_file, false_positive_rate)
        result_text.delete(1.0, tk.END)
        for email, result, color in results:
            # Change the color of the result if it contains "probably"
            if "probably" in result.lower():
                result_text.insert(tk.END, f"{email}: {result}\n", "green")
            else:
                result_text.insert(tk.END, f"{email}: {result}\n", color)
            
            result_text.insert(tk.END, 78 * "-" + "\n", "separator")  # Separator line
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# UI Configuration
root = tk.Tk()
root.title("Bloom Checker")
root.geometry("1000x500")
root.configure(bg="#f0f0f0")
root.resizable(False, False)

# Modified to use resource_path
icon_path = resource_path("resources/lotus-flower.ico")
root.iconbitmap(icon_path)

main_container = tk.Frame(root, bg="#f0f0f0")
main_container.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

left_column = tk.Frame(main_container, bg="#f0f0f0", width=300)
left_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
left_column.pack_propagate(False)

right_column = tk.Frame(main_container, bg="#f0f0f0", width=600)
right_column.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
right_column.pack_propagate(False)

container_width = 510
container_height = 470

left_frame = tk.Frame(left_column, bg="#e0e0e0")
left_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width, height=container_height)

right_frame = tk.Frame(right_column, bg="#e0e0e0")
right_frame.place(relx=0.5, rely=0.5, anchor="center", width=container_width + 100, height=container_height)

# Modified to use resource_path
image_path = resource_path("resources/file.png")
image = Image.open(image_path)
image = image.resize((90, 90), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

drop_zone = tk.Label(
    left_frame,
    image=photo,
    compound=tk.TOP,
    text="Click to select your CSV files",
    font=("Arial", 10),
    bg="#e0e0e0",
    padx=20, pady=20
)
drop_zone.image = photo
drop_zone.place(relx=0.5, rely=0.5, anchor="center")

# Added click event to open the file selector
drop_zone.bind("<Button-1>", lambda e: start_process())

header_label = tk.Label(
    right_frame,
    text="Verification Results: ",
    font=("Arial", 16, "bold"),
    bg="#e0e0e0",
    anchor="w",
)
header_label.place(relx=0.05, rely=0.05)

result_text = tk.Text(
    right_frame,
    wrap=tk.WORD,
    font=("Courier", 12),
    bg="#e0e0e0",
    relief=tk.FLAT,
    bd=0
)
result_text.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.8)

# Add tags for colored text
result_text.tag_configure("red", foreground="red")
result_text.tag_configure("green", foreground="green")
result_text.tag_configure("separator", foreground="gray", font=("Courier", 8))  

if __name__ == '__main__':
    root.mainloop()
