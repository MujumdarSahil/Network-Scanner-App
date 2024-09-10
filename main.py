import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
from scanner import scan_network

# Function to start scanning
def start_scan():
    ip_range = ip_range_entry.get().split(',')
    try:
        port_start = int(port_start_entry.get())
        port_end = int(port_end_entry.get())
        port_range = (port_start, port_end)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid port numbers.")
        return
    
    if not ip_range:
        messagebox.showerror("Input Error", "Please enter at least one IP address.")
        return
    
    result_text.delete(1.0, tk.END)
    results = scan_network(ip_range, port_range)
    
    if results:
        for ip, ports in results.items():
            result_text.insert(tk.END, f"IP: {ip} - Open Ports: {', '.join(map(str, ports))}\n")
    else:
        result_text.insert(tk.END, "No open ports found.")

# Create the main application window
root = tk.Tk()
root.title("Simple Network Scanner")
root.geometry("800x600")

# Load and set the background image
bg_image_path = "assets/image.png"  # Ensure the image is in this location

try:
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)  # Updated from ANTIALIAS to Resampling.LANCZOS
    bg_photo = ImageTk.PhotoImage(bg_image)

    # Use a label to display the background image
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Lower the label to make it a background
    bg_label.lower()  # Ensures widgets are placed on top of the background image
except FileNotFoundError:
    messagebox.showerror("File Not Found", f"Could not find the image at {bg_image_path}")
    # Continue running the app without background instead of destroying the window

# IP Range Entry
ip_range_label = tk.Label(root, text="Enter IP Range (comma-separated):", bg="lightblue", font=("Helvetica", 12))
ip_range_label.place(relx=0.5, rely=0.1, anchor="n")

ip_range_entry = tk.Entry(root, font=("Helvetica", 12))
ip_range_entry.place(relx=0.5, rely=0.15, relwidth=0.5, anchor="n")

# Port Range Entry
port_start_label = tk.Label(root, text="Enter Start Port:", bg="lightblue", font=("Helvetica", 12))
port_start_label.place(relx=0.3, rely=0.25, anchor="n")

port_start_entry = tk.Entry(root, font=("Helvetica", 12))
port_start_entry.place(relx=0.3, rely=0.3, relwidth=0.2, anchor="n")

port_end_label = tk.Label(root, text="Enter End Port:", bg="lightblue", font=("Helvetica", 12))
port_end_label.place(relx=0.7, rely=0.25, anchor="n")

port_end_entry = tk.Entry(root, font=("Helvetica", 12))
port_end_entry.place(relx=0.7, rely=0.3, relwidth=0.2, anchor="n")

# Scan Button
scan_button = tk.Button(root, text="Start Scan", font=("Helvetica", 14), command=start_scan)
scan_button.place(relx=0.5, rely=0.4, anchor="n")

# Result Text Box
result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Helvetica", 12))
result_text.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.4, anchor="n")

root.mainloop()
