<<<<<<< HEAD
def ski_size (height):
    results = height - 10
    return results

ski_size= 182
expert = + 10
=======
#introduction
print("Ski Sizing Chart (Beginners)")

#getting input from user
height = float( input('How tall are you in cm? ') )
experience = str(input('Whats your experience (Beginner, Intermediate, or Advanced)'))

#defining the formula
def skis (height):
    results = height - 10
    return results

#printing final ski size
if experience == "beginner":
  print(skis(height))
elif experience == "intermediate":
  print(skis(height + 4))
elif experience == "advanced":
   print(skis(height + 6))
else:
  print("You did not enter a valid option")
>>>>>>> 0242b40... Second Commit
