class Song:
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artist_count = {}
    
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Increment total count
        Song.count += 1
        
        # Add to genres set
        Song.genres.add(genre)
        
        # Add to artists set
        Song.artists.add(artist)
        
        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1
        
        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
