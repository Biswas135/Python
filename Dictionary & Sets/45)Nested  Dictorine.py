student = {
    "name": "Biswas",                # student's name
    "age": 32,                        # student's age
    "Subject": {                      # nested dictionary for subjects
        "chem": 32,                   # marks in chemistry
        "math": 49,                   # marks in math
        "Physics": 32,                # marks in physics
    }
}

print(student)                       # print the entire student dictionary
print(student["Subject"])             # print the nested "Subject" dictionary
print(student["Subject"]["chem"])     # print only the chemistry marks
