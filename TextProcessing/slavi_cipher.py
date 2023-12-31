import random


def encrypting_algorithm(user_profiles: dict, name: str, password: str):
    '''
    This functions take the password that the user had inputted,
    encrypt the pass and save the data into
    '''
    key_random = random.randint(1, 33)
    encrypted_message = ''
    for symbol in password:
        encrypted_message += chr(ord(symbol) + key_random)
    user_profile[name] = {'pass': encrypted_message, 'key': key_random}
    return True


def decrypting_algorithm(user_profiles: dict, name: str):
    """
    This function takes the name that has been inputted,
    decrypts it's pass and prints it to the user
    :return:
    """
    user_password = user_profiles[name]['pass']
    key = user_profiles[name]['key']
    decrypted_message = ''
    for symbol in user_password:
        decrypted_message += (chr(ord(symbol) - key))
    return decrypted_message


# Read User Message
name = input('Please enter your name: ')
password = input('Now your password: ')
user_profile = {}

# Call the Encrypting Algorithm function
encrypting_algorithm(user_profile, name, password)
print(user_profile)

# Call the Decrypting Algorithm function
print(decrypting_algorithm(user_profile, name))
