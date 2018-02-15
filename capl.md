# Coding Adventure Programming Language
Or, CAPL.  This language doesn't have an implementation. Yet.  The idea here to encapsulate the logic we'll need for our game.  This will allow a language agnostic description of a game that can be then implemented in the language of choice.

## Language Methods
```
state zone set key value
state zone get key
state zone has key 
state zone del key
rule zone match text state_change
localize zone # returns state_set,state_get,state_has,state_del,rule,alias functions localized to a given zone
```

## Zone
Zone is the locality in which the player currently finds themselves.  This is a room, in many games, but "room" doesn't makes sense when you're in a cave.  A zone is numeric.  By convention, zone 0 is global.

## Localize
This is a helper to make our code easier to write.  For a given zone, it returns a collection of functions, making local rules easier to write.

## State
Our game, of course, has state.  This state can get changed in a lot of ways and in response to any action.  For simplicity, and sanity, we'll define state as a series of key-value pairs.  The key will be a string, the value an integer.

There is a temptation to use state to, perhaps, store text responses.  This will introduce complexity and also make a save game a nightmare.  So, numbers only.

e.g.
```
state 1 set "door_open" 1
set,get,has,del,rz,az = localize 1
has "door_open"
```

## Rule
A rule is something that is matched based on the current state.  Here, part of that state will be the user entered command.  That command is pre parsed with three symbols present: c for the whole command, v for the first word, n for the second word.

e.g.
```
set,get,has,del,rz,az = localize 1
rz (c=="open door" && !(has "is_open")) 
  "The door creeks open ominously."
  (set "is_open")
rz (c=="open door") 
  "The door is already open"
```

This also demonstrates an important quality of rules: that are applied in order.  If a rule has been match, rule checking stops.  If a rule is not matched, if could be matched in zone 0.  e.g.
```
rule 0 (c=="open door") 
  "Door?  What door?  I don't see no stinking door.  Maybe you've gone stir crazy?"
```

The very last rule in your rule set should be something like:
```
rule 0 (v="look")
  "I don't see one of those around here."
rule 0 (true)
  "Sorry, I don't understand."
```
