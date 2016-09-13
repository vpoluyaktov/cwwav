#!/usr/bin/python

import os
import string
import random

MAX_SOX_FILES = 63	# sox can't catenate more than this many files

def main():
	sequenceLength = 200
	intermediateCount = sequenceLength / MAX_SOX_FILES
	for i in range(intermediateCount):
		makePracticeSequence(MAX_SOX_FILES, i)
	
	mergeIntermediate(intermediateCount)

def makePracticeSequence(letterCount, index):
	allChars = string.ascii_lowercase + string.digits
	charCount = len(allChars)
	cmd = "sox "
	for i in range(letterCount):
		character = allChars[random.randint(0, charCount -1)]
		cmd += "morse_%s.wav " % (character)
		cmd += "morseLetterGap.wav "
		cmd += "say_%s.wav " % (character)
		cmd += "interLetterGap.wav "
	cmd += "practice%02d.wav" % (index)
	os.system(cmd)

def mergeIntermediate(count):
	cmd = "sox "
	for i in range(count):
		cmd += "practice%02d.wav " % (i)
	cmd += "practice_out.wav"
	os.system(cmd)
	
if __name__ == "__main__":
	main()

