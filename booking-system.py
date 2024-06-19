
import tkinter as tk
from tkinter import ttk
from tkcalendar import DataEntry
from PIL import Image, Image
import sqlite3 

# Function to populate the Treeview with data
def populate_treeview(tree):
    # Clear existing data in Treeview
    for item in tree.get_children():
        tree.delete(item)
    
    # Fetch data from the database
    rows = fetch_data()
    
    # Insert data into Treeview
    for row in rows:
        tree.insert('', tk.END, values=row)

def sessions():
    conn = sqlite3.connect('A+.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name,phone FROM clients')
    rows = cursor.fetchall()
    conn.close()
    return rows

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('A+.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name, team,activity,phone FROM clients')
    rows = cursor.fetchall()
    conn.close()
    return rows



def showEntryfield():
    mainslot.place(relx=0.29, rely=0.42, relheight=0.48, relwidth=0.68)

def homepage():
    mainslot.place(relx=0, rely=0, relheight=0, relwidth=0)
    populate_treeview(tree)
    

    mainslot.place()
def show_image(self):
        # Open the image file using PIL
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Resize the image to fit the window
        image = image.resize((500, 300), Image.LANCZOS)

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
        image = image.resize((500, 300), Image.LANCZOS)

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
    destination = lbl_destination.get()
    checkin_date = entry_checkin.get_date()
    checkout_date = entry_checkout.get_date()

    # Here you can add the logic for searching

app = tk.Tk()
app.title("Booking.com Interface")
app.geometry("1400x800")

# Set background color that blends well with div color
app.configure(bg='#c2c2f6')

# Style
style = ttk.Style()
style.configure('TLabel', font=('Arial', 12), padding=5, background='#003560', foreground='white')
style.configure('TButton', font=('Arial', 12), padding=5)
style.configure('TEntry', padding=5)
style.configure('TFrame', background='#003560')

# Horizontal placement of text fields and entries at the bottom
bottom_y = 0.6
bottom_y2=0.8
entry_width = 15
bg='#003560'
textfont=("times",12)
checkin=0.27
checkout=0.27
checkw=12
slotbg="#e1e1f6"
slotfg="#003550"


frame_style =ttk.Style()
frame_style.configure('sidebar.TFrame', background='#d1d1f4')
frame_style.configure('mainslot.TFrame', background='#e1e1f6')
# Main Frame (acting as a div)
frame = ttk.Frame(app, padding="20")
frame.place(x=5, y=10, relwidth=0.98, relheight=0.4)

frame2=ttk.Frame(frame,)
frame2.place(x=700, y=30, relwidth=0.35, relheight=0.8)

sidebar= ttk.Frame(app, style='sidebar.TFrame')
sidebar.place(relx=0.0, rely=0.43, relheight=0.5, relwidth=0.32)

#button
DataEH= ttk.Button(frame, command=homepage,text="Admin Control Panel")
DataEH.place(relx=0.035, rely=0.35, relheight=0.18, relwidth=0.18)
DataEH= ttk.Button(frame, command=homepage,text="Home")
DataEH.place(relx=0.02, rely=0.85, relheight=0.14, relwidth=0.1)
DataEB= ttk.Button(frame, command=showEntryfield,text="Book in")
DataEB.place(relx=0.13, rely=0.85, relheight=0.14, relwidth=0.1)
DataEB= ttk.Button(frame,text="Cus-Contacts",command=sessions)
DataEB.place(relx=0.24, rely=0.85, relheight=0.14, relwidth=0.1)
DataEB= ttk.Button(frame,text="Booked time")
DataEB.place(relx=0.35, rely=0.85, relheight=0.14, relwidth=0.1)



#home booked sessions
Booked_sessions= ttk.Frame(app, style='mainslot.TFrame')
Booked_sessions.place(relx=0.29, rely=0.40, relheight=0.52, relwidth=0.68) 
#headder
sessions=ttk.LabelFrame(Booked_sessions, text='Booked sessions', relief='solid',)
sessions.place(relx=0.01, rely=0.05, relheight=0.99, relwidth=0.97) 

# Create a style
style = ttk.Style()
style.configure("Treeview",
                background="#d1d1f4",
                foreground="black",
                rowheight=25,
                fieldbackground="lightgray")

style.map('Treeview', background=[('selected', '#003560')])

# Change the font of the Treeview
style.configure("Treeview.Heading", font=('times', 14, 'bold',),background="blue")
style.configure("Treeview", font=('Arial', 10))


