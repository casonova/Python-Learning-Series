from song import Song
from album import Album

class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."
        return f"Band {self.name} already has {album.name} in their library."
    
    def remove_album(self,album_name):
        album = [alb for alb in self.albums if alb.name == album_name]

        if album:
            if album[0].published:
                return "Album has been published. It cannot be removed."
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."
    
    def detail(self):
        album_details = '\n'.join([album.detail() for album in self.albums])
        return f"Band {self.name}\n{album_details}"
    

song1 = Song("Running in the 90s", 3.45, False)
song2 = Song("Running in the 80s", 3.45, False)
song3 = Song("Running in the 70s", 3.45, False)

album1 = Album("Initial D", song1, song2)
print(album1.detail())
print(album1.add_song(song3))
print(album1.remove_song("Running in the 70s"))
band = Band("Manuel")
print(band.add_album(album1))
print(band.remove_album("Initial D"))
print(band.detail())