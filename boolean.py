is_rainy = True
has_umbrella = False

if is_rainy and not has_umbrella:
    print("Enjoy the rains")
    
else:
    print("Better take an umbrella")

# output: Enjoy the rains

----------------------------------------------------------------------------------------------------------

is_rainy = "True"
has_umbrella = "False" # now it's a string

if is_rainy and not has_umbrella:
    print("Enjoy the rains")
    
else:
    print("Better take an umbrella")

# Output: Better take an umbrella
'''
is_rainy = "True" → a string, not a boolean (True).

has_umbrella = "False" → also a string, not a boolean (False).

Step 2: How does Python evaluate this?

In Python, any non-empty string is considered True in a boolean context.

"True" → truthy

"False" → truthy (because it’s still a non-empty string)

if "True" and not "False": # false

Step 3: Evaluate not "False"

"False" is a non-empty string → truthy

not "False" → False

'''
