#!/usr/bin/python

import os
import string
import random

LETTER_REPEATS = 3

WAV_DIR = './wavs'
OUTPUT_DIR = './output'

allChars = string.ascii_lowercase + string.digits
charCount = len(allChars)

def main():

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for index in range(charCount):
        makeAlphabetLetter(index)

    mergeIntermediate(index)
    makeMp3Output()
    cleanUp()
    print("done")

def makeAlphabetLetter(index):
    cmd = "sox "
    character = allChars[index]
    for j in range(LETTER_REPEATS):
        cmd += "%s/morse_%s.wav " % (WAV_DIR, character)
        cmd += "%s/morseLetterGap.wav " % (WAV_DIR)
        cmd += "%s/say_%s.wav " % (WAV_DIR, character)
        cmd += "%s/morseLetterGap.wav " % (WAV_DIR)
    cmd += "%s/navy_%s.wav %s/interLetterGap.wav %s/alphabet_%02d.wav" % (WAV_DIR, character, WAV_DIR, OUTPUT_DIR, index)
    # print(cmd)
    os.system(cmd)


def mergeIntermediate(count):
    cmd = "sox "
    for i in range(count):
        cmd += "%s/alphabet_%02d.wav " % (OUTPUT_DIR, i)
    cmd += "%s/alphabet_out.wav" % (OUTPUT_DIR)
    # print(cmd)
    os.system(cmd)

def makeMp3Output():
    cmd = "lame %s/alphabet_out.wav %s/alphabet_out.mp3" % (OUTPUT_DIR, OUTPUT_DIR)
    os.system(cmd)

def cleanUp():
    cmd = "rm %s/*.wav" % (OUTPUT_DIR)
    os.system(cmd)

if __name__ == "__main__":
    main()
