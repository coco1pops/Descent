label advance_days:
    # Advancing time
    # ==============
    # Flexible advance time to reduce grind
    # Increment day
    # Can add more than one day.
    # (Week days can go and see C and I and go to shops)
    # Tuesdays and Thursdays chance to see Y and S
    # Default Weekday is work
    # Week Options

    # Status Update
    # =============
    #   Libido. Player needs to satisfy himself. Plays with object. Increases Self Loathing
    #   Self Loathing. Player hates himself so much he needs to go home - end game - plenty of
    #   warning
    #   Nightmare. Player dreams of K, C, Y or S. Increases SL
    #   Knowledge increases with studying. Can use more objects
    #

    label val_days:
        $ txt_day_count = renpy.input("Please input number of days to skip (1-7)", default = 1, length=1, allow="1234567")
        if txt_day_count == "":
            jump val_days
        $ day_count = int(txt_day_count)

    $ lTxt = "day"
    if day_count > 1:
        $ lTxt = "following "+ str(day_count) + " days"

    # call choose_focus(lTxt)

    scene time_passing

    label day_loop:

        $ cnt = 0
        $ outofcash = False
        while cnt < day_count and not outofcash:

            # Consider setting nvl mode here
            nvl show
            n "Day is [gDow]{nw}"
            # Roll the dice each day
            $ d20roll = renpy.random.randint(1, 20)

            if gDow in ["Monday", "Wednesday", "Friday"]:
                n "[i.c.name] goes to lectures in the day time{nw}"
                if gFoc == "Study":
                    n "Inspired by the lectures today, [i.c.name] spends the evening studying hard"
                elif gFoc == "Chill":
                    n "He\'s exhausted after listening to the lecturers drone on and [i.c.name] flops onto the couch and watches YouTube clips before bed"
                elif gFoc == "Game":
                    n "Needing some distraction, [i.c.name] switches on his laptop and gets involved in a game, playing until after midnight"

                elif gFoc == "Exercise":
                    n "After all day sitting around, [i.c.name] goes out for a long run before having a shower and an early night"
                else: #gFoc == "Party"
                    n "The guys are going to the pub after lectures and [i.c.name] tags along. They have a great time drinking and laughing, staggering back
                        at the end of the night"

                $ i.update_stats(gFoc, 2)

            elif gDow in ["Tuesday", "Thursday"]:
                n "[i.c.name] goes to lectures in the day time{nw}"
                n "In the evening [i.c.name] works{nw}"
                if d20roll == 1:
                    # Possibly turn off NVL mode
                    nvl hide
                    call choose_Yuki
                    nvl show
                    # Turn back on NVL mode
                elif d20roll == 2:
                    # Possibly turn off NVL mode
                    nvl hide
                    call choose_Satomi
                    nvl show
                    # Turn back on NVL mode

                call evening_text

            else:
                if gFoc == "Study":
                    n "[i.c.name] spends the day studying before having an early night"
                elif gFoc == "Chill":
                    n "[i.c.name] lazes around during the day, chatting with a couple of has flat-mates and
                        has a couple of drinks before bed"
                elif gFoc == "Game":
                    n "[i.c.name] gets up late and starts gaming. He becomes absorbed and doesn\'t get to bed until the
                        early hours"
                elif gFoc == "Exercise":
                    n "[i.c.name] goes to the gym in the afternoon and has a good, long workout. After showering, he
                        has a healthy snack and falls asleep"
                else: #gFoc == "Party"
                    n "[i.c.name] goes to a house party. It\'s very busy with loud music, lots of drink and he has a great time,
                        dancing until dawn. He doesn\'t get to bed until very late."

                $ i.update_stats(gFoc, 3)

            nvl clear
            call player_events
            call npc_events
            call in_bed

            call add_day
            $ gDow = _return
            $ cnt += 1

            if i.cash < gPartyMinCash and gFoc == "Party":
                n "[i.c.name] does not have enough money to continue partying"
                $ outofcash = True

            if i.cash < gGameMinCash:
                n "[i.c.name] does not have enough money to continue gaming"
                $ outofcash = True

            nvl clear

    label morning:
        scene bg room

    return

label evening:
    nvl clear
    n "It is the evening"

    call evening_text

    call player_events
    call npc_events
    nvl clear
    nvl hide

    call add_day
    $ gDow = _return

    return

