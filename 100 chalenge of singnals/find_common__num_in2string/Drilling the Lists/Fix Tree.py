"""Not long ago a young Christmas elf asked you to implement a function that
 creates Christmas trees made of asterisks ('*') similar to the one below:
    *
    *
   ***
  *****
 *******
*********
   ***
Unfortunately because of the extreme coldness the tree that you sent over was corrupted:
although its lines are given in the correct order, but are not aligned properly.
Now your task is to fix the given tree by centering the asterisks in each line.

Example

For
tree = [
  "      *  ",
  "    *    ",
  "***      ",
  "    *****",
  "  *******",
  "*********",
  " ***     "
]

"""
def fixTree(tree):
    return [' ' * ( (len(item) - len(item.strip()))//2 )+ item.strip() + ' '* ( (len(item) - len(item.strip()))//2 ) for item in tree]
#return [x.strip().center(len(x))for x in tree]
# return list(map(lambda s: s.strip().center(len(s)), tree))

tree = [
  "      *  ",
  "    *    ",
  "***      ",
  "    *****",
  "  *******",
  "*********",
  " ***     "
]
print(fixTree(tree))
print()