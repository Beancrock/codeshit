class GraphNode
  def __init__(self, ascii_char, x, y)
    self.x = x
    self.y = y
    self.ascii_char = ascii_char
    self.set_directions_from_ascii_char(ascii_char)
    self.population = new Population()

  def directions_from_ascii_char(char)
    # set the [n,s,e,w] from the crazy if else statement.  
    # or rewrite it so it is a map of ascii char keys to direction string array values
    self.directions = directionHash[char]
    # iterate directions so each can map to an x,y coordinate
    # maybe call it self.direction_targets
    self.direction_targets = {}
    for direction in self.directions
      x = 0
      y = 0
      if direction == 'n'
        x = self.x
        y = self.y + 1
      #... new case for each of the other directions
      self.direction_targets[direction] = {x: x, y: y}