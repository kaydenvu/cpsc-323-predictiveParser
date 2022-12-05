class ParsingTable():
  def __init__(self):
    self.parseTable = [[0 for _ in range(9)] for _ in range(6)] # populate an 9x6 matrix
    self.parseTable[1][1] = 11 # TQ
    self.parseTable[1][6] = 16 # TQ
    self.parseTable[2][2] = 22 # +TQ
    self.parseTable[2][3] = 23 # -TQ
    self.parseTable[2][7] = 27 # epsilon ε
    self.parseTable[2][8] = 28 # epsilon
    self.parseTable[3][1] = 31 # FR
    self.parseTable[3][6] = 36 # FR
    self.parseTable[4][2] = 42 # epsilon
    self.parseTable[4][3] = 43 # epsilon
    self.parseTable[4][4] = 44 # *FR
    self.parseTable[4][5] = 45 # /FR
    self.parseTable[4][7] = 47 # epsilon
    self.parseTable[4][8] = 48 # epsilon
    self.parseTable[5][1] = 51 # a
    self.parseTable[5][6] = 56 # (E)
  def get(self, row : int, col: int) -> int:
    return self.parseTable[row][col]
    
def convertToRow(c: str) -> int:
  return {
    'E': 1,
    'Q': 2,
    'T': 3,
    'R': 4,
    'F': 5
  }.get(c, 0)

def convertToColumn(c: str) -> int:
  return {
    'a': 1,
    '+': 2,
    '-': 3,
    '*': 4,
    '/': 5,
    '(': 6,
    ')': 7,
    '$': 8
  }.get(c, 0)

def pushBackToStack(stack: list, x: int) -> bool:
  if x == 0:
    return False
  elif x == 11:
    pass
  elif x == 16:
    print("Pushing TQ onto stack.")
    stack.append('Q')
    stack.append('T')
    print(stack)
    return True
  elif x == 22:
    print("Pushing +TQ onto stack.")
    stack.append('Q')
    stack.append('T')
    stack.append('+')
    print(stack)
    return True
  elif x == 23:
    print("Pushing -TQ onto stack.")
    stack.append('Q')
    stack.append('T')
    stack.append('-')
    print(stack)
    return True
  elif x == 31:
    pass
  elif x == 36:
    print("Pushing FR onto stack.")
    stack.append("R")
    stack.append("F")
    print(stack)
    return True
  elif x == 42:
    pass
  elif x == 43:
    pass
  elif x == 44:
    print("Pushing *FR onto stack.")
    stack.append("R")
    stack.append("F")
    stack.append("*")
    print(stack)
    return True
  elif x == 45:
    print("Pushing /FR onto stack.")
    stack.append("R")
    stack.append("F")
    stack.append("/")
    print(stack)
    return True
  elif x == 47:
    pass
  elif x == 48:
    print("Pushing ε (epsilon) onto stack.")
    stack.append("ε")
    print(stack)
    return True
  elif x == 51:
    print("Pushing a onto stack.")
    stack.append("a")
    print(stack)
    return True
  elif x == 56:
    print("Pushing (E) onto stack.")
    stack.append(")")
    stack.append("E")
    stack.append("(")
    print(stack)
    return True
  return False

def main():
  parsingTable = ParsingTable()
  terminals = ['(', ')', '$', 'a', '+', '-', '*', '/']
  nonterminals = ['E', 'Q', 'T', 'R', 'F']
  state = ''
  accepted = True
  stack = []
  stack.append("$")
  stack.append("E")
  inputStr = input("Enter a string: ")
  print(stack)
  while not state == "$":
    state = stack[-1]
    inputChar = inputStr[0]
    if state == "ε":
      print("Popping ε (epsilon) from stack.")
      stack.pop()
      print(stack)
    elif state in terminals:  
      if state == inputChar:
        print("Popping from stack: " + stack.pop())
        print(stack)
        inputStr = inputStr[1:]
        print("Input: " + inputStr)
      else:
        print("Rejected.")
        accepted = False
        break
    elif state in nonterminals:
      row = convertToRow(state)
      col = convertToColumn(inputChar)
      if not parsingTable.get(row, col) == 0 or (not(row == 5 and col == 1)):
        print("Popping from stack: " + stack.pop())
        print(stack)
        if not pushBackToStack(stack, parsingTable.get(row, col)):
          accepted = False
          break
      else:
        print("Rejected.")
        accepted = False
        break

  if accepted:
    print("Accepted.")
  else:
    print("Rejected")
main()