import tkinter as tk
from tkinter import font
from PIL import Image, ImageTk  # Install Pillow for image handling

# Set up the main window
root = tk.Tk()
root.title("VR Landing Page")
root.geometry("800x600")
root.config(bg="#0e0e11")

# Define custom fonts
title_font = font.Font(family='Helvetica', size=30, weight='bold')
subtitle_font = font.Font(family='Helvetica', size=12)
button_font = font.Font(family='Helvetica', size=12, weight='bold')

# Navigation Bar
nav_frame = tk.Frame(root, bg="#0e0e11")
nav_frame.pack(pady=20)

nav_items = ["About Us", "Our Project", "Community", "Resources"]
for item in nav_items:
    nav_label = tk.Label(nav_frame, text=item, fg="white", bg="#0e0e11", font=subtitle_font)
    nav_label.pack(side=tk.LEFT, padx=15)

signup_button = tk.Button(nav_frame, text="Sign Up", fg="#0e0e11", bg="#8cfa00", font=button_font, borderwidth=0)
signup_button.pack(side=tk.RIGHT, padx=15)

# Main Content Area
content_frame = tk.Frame(root, bg="#0e0e11")
content_frame.pack(pady=50)

# Title
title_label = tk.Label(content_frame, text="Let's explore your own VR world", fg="white", bg="#0e0e11", font=title_font)
title_label.pack(pady=10)

# Subtitle
subtitle_label = tk.Label(content_frame, text="Veta is the next evolution of the VR world, connecting people and eliminating distance.", fg="grey", bg="#0e0e11", font=subtitle_font)
subtitle_label.pack(pady=10)

# Action Buttons
button_frame = tk.Frame(content_frame, bg="#0e0e11")
button_frame.pack(pady=20)

explore_button = tk.Button(button_frame, text="Explore Now", fg="#0e0e11", bg="#8cfa00", font=button_font, borderwidth=0)
explore_button.pack(side=tk.LEFT, padx=15)

learn_button = tk.Button(button_frame, text="Learn More", fg="white", bg="#383838", font=button_font, borderwidth=0)
learn_button.pack(side=tk.LEFT, padx=15)

# Placeholder for the VR illustration
# Load an image if you have it; otherwise, use a Canvas or Label as a placeholder
canvas = tk.Canvas(content_frame, width=300, height=200, bg="#0e0e11", bd=0, highlightthickness=0)
canvas.pack(pady=20)

# Load an image and display it in canvas (optional)
# img = Image.open("path_to_image.png")
# img = img.resize((300, 200), Image.ANTIALIAS)
# img_tk = ImageTk.PhotoImage(img)
# canvas.create_image(0, 0, anchor=tk.NW, image=img_tk)

# Run the Tkinter main loop
root.mainloop()
