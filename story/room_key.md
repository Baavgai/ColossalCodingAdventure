# Room With a Key

"Are you in a dungeon?  You have no memory of the night before or how you got here.  There is a torch burning in a wall sconce, illuminating the what appears to be deep dark hole you've been thrown in.  There is a pile of bones in the corner and a single windowless door."

That's our intro text.  Putting it up here will hopefully set our tone.  It's also a good way to describe a given text adventure.  The first line of the novel is always pregnant with meaning and foreshadowing.

## High level summary

The puzzle is to escape the room.  The key is in the bone pile, which can be found on close examination.  The player will only be able to escape the room if they're taken both the key and the torch.

## Detail

Now we take the above and flesh it out.  There is a lot of room here for script writers to have fun.  A programmer might jump right into code here.  However, we don't know how we're going to code it exactly, yet.  Instead, we'll storyboard it, using a grid to show how each command gets a response based on state and possibly changes that state.  How a given language might implement this is entirely up to the programmer.

### Locations

Player, BonePile, Wall, Void

### Initial State

Flag | Value
---- | -----
done | false
location_key | Void
location_torch | Wall
door_open | false

### Player Actions

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

### Player Actions - Short Text

The fun of text adventures is the often humorous, often purplish, prose.  For some quick and dirty content, we'll go beige.

- look
  - "You see a door, a torch, and a pile of bones."
- look door
  - (door_open and location_torch==Player) "You can see the way out."
  - (door_open) "It is too dark to see beyond the doorway."
  - "The door is locked."
- open door
  - (door_open) "The door is already open."
  - (location_key==Player) "You unlock and open the door.  Beyond is dark."
  - "The door is locked."
- leave, go, exit, use door
  - (door_open and location_torch==Player) [done=true] "You are free.  Congratulations!"
  - (door_open)  [done=true] "You fall to your death."
  - "The locked door bars your escape."
- look bones, look bone, look pile
  - (location_key==Void) [location_key=BonePile] "You find a key in the bones."
  - (location_key==BonePile) "You see bones and a key."
  - "You see a pile of bones."
- take key, get key
  - (location_key==Player) "You already have a key.  You don't see any more around."
  - (location_key==BonePile) [location_key=Player] "You take the key."
- look key
  - (location_key==Player) "You have a door key."
  - (location_key==BonePile) "You see the key in the bone pile."
- look torch
  - (location_torch==Player) "The torch is in your hand."
  - "The torch hangs on the wall."
- take torch, get torch
  - (location_torch==Player) "You already have the torch."
  - [location_torch==Player] "You now have the torch."
