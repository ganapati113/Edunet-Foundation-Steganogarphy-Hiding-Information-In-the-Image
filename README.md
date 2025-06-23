# Edunet-Foundation-Steganogarphy-Hiding-Information-In-the-Image-
Edunet Foundation Project (Steganogarphy Hiding Information In the Image) 
# 🕵️‍♂️ Steganography Tool - Hide Secret Messages in Images
This project is a beginner-friendly Steganography Tool built in **Python** that allows users to **hide** and **reveal secret messages** in images using the **Least Significant Bit (LSB)** technique.
It features a simple yet powerful **GUI built with Tkinter**, making it accessible even to non-programmers.
## 📌 Features
- 🔐 **Encrypt Messages** into PNG or JPG images
- 🔓 **Decrypt Hidden Messages** from images
- 💡 **GUI Interface** using Tkinter for easy interaction
- 🧠 Learn fundamental concepts of Image Processing and Data Security

🧰 Requirements
To run this project, make sure the following are installed:
- ✅ Python 3.x
- ✅ [Pillow](https://pillow.readthedocs.io/en/stable/) (`pip install pillow`)
- ✅ Tkinter (pre-installed with most Python distributions)

🧑‍💻 Installation & Setup
1️⃣ Clone the Repository
2️⃣ Install Dependencies
pip install pillow
Tkinter is usually pre-installed. If not:
sudo apt-get install python3-tk  # For Linux/Ubuntu users
🚀 How to Run the Project
✅ Option 1: Run as Python Script (GUI Mode)
🔐 Encrypt a Message
python encrypt.py
```
> Steps:
> * GUI window opens.
> * Type your secret message.
> * Click "Select Image" and choose a `.png` or `.jpg` file.
> * Click "Encrypt Message" — a file named `encryptedImage.png` will be created with your hidden message.

🔓 Decrypt a Message
python decrypt.py
```
> Steps:
>
>  GUI window opens.
>  Click "Select Encrypted Image".
>  The hidden message will pop up in a dialog box.

📓 Option 2: Run in Jupyter Notebook (Step-by-Step)
Step 1: Import Libraries
```python
from PIL import Image
```
Step 2: Encode Function
```python
def encode_image(image_path, secret_message):
    img = Image.open(image_path)
    encoded_img = img.copy()

    binary_message = ''.join(format(ord(char), '08b') for char in secret_message) + '1111111111111110'
    data_index = 0

    for x in range(img.width):
        for y in range(img.height):
            if data_index < len(binary_message):
                pixel = list(img.getpixel((x, y)))
                pixel[0] = (pixel[0] & ~1) | int(binary_message[data_index])
                encoded_img.putpixel((x, y), tuple(pixel))
                data_index += 1

    encoded_img.save("encryptedImage.png")
    print("✅ Message encoded and image saved as encryptedImage.png")

Step 3: Decode Function
python
def decode_image(image_path):
    img = Image.open(image_path)
    binary_message = ""
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.getpixel((x, y))
            binary_message += str(pixel[0] & 1)
            if binary_message.endswith("1111111111111110"):
                break
    message = ""
    for i in range(0, len(binary_message)-16, 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    return message

Step 4: Use the Functions
python
encode_image("Nature.jpg", "This is a secret message!")
print(decode_image("encryptedImage.png"))

🏁 Project Structure
Stega-Aicte-Project/
├── encrypt.py              # GUI script to encrypt
├── decrypt.py              # GUI script to decrypt
├── Nature.jpg              # Sample image
├── encryptedImage.png      # Output image
├── README.md               # Documentation (this file)
```
⚠️ Notes & Tips
* 📏 Make sure your message fits within the number of pixels in your image.
* 🧠 Works best with `.png` images due to less compression.
* 🛑 Uses delimiter `1111111111111110` to detect end of message.
* 🖥️ Tkinter might behave differently across platforms — test locally.

🙌 Acknowledgements
Heartful thanks to:
* 🎓 Edunet Foundation for providing the platform and learning resources
* 🤖 IBM & AICTE for a valuable 6-week internship experience
* 💡 All mentors and peers for their continuous support

-📚 References
* 🔗 [Pillow Documentation](https://pillow.readthedocs.io/en/stable/)
* 🔗 [Tkinter Guide](https://docs.python.org/3/library/tkinter.html)
* 📘 Concepts of Steganography in Cybersecurity Research Papers

-💬 Final Words
> 🎯 “Sometimes, the best place to hide something... is in plain sight.”
> This project offers a practical introduction to cybersecurity and image processing with real-world relevance.


