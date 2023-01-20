import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room(
            {
                "RedRoom": {"guests": [], "capacity": 4, "songs": [], "fee": 5},
                "BlueRoom": {"guests": [], "capacity": 5, "songs": [], "fee": 5},
            }
        )
        self.guest = Guest("Lily", 35, "Hello", 25)

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

    def test_add_guests_to_room(self):
        self.assertEqual(
            ["Lily"], self.room.add_guest_to_room("RedRoom", self.guest.name)
        )

    def test_check_out_guest_from_room(self):
        self.room.add_guest_to_room("BlueRoom", "Sophie")
        self.room.add_guest_to_room("BlueRoom", "Jamie")
        self.assertEqual(
            ["Sophie"], self.room.check_out_guest_from_room("BlueRoom", "Jamie")
        )

    def test_add_song_to_room(self):
        self.assertEqual(
            ["Respect"],
            self.room.add_song_to_room("BlueRoom", self.song.song["Respect"]["title"]),
        )

    def test_add_new_room(self):
        self.assertEqual(
            ["RedRoom", "BlueRoom", "VioletRoom"], self.room.add_new_room("VioletRoom")
        )

    def test_full_capacity(self):
        self.assertEqual(["Sophie"], self.room.add_guest_to_room("RedRoom", "Sophie"))
        self.assertEqual(
            ["Sophie", "Jamie"], self.room.add_guest_to_room("RedRoom", "Jamie")
        )
        self.assertEqual(
            ["Sophie", "Jamie", "Florence"],
            self.room.add_guest_to_room("RedRoom", "Florence"),
        )
        self.assertEqual(
            ["Sophie", "Jamie", "Florence", "Hannah"],
            self.room.add_guest_to_room("RedRoom", "Hannah"),
        )
        self.assertEqual(
            "Sorry, this room is full.", self.room.add_guest_to_room("RedRoom", "Toni")
        )

    # def test_charge_guest(self):
    #     self.assertEqual(20, self.room.add_guest_to_room("RedRoom", "Lily"))