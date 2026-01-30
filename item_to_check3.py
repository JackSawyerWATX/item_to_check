# Given mission name
mission_name = "Sort"

# TODO: Print the first and the last character of the mission name
print(mission_name[0].lower())
print(mission_name[-1].upper())


# TODO: The mission needs a minor update. We aim to change its first letter to 'P' and the last letter to `k`, obtaining the word "Pork".
# Remember, strings in Python are immutable, so you cannot alter them directly.
revised_mission_name = "P" + mission_name[1:]
revised_mission_name = revised_mission_name[:-1] + "k"

# TODO: Print the updated mission name
print(revised_mission_name)