import itertools
import collections

# My Simple implementation of Levenshtein distance
def levenshtein_distance(string1, string2):


if len(string1) < len(string2):
string1, string2 = string2, string1

for i, v in itertools.izip_longest(string1, string2, fillvalue="-"):
if i != v:
distance += 1
return distance

# Find the string with the shortest edit distance.
list_of_string = ["AATC", "TAGCGATC", "ATCGAT"]

strings_distances = collections.defaultdict(int)

for strings in itertools.combinations(list_of_string, 2):
strings_distances[strings[0]] += levenshtein_distance(*strings)
strings_distances[strings[1]] += levenshtein_distance(*strings)

shortest = min(strings_distances.iteritems(), key=lambda x: x[1])