#!/usr/bin/python

import os
import string
import random

MAX_SOX_FILES = 50  # sox can't catenate more than this many files
LETTER_REPEATS = 3

WAV_DIR = './wavs'
OUTPUT_DIR = './output'

def main():
    sequenceLength = 1000
    intermediateCount = sequenceLength / MAX_SOX_FILES / LETTER_REPEATS
    for i in range(intermediateCount):
        makePracticeSequence(MAX_SOX_FILES, i)

    mergeIntermediate(intermediateCount)
    makeMp3Output()
    cleanUp()
    print("done")

def makePracticeSequence(letterCount, index):
    allChars = string.ascii_lowercase + string.digits
    charCount = len(allChars)
    cmd = "sox "
    for i in range(letterCount / LETTER_REPEATS):
        character = allChars[random.randint(0, charCount - 1)]
        for j in range(LETTER_REPEATS):
            cmd += "%s/morse_%s.wav " % (WAV_DIR, character)
            cmd += "%s/morseLetterGap.wav " % (WAV_DIR)
            cmd += "%s/say_%s.wav " % (WAV_DIR, character)
            cmd += "%s/interLetterGap.wav " % (WAV_DIR)
    cmd += "%s/practice%02d.wav" % (OUTPUT_DIR, index)
    # print(cmd)
    os.system(cmd)


def mergeIntermediate(count):
    cmd = "sox "
    for i in range(count):
        cmd += "%s/practice%02d.wav " % (OUTPUT_DIR, i)
    cmd += "%s/practice_out.wav" % (OUTPUT_DIR)
    # print(cmd)
    os.system(cmd)

def makeMp3Output():
    cmd = "lame %s/practice_out.wav %s/practice_out.mp3" % (OUTPUT_DIR, OUTPUT_DIR)
    os.system(cmd)

def cleanUp():
    cmd = "rm %s/*.wav" % (OUTPUT_DIR)
    os.system(cmd)

if __name__ == "__main__":
    main()
