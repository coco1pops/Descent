label choose_Yuki:
    # Need a flag for when available and first meeting. If first meeting then do light intro. Main attributes Hairy Worshiper, Toilet Slave
    # Player options: Enjoy greasy hair, lick hairy, stinking armpits, lick pussy stinking of pee, lick pussy after sex,
    # lick unwashed arse.
    # Yuki options: Farts, pees on player, wipes herself on player after poo
    # Need a standard outcome
    # Femboy makes no difference

    show screen control_bar(y)
    scene y_porch
    $ y.gapcnt = y.gap

    if y.level < 1:
        show i at right
        "[i.c.name] arrives at [y.c.name]\'s house. It looks pretty shabby and run down. Carefully holding
            the pizza in one hand, he rings the bell..."
        show y at left
        if y.level == -1:
            "After a couple of minutes [y.c.name] answers the door"
            "She is [y.description] and has [y.body].
                She is wearing [y.dress]"

            y.c "Well hello! I see I got a gorgeous extra side for my pizza. [m.c.name] said there was a hot new delivery guy"

            "[i.c.name] blushes. The smell of her suddenly hits him. A mixture of sweat and pee. What with her
                stained top, fleshy body and intense body odour, she must be such a slob"
            "[y.c.name] grins at his discomfort, thrusting out her big chest, giggling as his eyes are drawn
                to her massive, saggy breasts"
            $ y.level = 0
        else:
            "[y.c.name] answers the door. She smiles naughtily"

        y.c "Would you like to come in? I'm sure I could run to a little tip"

        "[i.c.name] gulps. He could do with the extra money. He\'s repelled by this fat, dirty woman who
            is more than twice his age and he\'s a little afraid of what will happen if he goes into her house"
        menu:
            "Go In":
                i.c "Yeah. A tip would be great"
                y.c "You\'d better come inside"
                jump yuki_0
            "Leave":
                i.c "I\'m so sorry. I need to get on with my deliveries. I can\'t stop"
                "[y.c.name] pouts, annoyed"
                show y cross at left
                y.c "Oh well. Maybe next time"
                i.c "Yeah. Maybe"
                "As [y.c.name] closes the door, he takes a deep breath and gets back on his scooter.
                    Was this a lucky escape or an opportunity missed?"
                $ i.libido += 1
                return

        label yuki_0:
            scene y_room
            show i at right
            show y at left
            "[y.c.name] leads [i.c.name] into her sitting room. It\'s very messy with dirty clothes
                scattered around. He tries to avoid looking at the stained underwear. She really
                is a disgusting woman"
            y.c "How does a £10 tip sound?"
            i.c "Sounds really good, thanks"
            y.c "Enough for a little kiss?"
            "She takes out a note and shows him, raising her eyebrows, her greasy hair framing her face.
                The smell of her body odour is even stronger in the house. He takes a deep breath."
            menu:
                "Kiss [y.c.name]":
                    i.c "Of course"
                    "He steps towards her, his hands gently wrapping around her waist, smoothing across
                        the roll of flesh that hangs over her tight jeans. She smiles and brings her mouth to his as
                        she pulls him against against her soft, warm body with one hand while groping his bottom
                        roughly with the other."
                    "Her lips force his apart and her tongue delves into his mouth as she rubs her fat body against his.
                        Her breath stinks and her tongue tastes sour. The smell of her dirty body is almost overwhelming and
                        he thinks he is going to retch. Even so he feels perversely aroused kissing [y.c.name]"
                    show y happy at left
                    "After a few seconds, [y.c.name] releases him, hands him the note and grins broadly."
                    y.c "Well wasn\'t that a nice way to earn some extra money"
                    i.c "Err. Yes. Thanks"
                    $ i.cash += 10
                    "He pockets the money and moves to leave. [y.c.name] scratches her bottom, smiling"
                    y.c "Perhaps next time we can have a little fun and up your tip [i.c.name]"
                    i.c "I don\'t know. I\'ll think about it. Perhaps"
                    "With an evil grin on her face, [y.c.name] waves him off as he gets on his scooter and leaves.
                        He\'s disgusted with himself at kissing such a horrible woman. What he finds even more
                        disgusting and confusing is that at one level he wants to do it again. And to go further"
                    $ i.loathing += 2
                    $ i.libido = i.dec_value(i.libido, 2)

                    # call self-loathing message and check
                    $ y.level += 1

                "Decline":
                    i.c "I\'m sorry. I have a girlfriend and I really love her"
                    show y cross at left
                    y.c "Well she\'s a lucky girl having such a handsome boyfriend but I'\m afraid
                        no kiss, no tip"
                    "[y.c.name] puts the money back in her pocket. [i.c.name] turns and leaves. As he gets
                        on his scooter, he wonders what might have been. [y.c.name] was really horrible but for
                        some reason the idea of kissing her seems so exciting"
                    $ i.libido += 2
            return

    # Player has kissed Yuki
    elif y.level == 1:
        show i at right
        "[i.c.name] arrives at [y.c.name]\'s house. He\'s worried after what happened last time
            but he admits to himself he\'s also excited. He rings the bell..."
        show y happy at left
        "After a couple of minutes [y.c.name] answers the door. She doesn\'t look to have washed
            or changed since the last time they met. She\'s smiling broadly"
        y.c "Why if it isn\'t my favourite delivery boy? I\'m feeling generous tonight and wondered if
            you\'d like a big tip?"
        "She holds the door open and beckons for him to go inside"

        menu:
            "Go In":
                "They walk into [y.c.name]\'s house"
                i.c "Is it the same deal as last time?"
                y.c "As I said, I\'m feeling generous. Come on through"
                jump yuki_1
            "Leave":
                i.c "I\'m sorry.I really can\'t spare the time tonight"
                "[y.c.name] screws up her face in annoyance"
                show y cross at left
                y.c "Next time, come just before a break"
                i.c "Yeah. Good idea"
                "[y.c.name] closes the door. He heads back into the night, trying to stop
                    himself thinking about [y.c.name]\'s huge breasts and enormous rump"
                $ i.libido += 2
                return

        label yuki_1:
            scene y_room
            show i at right
            show y at left
            "They are back in the sitting room. It\'s still a mess. It still smells
                strongly of [y.c.name]\'s dirty body."
            y.c "Another kiss or would you like a little more?"
            menu:
                "Kiss":
                    call yuki_ans_1
                    return

                "Ask For More":
                    call yuki_1_1


            return

    # Player has had sex with Yuki
    elif y.level == 2:
        show i at right
        "[i.c.name] arrives at [y.c.name]\'s house. He tells himself that having sex with a fat, dirty slob like [y.c.name]
            would be disgusting and so humiliating. He rings the bell..."
        show y happy at left
        "After a couple of minutes [y.c.name] answers the door. Her eyes narrow when she sees him, a smile creeps
        across her chubby face"
        y.c "Mmm. Hello Little Piggy. Would you like to come inside and play some more games with Mama-pig?
            She\'s all hot and stinky, just how you like her"
        "She holds the door open and beckons for him to go inside"

        menu:
            "Go In":
                "They walk into [y.c.name]\'s house"
                i.c "When did you last shower Mama-pig?"
                y.c "Oh, a couple of weeks ago maybe. I was hoping my cute Little Piggy\'s pretty mouth would
                    do all the washing I need"
                jump yuki_2
            "Leave":
                i.c "I\'m sorry.I can\'t do this. Not tonight"
                "[y.c.name] frowns, disappointed"
                show y cross at left
                y.c "Well you certainly enjoyed yourself last time"
                i.c "Yes. Sorry, just having a bad day"
                "[y.c.name] takes her pizza and slams the door. Seeing her huge tits was such a turn on
                    for [i.c.name] and he knows next time it will be even harder not to succumb"

                $ i.libido += 3
                return

        label yuki_2:
            scene y_room
            show i at right
            show y at left
            "They are back in the sitting room. The atmosphere is electric and he\'s breathing heavily in
                anticipation. Her smell seems even stronger and he admires the way her filthy teeshirt
                clings to her huge breasts"
            y.c "What would you like to do Little Piggy? I bet you can\'t wait to play with Mama-pig"
            menu:
                "Kiss":
                    call yuki_ans_1

                "Sex":
                    call yuki_ans_2

                "Worship":
                    call yuki_2_1

            return

    elif y.level == 3:
        show i at right
        "[i.c.name] arrives at [y.c.name]\'s house. The thought of spending the night with [y.c.name] is so revolting
            and yet so much of a turn on. He\'s conflicted, but his cock is so hard thinking about spending
            time with such a filthy, smelly MILF. He rings the bell"
        show y happy at left
        "[y.c.name] answers the door, her hair messy and lank, her clothes soiled and barely containing her chubby body. He feels a
            surge of desire. He wants to worship her body and wallow in her filth"
        y.c "Ooo I'd been hoping you would show up Little Piggy. Your Mama-pig has been very lazy since I last saw you.
            She\'s not showered, not changed her clothes and she\'s all dirty and smelly"
        i.c "Mmm. That\'s so hot. Your Little Piggy loves Mama-pig\'s stink and filth"
        "She grins and holds the door open"
        y.c "Let\'s go and have some fun!"

        scene y_room
        show i at right
        show y at left
        "They are back in the sitting room. He eagerly slips his arm round her thick waist, caressing
            the roll of fat falling over her jeans. She strokes his face, her eyes sparkling behind
            strands of her greasy hair. She stinks of old sweat and dried pee and it\'s turning him on so much"

        y.c "What would you like to do Little Piggy? I bet you can\'t wait to play with Mama-pig"
        menu:
            "Kiss":
                call yuki_ans_1

            "Sex":
                call yuki_ans_2

            "Worship":
                call yuki_ans_3

            "Spend the Night":
                call yuki_3_1

        return

