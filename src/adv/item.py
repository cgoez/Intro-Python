# This will be the base class for specialized item types to be declared later.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name