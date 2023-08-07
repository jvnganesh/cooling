# Cooling Load Calculator for a Building

# Get user inputs
area = float(input("Enter the area of the building (in square meters): "))
occupants = int(input("Enter the number of occupants in the building: "))
building_type = input("Enter the type of building (residential/commercial): ")
outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

# Calculate cooling load based on building type
if building_type == "residential":
    cooling_load = 100 * occupants
elif building_type == "commercial":
    cooling_load = 150 * occupants
else:
    print("Invalid building type")
    exit()

# Calculate heat transfer due to conduction
U = 30  # Overall heat transfer coefficient in W/m²°C
Q_conduction = U * area * (outdoor_temp - indoor_temp)

# Calculate sensible cooling load
sensible_cooling_load = Q_conduction + cooling_load

# Display results
print("\nCooling Load Calculator Results:")
print("-------------------------------")
print("Area of the building:", area, "square meters")
print("Number of occupants:", occupants)
print("Building type:", building_type)
print("Outdoor temperature:", outdoor_temp, "°C")
print("Indoor desired temperature:", indoor_temp, "°C")
print("Cooling Load:", cooling_load, "W")
print("Heat transfer due to conduction:", Q_conduction, "W")
print("Sensible Cooling Load:", sensible_cooling_load, "W")
