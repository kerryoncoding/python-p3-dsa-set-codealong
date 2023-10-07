class MySet:


# Pass in collection of value such as a list, and create new set with just unique values. Creating a Dictionary and store the values passed in as keys on the Dictionary
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
        

# checks if the value  is already included in the set - returns Trus if so, or False if not.  O(1) runtime        
    def has(self, value):
        # return self.dictionary[value]  --> this would return None instead of False
        return value in self.dictionary

# Add a value to the set if it isn't already present, and return the updated set. O(1) runtime
    def add(self, value):
        self.dictionary[value] = True
        return self

# removes a value from the set, and returns the updated set.  O(1) runtime
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

# return number of elements in the set
    def size(self):
        return len(self.dictionary)
    
# removes all items from set and returns set
    def clear(self):
        self.dictionary.clear()
    

       


