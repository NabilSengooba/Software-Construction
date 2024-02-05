import re

def rearrange_name(name):

# Use regular expression to match the expected name format

    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)

# Check if the name matches the expected format

    if result == None:

# If not, return the original name
        return name

# Rearrange the name in the desired format (last name, first name)
    return "{} {}".format(result[2], result[1])