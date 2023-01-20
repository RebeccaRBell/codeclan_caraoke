class Room:
    def __init__(self, rooms):
        self.rooms = rooms

    def add_guest_to_room(self, room, guest):
        if len(self.rooms[room]["guests"]) < self.rooms[room]["capacity"]:
            self.rooms[room]["guests"].append(guest)
            return self.rooms[room]["guests"]
        else:
            return "Sorry, this room is full."

    def check_out_guest_from_room(self, room, guest):
        self.rooms[room]["guests"].remove(guest)
        return self.rooms[room]["guests"]

    def add_song_to_room(self, room, song):
        self.rooms[room]["songs"].append(song)
        return self.rooms[room]["songs"]

    def add_new_room(self, new_room):
        all_rooms = []
        for rooms in self.rooms:
            all_rooms += [rooms]
        all_rooms.append(new_room)
        return all_rooms
