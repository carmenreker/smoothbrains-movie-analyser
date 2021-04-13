# Author(s): Taede Meijer, Carmen Reker, Sijbren van Vaals
import pysrt
from clean import clean

def loadsubtitles(filepath):
    """ Loads the subtitles and returns it """

    subs = pysrt.open(filepath[0][0])
    data = {}

    for subtitle in subs:
        # print(subtitle.start)
        # print(subtitle.text)
        text = subtitle.text
        text = text.replace("\n", " ")
        text = clean(text)
        time = str(subtitle.start)
        data[text] = time

        # print(text, time)
    # print(data)
    return data

# aanroepen met:
# data = loadsubtitles('testfiles/testsubtitles.srt')
# print(data)
