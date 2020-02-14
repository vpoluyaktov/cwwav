#!/usr/bin/python

import os
import sys
import string
import random


VOICE = 'Will Infovox iVox HQ' # 'Alex'

WAV_DIR = './wavs'
OUTPUT_DIR = './output'

NAVY_ALPHABET = {
    'a' : 'Alfa',
    'b' : 'Bravo',
    'c' : 'Charlie',
    'd' : 'Delta',
    'e' : 'Echo',
    'f' : 'Foxtrot',
    'g' : 'Golf',
    'h' : 'Hotel',
    'i' : 'India',
    'j' : 'Juliett',
    'k' : 'Kilo',
    'l' : 'Lima',
    'm' : 'Mike',
    'n' : 'November',
    'o' : 'Oscar',
    'p' : 'Papa',
    'q' : 'Quebec',
    'r' : 'Romeo',
    's' : 'Sierra',
    't' : 'Tango',
    'u' : 'Uniform',
    'v' : 'Victor',
    'w' : 'Whiskey',
    'x' : 'X-ray',
    'y' : 'Yankee',
    'z' : 'Zulu',
    '0' : 'Zero',
    '1' : 'One',
    '2' : 'Two',
    '3' : 'Three',
    '4' : 'Four',
    '5' : 'Five',
    '6' : 'Six',
    '7' : 'Seven',
    '8' : 'Eight',
    '9' : 'Niner',
    '-' : 'Dash',
    '.' : 'Full Stop',
    ',' : 'Comma'
}

def main():

    if not os.path.exists(WAV_DIR):
        os.makedirs(WAV_DIR)

    makeSilence(0.4, "morseLetterGap")
    makeSilence(1.1, "interLetterGap")

    allChars = string.ascii_lowercase + string.digits
    sys.stdout.write("Generating .wav files for the letter    ")
    sys.stdout.flush()
    for letter in allChars:
        sys.stdout.write("\b\b\b" + letter + "  ")
        sys.stdout.flush()
        morseLetter(letter)
        speakLetter(letter)
        speakNavy(letter)

    print "\nDone"

def morseLetter(letter):

    cmd = "echo \"%s\" |./cwwav -r 22050 --wpm 20 -o %s/morse_%s.wav 2> /dev/null" % (letter, WAV_DIR, letter)
    os.system(cmd)

def speakLetter(letter):
    cmd = "say '%s' -v '%s' --data-format=LEF32@22050 -o %s/say_%s.wav" % (letter, VOICE, WAV_DIR, letter)
    os.system(cmd)

def speakNavy(letter):
    if letter in NAVY_ALPHABET.keys() :
        cmd = "say '%s' -v '%s' --data-format=LEF32@22050 -o %s/say_navy_%s.wav" % (NAVY_ALPHABET[letter], VOICE, WAV_DIR, letter)
    else:
        cmd = "cp %s/morseLetterGap.wav %s/say_navy_%s.wav" % (WAV_DIR, WAV_DIR, letter)
    os.system(cmd)

def makeSilence(length, name):
    cmd = "sox -r 22050 -n %s/%s.wav trim 0.0 %f" % (WAV_DIR, name, length)
    os.system(cmd)

if __name__ == "__main__":
    main()
