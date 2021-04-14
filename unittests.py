# Author(s): Carmen Reker

from clean import clean
from labels import create_labels
from loadsubtitle import loadsubtitles
from matches import get_tag
from matches import get_matches
from main import compare


class TestClean:
    def test_clean(self):
        assert clean('<i>It was good...</i>') == 'It was good...'
        assert clean('- Are you game?') == 'Are you game?'


class TestSubs:
    def test_subtitles(self):
        assert loadsubtitles(
            [['testfiles/subtest.srt',
                'movies/mission_impossible/mi.txt']]) == (
                    {'OK... Here we go. Focus.': '00:00:48,690'})


class TestLabels:
    def test_label(self):
        assert 'N|     She then stops before ETHAN.' \
            in create_labels([['movies/mission_impossible/mi.txt',
                               'movies/mission_impossible/mi.srt']])
        assert 'C|                          FLIGHT ATTENDANT' \
            in create_labels([['movies/mission_impossible/mi.txt',
                               'movies/mission_impossible/mi.srt']])
        assert 'D|                Aruba, perhaps?' \
            in create_labels([['movies/mission_impossible/mi.txt',
                               'movies/mission_impossible/mi.srt']])
        assert 'S|     INT. PLANE - NIGHT' \
            in create_labels([['movies/mission_impossible/mi.txt',
                               'movies/mission_impossible/mi.srt']])
        assert 'M|                           THE END' \
            in create_labels([['movies/mission_impossible/mi.txt',
                               'movies/mission_impossible/mi.srt']])


class TestNames:
    def test_names(self):
        script = create_labels([['movies/mission_impossible/mi.txt']])
        subtitles = loadsubtitles([['testfiles/namestest.srt']])
        assert get_matches(script, subtitles) == (['01:45:49,593'],
                                                ['FLIGHT ATTENDANT '],
                                                ['Aruba, perhaps?'],
                                                ['D'])
                                                
class TestTag:
    def test_tag(self):
        assert get_tag('Hello', 'D|  Hello') == 'D'
