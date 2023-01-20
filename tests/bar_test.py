import unittest
from classes.guest import Guest
from classes.room import Room
from classes.bar import Bar


class TestBar(unittest.TestCase):
    def setUp(self):
        self.bar = Bar(
            500, {"Soda": {"price": 2.50}, "Beer": {"price": 4}, "Wine": {"price": 4}}
        )
        self.guest = Guest("Julia", 25, "I'm Like a Bird", 15)
        self.room = Room(
            {
                "RedRoom": {"guests": [], "capacity": 4, "songs": [], "fee": 5},
                "BlueRoom": {"guests": [], "capacity": 5, "songs": [], "fee": 5},
            }
        )

    def test_sell_a_drink(self):
        self.assertEqual(504, self.bar.sell_a_drink("Wine"))




