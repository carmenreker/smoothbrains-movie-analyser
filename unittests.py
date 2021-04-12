# Author(s): Carmen Reker

from clean import clean
from labels import create_labels
from loadsubtitle import loadsubtitles
#from names import add_names
#from timestamps import add_timestamps


class TestClean:
    def test_clean(self):
        assert clean('testfiles/cleantest.txt') == 'It was good...'
        assert clean('testfiles/cleantest2.txt') == 'Are you game?'
        
class TestSubs:
    def test_subtitles(self):
        assert loadsubtitles([["testfiles/subtest.srt", "movies/mission_impossible/mi.txt"]]) == (
        {'OK... Here we go. Focus.': '00:00:48,690'})
        
class TestLabels:
    def test_label(self):
        assert 'N|     She then stops before ETHAN.' \
        in create_labels([['movies/mission_impossible/mi.txt', 'movies/mission_impossible/mi.srt']])
        assert 'C|                          FLIGHT ATTENDANT' \
        in create_labels([['movies/mission_impossible/mi.txt', 'movies/mission_impossible/mi.srt']])
        assert 'D|                Aruba, perhaps?' \
        in create_labels([['movies/mission_impossible/mi.txt', 'movies/mission_impossible/mi.srt']])
        assert 'S|     INT. PLANE - NIGHT' \
        in create_labels([['movies/mission_impossible/mi.txt', 'movies/mission_impossible/mi.srt']])
        assert 'M|                           THE END' \
        in create_labels([['movies/mission_impossible/mi.txt', 'movies/mission_impossible/mi.srt']])