label yuki_1_1:
    "She plonks herself on the sofa
        patting the seat next to her"
    y.c "Come and sit down"
    "[i.c.name] nervously does as she asks, his eyes meeting hers as he settles
        down beside her"
    y.c "You like my tits don\'t you [i.c.name]? Why don\'t you have a little play?
        Maybe a little taste? Then we can have some real fun. Please me properly and
        you\'ll get a nice big tip"
    i.c "Your tits look really good, yes. I\'d really like to touch them"
    "He reaches out and puts his palms on her chest, feeling her soft, warm flesh. Her
        enormous breasts feel fabulous in his hands as he kneads them gently. She smiles,
        licking her lips seductively, her face half-hidden by her lank, greasy hair"
    "[y.c.name] peels off her teeshirt and unclips her bra, revealing a mass of white,
        flabby flesh, her huge tits sagging downwards. He notices a thick forest of hair under her
        arms as the stench of her dirty body wafts towards him"
    "[i.c.name] moans slightly as he caresses
        her once again, his palms rubbing her big nipples to points. This fat, hairy MILF
        is turning him on despite himself. [y.c.name] arches her back, enjoying his touch"
    y.c "You like that don\'t you [i.c.name]? You like getting your hands on my huge tits. I bet it\'s
        making your cock really hard"
    i.c "Mmm, yes. They feel so good"
    "She roughly grabs him by the hair and kisses him hard, her tongue slurping noisily round
        his mouth. He can feel her lust building as she crushes him against her big, soft body. Her
        mouth has a sour taste of old coffee and her body odour is really strong but, all of a sudden it
        doesn't seem to matter"
    y.c "Be a good boy and suck my tits!"
    "She pushes his head down to her chest. With a whimper he fastens his mouth on her nipple,
        sucking it hungrily and feeling the point harden. Her flesh is greasy and tastes salty. He laps
        at her eagerly. She kisses his head, covering him in a curtain of her greasy hair"
    "He kisses down into her cleavage, eagerly burying his face in her sweaty body. She squashes his
        face between her breasts before letting him suck on her other nipple"
    "They are both breathing heavily. She grabs his hair once more and guides his head up to her armpit.
        The smell is intense, really strong and rank. Her pit hair is glistening with her sweat and he
        hesitates"
    y.c "Go on Little Piggy, enjoy my filth. You know you want to"
    "She pushes his face into her armpit. He snuffles into the soft hair, wiping her sweat on his nose,
        cheeks and chin. He almost retches at the stench but, with a little moan, extends his tongue to taste
        her disgusting, dirty pit"
    "She presses his head into her armpit and, with her free hand, [y.c.name] undoes [i.c.name]'s belt and jeans,
        reaching into his boxers to grab his cock firmly. It's hard as a rock. As she wanks him slowly, he groans
        and starts to lap her armpit, worshiping her filthy body"
    y.c "That's it. There's a good Little Piggy. Doesn't a woman's natural scent taste wonderful?"
    "She pulls his head away and stands up, swiftly yanking down her jeans and panties and kicking them off. Her bush
        is enormous, thick and black and spreading across onto her inner thighs with a treasure trail running up to
        her navel. Her thighs are thick and covered with sparse hairs. She straddles him, crushing him against the sofa
        and positions herself over his cock"
    "He gasps as she impales herself on him, his cock sliding easily into her soaking pussy. His hands automatically
        reach to massage her breasts hard as she starts to bounce and grind on his massive erection. She turns her head
        and wipes her hair hard against his face, marking him with her smell."
    "She\'s so aroused, her face flushed, her rolls of fat wobbling as she fucks him. He feels her big, fleshy thighs
        twitch and it drives him over the edge, cumming and cumming deep inside her. She cums a few seconds later with a loud
        groan and she writhes on top of him, panting and moaning as she rides out her climax"
    "They rest for a couple of minutes, both trying to get their breath. She strokes his ear and smiles down at him.
        He holds her tight, stroking her enormous buttocks "
    y.c "Ooo, you can come here again Little Piggy. That was very good. You loved exploring Mama-pig didn't you?"
    i.c "Mmm. Thank you for letting me be your little piggy"
    "He kisses her, letting her probe his mouth with her tongue once more. Licking this fat, dirty woman\'s sweaty armpits
        was so disgusting but it turned him on so much. He can smell her dirty stench on him and he feels both aroused
        and ashamed at what he\'s done"
    "She clambered off him, his cum dripping from her pussy and down her leg. Picking up her jeans, she pulls
        £20 from her pocket. With a sly smile she rubs her top between her legs and wraps the note in it before handing it to him.
        He can see her juices and streaks of his cum on her top"
    y.c "Something to remember me by"
    i.c "Thank you. Thank you Mama-pig"
    "She grins broadly, sitting back down on the sofa as he pulls up his jeans, stuffing her gift in his bag.
        Licking her lips as she admires her conquest, she laciviously runs her fingers through her enormous bush"
    y.c "Come back soon and we can play some more naughty piggy games"
    "He nods before stumbling out of the room to resume his round, his mind a whirl at what\'s just happened"
    $ i.cash += 20
    python:
        for item in item_lookup:
            if item.name == "Yuki's Top":
                i.add_item(item)

    $ i.loathing += 4
    $ i.libido =i.dec_value(i.libido, 4)

    # call self-loathing message and check
    $ y.level += 1

    return

