<<<<<<< HEAD
"""

Project 1: Password Strength Checker 

Objective:

 Develop a Python program that evaluates the strength of a user's password.

  Requirements: 

• Accept password input from the user. 

• Check password length. 

• Verify the presence of:  

    o Uppercase letters (A-Z) 

     o Lowercase letters (a-z)  

    o Numbers (0-9) 

     o Special characters (@, #, $, %, &, etc.)  

• Categorize the password as:  

    o Weak  

    o Medium  

    o Strong  

 • Display the password strength along with appropriate feedback.





     Bonus Features:

      • Display missing password requirements. 

       • Prevent common passwords (e.g., 123456, password). 

        • Suggest improvements for weak passwords.

• Generate a strong password recommendation.

"""

import re
import random
import string


class PasswordStrengthChecker:

    def __init__(self, password):
        self.password = password
        self.score = 0
        self.missing = []

        self.common_passwords = [
            "123456",
            "password",
            "qwerty",
            "admin",
            "welcome",
            "12345678"
        ]

    def check_common_password(self):
        return self.password.lower() in self.common_passwords

    def check_length(self):
        if len(self.password) >= 8:
            self.score += 1
        else:
            self.missing.append("Minimum 8 characters")

    def check_uppercase(self):
        if re.search(r"[A-Z]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one uppercase letter")

    def check_lowercase(self):
        if re.search(r"[a-z]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one lowercase letter")

    def check_number(self):
        if re.search(r"\d", self.password):
            self.score += 1
        else:
            self.missing.append("At least one number")

    def check_special_character(self):
        if re.search(r"[@#$%&*!]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one special character")

    def evaluate_strength(self):

        if self.check_common_password():
            return "Weak"

        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_number()
        self.check_special_character()

        if self.score <= 2:
            return "Weak"
        elif self.score <= 4:
            return "Medium"
        else:
            return "Strong"

    def generate_password(self):
        password = (
            random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_lowercase) +
            random.choice(string.digits) +
            random.choice("@#$%&*!") +
            ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits +
                    "@#$%&*!",
                    k=8
                )
            )
        )
        return password

    def display_result(self):
        strength = self.evaluate_strength()

        print("\nPassword Strength:", strength)

        if self.missing:
            print("\nMissing Requirements:")
            for item in self.missing:
                print("-", item)

        if strength == "Weak":
            print("\nSuggestions:")
            print("- Use at least 8 characters")
            print("- Add uppercase and lowercase letters")
            print("- Include numbers")
            print("- Include special characters")

            print("\nRecommended Strong Password:")
            print(self.generate_password())


# Driver Code
password = input("Enter Password: ")

checker = PasswordStrengthChecker(password)
checker.display_result()
































=======
"""

Project 1: Password Strength Checker 

Objective:

 Develop a Python program that evaluates the strength of a user's password.

  Requirements: 

• Accept password input from the user. 

• Check password length. 

• Verify the presence of:  

    o Uppercase letters (A-Z) 

     o Lowercase letters (a-z)  

    o Numbers (0-9) 

     o Special characters (@, #, $, %, &, etc.)  

• Categorize the password as:  

    o Weak  

    o Medium  

    o Strong  

 • Display the password strength along with appropriate feedback.





     Bonus Features:

      • Display missing password requirements. 

       • Prevent common passwords (e.g., 123456, password). 

        • Suggest improvements for weak passwords.

• Generate a strong password recommendation.

"""

import re
import random
import string


class PasswordStrengthChecker:

    def __init__(self, password):
        self.password = password
        self.score = 0
        self.missing = []

        self.common_passwords = [
            "123456",
            "password",
            "qwerty",
            "admin",
            "welcome",
            "12345678"
        ]

    def check_common_password(self):
        return self.password.lower() in self.common_passwords

    def check_length(self):
        if len(self.password) >= 8:
            self.score += 1
        else:
            self.missing.append("Minimum 8 characters")

    def check_uppercase(self):
        if re.search(r"[A-Z]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one uppercase letter")

    def check_lowercase(self):
        if re.search(r"[a-z]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one lowercase letter")

    def check_number(self):
        if re.search(r"\d", self.password):
            self.score += 1
        else:
            self.missing.append("At least one number")

    def check_special_character(self):
        if re.search(r"[@#$%&*!]", self.password):
            self.score += 1
        else:
            self.missing.append("At least one special character")

    def evaluate_strength(self):

        if self.check_common_password():
            return "Weak"

        self.check_length()
        self.check_uppercase()
        self.check_lowercase()
        self.check_number()
        self.check_special_character()

        if self.score <= 2:
            return "Weak"
        elif self.score <= 4:
            return "Medium"
        else:
            return "Strong"

    def generate_password(self):
        password = (
            random.choice(string.ascii_uppercase) +
            random.choice(string.ascii_lowercase) +
            random.choice(string.digits) +
            random.choice("@#$%&*!") +
            ''.join(
                random.choices(
                    string.ascii_letters +
                    string.digits +
                    "@#$%&*!",
                    k=8
                )
            )
        )
        return password

    def display_result(self):
        strength = self.evaluate_strength()

        print("\nPassword Strength:", strength)

        if self.missing:
            print("\nMissing Requirements:")
            for item in self.missing:
                print("-", item)

        if strength == "Weak":
            print("\nSuggestions:")
            print("- Use at least 8 characters")
            print("- Add uppercase and lowercase letters")
            print("- Include numbers")
            print("- Include special characters")

            print("\nRecommended Strong Password:")
            print(self.generate_password())


# Driver Code
password = input("Enter Password: ")

checker = PasswordStrengthChecker(password)
checker.display_result()
































>>>>>>> d7e009b (Numpy Assignment)
