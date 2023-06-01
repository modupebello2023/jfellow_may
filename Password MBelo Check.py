#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def check_password(password):
    # Check the password length
    if len(password) < 6 or len(password) > 12:
        return "Password length should be between 6 and 12 characters"

    # Create flags to track the presence of required characters
    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    # Iterate through each character in the password
    for char in password:
        # Check if the character is a lowercase letter
        if char.islower():
            has_lowercase = True

        # Check if the character is an uppercase letter
        elif char.isupper():
            has_uppercase = True

        # Check if the character is a digit
        elif char.isdigit():
            has_digit = True

        # Check if the character is a special character
        elif char in "$#@":
            has_special = True

    # Check the presence of required characters
    if not has_lowercase:
        return "Password should have at least one lowercase letter"

    if not has_uppercase:
        return "Password should have at least one uppercase letter"

    if not has_digit:
        return "Password should have at least one digit"

    if not has_special:
        return "Password should have at least one special character [$#@]"

    return "Password is valid"

password = input("Enter your password: ")
print(check_password(password))


# In[ ]:





# In[ ]:




