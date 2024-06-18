import re

def check_password_strength(password):
     
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

     
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])

     
    if score == 5:
        return "Very Strong", score
    elif score == 4:
        return "Strong", score
    elif score == 3:
        return "Moderate", score
    else:
        return "Weak", score

def main():
    while True:
        password = input("Enter a password to check its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the program.")
            break
        
        strength, score = check_password_strength(password)
        print(f"Password strength: {strength} (Score: {score}/5)")

if __name__ == "__main__":
    main()
