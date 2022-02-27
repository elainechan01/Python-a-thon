# <----- READ ME ----->
# A marathon runner was on their daily run when they encountered a Python. Help them escape by figuring out the shortest distance they can take out of 4 paths. You are to implement the concept of recursion to find out which path is the shortest by adding up all the distances in the list. You are not allowed to modify any of the existing code. You are only allowed to add to it. The main implementation of the program can be found in the `main` function below.

# <----- TO DO----->
# How can you add to this function to implement the concept of recursion, such that the function will keep calling itself until all the distances in the list has been added to the total sum?
def add_distances(path, total):
  if not path:
    return total
  else:
    distance = path.pop()
    total += distance 

# <----- TO DO ----->
# How can you add to this function to print the shortest distance out of four paths?
def find_shortest(path1, path2, path3, path4):
  p1 = add_distances(path1, 0)
  p2 = add_distances(path2, 0)
  p3 = add_distances(path3, 0)
  p4 = add_distances(path4, 0)


def main():
  path1 = [40, 48, 6, 5, 16, 55]
  path2 = [16, 22, 42, 37, 9, 6]
  path3 = [100, 180]
  path4 = [45, 1, 2, 8, 9]
  find_shortest(path1, path2, path3, path4)

if __name__ == "__main__":
  main()