label yuki_2_1:
    "He shuts his eyes, trying to resist but it's no good. He knows he wants to have sex with this fat, dirty
        woman who\'s twice his age. He wants to explore her filthy body and wallow in her dirt"
    i.c "I\'d love to play with Mama-pig"
    "He takes her in his arms and kisses her. She grabs his head firmly and probes his mouth with
        her tongue. She feels warm and soft in his arms and her strong smell is making him so turned
        on"
    y.c "Why don\'t we go to the bedroom and Little Piggy can have a good snuffle around?"
    scene y_bedroom
    show i at right
    show y happy at left
    "She leads him by the hand and they enter the bedroom. It\'s really messy with soiled underwear
        scattered around the room and dirty sheets tangled on the bed. She pushes him on the bed and
        climbs on top of him"
    "They kiss once more, he feels her passion rising as he\'s squashed beneath her heavy body. She wipes
        her hair across his face and he whimpers slightly as he enjoys her hot, animal scent"
    y.c "Go on Little Piggy. Why don\'t you suck on Mama\'s udders"
    "She rolls off him and pulls off her teeshirt, revealing her white bra, straining with the weight
        of her huge breasts"
    "He buries his face in her cleavage, lapping hungrily at her salty, sweaty flesh. She reaches down and
        gently strokes the big bulge in his trousers"
    y.c "That\'s it Little Piggy. You like Mama-pig\'s big, sweaty body don\'t you?"
    "He grunts, his face pushed hard between her tits, enjoying her soft flesh against his cheeks. She
        reaches round and unclips her bra before pulling his hair to guide his mouth onto her big,
        aroused nipple"
    "He fastens his lips on the succulent point, sucking noisily. She kisses the top of his head, cuddling him
        into her, bathing him in her greasy, dirty hair and the stench of her sweaty body. He starts to moan softly"
    y.c "Ooo, you\'re making Mama-pig all hot and bothered. I haven\'t washed my armpits for a while and I bet they
        are really stinky"
    "[y.c.name] raises her arms to reveal the matted forest of hair. She grins encouragingly at [i.c.name], her tongue
        licking her top lip"
    "[i.c.name] gives a little moan and plants a firm kiss on her sweaty pit. The acrid smell of old sweat clings to the
        soft hairs and he rubs his face in it, lapping hungrily"
    y.c "Enjoy yourself Little Piggy. Drink up all of Mama-pig\'s lovely sweat"
    "He nuzzles into her armpit, whimpering. The rancid stench is overpowering and it turns him on so much. Kneading her
        big, soft tits hard, he moves over and licks the other stinky pit, bathing his face in her stench"
    "His cock is huge, straining so hard against his pants, it's almost painful. She grinds herself on him, her heavy body
        crushing his erection between her legs"
    "She pulls his head back with his hair and kisses him aggressively, the sour taste of old coffee on her tongue mixing with
        the rank stink of her dirty body in his mouth"
    "As she uses his mouth, his hands slip down over the fat folds of her tummy to unbutton her jeans and pull down the zip. She gives
        a grunt of satisfaction as he gropes the soft, warm flesh of her huge buttocks"
    "He kisses along [y.c.name]\'s chin, nuzzling into her neck, enjoying the heavy scent of her dirty hair"
    i.c "Little Piggy wants to explore between Mama-pig\'s legs"
    y.c "Mmm. Mama-pig doesn\'t always wipe herself properly and it\'s been a while since she washed. It\'s really going to be filthy
        down there and Little Piggy will love it"
    "[y.c.name]\'s eyes are shining with lust, her round face, framed by her long, greasy hair flushed and excited.
        She rolls off [i.c.name] and hooks her thumbs behind her jeans to push them down"
    "He helps her take them off, pulling down her panties at the same time. [i.c.name] notices that her frayed, off-white knickers
        have a big yellow stain at the front and the gusset is a dirty brown. He\'s hit by a wave of revulsion but, at the same time,
        he/'s so aroused"
    "She lies back on the bed, narrows her eyes and spreads her legs, presnting him her huge, thick bush. He can just see her
        aroused labia undermeath the mat of dark, curly hair"
    "He kneels between her legs, stroking her thick thighs, enjoying the feel of her hairy legs against his palms. He admires
        the line of hair running from her navel to her bush and the way her pussy extends onto her thighs and between her legs"
    "Moving onto his stomach, he kisses the inside of her thigh and up to the thick forest between her legs. He noses through her pubic hair,
        feeling it caress his face. She smells like a dirty toilet, a mixture of dried piss and sweat with an earthy hint of
        something even more disgusting"
    "She cups her hands behind his head, pushing his face into her swampy, hairy crotch"
    y.c "Come on Little Piggy. Lick my cunt!"
    "He obliges, kissing the ragged edges of her pussy hard before his tongue delves into her slit where he probes her deep, wet vagina
        before licking up to her little pleasure button and rubbing it with his lips. He feels her thighs twitch as she enjoys him mouth"
    "She grinds hard and slow against him, crushing his face into her groin. He can barely breathe. The stench is overpowering,
        his nose buried in her matted, sweaty, pissy pubic hair and his mouth filled with her pussy juice"
    "He spends some time pleasuring her, licking her so-wet slit, taking her big pussy lips into his mouth and sucking them gently, probing her pussy
        with his finger and teasing her clit. His face is smeared with her juices as he rubs his face into her smelly crotch"
    i.c "I need to fuck you"
    y.c "Well I\'m not going to stop you"
    "She releases his head. He wipes his face with the back of his hand, brushing some stray black hairs from his cheeks. His mouth tastes
        of piss and sex as he raises himself on his hands and knees"
    "He frantically loosens his belt and drops his trousers. His cock is so big and hard, the tip leaking pre-cum. With a grunt, he mounts
        her, slipping in easily and pushing into her wet, sloppy hole to his full length"
    "She clamps her big, hairy thighs around his waist and grabs his bum hard, urging him deeper, her face flushed and covered in perspiration"
    "He can\'t hold himself back and, with a series of fast, urgent thrusts, he\'s driven over the edge, cumming deep inside this
        filthy, fat MILF"
    "She takes a few more seconds to cum, her arms and legs clamping his slender body against her as she thrusts her pussy against his
        softening cock. With a series of grunts, she eventually cries out, throwing her head back as she cums with a loud groan, her
        whole body twitching with her powerful orgasm"

    "He rolls off her onto the bed. They are both breathing heavily"
    "Eventually she turns on her side, stroking his chest"
    y.c "There\s a good Little Piggy. Wasn\'t Mama-pig\'s stinky body nice to play with?"
    i.c "Yes Mama-pig. Your Little Piggy loved it"
    y.c "Mmm. Would you like to stay the night? We could have lots more fun. Mama-pig would get all hot and sweaty, just how you like her.
        As a treat you could even watch Mama-pig peeing"
    "Again he was hit by powerful feelings of base desire and revulsion. Looking at [y.c.name]\'s round, pretty face and sultry smile he\'s so tempted.
        On the other hand, whoring himself out to this disgusting slob is so degrading and revolting"
    i.c "I really can\'t tonight. I need to finish my shift. I need the money"
    "[y.c.name] pouts"
    y.c "That\'s OK. I\'ll call at the end of your shift next time. Or maybe you could just come and see me a night you\re free?"
    i.c "Err, yeah. That would be cool"
    "She rolls off the bed, farting loudly and he\'s hit by the dark stench of her bowels. She giggles"
    y.c "Sorry. Though I bet you like my smell don\'t you?"
    "[i.c.name] nods, blushing with shame"
    y.c "Why don\'t you keep these?"
    "She picks up her filthy panties and rubs them playfully across his face. He nods, pulling on his trousers and putting them in his pocket. She
        retrieves some notes from her bedside cabinet and writes her number on a slip of paper. She hands them to him with a smile as he prepares to
        leave"
    i.c "Thank you [y.c.name]"
    y.c "Hurry back"
    "She grins and lies on the bed, putting her arms above her head to show him her hairy pits. He takes a couple of seconds to enjoy the sight
        of her huge tits, wide thighs, thick, hairy bush and hairy thighs. He can still taste her smelly, wet pussy on his lips"
    i.c "Don\'t worry, I will"
    "He leaves. As the fresh air hits him, he tells himself he should never see her again but he knows he\'s so weak and she turns him on so much"

    $ i.cash += 40
    python:
        for item in item_lookup:
            if item.name == "Yuki's Knickers":
                i.add_item(item)

    $ i.loathing += 8
    $ i.libido =i.dec_value(i.libido, 8)

    $ y.level += 1

    return

