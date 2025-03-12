import re


def add_space_after_numbers(reg):
    # the \s checks if there is already a space after the numbers
    if not re.search(r'\d\s', reg):
        # Adds a space after the numbers if not therre
        # \d+ matches for 1 or more digits and then replaces the group (\1) with the same digits plus a space
        return re.sub(r'(\d+)', r'\1 ', reg)
    return reg
