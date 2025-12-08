student = {
    "name": "Biswas",
    "roll": 20,
    "sub": {
        "math": 90,
        "sci": 32,
        "social": 49,
    }
}

print(student.keys())     
# .keys() returns all keys in the dictionary → dict_keys(['name', 'roll', 'sub'])

print(student.values())   
# .values() returns all values in the dictionary → dict_values(['Biswas', 20, {'math': 90, 'sci': 32, 'social': 49}])

print(student.items())    
# .items() returns all (key, value) pairs as tuples → dict_items([('name','Biswas'), ('roll',20), ('sub', {...})])

pairs = list(student.items())
print(pairs[0])           
# convert items to a list, access first pair → ('name', 'Biswas')

print(student.get("name"))
# .get("name") returns the value for the key "name" → 'Biswas'

student.update({'city':'delhi'})
print(student)
# .update() adds or updates a key-value pair in the dictionary → adds 'city': 'delhi'