label yuki_3_1:
    y.c "Ooo. I hope you\'re feeling fit and strong Little Piggy. Mama-pig will need a lot of care and attention during the night"
    i.c ""

    return

label yuki_ans_1:

    "She grabs him around the waist and hugs him against her, grinding her
        hips into his crotch. They kiss, her tongue slurping noisily round
        his mouth as he\'s enveloped by her sweaty, smelly perfume"
    "After a few seconds she releases him and, with a big smile, hands him his
        tip. He stutters his thanks and leaves, wondering what would have
        happened if he\'d agreed to go further"
    $ i.cash += 5
    $ i.loathing += 2
    $ i.libido =i.dec_value(i.libido, 2)

    return

label yuki_ans_2:

    "She pushes him on the sofa and, with a sultry smile, starts to slowly strip.
        She peels off her top and unclips and tosses away her bra revealing her huge
        tits and fat tummy. She raises her arms above her head and turns on the spot, giving
        him a good view of her hairy armpits. He moans in anticipation"
    "Next, she slowly unbuttons her jeans and wriggles them down her legs. He\'s so turned
        on as she displays her thick, hairy pussy and huge rump."
    y.c "Time for Little Piggy to feed"
    "She climbs on his lap facing him. With a big grin, he smooths his hands over her
        enormous, sagging breasts before fastening his lips on her nipple. She rubs herself hungrily against
        his erection as he explores her chest with his mouth before kissing up to snuffle in her stinking,
        sweaty armpit. She reaches down and unfastens his trousers, pulling out his erect penis"
    i.c "Oh yes! Fuck me Mama-pig. Your Little Piggy is so turned on by your filthy body"
    "She mounts his cock and rides him hard, grinding out a huge, noisy climax. He too cums hard,
        her hair washing over his face as she bounces on him."
    i.c "Thank you Mama-pig. Thank you for letting your Little Piggy play with you"
    y.c "You are a good Little Piggy aren\'t you? Maybe next time you could have a little snuffle
    between Mama-pig\'s legs. She\'s very smelly down there and I know you like to wallow in her filth"
    "She gets off him and hands him £10 with a pout. He feels used and drained. He can\'t take
        his eyes off her fat, hairy body and he wonders just how perverted and depraved he is becoming"
    "Taking the money, he leaves the house to continue his deliveries. He can smell her dirty body on his
        lips and it tastes so disgusting and yet so wonderful"

    $ i.cash += 10
    $ i.loathing += 4
    $ i.libido = i.dec_value(i.libido, 4)

    return

