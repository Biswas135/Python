# Writing to a file (commented out here)
"""
with open("pratice.txt", "w") as f:  # open file in write mode
    f.write("Hi Everyone \nwe are learning FIle I/O\n")  # write first line
    f.write("using Java. \nI like programming in Java ")  # write second line
"""

# Reading the file
with open("pratice.txt", "r") as f:  
    data = f.read()  # read entire content of the file

# Replacing text
new_data = data.replace("Java", "Python")  # replace all occurrences of 'Java' with 'Python'
print(new_data)                            # print updated content

# Writing the updated content back to the file
with open("pratice.txt", "w") as f:        
    f.write(new_data)                       # overwrite file with new content
