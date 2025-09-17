# Remove all duplicate characters from a string while maintaining order

def remove_duplicates(string):

    result = ""

    for ch in string:

        if ch not in result:

            result += ch

    return sorted(result)

print(remove_duplicates("Remove all duplicate characters"))