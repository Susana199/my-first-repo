# This file is empty on purpose, try to follow
# along the video.
#
# If you get stuck you can see what the contents
# of the file are looking at the last commit in
# the repository ;)

file = open("hola.txt")
print(file)

for line in file:
    print(line)
    
file.close()

#%%

band = [
        "Johny",
        "Joey",
        "Markee",
        "Dee-dee"
]

file = open("ramones.txt", "w")

with open("ramones.txt", "w") as file:
    for member in band:
        file.write(member + "\n")
    
    
#%%
import csv

with open("records.csv") as file: 
    reader = csv.DictReader(file)
    doctors = 0
    for row in reader: 
        if row["profession"] == "doctor":
            doctors = doctors + 1
    print("there are " + str(doctors) + " doctors in the file")
    
#%%

beatles = [
    {"name": "John", "role": "singer"},
    {"name": "George", "role": "guitar player"},
    {"name": "Paul", "role": "bass"},
    {"name": "Ringo", "role": "drums"}
    ]
    
with open("beatles.csv", "w") as file:
    column_names = ["name", "role"]
    writer = csv.DictWriter(file, column_names)
    writer.writeheader()
    for beatle in beatles: 
        writer.writerow(beatle)
        
with open("beatles.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
