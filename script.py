def computeStats(values):
  '''
  Performs arithmetic operations on a list of values
  '''
  print "Select desired statistic"
  print "  1. Average"
  print "  2. Minimum Value"
  print "  3. Maximum value"
  print "  4. Sum"
  print "  5. Number of values in list in range [1,5]"

  # choice is what the user typed
  choice = raw_input("Choose your statistic [1-5]: ")

  if choice is "1":
    print computeAverage(values)
  elif choice is "2":
    print computeMinValue(values)
  elif choice is "3":
    print computeMaxValue(values)
  elif choice is "4":
    print computeSum(values)
  elif choice is "5":
    print computeRestriction(values)
  else:
    print "Unkonwn request!"

def computeAverage(values):
  '''
  returns the average of the list of values
  '''
  print "You haven't implemented computeAverage yet"

def computeMinValue(values):
  '''
  returns the minimum value of the list of values
  '''
  print "You haven't implemented computeMinvalue yet"

def computeMaxValue(values):
  '''
  returns the maximum value of the list of values
  '''
  print "You haven't implemented computeMaxValue yet"

def computeSum(values):
  '''
  returns the sum of the list of values
  '''
  print "You haven't implemented computeSum yet"

def computeRestriction(values):
  '''
  returns the values in the list in the range [1-5]
  '''
  print "You haven't implemented computeRestriction yet"

computeStats([2,4,5,7,8])
