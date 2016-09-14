#!/usr/bin/python

import os
import string
import random

def main():
	makeSilence(0.4, "morseLetterGap")
	makeSilence(1.5, "interLetterGap")

	allChars = string.ascii_lowercase + string.digits
	for letter in allChars:
		morseLetter(letter)
		speakLetter(letter)

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

if __name__ == "__main__":
	main()