label yuki_ans_3:
    scene y_bedroom
    show i at right
    show y happy at left

    "[y.c.name] grabs him by the hand and he follows her to the bedroom. It\'s still messy,
        the bed is unmade, the sheets are stained and there are old clothes and underwear scattered over
        the bed, floor and chairs"
    "She sits down on the bed, shaking back her hair and pulling him down beside her. They are both breathing
        heavily and they hug and kiss, their tongues fencing together. He almost chokes on the sour taste of her
        dirty mouth as she squeezes her big, soft body against his slender frame"
    "After a few seconds of hungry snogging, she grunts and pushes him down on his back, straddling his waist and
        trapping him beneath her. She peels off her shirt and bra as he sits up to feed from her breasts before she
        pulls his hair, guiding his mouth to her hairy, stinky armpit"
    "They both are getting excited and breathing heavily as he licks and sucks at her filthy, sweaty pits. She
        unbuttons her jeans and he helps her push them down over her huge buttocks and thighs, along with her knickers,
        dirty with yellow and brown stains"
    y.c "Lick me Little Piggy! Get your face between my legs and lick my filthy cunt!"
    i.c "Oh yesss! Sit on my face and use me!"
    "He lies back as she lowers her hairy pussy onto his mouth, squeezing his face between her fat, hairy thighs and
        burying him in the stinking forest between her legs. He eagerly pushes his tongue into her slit, lapping her
        slowly from vagina to clit and slurping her filthy juices into his willing mouth"
    y.c "Can you taste my dirt and piss Little Piggy?"
    i.c "Uhh-huh"
    y.c "You love it don/'t you? Ohhh!"
    "She shivers as he flicks her clit with his tongue and she grinds down on him, her head thrown back as she enjoys him
        licking her. He reaches up to grap and massage her huge, soft tits, making her wriggle with pleasure, crushing
        herself into his face even more"
    "She enjoys him for a few seconds before bending forward and roughly unbuttoning and unzipping his trousers, reaching inside
        to grab his cock and pull the huge, hard member free"
    "He moans as she bends forward and takes him in her mouth, sucking hard and noisily. The assault is so sudden and
        so stimulating, he almost cums. He licks her furiously, careless of the thick pubic hair in his mouth and the
        smell and dirt between her legs. He\'s so close and he wants her to finish at the same time"
    "She groans and responds, rubbing her crotch quickly against his mouth. She farts, bathing him in a stinking cloud
        just as her thick thighs spasm with a massive orgasm. Despite being gassed, he cums loudly, shooting his load into
        [y.c.name]\'s hungry mouth"
    "For a couple of minutes they lie there recovering. He\'s gasping for air underneath her. Eventually she rolls off
        and brings her mouth to his. She\'s kept his jizz in her mouth and their tongues dance in his salty, gooey seed as
        they kiss"
    "She lifts off him slightly, grinning broadly, her hair tangling round her face, his sperm dripping from her chin"
    y.c "Now that was nice"
    "He wipes her stink from his nose, mouth and chin with the back of his hand"
    i.c "Mmm. I love worshipping your body"
    "She sits on the bed to get his payment from the bedside table"
    y.c "You should spend the night one time. If you think you have the stamina that is"
    i.c "I think I need to go into training"
    "She curls an eyebrow"
    y.c "Plenty of training available here Little Piggy"
    "He grins and takes the money before pulling up his trousers. She slumps back on the bed and he waves goodbye, taking
        a monent to admire her naked, fat, hairy body before he leaves"
    "He takes a deep breath as he gets back on his bike. What is he doing? He\'s such a pervert and he should really stop
        whoring himself out to [y.c.name]"

    $ i.cash += 20
    $ i.loathing += 8
    $ i.libido = i.dec_value(i.libido, 8)

    return
