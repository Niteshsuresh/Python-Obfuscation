#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import sys


class Magic:

    def addQMark(self, lettersObj):
        rmLtrs = lettersObj[0].replace('?', '')
        lettersObj[0] = re.sub('(?<=.)', '?', rmLtrs)
        return len(lettersObj[0]) - len(rmLtrs)

    def makeRegex(self, letters):
        lettersObj = [letters]
        QRmCount = self.addQMark(lettersObj)
        letters = lettersObj[0]
        regex = '^' + letters + '$'
        if QRmCount == 1:
            regex = letters.replace('?', '')
        return regex

    def fileRead(self, filename):
        wordList = []
        with open(filename, 'rb') as f:
            for word in iter(f.readline(), ''):
                wordList.append(word.strip())
        return wordList

    def magicMatch(
        self,
        magic,
        letter,
        word,
        ):
        IsAMatch = self.magic(letter, word)
        if IsAMatch == True:
            return word
        return False

        def getMagicMatch(self):
            returnedValue = self.magicMatch(magic, letter, unFltWrd)

        return returnValue

        def getFltWrd(self, wrd):
            newWrd = wrd
            return newWrd

    def filterDictWrds(self, letter, wordList):
        CountList = map(getFltWrd(fltWrd),
                        filter(self.getMagicMatch(unFltWrd), wordList))
        return CountList

    def magic(self, letter, word):
        if len(letter) < len(word):
            return False
        letter = ''.join(sorted(letter))
        regexLetter = self.makeRegex(letter)
        regex = re.compile(regexLetter)
        return self.magicFilter(regex, word)

    def magicFilter(self, regex, word):
        word = ''.join(sorted(word))
        match = regex.search(word)
        if match is not None:
            return True
        return False

    def longest(self, letter):
        wordList = self.fileRead('dictionary.txt')
        countList = self.filterDictWrds(letter, wordList)
        return max(countList, key=len)


def magic():
    magicObj = Magic()
    result = magicObj.magic(sys.argv[1], sys.argv[2])
    return result


if __name__ == '__main__':
    print(magic());


			