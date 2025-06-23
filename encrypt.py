import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def encode_image(image_path, secret_message):
    img = Image.open("Nature.jpg")
    encoded_img = img.copy()
    
    binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '1111111111111110'  # Delimiter
    data_index = 0
    
    for pixel in encoded_img.getdata():
        if data_index < len(binary_message):
            new_pixel = list(pixel)
            new_pixel[0] = (new_pixel[0] & ~1) | int(binary_message[data_index])  # Modify the LSB
            encoded_img.putpixel((data_index % img.width, data_index // img.width), tuple(new_pixel))
            data_index += 1
            
    return encoded_img

def encrypt():
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return
    
    secret_message = message_entry.get()
    
    if not secret_message:
        messagebox.showerror("Error", "Please enter a secret message.")
        return
    
    encoded_img = encode_image(image_path, secret_message)
    output_path = "encryptedImage.png"
    encoded_img.save(output_path)
    
    messagebox.showinfo("Success", f"Message encrypted successfully into '{output_path}'.")

# GUI Setup
root = tk.Tk()
root.title("Steganography Encryption Tool")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

message_label = tk.Label(frame, text="Enter Secret Message:")
message_label.pack()

message_entry = tk.Entry(frame, width=50)
message_entry.pack(pady=5)

encrypt_button = tk.Button(frame, text="Encrypt Message", command=encrypt)
encrypt_button.pack(pady=5)

root.mainloop()
