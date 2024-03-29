from stack import Stack

print ("Let's play Towers of Hanoi!\n")

stacks = []
stacks.append(Stack("Left"))
stacks.append(Stack("Middle"))
stacks.append(Stack("Right"))

def get_disks():
    num_disks = int(input("How many disks do you want to play with: "))
    while num_disks < 3:
        num_disks = int(input("Enter a number greater than or equal to 3: "))
    for i in range(num_disks, 0, -1):
        stacks[0].push(i)
    return num_disks

def get_optimal_moves(num_disks):
    num_optimal_moves = 2 ** num_disks - 1
    print("\nThe fastest you can solve this game is in {} moves.".format(
        num_optimal_moves))
    return num_optimal_moves

def get_input(x):
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    user_input = input("\nWhich stack do you want to move {} ([L]eft, [R]ight, [M]iddle): ".format(x)).upper()
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

num_user_moves = 0
num_disks = get_disks()
num_optimal_moves = get_optimal_moves(num_disks)

while stacks[2].get_size() != num_disks:
  print("\n...Current Stacks...\n")
  for stack in stacks:
    stack.print_items()

  while True:
    from_stack = get_input("from")
    to_stack = get_input("to")

    if from_stack.is_empty():
      print("\n\nThat stack is empty. Try Again.")
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else:
      print("\n\nYou cannot move a disk onto a smaller one. Try Again.")

print("\n\nYou completed the game in {} moves, and the optimal number of moves is {}.".format(num_user_moves, num_optimal_moves))
