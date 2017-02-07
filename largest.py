# Write a function called largest that accepts an
# array and returns the largest value in the
# array. Return zero if the array is empty.
# largest([12, 40, 8]) should return 40
# largest([43, 90]) + largest([8, 2]) should compute 98
# largest([-100, -80, -40]) should return -40
def largest(a):
  if range(len(a) == 0):
      return none
  largest = a[0]
  for i in range(len(a)):
      if a[i] > largest:
          largest = a[i]
  return largest


#done

print(largest([12, 40, 8]))
print(largest([24, 53, 2, 92]))
print(largest([43, 90]) + largest([8, 2]))
print(largest([-100, -80, -40]))
print(largest([]))
print(largest([]) + largest([16, 32]))
