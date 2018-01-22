print ("Problem 1: arithmetic operations")

def operation():
  number1 = int (input("Enter number #1: "))
  number2 = int(input("Enter number #2: "))
  operation = int(input("Enter the operation number (1 for addition, 2 for subtraction, 3 for multiplication and 4 for division: "))
  print ("number1: ", number1)
  print ("number2: ", number2)
  print ("operation: ", operation)

  if operation == 1:
    result = number1+ number2
  elif operation == 2:
    result = number1 - number2
  elif operation == 3:
    result = number1 * number2
  else:
    result = number1 / number2

  print ("result is: ", result)

operation()
print ("\n")
