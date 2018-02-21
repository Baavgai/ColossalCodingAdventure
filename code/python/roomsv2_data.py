#!/usr/bin/env python3

import ccav2 as cca

class Location:
    VOID, PLAYER, R1, R2, R3, R4, R5 = range(7)

def all_rules():
    def rules_r1(rb):
        rb.default_check = {'player': Location.R1}
        r = rb.add
        r(("look",""),"You are in a small room with a bed, a creepy portrait, and an open door.", {'r1_door_open': True}),
        r(("look",""),"You are in a small room with a bed, a creepy portrait, and a closed door."),
        r(("look","door"),"The door is open, revealing a more spacious room beyond.", {'r1_door_open': True}),
        r(("look","door"),"The door is very sturdy, but appears unlocked.", {'r1_door_open': False}),
        r(("open","door"),"The door is already open.", {'r1_door_open': True}),
        r(("open","door"),"The door creeks open ominously.", None, {'r1_door_open': True}),
        r(("look",("painting","portrait","picture")),"The door creeks open ominously.", {'r1_pic_seen': True}),
        r(("look",("painting","portrait","picture")),"""
                The person portrayed hard to make out.
                The painting is either badly aged or actually painted out of focus.
                The subject could be a grotesque man or woman or angry lawn gnome.
                The only element piercingly clear are black blood shot eyes that stare back at you with malice.
                """, None, {'r1_pic_seen': True}),
        r(("close","door"),"The door appears stuck now, it won't budge.", {'r1_door_open': True}),
        r(("close","door"),"The door still closed."),
        r((("leave",),("go",),("exit",),("use","door")),"""
                You find yourself in another windowless room.
                In addition to the door you just walked through, there are two more doors, both closed.
                One is red, the other is blue.  Looking behind you, you see the one you just opened is yellow.
                Directly in front of you is another painting, the subject of which looks suspiciously like a slaughtered pig.
                """,{'r1_door_open': True}, {'player': Location.R2}),
        r((("leave",),("go",),("exit",),("use","door")),"The door still closed.")

    def rules_r2(rb):
        rb.default_check = {'player': Location.R2}
        r = rb.add
        r(("look",""),"You are in a room with three doors, yellow, red, and blue.  On the remaining wall is a disturbing painting.")
        r(("look",("painting","picture")),"""
            What initially looked like butchered swine turns out to be a field of blood red poppies on
            a hill of dead yellow grass.  Still creepy.  And vaguely porcine.
            """)
        r((("go","yellow"),("use","yellow"), ("yellow","")), "You exit the room through the yellow door.", None, {'player': Location.R1})

    def rules_default(rb):
        rb.add(("die",),"You throw yourself at the ground.  Hard.  Ouch.  The world swirls away into darkness.", None, {'done': True})
        rb.add(None, "confused by {verb} {noun}")

    rb = cca.RulesBuilder()
    rules_r1(rb)
    rules_r2(rb)
    rules_default(rb)
    return rb.rules
