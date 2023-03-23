import random
def caeser_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('a') if char.isupper() else ord('A')
            new_pos = (ord(char) - start + shift)%26
            char = chr(start + new_pos)
        result += char
    return result
def shifting():
    rand_num = random.randrange(1,26)
    return rand_num
def main():
    rand_num = shifting()
    text = caeser_cipher("The quick brown fox jumps over the lazy dog.", rand_num)
    txt_file = open("encrypted.txt","w")
    txt_file.write(text)
    txt_file.close()
main()