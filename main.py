print()

print("Enter numbers, or press enter to get the mean.\n")

numbers = []

while True:
  number = input("Enter a number: ")

  if number != "":
    numbers.append(float(number))
  elif len(numbers) == 0:
    print("\nEnter a number first.\n")
  else:
    mean = sum(numbers) / len(numbers)
    print(f"\nThe mean is {mean}.\n")
