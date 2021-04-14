# Author(s): Taede Meijer, Carmen Reker, Sijbren van Vaals
import pysrt
from clean import clean


def loadsubtitles(filepath):
    """ Loads the subtitles and returns it """

    subs = pysrt.open(filepath[0][0])
    data = {}

    for subtitle in subs:
        text = subtitle.text
        text = text.replace("\n", " ")
        text = clean(text)
        time = str(subtitle.start)
        data[text] = time

    return data

# Invoke with:
# data = loadsubtitles(filepath)
