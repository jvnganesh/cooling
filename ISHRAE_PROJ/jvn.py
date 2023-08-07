# User inputs
area = float(input("Enter the area of the building (in square meters): "))
occupants = int(input("Enter the number of occupants: "))
building_type = input("Enter the type of building (residential/commercial): ")
outdoor_temp = float(input("Enter the outdoor temperature (in Celsius): "))
indoor_temp = float(input("Enter the indoor desired temperature (in Celsius): "))

# Cooling Load Calculator

def calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp):
    if building_type == 'residential':
        cooling_load = 100 * occupants
    elif building_type == 'commercial':
        cooling_load = 150 * occupants
    else:
        print("Invalid building type.")
        return None

    U = 30  # Overall heat transfer coefficient in W/m²°C

    Q_conduction = U * area * (outdoor_temp - indoor_temp)
    sensible_cooling_load = Q_conduction + cooling_load

    return sensible_cooling_load


# Calculate and display the cooling load
cooling_load = calculate_cooling_load(area, occupants, building_type, outdoor_temp, indoor_temp)
if cooling_load is not None:
    print(f"Sensible Cooling Load: {cooling_load} W")

