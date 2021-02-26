import re

# Calculator prompt

calc_prompt = """
Which conversion calculator do you want to use?
1. temperature
2. weight
3. distance
Your input: """

temp_calc = ["temperature", "1", "temp"]
weight_calc = ["weight", "2"]
distance_calc = ["distance", "3"]

calc_prompt_answers = [temp_calc, weight_calc, distance_calc]

calc_input = ""

while calc_input not in (j for i in calc_prompt_answers for j in i):
    calc_input = input(calc_prompt)

calc_input = "".join(i[0] for i in calc_prompt_answers if calc_input in i)

print(f"\nYou chosen the {calc_input} calculator.")

# Unit prompt

temp_units = ["Fahrenheit", "Celcius"]
weight_units = ["Pounds", "Kilograms"]
distance_units = ["Miles", "Kilometers"]

if calc_input == "temperature":
    calc_units = temp_units
elif calc_input == "weight":
    calc_units = weight_units
elif calc_input == "distance":
    calc_units = distance_units 

unit_prompt = f"""
What unit of {calc_input} are you converted from/to?
1. {calc_units[0]} to {calc_units[1]}
2. {calc_units[1]} to {calc_units[0]}
"""

unit_input = ""

while unit_input not in ("1", "2"):
    unit_input = input(unit_prompt)

if unit_input == "1":
    unit_input = calc_units[0]
elif unit_input == "2":
    unit_input = calc_units[1] 

# Amount prompt

amount_prompt = "Input your amount: "
amount_input = ""

float_regex = r"[+-]?[0-9]+\.[0-9]+"
int_regex = r"[+-]?[0-9]+"

def check(n: float) -> bool:
    if re.search(float_regex, n) or re.search(int_regex, n):
        return True
    else:
        return False

while not check(amount_input):
    amount_input = input(amount_prompt)
    
def temp_conversion(degree: float, unit: str) -> float:
    if unit == "Celcius":
        # convert from C to F
        return degree * 1.8 + 32
    else: 
        # convert from F to C
        return degree * (9/5)

def weight_conversion(weight: float, unit: str) -> float:
    if unit == "Pounds":
        # convert from lbs to kg
        return weight * 0.45359237
    else:
        # convert from kg to lbs
        return weight * 2.20462262185

def distance_conversion(length: float, unit: str) -> float:
    if unit == "Miles":
        # convert from miles to kilometers
        return length * 1.609344
    else:
        # convert from kilometers to miles
        return length * 0.62137

amount_input = float(amount_input)

if calc_input == "temperature":
    result = temp_conversion(amount_input, unit_input)
elif calc_input == "weight":
    result = weight_conversion(amount_input, unit_input)
elif calc_input == "distance":
    result = distance_conversion(amount_input, unit_input)

print(f"Result: {result}")
