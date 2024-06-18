def caesar_cipher(text, shift, mode):
    result = ""

    
    if mode == 'decrypt':
        shift = -shift

    
    for char in text:
        if char.isalpha():
             
            start = ord('A') if char.isupper() else ord('a')
             
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            
            result += char

    return result

def main():
    while True:
        
        mode = input("Would you like to Encrypt or Decrypt or Exit the program? ").lower()
        if mode == 'exit':
            print("Exiting the program.")
            break
        elif mode not in ['Encrypt', 'Decrypt']:
            print("Invalid mode. Please choose 'Encrypt' or 'Decrypt' or 'Exit'.")
            continue

         
        try:
            shift = int(input("Enter the kay value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

         
        text = input("Enter the text to be processed: ")

         
        result = caesar_cipher(text, shift, mode)
        print(f"The result is: {result}")

if __name__ == "__main__":
    main()
