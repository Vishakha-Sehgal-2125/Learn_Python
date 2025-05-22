# String function
# Strings are immutable they do not change even if you perform certain functions when you perform functions it does change in a new string and print them the original string do not change.
string = "KuhuKhandelwalIsFriendOfRajatTiwari"

print(len(string)) 
# This prints length of string
print(string)
string.upper()
print(string)
print(string.upper())
print(string)
print(string.endswith("vbnm "))
# Returns boolean value to show whether it ends with given string or not.

print(string.startswith("qwerty"))
# Returns boolean value to show whether it starts with given string or not.

print(string.find("Is"))
# Returns the index of the first occurrence of the substring. Returns -1 if not found.

print(string.index("Friend"))
# Returns the index of the first occurrence of the substring. Raises a ValueError if not found.

print(string.replace("Friend", "Wife"))
# Returns a new string where all occurrences of a substring are replaced with another substring.

print(string.upper())
# Converts all characters of the string to uppercase.

print(string.lower())
# Converts all characters of the string to lowercase.

print(string.isalpha())
# Returns boolean value to show whether the string contains only alphabetic characters.

print(string.isdigit())
# Returns boolean value to show whether the string contains only numeric characters.

print(string.isspace())
# Returns boolean value to show whether the string contains only whitespace characters.

print(string.capitalize())
# Returns a copy of the string with its first character capitalized and the rest lowercased.

print(string.swapcase())
# Returns a copy of the string with uppercase characters converted to lowercase and vice versa.

print(string.title())
# Returns a copy of the string where the first letter of each word is capitalized.

print(string.split("t"))
# Returns a list of substrings separated by the specified value.

print("".join(["q", "w", "e"]))
# Joins elements of an iterable with the string as the delimiter.

print(string.count("t"))
# Returns the number of occurrences of the specified substring.

print(string.strip("g"))
# Removes leading and trailing characters specified in the argument from the string.

print(string.lstrip())
# Removes leading characters specified in the argument from the string.

print(string.rstrip())
# Removes trailing characters specified in the argument from the string.

print(string.zfill(40))
# Pads the string on the left with zeros to fill a specified length.

print(string.center(40, "$"))
# Centers the string and fills it with the specified character to reach the specified width.

print("abc" + "def")
print("abc" * 3)