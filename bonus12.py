
# def get_age(year_of_birth, current_year=2024):
#     return current_year- int(year_of_birth)

def calculate_time(g=9.80665):
    t = (2 * h / g) ** 0.5
    return t


time = calculate_time(100)
print(time)





exit()
feet_inches = input("enter feet and inches: ")

def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f'{parsed["feet"]} feet and {parsed["inches"]} inches is equal to {result}')

if result < 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")