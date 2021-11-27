def caesar_cipher(text, n):
    result = ''
    for char in range(len(text)):
        letter = text[char]
        if letter.isupper():  # Checks if letter is uppercase
            # Substracts 65 & 97 to calculat w/o ascii value
            # Adds 65 & 97 back in to convert after shift
            result += chr((ord(letter) + n - 65) % 26 + 65)
            # else, computers if letter is lowercase
        elif ord(letter) == 32:  # if space, then keep space.
            result += chr(32)
        else:
            result += chr((ord(letter) + n - 97) % 26 + 97)
    return result


test = 'Hello There'
print(caesar_cipher(test, 1))
