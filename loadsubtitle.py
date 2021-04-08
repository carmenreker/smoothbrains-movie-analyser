# Author(s): Taede Meijer, Carmen Reker
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
        data[text] = time

        #print(text, time)
    #print(data)
    return data

# aanroepen met:
#data = loadsubtitles('testfiles/testsubtitles.srt')
#print(data)
