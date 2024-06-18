from PIL import Image
import numpy as np
import os

def encrypt_image(image_path, key):
    # Open the image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Ensure image_array is of type int
    image_array = image_array.astype(np.int32)
    
    # Apply encryption by adding the key to each pixel value
    encrypted_array = (image_array + key) % 256
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    
    return encrypted_image

def decrypt_image(image_path, key):
    # Open the encrypted image
    image = Image.open(image_path)
    image_array = np.array(image)
    
    # Ensure image_array is of type int
    image_array = image_array.astype(np.int32)
    
    # Apply decryption by subtracting the key from each pixel value
    decrypted_array = (image_array - key) % 256
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    
    return decrypted_image

def main():
    input_image_path = r"C:\Users\ma970\Desktop\image encryption task 2\iphone-card-40-iphone15prohero-202309_FMT_WHH.jpeg"
    output_directory = r"C:\Users\ma970\Desktop\image encryption task 2"

    while True:
        # Ask the user for the mode
        mode = input("Would you like to (encrypt) or (decrypt) or (exit) the program? ").lower()
        if mode == 'exit':
            print("Exiting the program.")
            break
        elif mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt' or 'exit'.")
            continue

        # Get the key
        try:
            key = int(input("Enter the key (integer value): "))
        except ValueError:
            print("Invalid key. Please enter an integer.")
            continue

        if mode == 'encrypt':
            encrypted_image = encrypt_image(input_image_path, key)
            encrypted_image_path = os.path.join(output_directory, "encrypted_image.png")
            encrypted_image.save(encrypted_image_path)
            print(f"Image encrypted and saved as {encrypted_image_path}")
        elif mode == 'decrypt':
            decrypted_image = decrypt_image(input_image_path, key)
            decrypted_image_path = os.path.join(output_directory, "decrypted_image.png")
            decrypted_image.save(decrypted_image_path)
            print(f"Image decrypted and saved as {decrypted_image_path}")

if __name__ == "__main__":
    main()
