import re
import pysrt

def loadsubtitles(filepath):
    subs = pysrt.open(filepath)
    data = {}

    for subtitle in subs:      
        #print(subtitle.start)
        #print(subtitle.text)
        text = subtitle.text
        time = str(subtitle.start)
        if text not in data:
            data[text] = time

        print(text, time)

    return data


# aanroepen door:
#data = loadsubtitles('testfiles/testsubtitles.srt')
#print(data)
