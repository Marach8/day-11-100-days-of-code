print("\033[32mYear's Calculator\033[0m")
print()
b = input('Do you want to calculate for a leap year? y/n: ')
print()
if b == 'y':
  a = (60*60*24*366)
  print(f'\033[33mThere are {a} seconds in one leap year!\033[0m')
else:
  a = 60*60*24*365
  print(f'\033[33mThere are {a} seconds in one year!\033[0m')