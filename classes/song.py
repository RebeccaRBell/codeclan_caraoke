class Song:
    def __init__(self, song):
        self.song = song

    def add_song_to_list(self, new_song):
        song_list = []
        for song in self.song:
            song_list.append(song)
        song_list.append(new_song)
        return song_list
