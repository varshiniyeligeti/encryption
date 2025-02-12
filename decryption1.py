import cv2
import os

def decrypt_image():
    # Load the encrypted image
    img = cv2.imread(r"E:\encryptedImage.jpg")  # Replace with your actual encrypted image path
    if img is None:
        print("Error: Encrypted image not found.")
        return

    # Get the passcode for decryption
    password = input("Enter passcode for Decryption: ")

    # Ask for the encryption passcode and compare
    stored_password = input("Enter the passcode used for encryption: ")  # In real life, this should be securely stored

    if password != stored_password:
        print("Incorrect passcode. Access denied.")
        return

    # Flatten the image to 1D to easily extract the hidden message bits
    img_flat = img.flatten()

    # Extract the message from the LSBs (Least Significant Bits) of each pixel
    message_bits = []
    for i in range(len(img_flat)):
        # Get the LSB (least significant bit) of the current pixel
        message_bits.append(img_flat[i] & 1)

    # Group the bits into bytes (8 bits = 1 byte)
    byte_list = []
    for i in range(0, len(message_bits), 8):
        byte = 0
        for j in range(8):
            byte |= (message_bits[i + j] << (7 - j))  # Reconstruct byte from bits
        byte_list.append(byte)

    # Convert the byte list back to a string message
    try:
        message = bytes(byte_list).decode('utf-8')
    except UnicodeDecodeError:
        message = bytes(byte_list).decode('utf-8', errors='ignore')  # Ignore decoding errors for non-UTF characters

    # Print the decrypted message
    print("Decrypted message:", message)

if __name__ == "__main__":
    decrypt_image()