#treeview
tree=ttk.Treeview(sessions, columns=('Name','Team','Activity','Phone',),show="headings", padding=5)
tree.place(relx=0, rely=0.02, relheight=0.85, relwidth=0.96)
tree.heading('Name',text="Name")
tree.heading('Team',text="Team-Size")
tree.heading('Activity',text="Activity")
tree.heading('Phone',text="Phone")

# Define the column widths
tree.column('Name', width=100,anchor="center")
tree.column('Team', width=50,anchor="center")
tree.column('Activity', width=50,anchor="center")
tree.column('Phone', width=50,anchor="center")


#main Entry frame
mainslot= ttk.Frame(app, style='mainslot.TFrame')
mainslot.place(relx=0, rely=0, relheight=0, relwidth=0)

#name of the booking Company
LabelN=ttk.Label(mainslot, text="Company Name", background=slotbg, foreground=slotfg, relief="ridge")
LabelN.place(relx=0.08, rely=0.1,relheight=0.125,relwidth=0.2)
Entry1= ttk.Entry(mainslot,font=textfont)
Entry1.place(relx=0.3, rely=0.1, relheight=0.125, relwidth=0.3000)

#items in the side bar
Instructor=ttk.Label(sidebar, text="Available Instructors", background=bg, foreground="white", relief="ridge") 
Instructor.place(relx=0.08, rely=0.1,relheight=0.125,relwidth=0.6)
inst=ttk.Treeview(sidebar, columns=(1,2))
inst.place(relx=0.08, rely=0.2, relheight=0.8,relwidth=0.8)
inst.heading(1,text="Activity")
inst.heading(2,text="Instructor")

# Horizontal placement of text fields and entries at the bottom

# Check-in date
lbl_checkin = ttk.Label(mainslot, text="Check-in Date:", background=slotbg, foreground=slotfg, relief="solid", )
lbl_checkin.place(relx=0.08, rely=checkin)
entry_checkin = DateEntry(mainslot, width=checkw,font=textfont)
entry_checkin.place(relx=0.3, rely=checkin)

# Check-out date
lbl_checkout = ttk.Label(mainslot, text="Check-out Date:", background=slotbg, foreground=slotfg, relief="solid")
lbl_checkout.place(relx=0.47, rely=checkout)
entry_checkout = DateEntry(mainslot, width=checkw, font=textfont)
entry_checkout.place(relx=0.64, rely=checkout)

#Number of guests
LabelN=ttk.Label(mainslot, text="Team Size",background=slotbg, foreground=slotfg, relief="ridge")
LabelN.place(relx=0.64, rely=0.1,relheight=0.125,relwidth=0.15)
Entry1= ttk.Entry(mainslot)
Entry1.place(relx=0.8, rely=0.1, relheight=0.125, relwidth=0.15)

# Destination
lbl_destination = ttk.Label(mainslot, text="Booked Event:", background=bg, foreground='white')
lbl_destination.place(relx=0.08, rely=0.6)
destination_options = ["Canoeing", "Swimming", "Bike riding"]
selected_destination = tk.StringVar(value="Canoeing")  # Default value
destination_menu = ttk.OptionMenu(mainslot, selected_destination, *destination_options)
destination_menu.place(relx=0.3, rely=bottom_y )

lbl_ins = ttk.Label(mainslot, text="Instructor:", background=bg, foreground='white')
lbl_ins.place(relx=0.08, rely=0.8, )
entry_ins = ttk.Entry(mainslot, width=entry_width)
entry_ins.place(relx=0.3, rely=bottom_y2)

#Contacts
#Number of guests
LabelN=ttk.Label(mainslot, text="Phone",background=slotbg, foreground=slotfg, relief="ridge")
LabelN.place(relx=0.08, rely=0.4,relheight=0.125,relwidth=0.2)
Entry1= ttk.Entry(mainslot)
Entry1.place(relx=0.3, rely=0.4, relheight=0.125, relwidth=0.3)

# Title Label
title_label = ttk.Label(frame, text="A+ Booking System", font=('Arial', 20, 'bold'), foreground='white', background='#003560')
title_label.place(relx=0.05, rely=0.05)

# Number of guests
# Search button
btn_search = ttk.Button(frame, text="Search", command=search)
btn_search.place(relx=0.5, rely=bottom_y + 0.5)

# List of image paths
image_paths = ["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg", "image5.jpg"]

# Initialize slideshow in the slideshow frame
slideshow_app = SlideshowApp(frame2, image_paths)

app.mainloop()
