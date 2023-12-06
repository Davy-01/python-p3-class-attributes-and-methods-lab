class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        self.add_song_to_count()
        self.add_to_genres()
        self.add_to_artists()
        self.add_to_genre_count()
        self.add_to_artist_count()
        
    @classmethod
    def add_song_to_count(cls,increment=1):
        cls.count += increment

    @classmethod
    def add_to_genres(cls,genre):
        if cls.genres.count==0:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if cls.artists.count==0:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre) == None:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre]+=1

    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count(artist) == None:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] +=1

