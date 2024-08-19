# Lists - []
students = ["Marion", "Gakii", "Peris"]

for i in range(len(students)):
    print(i + 1, students[i])
    
# Dict - allows you to associate a key to a value {}

exes = {"Charity": "Mwihoko",
        "Marion": "Kiamunyi",
        "Sally": "Rafiki",
        "Gakii": "Hostel"

}
'''
print(exes["Charity"])
print(exes["Gakii"])
print(exes["Marion"])
print(exes["Sally"])
'''
for ex in exes:
    print(ex, exes[ex], sep="-")
    
    
family = [
    {"name": "James", "occupation": "Teacher", "Type": "Dad"},
    {"name": "Jane", "occupation": "BusinessLady", "Type": "Mom"},
    {"name": "Mercy", "occupation": "Student", "Type": "Sister"},
    {"name": "Robert", "occupation": None, "Type": "Brother"}
] 

for fam in family:
    print(fam["name"], fam["occupation"], fam["Type"], sep="-")
    