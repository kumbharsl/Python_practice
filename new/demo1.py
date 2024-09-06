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
welcome_font = font.Font(family='Helvetica', size=16, weight='bold')

# Function to update page content dynamically
def update_content(page_name, button):
    # Reset all button colors
    for nav_button in nav_buttons:
        nav_button.config(bg="#0e0e11", fg="white")

    # Change the color of the clicked button
    button.config(bg="#8cfa00", fg="#0e0e11")

    # Update the title, subtitle, and welcome label dynamically
    welcome_label.config(text=f"Welcome to {page_name}")
    title_label.config(text=f"Let's explore the {page_name} world")
    subtitle_label.config(text=f"{page_name} is the next evolution of the VR world, connecting people and eliminating distance.")

# Navigation Bar
nav_frame = tk.Frame(root, bg="#0e0e11")
nav_frame.pack(pady=20)

# Navigation buttons and storage
nav_items = ["About Us", "Our Project", "Community", "Resources"]
nav_buttons = []

for item in nav_items:
    button = tk.Button(nav_frame, text=item, fg="white", bg="#0e0e11", font=subtitle_font, borderwidth=0)
    button.pack(side=tk.LEFT, padx=15)
    nav_buttons.append(button)

# Bind click events to each button to update the content
nav_buttons[0].config(command=lambda: update_content("About Us", nav_buttons[0]))
nav_buttons[1].config(command=lambda: update_content("Our Project", nav_buttons[1]))
nav_buttons[2].config(command=lambda: update_content("Community", nav_buttons[2]))
nav_buttons[3].config(command=lambda: update_content("Resources", nav_buttons[3]))

signup_button = tk.Button(nav_frame, text="Sign Up", fg="#0e0e11", bg="#8cfa00", font=button_font, borderwidth=0)
signup_button.pack(side=tk.RIGHT, padx=15)

# Main Content Area
content_frame = tk.Frame(root, bg="#0e0e11")
content_frame.pack(pady=50)

# Welcome Line with Bullet and Shadow Effect
bullet_label = tk.Label(content_frame, text="●", fg="#8cfa00", bg="#0e0e11", font=welcome_font)
bullet_label.pack(side=tk.LEFT, padx=10)

# Shadow label slightly offset for shadow effect
shadow_label = tk.Label(content_frame, text="Welcome to our company", fg="#383838", bg="#0e0e11", font=welcome_font)
shadow_label.place(x=55, y=5)

# Foreground label on top for the text
welcome_label = tk.Label(content_frame, text="Welcome to our company", fg="white", bg="#0e0e11", font=welcome_font)
welcome_label.place(x=50, y=0)

# Title
title_label = tk.Label(content_frame, text="Let's explore your own VR world", fg="white", bg="#0e0e11", font=title_font)
title_label.pack(pady=40)

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
canvas = tk.Canvas(content_frame, width=300, height=200, bg="#0e0e11", bd=0, highlightthickness=0)
canvas.pack(pady=20)

# Initially set the first button's page to be active
update_content("About Us", nav_buttons[0])

# Run the Tkinter main loop
root.mainloop()
