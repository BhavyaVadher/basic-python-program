S= set()          # No repetition allowed!

S.add(1)

S.add(2)

# or Set = {1,2}
print(S)

# Methods 

s = {1,8,2,3}
# print(s)
# print(len(s)) #: Returns 4, the length of the set
# s.remove(8) #: Updates the set S and removes 8 from S
# print(s)
# s.pop() #: Removes an arbitrary element from the set and returns the element removed.
# print(s)
# s.clear() #: Empties the set S
# print(s)
print(s.union({8, 11})) #: Returns a new set with all items from both sets. #{1,8,2,3,11}
print(s.intersection({8, 11})) #: Returns a set which contains only items in both sets. #{8}