label evening_text:
    if gFoc == "Study":
        n "[i.c.name] spends a couple of hours before bed studying"
    elif gFoc == "Chill":
        n "[i.c.name] flops into bed at the end of his shift"
    elif gFoc == "Game":
        n "[i.c.name] switches on his computer and starts gaming. He plays until the early hours"
    elif gFoc == "Exercise":
        n "[i.c.name] stretches and does some push-ups before showering and getting to bed"
    else: # gFoc == "Party"
        n "[i.c.name] catches his flat mates at the pub at the end of his shift and they drink and chat
            until they are thrown out"

    $ i.update_stats(gFoc, 1)
    return

label add_day:
    $ gClock += datetime.timedelta(days=1)
    $ gDay_cnt += 1
    return(gClock.strftime('%A'))

label player_events:
    # Player events
    # =============

    #   Hair. At some point player's hair will be long enough so he doesn't need to wear a wig
    if i.hair_cnt > 0:
        $ i.hair_cnt -= 1
        if i.hair_cnt == 20:
            n "[i.c.name] notices his hair is getting long, down past his ears. Looking in the mirror,
                he wonders how short to cut it but then thinks he would look so much more feminine with
                longer hair. Perhaps he should leave it"
        elif i.hair_cnt == 0:
            n "[i.c.name] plays with his hair in the mirror, combing it into a pony-tail and shaking his
                fringe over his eyes. He looks so cute, so girly. [d.c.name] said she knew a really good hairdresser
                who catered for boys like him and he really wants to try her out, maybe asking for some highlights"

    #   Body. Player decides he wants to shave his body all the time
    if i.smooth == 0:
        n "His hairless body feels so nice and smooth. [d.c.name], [k.c.name] and [m.c.name] all said they liked him
            like this and he\'ll look so hot in a short skirt with his long, slim legs. He decides to shave all the time"
        $ i.smooth -=1

    #   Fem. Player admits to himself he likes being a girl. Triggers visit to I

    if i.smooth == -1 and i.hair_cnt == 0 and k.level >= 3 and m.level >= 3: # Need to add dependency on d
        n "Getting ready to go out, [n.c.name] admits to himself he really wants to put on jewellery and make-up.
            Perhaps a little pink top showing his belly button, short shorts and some high heels. He wants to
            mince into lectures, wiggling his cute bum and enjoying the guys looking at him. He needs help and to
            see [d.c.name] as soon as he can"
        $ i.fem = True

    #   Studying
    if gChiStudy:
        if gChiStudy.knowledge < i.knowledge and not gChiFlag:
            n "You have finished your paper on [gChiStudy.name] and mail it to [c.c.name] {nw}"
            n "He\'s learnt lots of new things that seem so naughty and deviant"
            $ i.libido -= gChiStudy.libido_mod
            $ gChiFlag = True

    #   Cash. Payments (rent, bills). Maybe ad hoc cash

    if gDow == "Saturday":
        n "Saturday is pay-day!{nw}"
        if m.level > 1:
            # Making money from OnlyFans
            $ of_cash = m.level * 10 # Maybe needs to drop off
            $ i.cash += of_cash
            n "[m.c.name] sends you £[of_cash] from OnlyFans {nw}"

        $ i.cash += gPizzaCash
        n "You get £[gPizzaCash] from working as a delivery boy {nw}"
        $ i.cash -= gPlayerCosts
        n "Your weekly living costs are £[gPlayerCosts] {nw}"

        n "You now have £[i.cash]"

    if int(gClock.day) == 30:
        if i.cash < gKasRent:
            jump end_game
        else:
            n "Well done, you have paid for [k.c.name]\'s rent"
            $ i.cash -= gKasRent
            n "You now have £[i.cash]"

    return

label npc_events:

    # NPC events
    # ==========
    # Things can happen in advance time, such as Kasumi becoming more dominant
    # Chihura setting assignments.
    # Check NPC events
    #   M sending update
    #   M sending cash
    #   C sending work (?)
    #   K becoming more Dom

    if k.countdown >= 0:
        $ k.countdown += 1
        if k.countdown == gKasTrigger:
            $ k.level += 1
            $ k.countdown = -1

    if m.countdown >= 0:
        $ m.countdown += 1
        if m.countdown == gMakTrigger:
            $ m.level += 1
            $ m.countdown = -1
            # Break out to have a call with Maki

    if k.gapcnt > 0:
        $ k.gapcnt -=1
    if m.gapcnt > 0:
        $ m.gapcnt -=1
    if c.gapcnt > 0:
        $ c.gapcnt -=1
    if d.gapcnt > 0:
        $ d.gapcnt -=1
    if y.gapcnt > 0:
        $ y.gapcnt -=1
    if s.gapcnt > 0:
        $ s.gapcnt -=1

    return

