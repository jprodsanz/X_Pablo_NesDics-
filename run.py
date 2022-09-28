# Change the value 10 in x to 15. 
# Once you're done, x should now be [ [5,2,3], [15,8,9] ]
from struct import Struct


x = [ [5,2,3], [10,8,9] ] 
x[1] [0] = 15
print(x)

# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = 'Bryant'
print(students)

# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)

# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]
z[0] ['y'] = 30
print(z)

# ! Iterate Through a List of Dictionaries
# Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
# the function loops through each dictionary in the list and prints each key 
# and the associated value. 

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def i_dict(list):
    for i in range(0, len(list)):
        result = ""
        for first,last in list[i].items():
            result += f" {first} - {last},"
        print(result)
i_dict(students)

# Create a function iterateDictionary2(key_name, some_list) that, 
# given a list of dictionaries and a key name, 
# the function prints the value stored in that key for each dictionary. 


# Michael
# John
# Mark
# KB

def i_dict2(first_name,list):
    for i in range(0, len(list)):
        
        for first,val in list[i].items():
            if first == first_name:
                print(val)
i_dict2('first_name',students)
i_dict2('last_name',students)

# Jordan
# Rosales
# Guillen
# Tonel

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def print_info(dictionary):
    for loc, inst in dictionary.items():
        print("")
        print(f'{len(inst)} {loc.upper()}')
        for i in range(0, len(inst)):
            print(inst[i])

print_info(dojo)
