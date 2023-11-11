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
    a = ''
    b = 0
    s = 0
    ciphertext = ""
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                if ord(plaintext[i]) + shift > ord('Z'):
                    s = ord('Z') - ord(plaintext[i])
                    shift2 = shift - s
                    b = ord('A') + shift2 - 1
                    a = chr(b)
                    ciphertext += a
                else:
                    a = ord(plaintext[i]) + shift
                    a = chr(a)
                    ciphertext += a
            if plaintext[i].islower():
                if ord(plaintext[i]) + shift > ord('z'):
                    s = ord('z') - ord(plaintext[i])
                    shift2 = shift - s
                    b = ord('a') + shift2 - 1
                    a = chr(b)
                    ciphertext += a
                else:
                    a = ord(plaintext[i]) + shift
                    a = chr(a)
                    ciphertext += a
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
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                if ord(ciphertext[i]) - shift < ord('A'):
                    s = ord(ciphertext[i]) - ord('A')
                    shift2 = shift - s
                    b = ord('Z') - shift2 + 1
                    a = chr(b)
                    plaintext += a
                else:
                    a = ord(ciphertext[i]) - shift
                    a = chr(a)
                    plaintext += a
            if ciphertext[i].islower():
                if ord(ciphertext[i]) - shift < ord('a'):
                    s = ord(ciphertext[i]) - ord('a')
                    shift2 = shift - s
                    b = ord('z') - shift2 + 1
                    a = chr(b)
                    plaintext += a
                else:
                    a = ord(ciphertext[i]) - shift
                    a = chr(a)
                    plaintext += a
        else:
            plaintext += str(ciphertext[i])
    return plaintext

 #33 буквы
