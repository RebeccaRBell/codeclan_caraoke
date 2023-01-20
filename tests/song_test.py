import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song(
            {
                "Respect": {"artist": "Aretha Franklin", "length" : 3.50},
                "Purple Rain": {"artist": "prince", "length": 3.20},
            }
        )

 
