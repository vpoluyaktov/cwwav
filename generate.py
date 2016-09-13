#!/usr/bin/python

import os
import string
import random

def main():
	makeSilence(0.3, "morseLetterGap")
	makeSilence(0.8, "interLetterGap")
	
	allChars = string.ascii_lowercase + string.digits
	for letter in allChars:
		morseLetter(letter)
		speakLetter(letter)
	
	makePracticeSequence(5)	# just to test
	
def morseLetter(letter):
	print letter
	cmd = "echo \"%s\" |./cwwav -r 22050 -o morse_%s.wav" % (letter,letter)
	os.system(cmd)

def speakLetter(letter):
	cmd = "say %s -o say_%s.aiff" % (letter,letter)
	os.system(cmd)
	cmd = "sox -r 22050 say_%s.aiff say_%s.wav" % (letter,letter)
	os.system(cmd)
	cmd = "rm say_%s.aiff" % (letter)
	os.system(cmd)
	
def makeSilence(length, name):
	cmd = "sox -r 22050 -n %s.wav trim 0.0 %f" % (name, length)
	os.system(cmd)
	
def makePracticeSequence(letterCount):
	allChars = string.ascii_lowercase + string.digits
	charCount = len(allChars)
	cmd = "sox "
	for i in range(letterCount):
		character = allChars[random.randint(0, charCount -1)]
		cmd += "morse_%s.wav " % (character)
		cmd += "morseLetterGap.wav "
		cmd += "say_%s.wav " % (character)
		cmd += "interLetterGap.wav "
	cmd += "practice.wav"
	os.system(cmd)
	
if __name__ == "__main__":
	main()

