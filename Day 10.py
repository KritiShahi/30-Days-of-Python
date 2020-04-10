"""1) Below is a tuple describing an album:
 (
    "The Dark Side of the Moon",
    "Pink Floyd",
    1973,
    (
    "Speak to Me",
    "Breathe",
    "On the Run",
    "Time",
    "The Great Gig in the Sky",
    "Money",
    "Us and Them",
    "Any Colour You Like",
    "Brain Damage",
    "Eclipse"
    )
 )
Inside the tuple we have the album name, the artist (in this case, the band), the year of release, and then
another tuple containing the track list.Convert this outer tuple to a dictionary with four keys."""
album = {
        "name": "The Dark Side of the Moon",
        "band_name": "Pink Floyd",
        "year_of_release": "1973",
        "track_list": (
                        "Speak to Me", "Breathe", "On the Run", "Time", "The Great Gig in the Sky", "Money",
                        "Us and Them", "Any Colour You Like", "Brain Damage", "Eclipse"
                      )
}
print(album)

"""2) Iterate over the keys and values of the dictionary you create in exercise 1. For each key and value, 
you should print the name of the key, and then the value alongside it."""
for key, value in album.items():
    print(f"{key} : {value}")

"""3) Delete the track list and year of release from the dictionary you created. Once you've done this, add a new key 
to the dictionary to store the date of release. The date of release for The Dark Side of the Moon was March 1st, 1973.
If you use a different album for the exercises, update the date accordingly."""
album.pop('year_of_release')
album.pop('track_list')
album.update({"year_of_release": "March 1st, 1973"})
print(album)

"""4) Try to retrieve one of the values you deleted from the dictionary. This should give you a KeyError. 
Once you've tried this, repeat the step using the get method to prevent the exception being raised."""
# print(album["track_list"])    This statement will give a KeyError
print(album.get('track_list', "Unknown"))
