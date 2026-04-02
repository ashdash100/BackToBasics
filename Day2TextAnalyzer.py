# Day 2 - 4/1
# TODO: Add exceptions
# TODO: Add paragraph count

def wordCounter():
  print("Hello! Thank you for using my text analyzer!")
  print("This is Day 2 of my Back To Basics Coding series\n")
  inputtext = text()
  commands = int(input("\nSelect what actions you would like: \n\t1. Word Count     2. Character Count     3. Number of Sentences     4. Full Analysis     5. Search for specific character/word\n"))
  sel = selection(commands)
  print("You have selected: " + sel)
  functions(commands, inputtext)
  again(inputtext)

# TODO: Edit so it can take multiple lines of input, using tab to end input
def text():
  inputtext = input("Please paste the text you would like analyzed here: \n")
  return inputtext

def selection(commands):
  selmenu = {1: "Word Count", 2: "Character Count", 3: "Number of Sentences", 4: "Full Analysis", 5: "Search for a specific character/word"}
  sel = selmenu[commands]
  return sel

def functions(commands, inputtext):
  funmenu = {1: words, 2: characters, 3: sentences, 4: full, 5: specificCharacter}
  fun = funmenu[commands](inputtext)
  sel = selection(commands)
  if commands in [1,2,3]:
    print(sel + ": " + str(fun))
  if commands == 4:
    print(selection(1) + ": " + str(fun[0]))
    print(selection(2) + ": " + str(fun[1]))
    print(selection(3) + ": " + str(fun[2]))

def words(inputtext):
  # Need to add exceptions for multiple spaces and random punctation
  numWords = len(inputtext.split())
  return numWords

def characters(inputtext):
  numChars = len(inputtext)
  return numChars

def sentences(inputtext):
  numSentences = inputtext.count(".") + inputtext.count("!") + inputtext.count("?")
  return numSentences

def full(inputtext):
  return words(inputtext), characters(inputtext), sentences(inputtext)

def specificCharacter(inputtext):
  char = input("\nPlease input the character/word you would like to search for: \n")
  lowertext = inputtext.lower()
  numSpecific = lowertext.count(char.lower())
  print("Your input '" + char + "' is in the text " + str(numSpecific) + " times.")
  return numSpecific

def again(inputtext):
  choice = int(input("\nWould you like to use this again? \n\t1. Yes, with the same text     2. Yes, with a new text     3. No\n"))
  if choice == 1:
    commands = int(input("\nSelect what actions you would like: \n\t1. Word Count     2. Character Count     3. Number of Sentences     4. Full Analysis     5. Search for specific character/word\n"))
    sel = selection(commands)
    print("You have selected: " + sel)
    functions(commands, inputtext)
    return again(inputtext)
  if choice == 2:
    return wordCounter()
  if choice == 3:
    print("\nThank you for using my text analyzer!")

wordCounter()
