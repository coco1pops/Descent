
# The game starts here.

label start:

    scene bg room

    call initgame from start_01
    # call intro from start_02
    # call game_start from start_03
    $ m.level = 4
    $ i.oname = "Petal"

    label main_loop:

        call check_end()
        if _return == True:
            jump end_loop

        show screen control_bar("None")
        call choose_focus from start_04

        $ chosen = ""
        call choose_character(chosen) from start_05

        hide screen control_bar

        if _return != "Skip":
            $ chosen = "choose_" + _return
            call expression chosen from start_06
            scene bg room
            hide screen control_bar
            call evening from start_07

        else:
            call advance_days from strt

        jump main_loop

    label end_loop:
        # if current_time == finish_time
        call episode_1

        call end_game

    # This ends the game.

    return


label choose_focus(multi="day"):

    menu:
        "Choose your focus for the [multi]"
        "Study":
            $ gFoc = "Study"

        "Chill":
            $ gFoc = "Chill"

        "Game" if (i.cash >= gGameMinCash):
            $ gFoc = "Game"

        "Exercise":
            $ gFoc = "Exercise"

        "Party" (i.cash >= gPartyMinCash):
            $ gFoc = "Party"
    return


label check_end:
    # if self loathing is too low, or Kasumi runs out of money, or Kasumi leaves Player then exit (failure)
    # if time is up then exit
    return

    # Allow user to select where he goes next from a map
    # May need to close down episodes already completed and
    # open up ones that have been made available

label choose_character(chosen):

    menu:
        "Who are you going to visit today?"

        "Your girlfriend [k.c.name]" if (m.level != 0 and k.gapcnt < 1):
            return "Kasumi"
        "[k.c.name]\'s friend [m.c.name]" if (m.level >= 0 and m.gapcnt < 1):
            return "Maki"
        "Your lecturer [c.c.name]" if (gDow != "Saturday" and gDow != "Sunday" and c.gapcnt < 1 and gChiFlag):
            return "Chihura"
        "Your councillor [d.c.name]" if (i.loathing >= gIndAvailable and d.gapcnt < 1):
            return "Indira"
        "The dirty, fat, hairy MILF [y.c.name]" if (y.level >= 3 and y.gapcnt < 1):
            return "Yuki"
        "The scary dom, [s.c.name]" if (s.level >= 3 and s.gapcnt < 1):
            return "Satomi"
        "Don\'t visit Anyone":
            return "Skip"

    return


label choose_Indira:
    # Need an indicator as to the stage of the relationship. Main attributes Chubby Chaser, Sweat Rag, Hairy Worshiper
    # Player options: Cuddle, gentle sex, hairy worship. Sex with Indira carries no self-loathing penalties
    # Indira options: Mothering, feminisation. Indira will suggest he shaves off his hair and becomes a femboy. He decides
    # in conversation with Indira
    # Indira will encourage his submissive nature
    # Every so often being mothered by Indira will reduce self loathing. They gradually grow to love each other
    $ d.gapcnt = d.gap
    if d.level < 0:
        "Intro to [d.c.name]"
        $ d.level += 1

    d.c "Come and sit down"
    "[d.c.name] pats the sofa next to her"


    menu:
        "Feeling Depressed":
            "General text around his life falling apart"
        "[k.c.name] Torturing Him": # if k.level > 4 and !gIndEvents[0]
            "[d.c.name] is appalled"
            $ gIndEvents[0] = True
        "[k.c.name] Finishing their Relationship": # if k.level > 5 and !gIndEvents[1]
            "[i.c.name] takes up with [d.c.name]"
            $ gIndEvents[1] = True
        "Unfaithful to [k.c.name] with [m.c.name]": # if m.level > 1 and !gIndEvents[2]
            "Discussion around what he\'s doing for [k.c.name]"
            $ gIndEvents[2] = True
        "Dressing as a Girl": # if m.level > 2 and !gIndEvents[3]
            "Explore if he likes it"
            $ gIndEvents[3] = True
        "Having Sex with Guys": # if m.level > 3 and !gIndEvents[4]
            "Discussion on his feelings. Warning from [d.c.name]"
            $ gIndEvents[4] = True
        "Seduced by [c.c.name]": # if c.level > 1 and !gIndEvents[5]
            "Gentle criticism from [d.c.name]"
            $ gIndEvents[5] = True
        "Whoring Himself to Dirty, Hairy MILF": # if y.level > 1 and !gIndEvents[6]
            "Explore motivation and feelings"
            $ gIndEvents[6] = True
        "Becoming [y.c.name]\'s Toilet Slave": # if y.level > 3 and !gIndEvents[7]
            "Stiff talking to from [d.c.name]"
            $ gIndEvents[7] = True
        "Becoming [s.c.name]\'s Sweat Rag": # if s.level > 2 and !gIndEvents[8]
            "Exploration of [i.c.name]\'s submissiveness"
            $ gIndEvents[8] = True
    return

label choose_Satomi:
    $ m.gapcnt = m.gap
    # Need a flag for when available and first meeting. If first meeting then do light intro. Main attributes Sweat Rag, Pain Slut
    # Player options: Lick sweaty armpits. Lick sweaty pussy. Lick sweaty arse. Lick sweaty feet. Let himself be
    # punished. Ask to be punished. Beg to be punished. Thank Satomi for punishing him
    # Satomi options: Riding crop, flogger, paddle, ball busting, CBT, scratching, biting, Strap-on/big dildo
    # Need a standard outcome once interactive outcomes are complete
    # Not so violent with a femboy. Suffocation, strap-on, light spanking
    show screen control_bar(s)
    $ s.gapcnt = s.gap
    "Satomi dialogue"
    return



label end_game:
    n "You have lost"
    # Final score and credits
