import re
import pysrt

def loadsubtitles():
    subs = pysrt.open('testfiles/testsubtitles.srt')
    
    for subtitle in subs:      
        print(subtitle.start)
        print(subtitle.text)

loadsubtitles()
