import sys
sys.path.append("/Users/seandaly/Documents/repos/wiktionaryaudioparser/WiktionaryAudioParser")

import WiktionaryParser

from sys import argv

parser = WiktionaryParser()

print ( 'starting' )
word = parser.fetch( "addict", 'english' )

# get first audio pronunciation from first entry
print ( word )
if ( len( word[0]['pronunciations']['audio'] ) > 0 ) :
    audio = word[0]['pronunciations']['audio'][0]

    print ( 'https:' + audio, end='' )