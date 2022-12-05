class ParsingTable():
  def __init__(self):
    self.parseTable = [[None for _ in range(8)] for _ in range(5)] # populate an 8x5 matrix
    self.parseTable[1][1] = 11
    self.parseTable[1][1] = 11
    self.parseTable[1][1] = 11
    self.parseTable[1][1] = 11
    self.parseTable[1][1] = 11
    self.parseTable[1][1] = 11

p = ParsingTable()
for row in p.parseTable:
  for element in row:
    print(element, end = ' ')
  print()