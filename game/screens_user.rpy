screen note_screen(iText):
    # Set the background image

    zorder 1
    modal True
    frame:
        background Solid("#10102012")
        add "images/notepaper.png"
        align (0.5, 0.5)
        xysize (348, 496)
        text "[iText]" area(40,30,258,350) font "BRUSHSCI.ttf" size 36 color "F00000"

        textbutton "OK":
             action Return ()
             align (0.5, 0.9)
             text_style "dbutton_text"
             style "sensitive_button"



screen control_bar(npc):
    zorder 1
    modal False

    frame:
        align (0.5, 0.0)
        background "#EFEFEF80"
        hbox:
            fixed:
                xysize (220, 80)
                text "[gDow]" yalign 0.5
            fixed:
                xysize (150, 80)
                text "Day: [gDay_cnt]" yalign 0.5
            fixed:
                xysize (120, 80)
                textbutton "P":
                    action Show("p_overview", None)
                    yalign 0.5
                    text_style "dbutton_text"
                    style "sensitive_button"
            fixed:
                xysize (120, 80)
                if npc != "None":
                    textbutton "[npc.id!u]":
                        action Show("npc_overview", None, npc)
                        yalign 0.5
                        text_style "dbutton_text"
                        style "sensitive_button"
                else:
                    text ""

# Player Overview
screen p_overview():
    # style_prefix "stat"
    default lib = i.lib_desc()
    default loath = i.loath_desc()
    default study = ""
    if gChiStudy:
        $ study = gChiStudy.name

    zorder 2
    modal True

    frame:
        xalign 0.0
        yalign 0.0
        padding (20,20)
        background "#EFEFEF"
        vbox:
            box_wrap True
            xmaximum 800

            hbox:
                xminimum 760
                xfill True
                vbox:
                    xminimum 380
                    text "{b}[i.c.name]"
                    text ""
                vbox:
                    xminimum 380
                    add "images/i icon.png" xalign 1.0

            text "[i.c.name] is a " + i.description + ". He wears a " + i.top + ", " + i.trousers + ", " + i.underwear + " and " + i.shoes + "."
            text "He has " + i.hair + " hair and " + i.bodyhair + " hair on his body"
            text ""

            grid 2 6 xspacing 20:
                text "{b}Attribute"
                text "{b}Value"
                text "Libido"
                text "[lib]"
                text "Self Loathing"
                text "[loath]"
                text "Cash"
                text "£[i.cash]"
                text "Knowledge"
                text "[i.knowledge]"
                text "Studying"
                text "[study]"

            text ""

            hbox:
                xfill True
                textbutton "Exit" action Hide() style "sensitive_button" text_style "dbutton_text" ypos 15 xalign 0.1
                if len(i.items) > 0:
                    textbutton "Items" action Show("p_collection", None, p=i) style "sensitive_button" text_style "dbutton_text" ypos 15 xalign 0.9

#
# NPC Overview
#
screen npc_overview(npc):
    # style_prefix "stat"
    zorder 2
    modal True

    frame:
        xalign 1.0
        yalign 0.0
        padding (20,20)
        background "#EFEFEF"
        vbox:
            box_wrap True
            xmaximum 800

            hbox:
                xminimum 760
                xfill True
                vbox:
                    add "images/[npc.id] icon.png" xalign 0.0

                vbox:
                    xalign 1.0
                    text "{b}[npc.c.name]"
                    text ""


            text "[npc.c.name] is a " + npc.description + ". She is " + npc.body + ". She wears " + npc.dress
            text ""
            text "{b}Personality:{/b} [npc.attitude]"
            text ""

            hbox:
                xfill True
                textbutton "Exit" action Hide() style "sensitive_button" text_style "dbutton_text" ypos 15 xalign 0.5

screen p_collection(p):
    zorder 3
    modal True

    default ix = 0

    frame:
        background "#AEAEAE"
        pos (0.1, 0.1)

        vbox:
            box_wrap True
            xmaximum 800

            text "{b} [p.c.name]\'s Collection" xalign 0.5
            hbox:
                frame:
                    background "#AEAEAE"
                    xsize 200
                    xfill True
                    text "{b}Item"
                frame:
                    background "#AEAEAE"
                    xsize 600
                    xfill True
                    text "{b}Description"

            for item in p.items:
                hbox:
                    frame:
                        background "#AEAEAE"
                        xsize 200
                        xfill True
                        text "[item.name]"
                    frame:
                        background "#AEAEAE"
                        xsize 600
                        xfill True
                        text "[item.description]"

            text ""
            hbox:
                xfill True

                textbutton "Exit" action Hide() style "sensitive_button" text_style "dbutton_text" align (0.5,1.0)
