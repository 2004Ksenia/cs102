def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    new_number = 0
    while len(plaintext) > len(keyword):
        keyword += keyword[new_number]
        new_number += 1

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                shift = ord(keyword[i].upper()) - ord("A")
                if ord(plaintext[i]) + shift > ord("Z"):
                    sdwig = ord("Z") - ord(plaintext[i])
                    shift2 = shift - sdwig
                    new_letter_number = ord("A") + shift2 - 1
                    new_letter = chr(new_letter_number)
                    ciphertext += new_letter
                else:
                    new_number = ord(plaintext[i]) + shift
                    new_letter = chr(new_number)
                    ciphertext += str(new_letter)
            if plaintext[i].islower():
                shift = ord(keyword[i].lower()) - ord("a")
                if ord(plaintext[i]) + shift > ord("z"):
                    sdwig = ord("z") - ord(plaintext[i])
                    shift2 = shift - sdwig
                    new_letter_number = ord("a") + shift2 - 1
                    new_letter = chr(new_letter_number)
                    ciphertext += new_letter
                else:
                    new_number = ord(plaintext[i]) + shift
                    new_letter = chr(new_number)
                    ciphertext += str(new_letter)
        else:
            ciphertext += str(plaintext[i])
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    new_number = 0
    while len(ciphertext) > len(keyword):
        keyword += keyword[new_number]
        new_number += 1

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                shift = ord(keyword[i].upper()) - ord("A")
                if ord(ciphertext[i]) - shift < ord("A"):
                    sdwig = ord(ciphertext[i]) - ord("A")
                    shift2 = shift - sdwig
                    new_letter_number = ord("Z") - shift2 + 1
                    new_letter = chr(new_letter_number)
                    plaintext += str(new_letter)
                else:
                    new_number = ord(ciphertext[i]) - shift
                    new_letter = chr(new_number)
                    plaintext += str(new_letter)
            if ciphertext[i].islower():
                shift = ord(keyword[i].lower()) - ord("a")
                if ord(ciphertext[i]) - shift < ord("a"):
                    sdwig = ord(ciphertext[i]) - ord("a")
                    shift2 = shift - sdwig
                    new_letter_number = ord("z") - shift2 + 1
                    new_letter = chr(new_letter_number)
                    plaintext += str(new_letter)
                else:
                    new_number = ord(ciphertext[i]) - shift
                    new_letter = chr(new_number)
                    plaintext += str(new_letter)
        else:
            plaintext += str(ciphertext[i])
    return plaintext
