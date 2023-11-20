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
    a = 0
    while len(plaintext) > len(keyword):
        keyword += keyword[a]
        a += 1

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                shift = ord(keyword[i].upper()) - ord("A")
                if ord(plaintext[i]) + shift > ord("Z"):
                    s = ord("Z") - ord(plaintext[i])
                    shift2 = shift - s
                    b = ord("A") + shift2 - 1
                    a = chr(b)
                    ciphertext += a
                else:
                    a = ord(plaintext[i]) + shift
                    a = chr(a)
                    ciphertext += a
            if plaintext[i].islower():
                shift = ord(keyword[i].lower()) - ord("a")
                if ord(plaintext[i]) + shift > ord("z"):
                    s = ord("z") - ord(plaintext[i])
                    shift2 = shift - s
                    b = ord("a") + shift2 - 1
                    a = chr(b)
                    ciphertext += a
                else:
                    a = ord(plaintext[i]) + shift
                    a = chr(a)
                    ciphertext += a
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
    a = 0
    while len(ciphertext) > len(keyword):
        keyword += keyword[a]
        a += 1

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                shift = ord(keyword[i].upper()) - ord("A")
                if ord(ciphertext[i]) - shift < ord("A"):
                    s = ord(ciphertext[i]) - ord("A")
                    shift2 = shift - s
                    b = ord("Z") - shift2 + 1
                    a = chr(b)
                    plaintext += a
                else:
                    a = ord(ciphertext[i]) - shift
                    a = chr(a)
                    plaintext += a
            if ciphertext[i].islower():
                shift = ord(keyword[i].lower()) - ord("a")
                if ord(ciphertext[i]) - shift < ord("a"):
                    s = ord(ciphertext[i]) - ord("a")
                    shift2 = shift - s
                    b = ord("z") - shift2 + 1
                    a = chr(b)
                    plaintext += a
                else:
                    a = ord(ciphertext[i]) - shift
                    a = chr(a)
                    plaintext += a
        else:
            plaintext += str(ciphertext[i])
    return plaintext
