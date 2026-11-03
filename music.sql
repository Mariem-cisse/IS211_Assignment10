-- Create the artist table
CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

-- Create the album table
CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    artist_id INTEGER NOT NULL,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
);

-- Create the song table
CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    album_id INTEGER NOT NULL,
    track_number INTEGER NOT NULL,
    duration_seconds INTEGER NOT NULL,
    FOREIGN KEY (album_id) REFERENCES album(id)
);

