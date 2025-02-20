import cv2
import os

img_path = r"C:\Users\Nadeem\Documents\Project Edunet\rubies.png"  # Use a PNG image
img = cv2.imread(img_path)

if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}

n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]  # Storing ASCII value in pixel
    z = (z + 1) % 3
    if z == 0:
        m += 1
        if m >= img.shape[1]:  # Move to next row
            m = 0
            n += 1

cv2.imwrite("encryptedImage.png", img)  # Save as PNG
print("Message encoded in 'encryptedImage.png'.")

# Save the password & message length
with open("password.txt", "w") as f:
    f.write(password)
with open("msg_length.txt", "w") as f:
    f.write(str(len(msg)))

os.system("start encryptedImage.png")  # Open image on Windows



