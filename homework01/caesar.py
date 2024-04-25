def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    new_number = 0
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                if ord(plaintext[i]) + shift > ord("Z"):
                    sdvig = ord("Z") - ord(plaintext[i])
                    shift2 = shift - sdvig
                    new_letter_number = ord("A") + shift2 - 1
                    new_letter = chr(new_letter_number)
                    ciphertext += str(new_letter)
                else:
                    new_number = ord(plaintext[i]) + shift
                    new_letter = chr(new_number)
                    ciphertext += str(new_letter)
            if plaintext[i].islower():
                if ord(plaintext[i]) + shift > ord("z"):
                    sdvig = ord("z") - ord(plaintext[i])
                    shift2 = shift - sdvig
                    new_letter_number = ord("a") + shift2 - 1
                    new_letter = chr(new_letter_number)
                    ciphertext += str(new_letter)
                else:
                    new_number = ord(plaintext[i]) + shift
                    new_letter = chr(new_number)
                    ciphertext += str(new_letter)
        else:
            ciphertext += str(plaintext[i])
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    new_number = 0
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
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
