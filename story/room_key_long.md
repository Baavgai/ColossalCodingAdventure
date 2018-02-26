# Room With a Key

More detailed script for [Room With a Key](https://github.com/Baavgai/ColossalCodingAdventure/tree/master/story/room_key.md).

### Player Actions - Long Text
- look
  - "You are in a dank cell with moldy stone walls.  There is a torch on the wall and a pile of bones on the floor.  The sturdy door blocks your escape."
- look door
  - (door_open and location_torch==Player) "Freedom awaits! There is a pit right outside the door that you can easy walk around.  Good thing you're holding that torch."
  - (door_open) "It's very dark beyond the doorway.  Who knows what lies beyond?"
  - "The door is very thick and locked tight.  If only you had a key."
- leave, go, exit, use door
  - (door_open and location_torch==Player) [done=true] "You are free.  Congratulations!"
  - (door_open)  [done=true] "You fall in the darkness to your death.  Pity you couldn't have seen that coming."
  - "The locked door bars your escape."
- look bones, look bone, look pile
  - (location_key==Void) [location_key=BonePile] "The bones appear to be human remains.  As you desecrate these, you find an unexpectedly shiny object.  A key!"
  - (location_key==BonePile) "You see a human skull and other rotting person bits.  And, of course, that key."
  - "You see a human skull and other rotting person bits."
- take key, get key
  - (location_key==Void) "Sorry, I don't see any keys around here."
  - (location_key==Player) "You already have a key.  You don't see any more around."
  - [location_key=Player] "You have the key!  And, you know, some unpleasant meaty residue you'd rather not think about."
- look key
  - (location_key==Void) "Sorry, I don't see any keys around here."
  - (location_key==Player) "You turn it over your hand.  This could be your key to freedom."
  - "It rests in the human bones.  You don't know why the former human didn't use it.  Maybe you could."
- look torch
  - (location_torch==Player) "It burns hot and bright in your raised hand, lighting your way."
  - "It rests in a rusty wall sconce, allowing you to see your squalid surroundings.  You might be able to get it free, if you wanted."
- take torch, get torch
  - (location_torch==Player) "You're already hold the torch."
  - [location_torch==Player] "You manage to wrest the torch free from the wall.  You are now holding the torch aloft.  It's heavier that it looked."
