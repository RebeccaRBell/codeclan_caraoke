class Guest:
    def __init__(self, name, age, fav_song, wallet):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.wallet = wallet

    def add_guest(self, new_guest):
        guest_names = [self.name]
        guest_names.append(new_guest)
        return guest_names

    def add_fav_song_to_guest(self, guest, new_song):
        fav_song = []
        fav_song += [self.fav_song]
        fav_song.append(new_song)
        return fav_song

    def entry_fee(self, fee):
        self.wallet -= fee
        return self.wallet

    def guest_fav_song(self, guest, room):
        if self.fav_song in room["songs"]:
            return f"{guest} says Woohoo!"

    def buy_a_drink(self, drink):
        self.wallet -= drink["price"]
        return self.wallet
