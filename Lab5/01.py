import re

pattern = r"ab*" 
test_strings = ["a", "ab", "abb", "ac", "abc"]

for i in test_strings:
    if re.fullmatch(pattern, i):
        print(f"Matched: {i}")