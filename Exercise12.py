# Define a function that has two parameters, year of birth and current year. The current year parameter should be a default parameter with the current year as a default value.

# Add a message if the user is 120 years older and another if they are younger. 

birth_year = input("What year were you born?: ")

def age_calc(birth_year, this_year=2023):
    convert = float(this_year) - float(birth_year) 
    return(convert)
conversion = age_calc(birth_year)

if conversion <= 120:
    print("You are still young.")
else:
    print("You're pretty old.")


# ======================================================

# Write a program that gets a list of names from the user and returns the number of names given. You are encouraged to use a function. Here is how the program would work:

names = input("Enter names seperated by commas with no spaces: ")

def num_names(names):
   name = names.split(",")
   return len(name)
    
print(num_names(names))
