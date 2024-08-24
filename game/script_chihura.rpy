label choose_Chihura:
    # Chihura is Player's main teacher. He sees her most weekdays. She is indifferent to him but her fat, smell and hairiness begins
    # to fascinate Player. Interactions with Chihura are time driven but if he chooses to study this speeds up their occurence
    # He begins to work hard in class and she's impressed. He can help her with cataloguing antiquities
    #
    scene c_office
    show screen control_bar(c)
    show c at left
    show i at right
    $ c.gapcnt = c.gap
    "[i.c.name] arranges to see [c.c.name] in her office to talk about his studies"

    if c.level == -1:

        # Description

        "[c.c.name] is [i.c.name]\'s favourite lecturer. She studies English Literature with a special interest in the 16th to 19th
            centuries. She talks about her subject with passion and enthusiasm, motivating the class.
            He\'s very happy that she\'s his tutor"
        "[c.c.name] answers the door. She is [c.description] and has [c.body].
            She is wearing [c.dress]"

        # Criticism

        "She shows him into her office, indicating he should sit facing her desk. She sits down and fixes him with a hard stare,
            looking severe"
        c.c "Well [i.c.name]. How are you?"
        "He shrugs"
        i.c "Yeah, fine thanks. I\'m really enjoying your course"
        "She frowns and narrows her eyes"
        c.c "Really. I don'\t get that impression"
        "He feels himself panicking a little"
        i.c "Why? I go to your lectures. My marks have been OK"
        "She sighs"
        c.c "Just occasionally [i.c.name] I would like my students to try to do a good job, rather than
            cobbling together the bare mimumum to pass. Especially the boys"
        "He lowers his eyes. Her criticism does ring true. She turns to her computer, bringing up a list of
            his 3 essays so far and her marks"
        c.c "You\'re below average on all your work [i.c.name]. You may well pass but it\'s hardly a record to be proud of"
        i.c "I\'m sorry. I guess I\'ve just been busy"
        c.c "The thing is [i.c.name], your first essay showed promise, the first part anyway. The analysis of text was very good.
            Your conclusions were nonsense but that is something you could work on"
        "[i.c.name] is ashamed. He knows he could do better"
        i.c "I will try harder next time"

        # Challenge

        c.c "I know there are a lot of distractions here [i.c.name] but the purpose of studying at college is to learn, not to party
            and chase girls. I sometimes think I have two types of students, those with brains and those with cocks"
        "He stifles a smile. She\'s obviously pissed off"
        i.c "I\'ll do a really good job next time. I promise"
        c.c "I\'m going to set you some extra work [i.c.name]. Do it well and I can help you get a good grade. Prove to yourself
            you can do quality work and be successful"
        "He likes [c.c.name]. She obviously cares and is passionate about her work. (She\'s also pretty hot). If she\'s going to help
            him, he doesn\'t mind doing extra work"
        i.c "Thanks very much. I won\'t let you down"

        $ c.level = 0

    elif gChiStudy: # If studying and here then object is studied
        $ c.level += 1

        if c.level == 1:
            "They sit down opposite each other in her office once again. She has his essay on screen. He\'s put in a lot
                of effort for a change and wants to do well"
            c.c "How did you find [gChiStudy.name]? I deliberately gave you something challenging"
            "[c.c.name] is serious and not giving anything away as to whether she likes what he\'s done"
            i.c "It was something different and, er, surprising. I guess it\'s the type of thing you see in niche internet forums
                these days"
            c.c "And what did you think about the author\'s ideas?"

            if gChiStudy.desire == "Dom" or gChiStudy.desire == "Sub":
                $ ltmp = "sexuality"
            elif gChiStudy.desire == "Girl":
                $ ltmp = "gender identity"
            else:
                $ ltmp = "female beauty"
            i.c "It was interesting to read how he developed his views on [ltmp]. It certainly opened my eyes to a different perspective.
                What did you think of my analysis?"
            "[c.c.name] sniffs. His heart sinks"
            c.c "Well it\'s far too long and you\'re trying too hard to be clever with your prose. Clarity is much more important
                than trying to regurgitate a dictionary"
            "[i.c.name] hangs his head"
            i.c "I did try"
            c.c "But! I really like your perspective. Surprisingly, most young guys like you to have very traditional ideas about
                [ltmp] and anything out of the ordinary is condemned and treated as somehow freakish. You take a very reasoned
                approach and your argument that the author is ultimately pro-women is strong"
            i.c "Yes. He may have an unusual perspective but he\'s not doing anyone any harm and he only wants to please women"
            "[c.c.name] smiles. He\'s so relieved"

            "They spend time discussing his report. She points out where the text is too verbose and suggests where he could tighten it up.
                They get on well. [c.c.name] does know her stuff and shows him how he could improve"


        elif c.level == 2:
            "[i.c.name] was very pleased with the feedback from his last essay and he\'s tried hard to improve his work this time, making
                it shorter and clear. [c.c.name] seems more welcoming when she invites him into her office"
            c.c "I must say this was a much better effort [i.c.name]. I\'m really pleased with your progress. It\'s good to see there\'s
                at least one boy with some brains"
            "[i.c.name] smiles broadly"
            i.c "Thanks very much"
            c.c "Why don\'t we sit down on the couch? It will be more comfortable going through your essay there"
            i.c "Cool!"
            "She grabs her laptop and they sit together. He finds being close to her exciting with her full figure and lovely
                long, blond hair"
            c.c "The text is much more concise and to the point. Very good"
            "He smiles"
            c.c "Now this time I\'d say you\'ve been actually sympathetic to the author rather than staying neutral. Was that
                conscious decision?"
            i.c "Err, no. I guess it\'s just how the essay came out. Should I be more detached?"
            c.c "Not necessarily. You need to argue your point convincingly. I\'m not sure I\'m totally clear
                on your argument and I think your conclusions could do with some work. What exactly are you trying to say?"

            if gChiStudy.desire == "Dom" or gChiStudy.desire == "Sub":
                i.c "Well, a man\'s role is traditionally dominant but not every man wants that. There are, I\'m sure,
                    women who want to be in charge, both in life and in the bedroom. It\'s liberating for both to be freed from these traditional roles"
            elif gChiStudy.desire == "Girl":
                i.c "Being attractive is very important for many girls, but there are guys who want to be beautiful too, who like women\'s clothes and enjoy
                    being pretty and attractive. The ancient Greeks celebrated pretty boys and we should do the same"
            else:
                i.c "I\'m sure most men don\'t find very skinny women who look like dolls particularly attractive. We should celebrate women with
                    round bodies and natural hair"

            "He turns towards her. She's looking at him quizzically with a slight smile. She may be twice his age but she\'s
                still very beautiful. He feels a little uncomfortable. There\'s a short pause before she speaks"

            c.c "It\'s a good argument. Why don\'t we revise the text a little to make it more clear?"
            "[i.c.name] smiles and nods. They go through the second half of his essay. She wriggles a little closer to him
                and he feels the warmth of her leg against him and the soft pressure of her large breast against his arm. She doesn\'t
                wear perfume and the natural scent of her body is so exciting"
            c.c "I hope you found that useful [i.c.name]"
            i.c "Err. Yes. Thanks very much"

        elif c.level == 3:
            "He\'s really looking forward to see [c.c.name] again. Not only to hear what she thinks about his essay but
                also to be close to her. There was definitely a spark between them the last time"
            "[c.c.name] opens her door with a big smile"
            c.c "Come in! Come in!"
            "She grabs her computer and plonks herself down on the sofa, patting the seat beside her. She looks great as always and
              he eagerly sits next to her"
            c.c "I know you\'ve tried hard with this [i.c.name] but I don\'t think this was quite as good as your last effort"
            "He frowns, disappointed"
            i.c "What makes you say that?"
            "She pats his leg, leaving her hand there"
            c.c "You seem to get very involved and emotional in your review. I know the material can be challenging but you need to
                be objective. I hope these books haven't been disturbing for you"
            "He takes a deep breath, looking into her face. She\'s so pretty"
            c.c "Did the ideas in the book affect you [i.c.name]?"
            i.c "Can I be honest?"
            c.c "Nothing leaves this office [i.c.name]"
            "He gulps and bows his head"

            if gChiStudy.desire == "Dom" or gChiStudy.desire == "Sub":
                i.c "I do find the idea of submitting to a powerful woman very exciting"
                $ ltmp = "pretty little sub"
            elif gChiStudy.desire == "Girl":
                i.c "It did make me wonder what I\'d look like dressed as a girl. I really like the idea"
                $ ltmp = "beautiful tranny"
            else:
                i.c "I can\'t get the idea of a curvy, natural woman with thick body-hair out of my mind"
                $ ltmp = "boy who worships hairy women"

            "[c.c.name] smiles, stroking his leg once more"
            c.c "Mmm. I\'ve got a confession to make too. I\'ve always wanted a [ltmp] to play with"
            "His eyes meet hers. They are both breathing heavily. The tension is electric"
            "She reaches behind his neck and pulls their mouths together in a deep kiss. He feels
                the warmth of her body against him. He wraps his arms around her thick waist"
            "Her tongue probes his mouth. He sucks on it gently. He knows he wants to submit to her,
                to worship her"
            "Eventually she breaks the kiss, releasing his head"
            c.c "I\'m sorry [i.c.name]. I really shouldn\'t have done that"
            "He meets her hungry eyes. She doesn\'t look sorry"
            i.c "I don\'t want you to stop"
            "She smiles slightly, before standing up and tidying her hair. She stands over him"
            c.c "I\'ll understand if you don\'t want to carry on with this extra tuition [i.c.name]"
            i.c "You didn\'t take advantage of me [c.c.name]. Really. I\'ll do whatever you want"
            c.c "Now there\'s an offer that\'s hard to refuse. Especially from a [ltmp]"
            "He thrills at her words, glad that she understands his needs"
            c.c "It\'s important to me though [i.c.name] that you do work hard and do well whatever
                happends between us. Do you understand?"
            i.c "Yes! I\'ll try to be much more objective next time"
            c.c "Well shall we give you another try then? Perhaps I\'ll give you a reward if your work improves"

        elif c.level == 4:
            "He found [gChiStudy.name] very erotic but tried hard to distance himself and write objectively. He
                wanted [c.c.name] to be happy with it. She\'d promised him a reward if he did well
                and he was eager to claim it"
            "She shows him into the room and they sit together on the sofa as normal. She is very business-like,
                bringing his essay up on her computer and studying it. "
            c.c "Now [i.c.name]. How did you think you got on?"
            i.c "I tried hard to be objective, to be concise and to present the argument clearly"
            c.c "And did you find that difficult with the subject matter?"
            "He nods, a little ashamed"

            if gChiStudy.desire == "Dom" or gChiStudy.desire == "Sub":
                i.c "I did find the section where he totally submits to a dominant woman very exciting"
                $ ltmp = "little subby whore"
            elif gChiStudy.desire == "Girl":
                i.c "It did make me wonder what I\'d look like dressed as a girl. I really like the idea"
                $ltmp = "slutty femboy"
            else:
                i.c "I loved the part where he describes his excitement at seeing a woman\'s unshaven,
                    hairy armpits"
                $ltmp = "sex toy for a big, hairy woman"

            c.c "Well it doesn\'t come through in your work I must say. Your essay was very good"
            "She gives him a little smile, her eyes narrowing"
            i.c "That\'s a relief. Glad to hear I\'m back on track"
            c.c "Mmm. It\'s exciting to hear you liked the book too and I did offer you a little treat"
            "Her hand crept across to his thigh, stroking him"
            i.c "It was a big incentive"
            c.c "I know I\'ve worked you hard Honeybun and I know you want to be a [ltmp] so I want to help
                you"
            "Hearing her call him Honeybun is so hot. He smiles at her as they snuggle together"
            "He felt her fingers stroke his cock through his jeans. He was so aroused and she smiled as she
                gently caressed his erection. With a naughtly grin, she gives him a peck on the cheek"
            i.c "That feels so good [c.c.name]"
            "Her face is suddenly serious"
            c.c "Please call me mistress"
            "He gulps"
            i.c "Of course mistress"

            if gChiDict["Dom"]["count"] > 1:
                "All of a sudden she digs her nails into his groin hard, making him yelp"
                c.c "You\'d like your mistress to be rough with you though, wouldn't you"
                "She presses hard, really hurting"
                i.c "Yes mistress. I know I can be bad and need to be punished"
                "With a smile she releases him and gently strokes him once more"
                c.c "There's a good boy"

            "[c.c.name] tries to loosen his belt. He helps her and hurriedly pushes down his
                jeans and pants. He\'s so aroused and she smiles excitedly"
            c.c "Ooo, such a big boy!"
            i.c "Such a big boy for you"
            "Her hand slips over his penis once more. She barely touches him as she slowly strokes
                up and down his length"
            c.c "Would you like to play with my boobs [i.c.name]. I bet you like a girl with nice
                big tits"
            i.c "Oh wow, yes!"
            "Flicking her hair behind her ear, she slips off her jacket and unbuttons her blouse to reveal
                her sumptuous chest, barely contained by her white, lace bra. He gives a little grunt and smooths
                his hands over her perfect globes. She reaches behind her back to loosen her bra, revealing thick patches of
                light-brown hair under her arms"
            "His hands fondle her chest eagerly, caressing her nipples between thumb and forefinger and driving them to points. She
                strokes his penis once again, the tip now dripping with his precum"

            if gChiDict["Natural"]["count"] > 1:
                "She raises one arm over her head, revealing her hairy pit. He can see it\'s damp with perspiration"
                c.c "Would you like to taste a natural woman [i.c.name]?"
                "He doesn't answer but his hand snakes round her back so he can pull his face towards her body. She giggles as he kisses
                    her armpit gently, snuffling in the long, soft hair before lapping hungrily"
                c.c "Mmm. That\'s it Honeybun. Enjoy your mistress's sweat"

            "Her hand grips his penis harder but she still continues to wank him slowly, keeping him on the edge"
            c.c "Just lie back and enjoy yourself"
            "He relaxes back onto the couch"
            i.c "I\'m so close mistress, please let me cum"

            if gChiDict["Girl"]["count"] > 1:
                c.c "Lift your legs up Honeybun!"
                "He does as she asks and she guides the soles of his feet resting on the sofa. She grips his cock once more as her other hand sneaks
                    between his buttocks. She starts to massage his anus with her finger tips"
                c.c "You\'d love to be taken like a girl, wouldn't you?"
                "He groans"
                i.c "Oh yes, I'd love to take a nice big cock up my arse"
                "She pushes her finger into his back passage. It\'s dry and hurts a little but he doesn\'t care. It\'s
                    so hot, so deviant"

            "He can take it no more and he thrusts himself into her hand. With a cry, he cums hard and long, writhing on the sofa,
                his cum spurting over his body and the cushions"
            "She smiles naughtily as he calms"
            c.c "Good boy. You liked your reward didn\'t you?"
            i.c "Oh yes. Thank you so much"

            if gChiDict["Sub"]["count"] > 1:
                "She uses her fingers to scoop up a big blob of his seed from his chest before leaning over him"
                c.c "Open wide!"
                i.c "Well, I..."
                "She pushes her cum-soaked fingers into his open mouth. He dutifully swallows the salty goo down"
                c.c "A good little sub should tidy up after himself, don't you think?"
                i.c "Yes mistress"

            "She throws him some tissues as he tries to gather himself before cleaning up. She puts her clothes
                back on"
            c.c "I\'m sure you don\'t need any more of my lessons [i.c.name]. Your work is really good now and,
                if you keep up that standard, you'll get a very good degree. Shall we make this the last lesson?"
            "He\'s shocked, his eyes wide with surprise and horror. She thinks he looks so cute"
            i.c "But [c.c.name]!"
            "She raises an eyebrow. He tries to stop panicking."
            i.c "But mistress. I so want to be your Honeybun. You\'ve opened my eyes to so much and there\'s so
                much more I want to learn"
            c.c "Well I suppose we could continue but I would be much stricter with you [i.c.name]. I would demand total
                obedience and you need to do everything you can to please me. I\'m sure a little pain would focus your mind
                if you step out of line"
            i.c "Oh yes mistress. Just give me a chance! I\'m begging you"
            "[c.c.name] strokes his hair with a smug smile"
            c.c "I like the thought of you begging Honeybun. Let\'s continue then"

        elif c.level == 5:
            if gChiStudy:
                if gChiStudy.desire == "Dom":
                    $ ltmp = "He so wants to be dominated"
                    $ ltmp1 = "I really like the idea of you hurting me"
                elif gChiStudy.desire == "Sub":
                    $ ltmp = "He wants to worship [c.c.name], to fulfil her every need"
                    $ ltmp1 = "I want to submit myself to you completely"
                elif gChiStudy.desire == "Natural":
                    $ ltmp = "He can\'t wait to exmplore [c.c.name]\'s lovely hairy body"
                    $ ltmp1 = "Beautiful, big, hairy women really turn me on"
                else:
                    $ ltmp = "He loved being a girl for [c.c.name]"
                    $ ltmp1 = "The thought of dressing up in lovely girly clothes is so exciting"

            # Intro

            "[i.c.name] is so looking forward to seeing [c.c.name] again. [ltmp]. He takes a deep
                breath and knocks at her office door. She open it with a big smile on her face"
            c.c "Hello Honeybun. Why don\'t you come in?"
            "He follows her inside"
            c.c "Lock the door. We don\'t want to be disturbed do we?"
            i.c "Yes mistress"
            "He does as she asks and she takes him in her arms. Gazing into her pretty, smiling face and having her soft, sumptuous body
                against him is so hot"
            c.c "Mmm. You look sooo pretty Honeybun. Did [gChiStudy.name] get you all excited?"
            i.c "Oh yes! [ltmp1]."
            c.c "Well we\'re going to have lots of fun"
            "She kisses him gently as her hands slip under his shirt and tweak his nipples sharply. He yelps
                in pain and surprise"
            c.c "Aww, you\'re so cute when you\'re hurt Honeybun. You\'d look lovely with tears running down your cheeks"
            "He gulps"
            i.c "You can do anything you like to me mistress"

            # Prep

            c.c "Mmm. Good boy. Why don\'t you get undressed and put on the nice girly tights your mistress has bought you"
            "She leads him to the sofa where he throws his clothes off and, sitting down, pulls on a pair of black, fishnet tights
                she left on the arm rest. She helps him with the matching suspender belt, her hands gently stroking his penis, balls and arse"
            i.c "I love being a girl for you mistress"
            c.c "I know Honeybun. Stand up so that I can admire you properly"
            "He poses in front of her, the tights look good on his slender legs, his so-hard cock is proud and erect. She signals for him
                to turn round and, after he does so, she fondles his tight buttocks, kneading him hard"
            c.c "A little spanking first I think. Lean over the desk Honeybun"
            i.c "Yes mistress"
            "She stands over him, stroking his bottom softly, gently. He shuts his eyes in delicious anticipation. All of a sudden she whacks
                him hard with her palm, making him grunt. She gives him a few more slaps, not holding back. It\'s quite painful and he bites
                his lip. It\'s also very hot"
            c.c "Ooo, your bottom is lovely and red"
            "She reaches underneath him to squeeze his cock"
            c.c "You did like that didn\'t you, you naughty boy"
            i.c "Oh yes. Being dominated by you is so good!"
            c.c "Mmm. Now just stay there"
            "She pulls out a pink butt-plug from her desk drawer, smiling as she rubs it against his cheek"
            c.c "You\'re going to have to stretch your boy-pussy Honeybun if you want to take some nice big cocks and this is
                just the thing"
            i.c "You'd better put it in me then mistress"
            "[c.c.name] squirts some lube on the plug and squeezes it into his back entrance. With a gasp he feels it widen
                his tight little ring before being swallowed by his anus. It feels so good having something hard up there"

            # Worship

            c.c "Now that\'s you all ready Honeybun. It\'s time you did something to please your mistress"
            "She sat down on the sofa, playing with her hair and giving him a stern stare"
            c.c "Kiss my feet! Show me what a subby little whore you are!"
            i.c "Of course mistress"
            "He gets down on the floor and crawls towards her. She points her smart, shiny shoe at him expectantly.
                He reverentially kisses the toe before carefully slipping it off her foot"
            "She wiggles her toes and giggles"
            "Breathing heavily he kisses each of her toes in turn. Her feet smell musty and a little cheesy. He loves it"
            "She's not wearing tights and, with a thrill of excitement he notices the soft, light brown hair decorating her shins and he strokes them gently.
                It'\s so arousing worshiping a hot, hairy woman"
            "He spends time licking between her toes, carefully cleaning them before moving on to her other foot. Again, lifting it
                gently to his mouth and petting it lovingly"
            c.c "Now my legs"

            "He strokes his cheek against her shins before kissing her, feeling her body-hair against his face"
            i.c "So beautiful"
            "She loosens her skirt and pulls it up to reveal her thighs, also covered in sparse hair that merges into her
                very full bush, her pubic hair thick and long and running between her legs and across to her inner thighs"
            "He kisses slowly up her thighs. She spreads her legs, revealing the ragged lips of her pussy peeping out
                from the forest between her legs. He noses through the wiry mat, enjoying the hot smell of her arousal. As
                he kisses her pussy softly, she grabs his hair, pushing his face into her sex"
            "He gives a little moan. It hurts but he carries on worshiping her, kissing her pussy and slipping his tongue into her
                slit. She\'s so turned on and he pushes her open with his lips so he can pet her from her clit to her vagina"
            c.c "Ooo. That feels so good"
            "She pulls his head hard into her groin, his nose hurting as it\'s rammed into her hairy mound. He kisses her little
                pleasure-button, rubbing it with his lips and making her groan and twitch. She grinds herself against his face,
                smearing her juices across his nose, mouth and chin"
            "After a few minutes using him, [c.c.name] is panting heavily. Suddenly she yanks his head back roughly"
            c.c "I need to cum now. Sit on the sofa, I want to ride you!"
            "Wiping his face with the back of his hand, he hurriedly complies. He\'s also so turned on after being spanked
                anally probed and forced to worship [c.c.name]\'s hot, hairy body. His cock is rock hard and leaking pre-cum"
            "Facing him, she mounts him, sliding on his huge erection easily and crushing him against the sofa. They both moan as
                he kneads her big, fleshy buttocks"
            "Flushed and aroused, she fixes him with a stern stare"
            c.c "You\'re not to cum Honeybun"
            "He throws his head back against the sofa. He\'s nearly cumming, his cock deep in her warm, soft body her hairy thighs squeezing his
                waist and his hands caressing her lovely bottom"
            i.c "Please mistress!"
            c.c "No! Your job is to service me. You can cum when I say so and not before"
            "He shuts his eyes and tries to relax, digging his nails into the palms to try to hold himself back"
            "He screws up his face as she rides him hard, her big body bouncing on his cock. Her nails dig hard into his shoulders and he
                embraces the pain. Anything to stop himself cumming"
            "Her little moans turning to loud groans and, as her breathing becomes heavier, her whole body is shaking
                as she eventually squeals with a massive climax"
            "She seems to cum forever, writhing on top of him, her arms clamped around his slender body her hair tangling over his face. He
                just about manages to hold himself back. She stills, panting hard and resting her forehead against his, his eyes are still
                tight shut"
            c.c "Ooo. That was nice. Are you very desperate to cum Honeybun?"
            i.c "God yes! Let me cum mistress. I need to so much"
            c.c "I like it that you\'re still hard inside me. Mmm, but you have been a good boy. Do you promise to clean up after yourself?"
            "She strokes his cheek. He opens his eyes wide"
            i.c "I promise"
            "With a grin she lifts herself off him slightly. With a load moan, he grabs her buttocks once more and thrusts into her quick and
                hard"
            "The release comes quickly and powerfully, his body spasms as he cums inside her, his moans filling the room"
            "She cuddles his head into her chest, kissing the top of his head"
            i.c "That was a great lesson mistress"
            "[c.c.name] giggles"
            c.c "I\'m enjoying our little tutorials too"
            c.c "Come on, one last thing to do"
            "She clambers off him and stands up. She grabs his hair and pulls him to his knees in front of her. Her pussy is
                engorged, the lips large and open, the thick hair matted and damp with sweat and their cum"
            "He dutifully caresses her big hairy thighs and kisses her soaking pussy before carefully lapping up the mixture of her tart juices
                and his gooey, salty cum between her legs"
            i.c "Mmm. That was lovely"
            "She smiles down at him, caressing his cheek"
            c.c "You\'re learning fast Honeybun. Would you like to study another naughty book"
            i.c "Yes please mistress. The naughtier the better"
            "They get dressed. To her delight, he decides to leave the butt-plug in because it feels so nice"

            python:
                for item in item_lookup:
                    if item.name == "Chihura's Butt Plug":
                        i.add_item(item)

        elif c.level == 6:
            "Worship, 69"
            # If not reached fem then stay here
        elif c.level == 7:

            # Entrance

            "He\'s really excited to show [c.c.name] [i.oname]. He spends a long time getting ready,
                making sure his body is completely shaved, washing and combing his hair before putting
                it in a cute pony-tail and carefully applying his make up"
            "Pulling on some tight jeans shorts, a pink crop-top and some gold sandals, he admires himself in the mirror, twisting to
                see how the shorts emphasize his cute bum. Adding little gold hooped earrings and a gold nose ring
                completes his outfit"
            "He puts on some dark glasses and a long coat before taking a taxi to [c.c.name]\'s office"
            "Once he\'s standing outside her door, he takes a deep breath and slips off his coat. Checking nobody else
                is around, he unbuttons the top of his jeans, the bulge of his erection clearly visible. He knocks"
            "[c.c.name] opens the door. Her eyes open wide in shock"
            c.c "Oh my God!"
            "He flutters his eyelashes and blushes slightly. She quickly pulls him inside, locking the door"
            c.c "Oh Honeybun! You look gorgeous!"
            i.c "Thank you mistress. I was so looking forward to showing you the new me"

            # Fun

            c.c "Oh wow, wow!"
            "She strokes his cheek gently and caresses his ear. Her other hand brushes over his smooth waist and slowly rubs
                between his legs, enjoying his hardness. Her eyes are filled with hunger for this pretty femboy"
            c.c "You\'re so beautiful, your hair, your face, your jewellery, your cute little bum in those cute little shorts. I can\'t
                keep my hands off you"
            i.c "I\'m so pleased you like me mistress. I so love being a pretty girl. Thank you for teaching me all about femboys"
            "She unzips his shorts to reveal his frilly pink knickers, his cock huge and straining to be released. She kisses him their
                lips embracing passionately, her tongue delving inside his willing mouth. They are both so excited. Her hot, warm body is
                squirming against his as she rubs herself against his erection"
            "She breaks the kiss and rests her forehead against his"
            c.c "I hope you\'re going to be a girl from now on [i.c.name]. It\'d be a pity if you went back to being a dull, boring boy"
            i.c "I\'m going to try to be [i.oname]. I\'m not sure I can do it all the time though - I\'d be very nervous about people
                looking at me"
            c.c "[i.oname] is a lovely name Honeybun. She\'d be very distracting if she came to my lectures so perhaps she should only
                appear when you come to see me"
            i.c "Of course mistress"
            "They kiss once more, each grabbing the other\'s bum, her groping his firm cheeks, him kneading her soft, huge buttocks. [c.c.name]
                nibbles on his earlobe and whispers"
            c.c "Would you like me to get my strap-on out and fuck you like a girl?"
            i.c "Mmm. Sounds wonderful"
            c.c "You need to look after your mistress\'s needs first"
            i.c "Of course"
            "They walk to the sofa hand in hand. The teacher and her pretty femboy. Sitting down they cuddle, kissing passionately. He
                unbuttons her blouse and she slips it off before unclipping her bra to reveal her glorious hairy pits and let her big, white,
                succulent boobs free"
            "With a whimper her kisses her armpit, nosing through the soft hair. She giggles. After a few seconds he slides onto the floor
                so he can worship her tits, taking her nipple in his mouth and sucking it gently. She finds it so arousing having this pretty
                boy pleasure her and she kisses the top of his head, her blond hair falling over his face and shoulders"
            c.c "There\'s a good girl"
            "Cradled in her arms, he lavishes his attention on her breasts, licking around her nipples, nibbling the sharp points gently whilst his
                hands massaged them eagerly. She hugs him tight against her chest, her excitment rising as sweat started to drip from her
                lovely hairy pits"
            "She releases him and gently pulls him off her breast with his pony-tail before standing up and unzipping her skirt. He helps her take it off
                along with her black knickers. He gives a little moan of delight as he strokes her thick, hairy thighs and admires her huge, dark-brown bush"
            "She turns round, presenting him with her big, sumptuous buttocks, looking down on him, her face stern. He knows what he has to do. He
                smooths his hands over her bum, kneading the heavy flesh before parting her buttocks to revewal her most secret place, her tight
                little anus ringed by dark skin and decorated with thick, wiry hair"
            c.c "Come on Honeybun. Worship your mistress"
            "With a gasp, he buries her face in her ass crack, his lips seeking out her shit-hole and giving it a long, loving kiss. Licking ass is so
                subservient, so deviant and it turns him on so much. His tongue caresses her tight little ring, lapping the short, thick hair round the edge"
            "She gasps and wriggles her bum against his face, so enjoying him pleasuring her"
            c.c "Mmm. You\'re such a great ass licker Honeybun. Don\'t stop"
            "She strokes his silky hair, running her fingers through his pony-tail as he graps her thighs and pulls his face deep into her crack. He\'s in
                heaven with her big buttocks pressing against his cheeks, his tongue probing her anus, the animal scent of her arousal
                and the feel of her lovely hairy thighs in his hands"
            "She luxuriates in him rimming her for a couple of minutes before pulling his head back and turning round. He eagerly pushes his face
                into her hairy mound as she guides him into her pussy. She looks down at his pretty, innoocent face, made up and so lovely, his nose
                deep in her bush, as his tongue tickles her clit"
            "He kisses her little pleasure-button As she grinds herself against his mouth, burying him in her hairy pussy and smearing her juices
                over his face. He loves being on his knees worshipping her, his mouth full of the taste of her excitement. He\'s so turned on"
            c.c "Ooo. That\'s so good! Mistress needs to cum now"
            "He gives her pussy one last kiss before sitting back on his hauches. She sits on the sofa and spreads her legs wide, showing him her
             big, aroused labia surrounded by the forest of thick hair that covers her groin. He kisses the tangled mess, wet with her arousal and
             his saliva before mounting her"
            "She gives a little groan as he enters her. She\'s so wet and his cock pushes deep inside, fitting her perfectly"
            c.c "Remember, no cummies for you Honeybun"
            i.c "No mistress"
            "He shuts his eyes and bites his lip hard, trying to concentrate on the pain. She wraps her thick legs round his waist as he
                pumps himself quickly into her, a little too fast to make himself cum"
            "She loves it, grabbing his buttocks and digging her nails into his tight little bum. Although he\'s on top, she\'s in control,
                grinding herself against him as he rides her"
            "Throwing back her head, she lets out a series of little moans, rising in pitch, before climaxing with a massive orgasm that rips
                through her body. It\'s all he can do not to cum. He\'s so close but he manages to hold back, to stay hard for his mistress"
            "He thinks she looks so beautiful, her face flushed and panting hard as she lies underneath him. He strokes her cheek as she tries
                to recover"
            i.c "I love making you happy mistress. I'm so glad I'm your subby little slave"
            "She kisses him"
            c.c "Mmm. You are a good girl aren\'t you. Would you like your mistress to fuck you with her big strap-on now?"
            i.c "Yes please mistress. I want to be a really slutty girl who can take big cocks"
            "He climbs off her and she retrieves her toy from a cupboard. He gulps, it\'s big and thick, perhaps seven inches long, black and
                smooth. She smiles at him naughtily as she attaches the harness, positioning it on her groin and tightening the thin, black belts
                around her waist and thighs"
            "He flutters his eyelashes and kneels on the floor, resting his elbows on the sofa, presenting his backside to [c.c.name]. She carefully
                applies some lube to the big dildo before kneeling behind him"
            c.c "Shut your eyes and imagine there\'s a nice tall, muscular guy behind you Honeybun. He\'s so big and hard and needs to cum"
            "She guides the tip of the toy to his anus and probes gently, adding a little more lube to the tip"
            i.c "Oh yes! I so want him in me, using me, taking me hard and stretching me wide"
            c.c "And he wants you Honeybun. You\'re so pretty and girly"
            "With that, she pushes firmly on his backside. He squeaks as she forces her plastic cock into his tight, little ring and tries to
                relax as the thick toy stretches his back passage"
            i.c "Having a nice big cock in my boy-pussy is sooo good"
            "She grabs his thighs and thrusts into him slowly, she doesn\'t want to hurt him. He throws his head back. She enjoys her control over this
                pretty femboy, his smooth, slender body impaled on her strap-on, his pretty pony-tail sweeping across his back"
            "She reaches underneath him to firmly grap his penis. It\'s finally too much for him and he cums with a loud groan, pushing himself onto
                her toy as he shoots long ropes of his cum onto the floor"
            "He collapses onto the ground whimpering as she pulls out. His anus gapes wide before the little ring tightens once more"
            "She flops on the sofa as he dutifully grovels at her feet, sucking up his cum and tidying up like a good sub"
            "When he\'s finished, she pats the sofa beside her and he joins her for a cuddle. She\'s struck once again how pretty he his,
                even with his lipstick smeared, strands of hair escaping from his pony-tail and his chin glistening with her juices and his jizz.
                They smile at each other, satisfied and happy"
            c.c "You\'re so good to play with Honeybun. Particularly now that you\'re a beautiful girl with a nice, big cock"
            "He giggles, tossing his head"
            i.c "That\'s because my lovely mistress taught me to be so naughty and pervy"
            "They hug and kiss for a few minues. [c.c.name] has a lecture to do so they reluctantly untangle themselves and get
            dressed"



        else: # c.level >= 8:
            "On-going sex"

        $ gChiStudy = None

    else:
        "Not studying anything"

    if c.level < gChiMax:
        $ lchoice = ""
        menu:
            c.c "What would you like to study next?"
            "Female Beauty" if gChiDict["Natural"]["count"] <= gChiDict["Natural"]["max"]:
                $ lchoice = "Natural"

            "Boys Being Girls" if gChiDict["Girl"]["count"] <= gChiDict["Girl"]["max"]:
                $ lchoice = "Girl"

            "Male Submission" if gChiDict["Sub"]["count"] <= gChiDict["Sub"]["max"]:
                $ lchoice = "Sub"

            "Female Domination" if gChiDict["Dom"]["count"] <= gChiDict["Dom"]["max"]:
                $ lchoice = "Dom"

            "Skip for now":
                "You leave [c.c.name]\'s office and head back to your room"
                return


        $ filtered_objs = [obj for obj in item_lookup if obj.chiitem]
        $ ix = 0
        label find_objs:
            if filtered_objs[ix].desire != lchoice or gChiDict[lchoice]["count"] != filtered_objs[ix].level:
                $ ix += 1
                jump find_objs

        $ ltmp = filtered_objs[ix].name
        "[c.c.name] hands you a book titled: [ltmp]"
        if filtered_objs[ix].level == 1:
            "It seems an unusual thing to study but [i.c.name] wants to do well and he will try his best"
        elif filtered_objs[ix].level == 2:
            "After the previous book from [c.c.name], he doesn\'t know if he wants to read another one. Some of the ideas
                were quite intriguing though"
        else:
            "[i.c.name] knows this will be really deviant and potentially disturbing. He knows it should be forbidden but
                he can\'t wait to read it"

        if c.level > 0 and c.level < 3:
            "He leaves. He\'s learnt a lot and is keen to work on his assignment for [c.c.name]"
        elif c.level >= 3 and c.level < 5:
            "Taking a breath, he leaves. [c.c.name] is so hot and she really likes him. He resolves to do his
                best with his task and maybe she\'ll take things further"
        elif c.level >= 5:
            "They hug and she gives him a little kiss"
            c.c "See you soon Honeybun"
            "He smiles happily before leaving the office"

        $ gChiStudy = filtered_objs[ix]
        $ gChiDict[lchoice]["count"] += 1
        $ i.add_item(filtered_objs[ix])
        $ i.knowledge = 0
        $ gChiFlag = False

    return
