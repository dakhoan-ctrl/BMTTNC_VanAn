class CaesarCipher:
    def encrypt(self, text, key):
        result = ""
        key = int(key)
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + key - 65) % 26 + 65)
            elif char.islower():
                result += chr((ord(char) + key - 97) % 26 + 97)
            else:
                result += char
        return result