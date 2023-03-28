numerator = 10**309
denominator = int(input("enter a number for the denominator: "))

try:
  result = float(numerator / denominator)
except ZeroDivisionError:
  print("Division by zero is undefined.")
except OverflowError:
  print("Too big!")
else:
  print("Result = ", result)
finally:
  print("All done here.")