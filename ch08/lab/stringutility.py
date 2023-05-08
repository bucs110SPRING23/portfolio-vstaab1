class StringUtility:
    def __init__(self, string):
        self.string = string
    def __str__(self):
        return str(self.string)
    def vowels(self):
        self.num = len(self.string)
        self.count = 0
        for letter in self.string:
            self.letter = letter
            if self.letter == "a" or self.letter == "e" or self.letter == "i" or self.letter == "o" or self.letter == "u":
                self.count += 1
        if self.count < 5:
            return str(self.count)
        else:
            return str("many")
    def bothEnds(self):
        if len(self.string) > 2:
            self.ends = str(self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
        else:
            self.ends = ""
        return str(self.ends)
    def fixStart(self):
        if len(self.string) > 1:
            self.first_letter = self.string[0]
            self.word = self.first_letter
            self.newstring = ""
            for i in range(1,len(self.string)):
                self.newstring += self.string[i]
            for letter in self.newstring:
                self.letter = letter
                if self.letter == self.first_letter:
                    self.letter = '*'
                self.word += self.letter
            return str(self.word)
        else:
            return str(self.string)
    def asciiSum(self):
        self.sum = 0
        for letter in self.string:
            self.code = int(ord(letter))
            self.sum += int(self.code)
        return int(self.sum)
    def cipher(self):
        result = ""
        for char in self.string:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                new_pos = (ord(char) - start + len(self.string))%26
                char = chr(start + new_pos)
            result += char
        return result