from room import rooms

current = rooms["hall"]
inventory = {}

print("Spacecraft escape")
print("Zeus 3400 has crashed. Your only mission is to leave the craft as quickly as possible.")
print("Type \"help\" to display help message")
print("Type \"hint\" to receive hint")

def main():
  while True:
    global current

    print()
    print(current.name.title())
    print(current.description)

    if current == rooms["victory"]:
      print("Thanks for playing this game!")
      print()
      print("For reporting bugs or adding new features, please contact to email: bilolbeknormuminov@gmail.com")
      print("Link in bio: https://lnk.bio/QIeZ")
      print("Consider supporting me: https://www.patreon.com/bilolbeknormuminov")
      print()
      input("Press any key to exit...")
      return

    for item in current.items:
      print("  " + item.hint)
    
    inputs = input("> ").split()
    command = inputs[0]
    
    inputs.pop(0)
    attributes = inputs

    try:
      match command:
        case "go":
          current = current.go(attributes[0])
        case "pick" | "take":
          for item in current.items:
            print(f"You picked up {item.name}")
            
            inventory[item.name] = item

          current.items = []
        case "inventory":
          if not inventory:
            print("Nothing in the inventory")
          else:
            for item in inventory:
              print(inventory[item].name.title())
              print("- " + inventory[item].description)
        case "use":
          match attributes[0]:
            case "key":
              if current == rooms["corridor"]:
                if inventory["key"] is not None:
                  print("You opened a door to the Storage room")
                  rooms["corridor"].link("up", rooms["storage"])
                  inventory.pop("key")
            case "eye" | "eye of captain":
              if current == rooms["pathway"]:
                if inventory["eye of captain"] is not None:
                  print("The door to the emergency exit opens")
                  rooms["emergency exit"].link("right", rooms["pathway"])
                  inventory.pop("eye of captain")
            case "gun" | "laser gun":
              if current == rooms["hall"]:
                if inventory["laser gun"] is not None:
                  print("The door falls of")
                  rooms["hall"].link("left", rooms["navigation"])
        case "hint":
          print("Hint: " + current.hint)
        case "help":
          print("Help message")
          print("Command\t\tDescription")
          print("go [dir]\tTramsforms the player to the room in the direction dir [up|right|down|left]")
          print("pick\t\tPicks up every item in the room")
          print("take\t\tPicks up every item in the room")
          print("inventory\tShows all available items in the player's inventory")
          print("use [item]\tActivate item")
          print("hint\t\tReceive hint")
          print("help\t\tPrint out this help message")
          print("exit\t\tExit the game")
          print("quit\t\tQuit the game")
        case "exit" | "quit":
          return
        case _:
          print("What?")
    except:
      print("?")

if __name__ == "__main__":
  main()
