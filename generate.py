#!/usr/bin/python

import os
import string
import random


VOICE = 'Will Infovox iVox HQ' # 'Alex'

WAV_DIR = './wav'
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
    for letter in allChars:
        morseLetter(letter)
        speakLetter(letter)
        speakNavy(letter)

def morseLetter(letter):
    print letter
    cmd = "echo \"%s\" |./cwwav -r 22050 --wpm 20 -o %s/morse_%s.wav" % (letter, WAV_DIR, letter)
    os.system(cmd)

def speakLetter(letter):
    cmd = "say '%s' -v '%s' -o %s/say_%s.wav" % (letter, VOICE, WAV_DIR, letter)
    os.system(cmd)

def speakNavy(letter):
    if letter in NAVY_ALPHABET.keys() :
        cmd = "say '%s' -v '%s' -o say_navy_%s.aiff" % (NAVY_ALPHABET[letter], VOICE, letter)
        os.system(cmd)
        cmd = "sox -r 22050 say_navy_%s.aiff say_navy_%s.wav" % (letter, letter)
        os.system(cmd)
        cmd = "rm say_navy_%s.aiff" % (letter)
        os.system(cmd)
    else:
        cmd = "cp morseLetterGap.wav %s/say_navy_%s.wav" % (WAV_DIR, letter)

def makeSilence(length, name):
    cmd = "sox -r 22050 -n %s/%s.wav trim 0.0 %f" % (WAV_DIR, name, length)
    os.system(cmd)

if __name__ == "__main__":
    main()
