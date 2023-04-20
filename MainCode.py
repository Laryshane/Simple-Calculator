# Creates Calculator function.
def calculator(num_1, num_2, op):
  result = 0
  
  # Additon action.
  if op == "+":
    result = num_1 + num_2
    
  # Subtraction action.
  elif op == "-":
    result = num_1 - num_2
    
  #Multiplication action.
  elif op == "*":
    result = num_1 * num_2
    
  # Print Calculations.
  print(f"{num_1} {op} {num_2} = {result}")
  
# Input to calculate
calculator(5, 10, "*")
