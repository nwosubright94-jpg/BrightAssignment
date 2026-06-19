# This is my exercise 3 assignment
street = [
    ("Unity Plaza", "Commercial", 1998),
    ("Hope House", "Residential", 2005),
    ("Grace Secondary School", "Educational", 2001),
    ("Family Clinic", "Healthcare", 2010),
    ("Royal Mall", "Commercial", 2018),
    ("Winners Chapel", "Church", 1995),
    ("Green Villa", "Residential", 2014),
    ("Mandella Mall", "Government", 1987)
]

currentYear = 2026

oldestBuilding = street[0]

for building in street:
    if building[2] < oldestBuilding[2]:
        oldestBuilding = building

buildingTypes = set()

for building in street:
    buildingTypes.add(building[1])

after2000 = []

for building in street:
    if building[2] > 2000:
        after2000.append(building)

totalAge = 0

for building in street:
    age = currentYear - building[2]
    totalAge += age

averageAge = totalAge / len(street)

print("STREET REPORT")
print("-------------------------")

print("Oldest Building:")
print(oldestBuilding)

print("\nBuilding Types:")
print(buildingTypes)

print("\nBuildings Built After 2000:")
for building in after2000:
    print(building)

print("\nAverage Building Age:")
print(round(averageAge, 2))
