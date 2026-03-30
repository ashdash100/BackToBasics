def TemperatureConverter():
  print("Hello! Thank you for using my temperature converter!")
  print("This is Day 1 of my Back To Basics Coding series\n")
  start = startMenu()
  start, end = convertMenu(start)
  num = numMenu(start)
  start, end, num, startunit, endunit = conversion(start, end, num)
  value = converter(start, end, num)
  print(str(num) + " degrees " + startunit + " equals " + str(value) + " degrees " + endunit)

def startMenu():
  start = int(input("Please select your CURRENT unit of temperature: \n\t1. Celsius (C)     2. Fahrenheit (F)     3. Kelvin (K)\n"))
  if start not in [1, 2, 3]:
    print("I'm sorry, please enter a valid unit (1 2 3).\n")
    return startMenu()
  unit = selection(start)
  print("You have selected " + unit)
  return start

def convertMenu(start):
  end = int(input("\nPlease select your GOAL unit of temperature: \n\t1. Celsius (C)     2. Fahrenheit (F)     3. Kelvin (K)    4. Go back (Change original unit)\n"))
  if end not in [1,2,3,4]:
    print("I'm sorry, please enter a valid unit (1 2 3).\n")
    return convertMenu(start)
  unit = selection(end)
  print("You have selected " + unit)
  if end == 4:
    print(" ")
    start = startMenu()
    return convertMenu(start)
  return start, end

def numMenu(start):
  num = float(input("\nPlease input the number you hope to convert: \n"))
  return num

def selection(sel):
  if sel == 1:
    unit = "Celsius (C)"
  if sel == 2:
    unit = "Fahrenheit (F)"
  if sel == 3:
    unit = "Kelvin (K)"
  if sel == 4 or sel == "B":
    unit = "to Go Back"
  return unit

def conversion(start, end, num):
  startunit = selection(start)
  endunit = selection(end)
  print("\nWould you like to convert " + str(num) + " degrees " + startunit + " to " + endunit)
  proceed = int(input("Enter '1' to proceed or '2' to restart:\n"))
  print(" ")
  if proceed == 2:
    print(" ")
    start = startMenu()
    start, end = convertMenu(start)
    num = numMenu(start)
    return conversion(start, end, num)
  return start, end, num, startunit, endunit

def converter(start, end, num):
  # Same units
  if start == end:
    val = num
  # C --> F
  if start == 1 and end == 2:
    val = num * 1.8 + 32
  # C --> K
  if start == 1 and end == 3:
    val = num + 273.15
  # K --> F
  if start == 3 and end == 2:
    val = (num - 273.15) * 1.8 + 82
  # K --> C
  if start == 3 and end == 1:
    val = num - 273.15
  # F --> C
  if start == 2 and end == 1:
    val = (num - 32) / 1.8
  # F --> K
  if start == 2 and end == 3:
    val = ((num - 32) / 1.8) + 273.15
  val = round(val, 4)
  return val
  
temp = TemperatureConverter()
temp
