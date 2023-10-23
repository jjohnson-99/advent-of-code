import os

## assumes that we already have the puzzle text in "puzzle.txt"
## and that the text is in the directory above (indicated by ../)

data_array = []
# with open handles closing the file when done
with open("../puzzle.txt", 'rt) as fd:
          for line in fd:
            data_array.append(line.rstrip("\n"))

# we now have the data as strings in a list
calorie_array = []
count = 0
for entry in data_array:
  in entry != '':
    count += int(entry)
  else: # we have finished with an elf
    calorie_array.append(count)
    count = 0

# sum the top n calorie counts and return the total
def top_n(array: list[int], n: int) -> int:
  total = 0
  for i in range(n):
      index = array.index(max(array))
      total += array[index]
      array[index] = -array[index] # I did this to 'preserve' the data
  return total

print(top_n(calorie_array, 3))
