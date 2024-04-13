print("***WHICH GOT CHARACTER ARE YOU?***")
print()
tyrion = input("Do you frequent the pleasure houses?: ")
if tyrion == "yes":
  print("Ah, then you are Tyrion!")
else:
  print("OK. So you must be someone else! Lets try again...")
print()
cersei = input("Do you like to scheme and lie and occasionally sleep with your brother?: ")
if cersei == "yes":
  print("Then you must be Queen Cersei! Congrats you craven witch!")
else:
  print("Ok, then I think you may be summat else...")
print()
snow = input("Were you born a bastard in the North?: ")
if snow == "yes":
  print("Congrats! You are John Snow, King of the North! '\u2744\ufe0f'")