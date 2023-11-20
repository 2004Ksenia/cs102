plaintext = input()
keyword = input()
a = 0
s = 0
b = 0
ciphertext = ''
while len(plaintext) > len(keyword):
        keyword += keyword[a]
        a += 1

for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                shift = ord(keyword[i].upper()) - ord('A')
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
                shift = ord(keyword[i].lower()) - ord('a')
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

print(keyword)
print(len(plaintext))
print(len(keyword))
print(ciphertext)

