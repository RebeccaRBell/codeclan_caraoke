import unittest
from classes.guest import Guest
from classes.room import Room
from classes.bar import Bar


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Julia", 25, "I'm Like a Bird", 15)
        self.room = Room(
            {
                "RedRoom": {"guests": [], "capacity": 4, "songs": [], "fee": 5},
                "BlueRoom": {"guests": [], "capacity": 5, "songs": [], "fee": 5},
            }
        )
        self.bar = Bar(
            500, {"Soda": {"price": 2.50}, "Beer": {"price": 4}, "Wine": {"price": 4}}
        )

    def test_add_guest(self):
        self.assertEqual(["Julia", "Mona"], self.guest.add_guest("Mona"))

    def test_add_fav_song_to_guest(self):
        self.assertEqual(
            ["I'm Like a Bird", "Goodbye"],
            self.guest.add_fav_song_to_guest("Ellen", "Goodbye"),
        )

    def test_entry_charge(self):
        self.assertEqual(10, self.guest.entry_fee(self.room.rooms["RedRoom"]["fee"]))

    def test_guest_fav_song(self):
        self.guest.add_fav_song_to_guest("Ellen", "Hello")
        self.room.add_guest_to_room("RedRoom", "Ellen")
        self.room.add_song_to_room("RedRoom", self.guest.fav_song)
        self.assertEqual(
            "Ellen says Woohoo!",
            self.guest.guest_fav_song("Ellen", self.room.rooms["RedRoom"]),
        )

    def test_buy_a_drink(self):
        self.assertEqual(11, self.guest.buy_a_drink(self.bar.drinks["Wine"]))
