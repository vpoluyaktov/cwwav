#!/usr/bin/python

import os
import string
import random

MAX_SOX_FILES = 50  # sox can't catenate more than this many files
LETTER_REPEATS = 3


def main():
    sequenceLength = 600
    intermediateCount = sequenceLength / MAX_SOX_FILES / LETTER_REPEATS
    for i in range(intermediateCount):
        makePracticeSequence(MAX_SOX_FILES, i)

    mergeIntermediate(intermediateCount)
    makeMp3Output()
    print("done")

def makePracticeSequence(letterCount, index):
    allChars = string.ascii_lowercase + string.digits
    charCount = len(allChars)
    cmd = "sox "
    for i in range(letterCount / LETTER_REPEATS):
        character = allChars[random.randint(0, charCount - 1)]
        for j in range(LETTER_REPEATS):
            cmd += "morse_%s.wav " % (character)
            cmd += "morseLetterGap.wav "
            cmd += "say_%s.wav " % (character)
            cmd += "interLetterGap.wav "
    cmd += "practice%02d.wav" % (index)
    print(cmd)
    os.system(cmd)


def mergeIntermediate(count):
    cmd = "sox "
    for i in range(count):
        cmd += "practice%02d.wav " % (i)
    cmd += "practice_out.wav"
    print(cmd)
    os.system(cmd)

def makeMp3Output():
    cmd = "lame practice_out.wav practice_out.mp3"
    os.system(cmd)

if __name__ == "__main__":
    main()
