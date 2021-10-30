from item import *

class Room:
  class Deadlock:
    def __init__(self, message = ""):
      self.message = message
  
  def __init__(self, name, description = "", hint=""):
    self.name = name
    self.description = description
    self.hint = hint

    # Directions
    self.directions = {
      "up": Room.Deadlock("Blocked"),
      "right": Room.Deadlock("Blocked"),
      "down": Room.Deadlock("Blocked"),
      "left": Room.Deadlock("Blocked")
    }

    self.items = []
  
  def reverse(direction):
    match direction:
      case "up":
        return "down"
      case "right":
        return "left"
      case "down":
        return "up"
      case "left":
        return "right"

  def link(self, direction, room):
    self.directions[direction] = room
    room.directions[Room.reverse(direction)] = self
  
  def link_deadlock(self, direction, message):
    self.directions[direction] = Room.Deadlock(message)
  
  def go(self, direction):
    room = self.directions[direction]
    if type(room) is Room.Deadlock:
      print(self.directions[direction].message)
      return self
    else:
      return room

rooms = {
  "hall": Room(name="hall", description="Where it all started", hint="Nothing here. Try observing other rooms"),
  "navigation": Room(name="navigation", description="Eye of God", hint="Look around"),
  "corridor": Room(name="corridor", description="Long room, leading to several doors", hint="Where can I go?"),
  "dormitory": Room(name="dormitory", description="Nobody left alive", hint="Look around"),
  "storage": Room(name="storage", description="Boxes boxes boxes", hint="You are halfway done"),
  "pathway": Room(name="pathway", description="You see a scan at the other end", hint="Hmm. This door leads to somewhere..."),
  "emergency exit": Room(name="emergency exit", description="Your chance!", hint="One step away from victory"),
  "victory": Room(name="victory", description="You won! Only 0.01 percent of players achieved that!", hint="You won! You can replay the game. Type \"exit\" to quit the game"),
}

# Linking rooms to one another
rooms["hall"].link(direction="right", room=rooms["corridor"])
rooms["corridor"].link(direction="right", room=rooms["dormitory"])
rooms["hall"].link(direction="left", room=rooms["navigation"])
rooms["pathway"].link(direction="right", room=rooms["storage"])
rooms["victory"].link(direction="right", room=rooms["emergency exit"])

# Deadlocks
rooms["pathway"].link_deadlock(direction="left", message="Blocked door to emergency exit")
rooms["hall"].link_deadlock(direction="left", message="Blocked door to navigation room. (Hint: use gun to open)")
rooms["corridor"].link_deadlock(direction="up", message="The door is locked")

# Adding items to the rooms
rooms["storage"].items.append(items["laser gun"])
rooms["dormitory"].items.append(items["key"])
rooms["navigation"].items.append(items["eye of captain"])
