# Author(s): Taede Meijer, Carmen Reker

import re
import pysrt

def loadsubtitles(filepath):
    """ Loads the subtitles and returns it """
    subs = pysrt.open(filepath)
    data = {}

    for subtitle in subs:      
        #print(subtitle.start)
        #print(subtitle.text)
        text = subtitle.text
        time = str(subtitle.start)
        if text not in data:
            data[text] = time

        #print(text, time)

    return data

# aanroepen met:
#data = loadsubtitles('testfiles/testsubtitles.srt')
#print(data)
