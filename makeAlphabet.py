#!/usr/bin/python

import os
import string
import random

LETTER_REPEATS = 3

allChars = string.ascii_lowercase + string.digits
charCount = len(allChars)

def main():

    for index in range(charCount):
        makeAlphabetLetter(index)

    mergeIntermediate(index)
    makeMp3Output()
    print("done")

def makeAlphabetLetter(index):
    cmd = "sox "
    character = allChars[index]
    for j in range(LETTER_REPEATS):
        cmd += "morse_%s.wav " % (character)
        cmd += "morseLetterGap.wav "
        cmd += "say_%s.wav " % (character)
        cmd += "morseLetterGap.wav "
    cmd += "interLetterGap.wav alphabet_%02d.wav" % (index)
    print(cmd)
    os.system(cmd)


def mergeIntermediate(count):
    cmd = "sox "
    for i in range(count):
        cmd += "alphabet_%02d.wav " % (i)
    cmd += "alphabet_out.wav"
    print(cmd)
    os.system(cmd)

def makeMp3Output():
    cmd = "lame alphabet_out.wav alphabet_out.mp3"
    os.system(cmd)

if __name__ == "__main__":
    main()