label in_bed:

    $ tLoath = 0
    $ tLib = 0
    $ tcnt = 0

    if i.libido > 10:
        n "[i.c.name] can\'t sleep so he decides to have some fun{nw}"

        # Dress up
        if i.libido > 25 and m.level > 2 and i.dress > 0:
            $ obj = i.get_obj("Dress", i.dress)
            $ tmp_dsc = obj.description[:1].lower() + obj.description[1:]
            n "The thought of becoming a girl feels so deviant and exciting.
                How pretty he looked, how sexy. Dressing up as a pretty femboy would spice
                up his evening. He hurriedly searches his chest of drawers to retrieve [obj.name], [tmp_dsc] {nw}"
            n "[obj.usage]{nw}"
            $ tLoath += obj.loathing_mod
            $ tLib += obj.libido_mod
            $ tcnt += 1

        # Toy
        if i.libido > 20 and m.level > 3 and i.toys > 0:
            $ obj = i.get_obj("Toy", i.toys)
            $ tmp_dsc = obj.description[:1].lower() + obj.description[1:]
            n "Remembering how much he enjoyed being penetrated, [i.c.name] pulls out the [obj.name] from
                a box under his bed. It felt so good, so submissive, it\'s [tmp_dsc]{nw}"
            n "[obj.usage]{nw}"
            $ tLoath += obj.loathing_mod
            $ tLib += obj.libido_mod
            $ tcnt += 1

        # Face
        if i.libido > 15 and i.clothes > 0:
            $ obj = i.get_obj("Clothes", i.clothes)
            $ tmp_dsc = obj.description[:1].lower() + obj.description[1:]
            n "Thoughts of worshipping big, fat, sweaty women turn him on so much. He wants to enjoy the
                taste and smell of their luscious, swampy bodies. He goes to his wardrobe to retrieve
                a bag hidden under his clothes and pulls out [obj.name], it\'s [tmp_dsc]{nw}"
            n "[obj.usage]{nw}"
            $ tLoath += obj.loathing_mod
            $ tLib += obj.libido_mod
            $ tcnt += 1

        if tcnt > 1:
            n "Press <Next> to continue"
            nvl clear

        # Read
        if i.books > 0:
            $ obj = i.get_obj("Book", i.books)
            $ tmp_dsc = obj.description[:1].lower() + obj.description[1:]
            n "He craves all that is deviant and perverse. Forbidden books about submissive sexual fantasies and
                feminisation are just so erotic. He pulls out [obj.name] from his bookshelf, it\'s [tmp_dsc]{nw}"
            n "[obj.usage]{nw}"
            $ tLoath += obj.loathing_mod
            $ tLib += obj.libido_mod

        if tLib < -10:
            $ tCaption =  i.c.name + "\'s cock has never been so hard as he loses himself in dreams of being dressed as a girl and "
            $ tCaption += "having depraved sex with fat, dirty, hairy women who dominate him and use his mouth and cock for their pleasure. He cums so hard he nearly passes out"
        elif tLib < -5:
            $ tCaption = i.c.name + "\'s head is filled with delicious sexual perversions. Having sex with big, hairy women, becoming a pretty femboy, "
            $ tCaption += "being spanked or even whipped. With a loud groan, he cums in a big pool all over his chest"
        elif tLib < -2:
            $ tCaption = i.c.name + " explores his submissive fantasties, dreaming of worshiping a big woman like " + m.c.name + " and exploring her sumptuous, "
            $ tCaption += "heavy body with his hands and mouth before she mounts him. He cums quickly, writhing on the bed in a exquisite pleasure"
        else:
            $ tCaption = i.c.name + " conjures images of sex with his lovely girlfriend. As his orgasm approaches, his thoughts stray to fantasies about "
            $ tCaption += "making love to " + m.c.name + ", losing himself in her huge breasts and watching her pretty face as she cums with him inside her."
            $ tCaption +=" Finally he cums himself with a satisfied moan"

        n "Settling down on his bed, [i.c.name] starts stroking his cock. [tCaption]"

        $ i.loathing += tLoath
        $ i.libido = i.dec_value(i.libido, tLib)

    return
