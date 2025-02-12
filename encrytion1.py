import cv2
import os
import string

def encrypt_image():
    # Load the image (using raw string literal to handle backslashes in the file path)
    img = cv2.imread(r"C:\Users\acer\Downloads\varshini.jpg")  # Replace with the correct image path

    if img is None:
        print("Error: Image not found.")
        return

    # Get the secret message and password
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    # Convert the message to ASCII (ignoring non-ASCII characters if any)
    msg = msg.encode('ascii', 'ignore').decode('ascii')  # Ignore non-ASCII characters if present

    # Create dictionaries for encryption
    d = {}
    c = {}
    for i in range(255):
        d[chr(i)] = i
        c[i] = chr(i)

    # Encryption logic
    n, m, z = 0, 0, 0
    for i in range(len(msg)):
        img[n, m, z] = d[msg[i]]
        n += 1
        m += 1
        z = (z + 1) % 3

    # Save the encrypted image
    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

    print("Encryption complete! Image saved as encryptedImage.jpg")
    return password  # Returning password for future decryption


if __name__ == "__main__":
    encrypt_image()
