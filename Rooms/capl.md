# CAPL Code

```
state 0 set "player_loc" 1

set,get,has,del,rz,az = localize 1

rz (c=="look" && !(has "door_open")) 
  "You are in a small room with a bed, a creepy portrait, and a closed door."

rz (c=="look") 
  "You are in a small room with a bed, a creepy portrait, and an open door."

rz (c=="look door" && (has "door_open")) 
  "The door is open, revealing a more spacious room beyond."

rz (c=="look door") 
  "The door is very sturdy, but appears unlocked."

rz (c=="open door" && (has "door_open")) 
  "The door is already open."

rz (c=="open door") 
  "The door creeks open ominously."
  (set "door_open" 1)

rz (c=="close door" && (has "door_open")) 
  "The door appears stuck now, it won't budge."

rz (v=="leave" && (has "door_open")) 
  "You find yourself in another windowless room.  In addition to the door you just walked through, there are two more doors, both closed.  One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.  Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig."
  (state 0 set "player_loc" 2)

rz (c in ["close door","leave room"]) 
  "The door still closed."

rz (v=="look" && n in ["painting","portrait","picture"] && !(has "pic_seen"))
  "The person portrayed hard to make out.  The painting is either badly aged or actually painted out of focus.  The subject could be a grotesque man or woman or angry lawn gnome.  The only element piercingly clear are black blood shot eyes that stare back at you with malice."
  (set "pic_seen" 1)

rz (v=="look" && n in ["painting","portrait","picture"])
  "The painting stares back at you.  You feel the desire to not be seen by it."

set,get,has,del,rz,az = localize 2


```