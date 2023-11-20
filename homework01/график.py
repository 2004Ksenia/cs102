ciphertext = input()
keyword = input()
a = 0
s = 0
b = 0
plaintext = ''
while len(ciphertext) > len(keyword):
        keyword += keyword[a]
        a += 1

for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                shift = ord(keyword[i].upper()) - ord('A')
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
                shift = ord(keyword[i].lower()) - ord('a')
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
print(plaintext)