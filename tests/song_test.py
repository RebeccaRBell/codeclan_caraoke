import unittest
from classes.song import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song(
            {
                "Respect": {
                    "title": "Respect",
                    "artist": "Aretha Franklin",
                    "length": 3.50,
                },
                "Purple Rain": {
                    "title": "Purple Rain",
                    "artist": "prince",
                    "length": 3.20,
                },
            }
        )

    def test_add_song_to_list(self):
        self.assertEqual(
            ["Respect", "Purple Rain", "Proud Mary"],
            self.song.add_song_to_list("Proud Mary"),
        )
