import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SlideshowApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Slideshow")
        self.master.geometry("400x200")

        # Create a list of image paths
        self.image_paths = ["image1.jpg", "image2.jpg", "image3.jpg"]

        # Create a label for displaying images
        self.image_label = tk.Label(self.master)
        self.image_label.pack(fill=tk.BOTH, expand=True)

        # Initialize index for the current image
        self.current_image_index = 0

        # Display the first image
        self.show_image()

        # Call the next_image method after a delay
        self.master.after(2000, self.next_image)

    def show_image(self):
        # Open the image file using PIL
        image_path = self.image_paths[self.current_image_index]
        image = Image.open(image_path)

        # Resize the image to fit the window
        image = image.resize((400, 200))

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

def main():
    root = tk.Tk()
    app = SlideshowApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
