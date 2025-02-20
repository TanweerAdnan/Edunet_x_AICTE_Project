import cv2
import os

img_path = "encryptedImage.png"  # Use PNG to prevent corruption
img = cv2.imread(img_path)

if img is None:
    print("Error: Encrypted image not found!")
    exit()

# Read stored password and message length
try:
    with open("password.txt", "r") as f:
        stored_password = f.read().strip()
    with open("msg_length.txt", "r") as f:
        msg_length = int(f.read().strip())
except:
    print("Error: Password or message length file missing!")
    exit()

c = {i: chr(i) for i in range(255)}

pas = input("Enter passcode for decryption: ")
if pas == stored_password:
    n, m, z = 0, 0, 0
    decoded_msg = ""

    for _ in range(msg_length):
        decoded_msg += c[img[n, m, z]]  # Retrieve ASCII and convert back to character
        z = (z + 1) % 3
        if z == 0:
            m += 1
            if m >= img.shape[1]:
                m = 0
                n += 1

    print("Decryption message:", decoded_msg)
else:
    print("YOU ARE NOT AUTHORIZED!")


