class Item:
  def __init__(self, name, description = "", hint = ""):
      self.name = name
      self.description = description
      self.hint = hint

items = {
  "key": Item(name="key", description="Shape I don't regocnize", hint="Shiny"),
  "laser gun": Item(name="laser gun", description="Powerful weapon", hint="Bzz-bzz"),
  "eye of captain": Item(name="eye of captain", description="Oh, my lord", hint="Ewww")
}
