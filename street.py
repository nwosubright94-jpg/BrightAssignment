# This is my Exercise 3 assignment.
# I created a list of buildings on a street.
# Each building contains:
# (Building Name, Building Type, Year Built)

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

# Store the current year for age calculations
currentYear = 2026

# Assume the first building is the oldest initially
oldestBuilding = street[0]

# Loop through all buildings to find the oldest one
for building in street:

    # Compare the construction year of each building
    # A smaller year means the building is older
    if building[2] < oldestBuilding[2]:
        oldestBuilding = building

# Create an empty set to store unique building types
buildingTypes = set()

# Loop through all buildings and collect their types
for building in street:

    # Add the building type to the set
    # Sets automatically remove duplicates
    buildingTypes.add(building[1])

# Create an empty list for buildings built after the year 2000
after2000 = []

# Check each building's construction year
for building in street:

    # If the building was built after 2000,
    # add it to the new list
    if building[2] > 2000:
        after2000.append(building)

# Create a variable to store the total age of all buildings
totalAge = 0

# Calculate the age of each building
for building in street:

    # Find the building's age
    age = currentYear - building[2]

    # Add the age to the running total
    totalAge += age

# Calculate the average age of all buildings
averageAge = totalAge / len(street)

# Display the report title
print("STREET REPORT")
print("-------------------------")

# Display the oldest building found
print("Oldest Building:")
print(oldestBuilding)

# Display all unique building categories
print("\nBuilding Types:")
print(buildingTypes)

# Display buildings that were constructed after 2000
print("\nBuildings Built After 2000:")
for building in after2000:
    print(building)

# Display the average age of all buildings
print("\nAverage Building Age:")
print(round(averageAge, 2))
