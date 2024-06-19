import sqlite3

try:
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('A+.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Create a table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        team INTEGER NOT NULL,
        activity TEXT NOT NULL,
        phone TEXT NOT NULL
    )
    ''')

    # Insert sample data into the table
    cursor.execute('INSERT INTO clients (name, team, activity, phone) VALUES (?, ?, ?, ?)', ('Alice', 10, 'swimming', '0998765'))
    cursor.execute('INSERT INTO clients (name, team, activity, phone) VALUES (?, ?, ?, ?)', ('Bob', 35, 'swimming', '09987654'))

    # Commit the transaction
    conn.commit()
except sqlite3.Error as e:
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    if conn:
        conn.close()
import sqlite3
import tkinter as tk
from tkinter import ttk

# Function to fetch data from the database
def fetch_data():
    conn = sqlite3.connect('A+.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    rows = cursor.fetchall()
    conn.close()
    return rows

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

# Create the main window
root = tk.Tk()
root.title("SQLite Data Viewer")

# Create a style
style = ttk.Style()
style.configure("Treeview",
                background="lightgray",
                foreground="black",
                rowheight=25,
                fieldbackground="lightgray")

style.map('Treeview', background=[('selected', 'blue')])

# Change the font of the Treeview
style.configure("Treeview.Heading", font=('Arial', 12, 'bold',),background="blue")
style.configure("Treeview", font=('Arial', 10))

# Create a Treeview widget
tree = ttk.Treeview(root, columns=('ID', 'Name', 'Team', 'Activity', 'Phone'), show='headings', style="Treeview")

# Define the column headings
tree.heading('ID', text='ID')
tree.heading('Name', text='Name')
tree.heading('Team', text='Team')
tree.heading('Activity', text='Activity')
tree.heading('Phone', text='Phone')

# Define the column widths
tree.column('ID', width=20, anchor="center")
tree.column('Name', width=150,anchor="center")
tree.column('Team', width=50,anchor="center")
tree.column('Activity', width=50,anchor="center")
tree.column('Phone', width=50,anchor="center")

# Pack the Treeview widget
tree.pack(fill=tk.BOTH, expand=True)

# Populate the Treeview with data
populate_treeview(tree)

# Run the main loop
root.mainloop()

