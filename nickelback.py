# Instructions
# Define a set that contains tuples. Each tuple should contain two strings:
# The name of an artist
# A song by that artist
# Make sure that some of the songs are from the band Nickelback.
# Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.

songs = {
    ('Nickelback', 'How You Remind Me'),
    ('2Chainz and Lil Wayne', 'Bounce'),
    ('Dr. John', 'Iko Iko'),
    ('Nickelback', 'Animals')
}
refined_songs = {(artist, song) for artist, song in songs if artist !='Nickelback'}
# Could also be:
# refined_songs = {item for item in songs if item[0] !='Nickelback'}
print(refined_songs)
