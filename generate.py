#!/usr/bin/python

import os
import sys
import string
import random

# VOICE = 'Alex'
# VOICE = 'Will Infovox iVox HQ'
VOICE = 'Heather Infovox iVox HQ'

WAV_DIR = './wavs'

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

    makeSilence(0.3, "morseLetterGap")
    makeSilence(1.0, "interLetterGap")

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
    cmd = "say '%s' -v '%s' -o %s/say_%s.aiff" % (letter, VOICE, WAV_DIR, letter)
    os.system(cmd)
    cmd = "sox -r 22050 %s/say_%s.aiff %s/say_%s.wav" % (WAV_DIR, letter, WAV_DIR, letter)
    os.system(cmd)
    cmd = "rm %s/say_%s.aiff" % (WAV_DIR, letter)
    os.system(cmd)

def speakNavy(letter):
    if letter in NAVY_ALPHABET.keys() :
        cmd = "say '%s' -v '%s' -o %s/navy_%s.aiff" % (NAVY_ALPHABET[letter], VOICE, WAV_DIR, letter)
        os.system(cmd)
        cmd = "sox -r 22050 %s/navy_%s.aiff %s/navy_%s.wav" % (WAV_DIR, letter, WAV_DIR, letter)
        os.system(cmd)
        cmd = "rm %s/navy_%s.aiff" % (WAV_DIR, letter)
        os.system(cmd)
    else:
        cmd = "cp %s/morseLetterGap.wav %s/navy_%s.wav" % (WAV_DIR, WAV_DIR, letter)
        os.system(cmd)

def makeSilence(length, name):
    cmd = "sox -r 22050 -n %s/%s.wav trim 0.0 %f" % (WAV_DIR, name, length)
    os.system(cmd)

if __name__ == "__main__":
    main()
