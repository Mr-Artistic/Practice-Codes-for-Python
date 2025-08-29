
def  make_album(album_title, artist_name, songs_number=None):
    """Album details."""

    if songs_number:
        return {'title': album_title, 'artist': artist_name, 'no_songs': songs_number}
    else:
        return {'title': album_title, 'artist': artist_name}


albums = []
session_active = True

while session_active:
    
    title_entry = input("Enter your album title (or enter 'quit' to stop): ")
    if title_entry == 'quit':
        session_active = False
        break
    
    artist_entry = input("Enter your album artist (or enter 'quit' to stop): ")
    if artist_entry == 'quit':
        session_active = False
        break

    song_entry = input("Enter number of songs in album (you can skip this by enter): ")
    if artist_entry == 'quit':
        session_active = False
        break
    
    
    album = make_album(title_entry, artist_entry, song_entry)
    albums.append(album)


for album in albums:
    print(album)




'''

for key, value in album_dict.items():
    print(f"{key}: {value}")



   
album1 = make_album("Pal Pal Dil ke Paas", "Kishor Kumar")
album2 = make_album("Tu Zindagi Hai", "Kumar Sanu")
album3 = make_album("Aye Mere Humsafar", "Udit Narayan")
album4 = make_album("Heatless", "Badshah", songs_number=7)
    
print(f" title: {album_dict['title']}", f" artist: {album_dict['artist']}")
print(album2)
print(album3)
print(album4)

'''