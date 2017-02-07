def is_ascending(a):
  for i in range(1, len(a)):
      if a[i - 1] > a[i]:
          return False
  else:
    return True

"""done"""


a1 = [1, 2, 3, 4, 8, 10];
a2 = [1, 2, 3, 4, 8, 6, 10];
if is_ascending(a1):
  print("a1 is ascending!!")

if is_ascending(a2):
  print("a2 is ascending!!")
