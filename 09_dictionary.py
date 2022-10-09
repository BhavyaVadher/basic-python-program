a = {
    'key' : 'value',
    'harry' : 'code',
    'marks' : '100',
    'list' : [1,2,9]}
print(a['key'])	# Prints value
print(a['list'])	# Prints [1,2,9]

# Method 
a = {'name': 'Harry',
	'from': 'India',
	'marks': [92,98,96]}

print(a.items())#: returns a list of (key,value) tuple.
print(a.keys()) #: returns a list containing dictionary’s keys.
print(a.update({'friend': 'Sam'})) #: updates the dictionary with supplied key-value pairs.
print(a.get('name')) #: returns the value of the specified keys
print(a)