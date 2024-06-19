import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk

def show_image(self):
        # Open the image file using PIL
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Resize the image to fit the window
        image = image.resize((400, 200), Image.LANCZOS)

        # Convert the image to Tkinter format
        tk_image = ImageTk.PhotoImage(image)

        # Display the image on the label
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to prevent garbage collection

def next_image(self):
        # Increment the current image index
        self.current_image_index += 1

        # If reached the end of the image list, loop back to the beginning
        if self.current_image_index == len(self.image_paths):
            self.current_image_index = 0

        # Display the next image
        self.show_image()

        # Call the next_image method after a delay
        self.master.after(2000, self.next_image)

class SlideshowApp:
    def __init__(self, master, image_paths):
        self.master = master
        self.image_paths = image_paths
        self.current_image_index = 0

        # Create a label for displaying images
        self.image_label = tk.Label(self.master)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Display the first image
        self.show_image()

        # Call the next_image method after a delay
        self.master.after(2000, self.next_image)

    def show_image(self):
        # Open the image file using PIL
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Resize the image to fit the window
        image = image.resize((400, 200), Image.LANCZOS)

        # Convert the image to Tkinter format
        tk_image = ImageTk.PhotoImage(image)

        # Display the image on the label
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image  # Keep a reference to prevent garbage collection

    def next_image(self):
        # Increment the current image index
        self.current_image_index += 1

        # If reached the end of the image list, loop back to the beginning
        if self.current_image_index == len(self.image_paths):
            self.current_image_index = 0

        # Display the next image
        self.show_image()

        # Call the next_image method after a delay
        self.master.after(2000, self.next_image)

def search():
    destination = selected_destination.get()
    checkin_date = entry_checkin.get_date()
    checkin_time = entry_checkin_time.get()
    checkout_date = entry_checkout.get_date()
    checkout_time = entry_checkout_time.get()
    guests = entry_guests.get()
    # Here you can add the logic for searching
    print(f"Searching for {destination} from {checkin_date} {checkin_time} to {checkout_date} {checkout_time} for {guests} guests.")

app = tk.Tk()
app.title("Booking.com Interface")
app.geometry("1600x800")

# Set background color that blends well with div color
app.configure(bg='#002244')

# Style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), padding=5, background='#003580', foreground='white')
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', padding=5)
style.configure('TFrame', background='#003580')

# Main Frame (acting as a div)
frame = ttk.Frame(app, padding="20")
frame.place(x=0, y=2, relwidth=0.9, relheight=0.4)

# Title Label
title_label = ttk.Label(frame, text="Booking.com", font=('Arial', 20, 'bold'), foreground='white', background='#003580')
title_label.place(relx=0.05, rely=0.05)

# Horizontal placement of text fields and entries at the bottom
bottom_y = 0.7
entry_width = 15

# Destination
lbl_destination = ttk.Label(frame, text="Booked Activity:", background='#003580', foreground='white')
lbl_destination.place(relx=0.05, rely=bottom_y)
destination_options = ["Canoeing", "Swimming", "Bike riding"]
selected_destination = tk.StringVar(value="Canoeing")  # Default value
destination_menu = ttk.OptionMenu(frame, selected_destination, *destination_options)
destination_menu.place(relx=0.15, rely=bottom_y)

# Check-in date
lbl_checkin = ttk.Label(frame, text="Check-in Date:", background='#003580', foreground='white')
lbl_checkin.place(relx=0.3, rely=bottom_y)
entry_checkin = DateEntry(frame, width=entry_width)
entry_checkin.place(relx=0.4, rely=bottom_y)


# Check-out date
lbl_checkout = ttk.Label(frame, text="Check-out Date:", background='#003580', foreground='white')
lbl_checkout.place(relx=0.3, rely=bottom_y + 0.1)
entry_checkout = DateEntry(frame, width=entry_width)
entry_checkout.place(relx=0.4, rely=bottom_y + 0.1)



# Number of guests
lbl_guests = ttk.Label(frame, text="Number of Guests:", background='#003580', foreground='white')
lbl_guests.place(relx=0.8, rely=bottom_y)
entry_guests = ttk.Entry(frame, width=entry_width)
entry_guests.place(relx=0.9, rely=bottom_y)

# Search button
btn_search = ttk.Button(frame, text="Search", command=search)
btn_search.place(relx=0.5, rely=bottom_y + 0.2)

# Div for slideshow of images


# List of image paths
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]

# Initialize slideshow in the slideshow frame
slideshow_app = SlideshowApp(frame, image_paths)

app.mainloop()
