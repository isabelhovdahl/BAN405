# -*- coding: utf-8 -*-
"""
Week 01 - Home exercise 4: City temperatures

Solution proposal.

Daily temperatures Monday-Friday for three cities:

| Day       | London | Paris | Rome |
|-----------|--------|-------|------|
| Monday    | 18.5   | 21.0  | 26.1 |
| Tuesday   | 19.0   | 22.5  | 27.3 |
| Wednesday | 17.8   | 20.2  | 25.0 |
| Thursday  | 20.1   | 23.1  | 26.7 |
| Friday    | 21.3   | 24.0  | 28.4 |

1. Store the data in a dictionary, city name -> list of five temperatures.
2. Display the temperature in Paris on Wednesday.
3. Display each city's average, rounded to one decimal.
4. Display the warmest single reading in the table, and which city it came from.
"""

# 1. City names as keys, lists of daily temperatures as values.
#
# Note that this arrangement is a choice. We could equally have used the days
# as keys, with a list of three city temperatures as each value. City-as-key is
# the better choice here because every question we are asked is about a city.
cities = {
    "London": [18.5, 19.0, 17.8, 20.1, 21.3],
    "Paris":  [21.0, 22.5, 20.2, 23.1, 24.0],
    "Rome":   [26.1, 27.3, 25.0, 26.7, 28.4]
}

# 2. Paris on Wednesday.
#
# Look up the key to get the list, then index into that list. Wednesday is the
# third day, so index 2 - zero-based indexing again.
print(f"Paris on Wednesday: {cities['Paris'][2]}°C")

# 3. Averages.
#
# len() rather than a hard-coded 5, so the code still works if a sixth day is
# added later.
avg_london = sum(cities["London"]) / len(cities["London"])
avg_paris = sum(cities["Paris"]) / len(cities["Paris"])
avg_rome = sum(cities["Rome"]) / len(cities["Rome"])

print("\nAverage temperatures:")
print(f"  London: {avg_london:.1f}°C")
print(f"  Paris:  {avg_paris:.1f}°C")
print(f"  Rome:   {avg_rome:.1f}°C")

# 4. Warmest single reading.
#
# max() gives the warmest reading within one city's list. To get the warmest
# across the whole table, take the max of those three values.
max_london = max(cities["London"])
max_paris = max(cities["Paris"])
max_rome = max(cities["Rome"])

warmest = max(max_london, max_paris, max_rome)

print(f"\nWarmest single reading: {warmest}°C, in Rome")


# ---------------------------------------------------------------------------
# On question 4
#
# Naming Rome by hand is fine for three cities, but it is not a real solution -
# if the data changed, the sentence would quietly become wrong. Finding *which*
# city holds the maximum needs a way to go through the dictionary and compare as
# you go, which is a loop. Loops come later in the course, and this exercise is a
# preview of why they are worth having.
# ---------------------------------------------------------------------------
