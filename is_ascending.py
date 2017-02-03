def is_ascending(a):
  # start the for loop at 1 and run it to the end of the array.
  # this gives us one space to look behind every current index
  # and guarantees we won't access an array beyond it's bounds.
  for i in range(1, len(a)):
    # the last value must be less than or equal to the current value.
    if not a[i - 1] <= a[i]:
      return False;
  return True;

a1 = [1, 2, 3, 4, 8, 10];
a2 = [1, 2, 3, 4, 8, 6, 10];
if is_ascending(a1):
  print("a1 is ascending!!")

if is_ascending(a2):
  print("a2 is ascending!!")

