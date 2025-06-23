import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ""
    
    for pixel in img.getdata():
        binary_message += str(pixel[0] & 1)  # Read the LSB
        
        if binary_message.endswith('1111111111111110'):  # Check for delimiter
            break
            
    message = ""
    for i in range(0, len(binary_message) - 16, 8):  # Convert binary to characters
        byte = binary_message[i:i + 8]
        message += chr(int(byte, 2))
        
    return message

def decrypt():
    image_path = filedialog.askopenfilename(title="Select Encrypted Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if not image_path:
        return
    
    hidden_message = decode_image(image_path)
    
    if hidden_message:
        messagebox.showinfo("Decrypted Message", f"Decrypted Message: {hidden_message}")
    else:
        messagebox.showerror("Error", "No hidden message found.")

# GUI Setup
root = tk.Tk()
root.title("Steganography Decryption Tool")

decrypt_button = tk.Button(root, text="Decrypt Message", command=decrypt)
decrypt_button.pack(pady=20)

root.mainloop()
