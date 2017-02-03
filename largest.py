# Write a function called largest that accepts an
# array and returns the largest value in the
# array. Return zero if the array is empty.
# largest([12, 40, 8]) should return 40
# largest([43, 90]) + largest([8, 2]) should compute 98
# largest([-100, -80, -40]) should return -40
def largest(a):
  # handle empty arrays.
  if len(a) == 0:
    return 0
  
  # have a variable that keeps track of the
  # largest thing we've seen so far.
  largest = a[0]
  
  # use a for loop to look at every single element
  # let python pass the values of a directly to the item variable.
  # no `i` needed!
  for item in a:
    # test each element against the largest we've seen
    if item > largest:
      # update the largest if something beats it
      largest = item

  # return the largest value
  return largest

print(largest([12, 40, 8]))
print(largest([24, 53, 2, 92]))
print(largest([43, 90]) + largest([8, 2]))
print(largest([-100, -80, -40]))
print(largest([]))
print(largest([]) + largest([16, 32]))
