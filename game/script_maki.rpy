label choose_Maki:
    # Need an indicator as to the stage of the Maki relationship. Main attributes Chubby Chaser, Femboy, Cock Sucker, Anal Whore
    # Player options: Have sex, worship her body, become a femboy, Appear on OnlyFans, Depraved OnlyFans shows
    # Maki options: Flirt, sexual dominance, pegging, feminisation, Solo OnlyFans, Dom/Sub OnlyFans, Femboy gangbang OnlyFans
    # Need a standard outcome but she will encourage him to be more deviant and to become a femboy

    $ m.gapcnt = m.gap

    if m.level < 2:
        scene m_house
        show screen control_bar(m)

        if m.level == 0:
            "[i.c.name] messages [m.c.name] introducing himself as [k.c.name]\'s boyfriend and asking if she was going to be in to pick up the present"
            "[m.c.name] replies that she is. She also tells him that she\'s really looking forward to seeing him, which he finds a little unsettling"

        show i at right
        "[i.c.name] arrives at [m.c.name]\'s flat. It's well kept in a nice part of town"
        show m at left
        if m.level == 0:
            "[m.c.name] answers the door. She is [m.description] and has [m.body].
                She is wearing [m.dress]"

            m.c "Nice to see you again [i.c.name]. [k.c.name] said you might pick up your present"
            show m happy at left
            m.c "She also said you were going to help her pay her rent. That\'s so good of you!"

            "[i.c.name] finds her so disconcerting. With her pretty, wide smile, gorgeous silky hair and sumptuous body she\'s
                really hot"
            "[m.c.name]\'s eyes twinkle as she sees him admiring her. She runs her fingers through her hair, thrusting out her big boobs,
                giggling as his eyes scoot lower to admire her huge chest"

            "She hands him a box, which he opens to reveal two beautiful gold promise rings. One small and delicate with a cursive \'D\'
                etched on the small disk, the other larger and plainer with an \'S\'"

            i.c "Thank you so much. They are amazing! I feel a bit embarrassed about such a lovely gift"
            m.c "Well don\'t be. [k.c.name] is a good friend and you\'re being so nice to her"
            i.c "What do the D and the S mean?"
            m.c "That\'s for you and [k.c.name] to find out"

            # Need to add ring to inventory

            "Her smile is mysterious and tempting"

            show m at left

            m.c "There\'s also a way I could help you earn some cash [i.c.name]. If you were brave that is"
            show i confused at right
            i.c "What do you mean brave? What would I need to do?"
            m.c "Well I help people start on OnlyFans. Having a professional photographer and business advisor gives people the
                best chance of success. I could help you set yourself up. A pretty boy like you could make some good money"
            i.c "But I thought OnlyFans was guys leering at girls!"
            m.c "It is, but I could make you a girl. A gorgeous femboy that guys and girls would both find so sexy. You wouldn\'t
                have to take your clothes off or anything. I\'d just take some classy shots of you looking beautiful"
            show i cross at right
            i.c "That\'s a terrible idea! I\'m a guy. I\'m straight"
            m.c "I didn\'t say you weren\'t. All you need to do is to put on a little make-up, a wig and some nice girly clothes and
                jewellery. It\'d be a regular income too"

            $ m.level = 1
        else:
            "[m.c.name] answers the door. She has a sultry smile"

        m.c "Would you like to see my studio [i.c.name]. We could try a couple of shots. Just to see how good you could look.
            I\'m not going to do anything you don\'t feel comfortable with"

        "[i.c.name] considers. The offer is tempting but he\'s not sure he wants to do something so deviant"
        menu:
            "Go In":
                i.c "I guess I do need the money"
                show m happy at left
                m.c "You won\'t regret this [i.c.name]. I think you\'ll actually enjoy it"
                jump maki_0
            "Leave":
                i.c "I can\'t do this [m.c.name]. It would be so humiliating! So perverse!"
                "[m.c.name] shrugs"
                show m at left
                m.c "Well the offer is always open [i.c.name]. If you\'re ever short of money then just think
                    about it."
                i.c "Err. OK. I really don't think it would be a good idea"
                "As he starts to walk back to his flat, [i.c.name] turns the offer over in his mind. He feels
                    he was right to turn [m.c.name] down but he does need money and would it be so bad if he
                    just did a few poses? Don\'t people dress up in drag all the time?"
                $ i.libido += 2
                return

        label maki_0:
            scene m_basement
            show i at right
            show m at left
            "[m.c.name] takes [i.c.name] down some steps into her basement. They enter a large main room, obviously used as a studio,
                with lights and a screen. At the other side to the camera equipment there are racks of clothes and some cupboards.
                There\'s also a bathroom and an office"
            "[m.c.name] grins and takes [i.c.name] by the hand and leads him to a chair in front of a sink and mirror at the back of the room"
            m.c "I\'m going to make you beautiful [i.c.name]"
            i.c "You won\'t do anything permanent will you?"
            m.c "Oh, no! Just a wig and a little make up"

            "She carefully washes his face. He doesn\'t have much facial hair and she uses a razor to make his skin perfectly smooth as well as trimming and
                shaping his eyebrows. Next, she applies foundation and powder before carefully adding some eye-shadow. She\'s blocking the mirror
                so he can\'t actually see what he looks like"
            "The atmosphere is electric. Having her so close to him he finds so erotic"
            m.c "Shut your eyes honey. I don\'t want you to see yourself before I\'ve finished"
            "He does as she asks and hears her opening drawers. Eventually she pulls a wig over his head, tucking his hair under the cap"
            m.c "You have lovely hair. You should grow it so we wouldn\'t need a wig"
            i.c "I wasn\'t planning to do this regularly"
            "She clips some earrings on him"
            m.c "We\'ll have to get your ears pierced too"
            i.c "[m.c.name]! I don\'t want to become a girl!"
            m.c "Even one as beautiful as this"
            "She moves aside, letting him see himself in the mirror"
            show i fem at right
            "He gasps. The transformation is incredible. He looks so feminine. So pretty. She stands behind him, hands on his shoulders and
                gives his head a little kiss"
            m.c "What do you think?"
            i.c "I don\'t know what to say. I really do look like a girl"
            m.c "You look gorgeous. You\'re going to be a real star"
            "He hooks his hair behind his ear, turning his head from side to side admiring his earrings"
            m.c "You\'ve done really well so far. I think we\'ll just do some photos of your top half today"
            "She presents him with some black fishnet sleeves and a lacey black bodice. He tentatively takes them. As
                [m.c.name] bustles around setting props in front of the cameras, he takes off his shirt and puts them on.
                The bodice is tight and is obviously designed for a very thin woman. The cups are small too and don\'t look too out of place on his
                flat chest"
            "[m.c.name] has set up an easy chair in front of the wall with a lamp beside it, giving the impression of a sitting room"
            m.c "Just sit down and look at the camera. Act a little shy but try to vary your expression"
            "He does as she asks. The first few shots he\'s very nervous, his eyes blinking with the flash"
            m.c "Relax [i.c.name]. Show everyone how pretty you are, what a lovely girl you have become"
            "Taking a deep breath, he poses more confidently, smiling at the camera, fluttering his eyelashes, putting his arms
                behind his head and shaking his hair over his face"
            m.c "Oh wow! Just think of all those boys who are going to be getting hard for you"
            "He blushes hard. She thinks he looks so cute and the camera flashes again and again. A shy smile creeps across his face
                and he licks his lips before resting his chin on his cupped hands"
            "Eventually she puts down the camera"
            m.c "That was enough to get started I think. How do you feel?"
            i.c "I suppose I got into it. I didn\'t think I would"
            m.c "You were great. Very sexy"
            "She takes his face in her hands and kisses him. Initially their lips meet softly but they fall into a long, loving kiss. He
                tries to remember this is [k.c.name]\'s friend and he really shouldn\'t be doing this. Eventually she pulls back"
            m.c "Yes, well, I\'ll get your OnlyFans account set up. I suppose you don\'t want it in your own name?"

            $ valid_name = False
            while not valid_name:
                $ player_name = renpy.input("Please enter your character\'s OnlyFans name (at least three characters)", default = "Yumi")
                $ player_name = player_name.strip()  # Remove leading/trailing spaces
                if player_name.isalpha() and len(player_name) >= 3:
                    $ valid_name = True
                else:
                    "Please enter a valid name with at least three alphabetic characters."

            $ i.oname = player_name

            m.c "[i.oname] is a good name. I think I\'ll call you that from now on. I\'ll also send you the
                link to the pictures when I post them and the money at the end of the week"
            i.c "Do you think I\'ll make any money?"
            m.c "Oh yes. The first set will get people excited and they'll want to see more. A lot more. They will also
                be prepared to pay for it"
            i.c "I\'m not sure I want to go any further. It\'s humiliating being a guy posing as a girl "
            m.c "I think you\'re going to enjoy being [i.oname]. Perhaps more than being [i.c.name]"
            "[m.c.name]\'s eyes twinkle excitedly. He frowns, the idea is unsettling. [m.c.name] obviously finds it very
                exciting"
            "She helps him remove the wig and clean the make up of his face. He puts his teeshirt back on and prepares to leave"
            m.c "Just give me a call when you want to show the world your lovely body [i.oname]"
            i.c "I\'ll think about it"
            "[m.c.name] smiles at him, her eyes shining. As he leaves, he wonders what he\'s done. He hopes [k.c.name] doesn\'t find out"

            $ m.level += 1
            $ i.loathing += 2
            $ i.libido =i.dec_value(i.libido, 2)

            return

    # Player has OnlyFans account
    elif m.level == 2:
        scene m_house
        show screen control_bar(m)

        show i at right
        "[i.c.name] approaches [m.c.name]\'s house nervously. The OnlyFans money has been really good but is he
            willing to go further? Then there\'s [m.c.name] herself. He finds her so attractive and she obviously likes him.
            Does he really want to be unfaithful to [k.c.name]?"
        "He rings the bell"
        show m sultry at left
        m.c "Hi [i.oname]. Are you ready to be a beautiful girl again? Your fans really want to see more?"
        menu:
            "Take the Next Step":
                jump maki_1

            "Art Shoot":
                call maki_ans_1

            "Leave":
                call maki_leave

        return

        label maki_1:
            i.c "I think I\'m ready to take things a little further, yes"
            show m happy at left
            m.c "Ooo [i.oname]! You\'re getting me all excited. Come in and let\'s get started"
            scene m_basement
            show m happy at left
            show i at right
            "[m.c.name] is obviously so pleased with his decision, grinning broadly. He feels very apprehensive"
            m.c "Now we\'re going to be showing more of you today [i.oname]. Very tastefully you understand. I know you\'re not
                a very hairy boy but femboys are nice and smooth so you need to get rid of all your body hair. Do you want to shave
                yourself or shall I do it?"
            show i confused at right
            i.c "Err, I\'ll do it"
            "There'\s a flash of disappointment on [m.c.name]\'s face but she shrugs it off"
            m.c "OK then. The bathroom is over there. Here are some clothes to put on"
            "She hands him a pretty pink dress, small blue knickers and pink socks along with a razor. He gulps but takes them and
                goes into the bathroom"

            "He carefully shaves himself, legs, arms, armpits and groin. Several times he asks himself what is he actually doing but
                he carries on and finishes before pulling on the clothes. The dress hangs only half way down to his knees and the
                panties barely contain his cock. For some reason he is getting aroused as well as ashamed"
            "Eventually, blushing prettily, he emerges from the bathroom. [m.c.name] grins and claps her hands"
            m.c "You look lovely! Let\'s get you made up"
            "He sits down in the make-up chair and she starts her work. Putting on his wig, fixing his face, clipping on earrings and
                this time a gold necklace. She takes her time, making sure [i.oname] is a perfect creation"
            show i fem at right
            "When she\'s finished, she lets him admire himself in the mirror"
            m.c "Don\'t you look gorgeous?"
            "She teases his hair, a big grin on her face. He can\'t disagree. What is he turning into?"
            i.c "I do look good. Thank you [m.c.name]"
            "[m.c.name] takes him by the hand and leads him to the studio. She\'s set up a bed in front of the cameras. It\'s strewn
                with rose petals"
            m.c "Just start slowly [i.oname]. We'll just have some shots of you on the bed first. Just show everyone what a beautiful girl
                you are"
            "[i.c.name] lies on the bed, getting comfortable before smiling at the camera so cutely. [m.c.name] takes full length pictures of
                him with his long, smooth legs and a glimpse of his knickers underneath his short little skirt"
            m.c "Now, tease as you take off your dress"
            "He takes a deep breath and unbuttons the front, looking sensually at the camera. Next, he lifts it to his waist, showing the camera
                the obvious bulge in his panties. Finally he takes it off and lies back, his arms straggling over his head. His slender,
                smooth body in full view of [m.c.name]\'s eager camera"
            "[m.c.name] reaches out and starts to stroke the bulge in his panties. He\'s already semi-hard but her touch soon makes him fully aroused"
            m.c "Mmm. My beautiful girl has such a lovely cock"
            "He shakes back his hair smiling and spreads his legs. His panties are straining obscenely against his erection and his balls are
                clearly visible. [m.c.name]\'s camera clicks furiously "
            "Swept away by the moment, he slips down his knickers, giving her full view of his smooth cock and balls. Putting his hands behind his head
                he presents himself to her"
            m.c "Turn over [i.oname]. Let me see that lovely bottom"
            "Pouting, he turns over, kneeling on the bed and wiggles his smooth, pert, tight bottom at the camera, his face so innocent and sweet. Narrowing
                his eyes, he spreads his buttocks to display his back entrance, offering himself to his fans"
            m.c "Oh wow [i.oname]"
            "She\'s breathing heavily, her face slightly flushed. She\'s obviously so aroused. She lays the camera down carefully and joins him on the bed,
                her hand cupping his cock and balls and stroking him slowly. He pulls her mouth to his and they kiss passionately, tongues delving into
                one another\'s mouth"
            "They struggle with her dress, almost ripping it as they pull it over her head. Their mouths slurp together once more as she frantically unclips her bra
                and pulls down her knickers. His hands maul her huge tits, squeezing the soft flesh hard"
            "She gropes his backside, urging him on. He tries to push her back
                but she takes control and uses her weight to force him down beneath her. She mounts him, impaling herself on his huge cock"
            "Their bodies thrash together frantically, both needing release. She grinds herself against him, bouncing hard, her breasts and stomach wobbling deliciously.
                He matches her thrusts as their cries and moans get quicker and louder"
            "It was never going to take long and she cums with a shriek. He burts inside her, almost passing out as he pumps her full of his seed. She collapses on
                top of him and they rest, panting hard. After a minute or so, they kiss passionately once again"
            i.c "That was so... so intense!"
            m.c "I tried to hold myself back but you were too fucking hot!"
            "[i.c.name] strokes her cheek, they are both grinning happily, [m.c.name] looks like a cat who got the cream"
            i.c "Do you prefer me as a girl?"
            m.c "Oh yes! You\'re so gorgeous [i.oname]. Those snaps will be fabulous. Perhaps next time we\'ll do a little video"
            "She rolls off him and they cuddle, he smooths his palm over her huge breasts, flabby stomach, enormous buttocks and fat thighs. He admitted to himself
                that he finds her irresistable. If dressing like a girl gets him sex this good then maybe he should do it more"
            "Eventually they decide to move, gathering their clothes and starting to get dressed"
            i.c "Please don\'t tell [k.c.name]"
            m.c "Of course not, [i.oname]. It\'ll be our secret. Though she should be thanking us for paying her rent"
            "She grins naughtily and they kiss once more"
            i.c "I really want to do this again"
            m.c "Mmm. Me too. I\'ve got some very naughty ideas for pictures of my gorgeous femboy for next time. Why don\'t you take the jewellery
                and practice being pretty and girly?"

            python:
                for item in item_lookup:
                    if item.name == "Jewellery from Maki":
                        i.add_item(item)
            i.c "Mmm. I can\'t wait. It was so exciting being a girl"

            "Taking his leave, he tries not to think too hard about what\'s just happened. He feels so bad about betraying [k.c.name]. He wonders
                whether being with [m.c.name] turned him on so much or was it dressing as a girl. He heads back home troubled"

            $ i.libido = i.dec_value(i.libido, 4)
            $ i.loathing += 3
            $ m.level += 1
            $ i.hair_cnt = 30
            $ i.smooth -= 1
        return



    elif m.level == 3:
        scene m_house
        show screen control_bar(m)

        show i at right
        "[i.c.name] steels himself as he approaches [m.c.name]\'s house. He still hasn\'t admitted to himself he likes dressing as a girl
            and posing naked for the camera but he can\'t wait to see [m.c.name] again. This big, sexy girl turns him on so much
            and he knows he won\'t be able to stay totally faithful to [k.c.name]"
        "[m.c.name] answers the door"
        show m sultry at left
        m.c "How\'s my favourite internet porn star?"
        "[i.c.name] laughs"
        i.c "I wouldn\'t go as far as calling myself a porn star"
        m.c "Have you read the comments on your site? Lots of people think you have star quality"
        i.c "Lots of people want to do all sorts of filthy things to me"
        "[m.c.name] stands close to him. He can smell her intoxicating perfume as he gazes into those mesmeric blue eyes. She strokes
            his cheek"
        m.c "I\'d like to do some filthy things to [i.oname]. She\'s so gorgeous. I bet she can be a dirty little slut too. What do you
            want to do today? We could try something really naughty if you like"

        menu:
            "Explicit Session":
                jump maki_2

            "Pose Naked":
                call maki_ans_2

            "Art Shoot":
                call maki_ans_1

            "Leave":
                call maki_leave


        label maki_2:
            "[i.c.name] bites his lip. Maybe if he really goes for it, he can have sex with [m.c.name] again"
            i.c "I\'d be ok with really naughty"
            show m happy at left
            m.c "I\'m so glad! Let\'s get going"
            "They go down to the basement. [i.c.name] sits in the make-up chair. [m.c.name] stands behind him and strokes his head, grinning broadly.
                He takes a deep breath"
            i.c "Can you show me what to do? I\'d like to be able to turn myself into [i.oname]"
            m.c "Of course [i.oname]. It\'s so lovely to hear you\'re embracing your true self. She kisses the top of his head"
            "She lets him tidy his face and shows him how to apply the foundation and powder. He is a little clumsy with his eye-liner
                and, after giggling at his incompetence, [m.c.name] shows him how to put it on properly. They finish with some dark eye-shadow and
                lipstick"
            show i fem at right
            "[m.c.name] attaches his earrings and he admires [i.oname] in the mirror. She really is a pretty girl. [m.c.name] bends down and rests her chin
                on his shoulder, her blue eyes sparkling"
            m.c "This is who you are [i.oname]. A beautiful, sexy femboy. The perfect fuck-toy"
            "She turns his head towards her and they kiss, gently at first but it soon becomes hungry and passionate"
            "He caresses her neck, holding their lips together. At that moment, he wants to be [i.oname], he wants to be a pretty girl"
            i.c "Thank you for turning me into a girl [m.c.name]. I feel so beautiful and sexy"
            m.c "Mmm. Too sexy. We\'d better get going with the shoot before I fuck your brains out"
            "She tears herself away from him and picks up a black lace camisole, matching knickers and some fishnet tights
                and suspenders"
            "He undresses. She grins as she admires his smooth body and sizeable erection"
            m.c "You do like being a girl don\'t you?"
            i.c "Yes I do. I really like being a girl for you [m.c.name]"
            "He pulls on the knickers, hooking them over his big cock before pulling on the tights. She
                helps him fasten his suspender belt round his waist and clip them to the top of the tights.
                Finally the pulls the loose cami over his head"
            show i cami at right
            "Admiring himself in the mirror, the silky top and sexy tights look and feel so good on him and the big bulge
                in his panties is so deliciously deviant. He shakes his hair over his shoulders. He loves being a girly slut"
            "[m.c.name] hugs him gently from behind"
            m.c "Mmm. Perfect [i.oname]"
            i.c "I want to be a very naughty little femboy [m.c.name]. I want my fans to fantasize about using me for their pleasure"
            m.c "I thought we could do some shots of you putting some nice toys in your boy-pussy, perhaps a little video too.
                You can show them you\'re ready for their cocks"
            i.c "Mmm. That\'s so rude!"
            m.c "And you love it!"
            "They both laugh and kiss once more before [m.c.name] picks up two dildos from a shelf along with a bottle of lube.
                There's one small, silver vibrator with a dial on the bottom and a larger purple toy, which is a big piece of smooth plastic"
            "They go over to the studio area where she\'s set up a bed. No petals this time but some light pink sheets and a cute
                little teddy with bows in its hair positioned between the pillows"
            m.c "We\'ll put them under the pillow and you can get them out and play with them after you\'ve done some teasing first"
            i.c "Are you going to film me?"
            m.c "Not at first, perhaps a few minutes at the end when you\'re all excited"
            "[i.c.name] gets on the bed and [m.c.name] focuses the camera on him"
            "He starts to pose, his face innocent then smiling then sultry. He lies back on the bed and spreads his legs, letting
                [m.c.name] take shots of the big bulge in his panties, before he turns over and displays his tight little bottom. He
                looks so cute and lovely in his lovely cami, tights and knickers"
            "[m.c.name] encourages him. She thinks he\'s so beautiful, so sexy"
            "Lying on his side, a little smile crosses his face and he reaches under the pillow to pull out the two toys.
                Narrowing his eyes, he strokes the little silver dildo against his cheek before kissing it"
            m.c "Take your knickers off [i.oname]. Then we can start filming"
            "He unclips his suspenders and pulls down his panties. He is fully erect. He so loves the thought of hungry guys admiring
                his naked body. Clipping the tights back on, he displays himself to the camera shamelessly, spreading his legs and
                turning over once again to show off his bottom"
            i.c "Do you want to start the video now?"
            m.c "OK. Start with the vibrator and then use the big dildo"
            "He grins naughtily at the camera as he applies lube to the tip of the vibrator then giggles when he turns it on. Next, he turns
                over on his front, raises his bum and wiggles his cute little booty at the camera"
            "With one hand he pulls his buttock to the side as he brings the tip of the toy to his back entrance. He gives a little squeak
                of delight as he starts to probe his back passage with the humming vibrator"
            "He gasps as he pushes the little dildo inside his anus, pouting at [m.c.name]. He feels so naughty, so deviant. [m.c.name] takes
                shot after shot as the video camera continues to capture him enjoying himself"
            "He rolls on his back and lifts his knees to his chest, toying himself and throwing his head back. His cock is big and erect as
                he puts the full length inside himself"
            "With his free hand he picks up the other dildo and starts sucking it hungrily, cramming the thick plastic into his mouth. Tossing
                the little vibrator aside, he lubes up the purple dong and rubs the tip against his asshole"
            "Fixing the camera with a sultry stare, he grabs the base firmly. His eyes flicker as he pushes it hard against his tight anus,
                breaching the little ring. He squeaks as it stretches him. [m.c.name], breathing heavily, kneels down between his legs to
                takes some shots of the big toy buried in his ass"
            "Eyes shut, he works it in deeper, his pretty face a mixture of pleasure and pain. His free hand strokes his cock, the tip dripping
                pre-cum. He\'s obviously so turned on at having a big cock inside him and he\'s biting his top lip, smearing his red
                lipstick"
            "Most of the dildo is inside him as he writhes on the bed. All of a sudden it becomes too much and he cums hard, great ropes of
                his jizz spurting over his chest and onto the sheets, the video camera capturing his spasming body, ecstatic expression and
                the big spatter of cum on his body"
            m.c "Wow [i.oname], you really enjoyed that didn\'t you?"
            "[i.c.name] nods weakly"
            i.c "It felt sooo good"
            m.c "I bet you were fantasizing that it was a real cock, that some big, hunky guy was fucking you like a girl"
            "[i.c.name] blushes and giggles. [m.c.name], her blue eyes sparkling, strokes his cheek and smiles. Her thumb
                sneaks into his mouth and he sucks it eagerly"
            m.c "You looked so pretty, so hot"
            "He strokes her thick thigh and licks his lips"
            i.c "Thank you for making me a pretty little anal whore. Would you like to sit on my face so I can thank
                you properly"
            "With a growl, [m.c.name] climbs on the bed and tears off her knickers. She straddles his head and lowers
                her aroused pussy onto his face. He kisses the ragged edges of her labia, wet with her arousal, as his nose
                burrows into her sparsely covered pussy"
            "He starts to lap her gently, his tongue seeking out her little pleasure button in her so-wet slit. One of his
                hands smooths across her white, fleshy thigh to grab her huge bum kneads it gently. His other hand reaches up
                and grabs her breast, squeezing the succulent mountain of flesh"
            "[m.c.name] throws her head back and groans as his tongue flicks across her clit. He\'s crushed between her thick thighs as
                she grinds herself onto his face. She really is wet and her juices coat his nose and chin as he tries to breathe as
                she rides him"
            "She\'s so turned on and it only takes a couple of minutes before she gasps and shudders as a huge orgasm rips through her
                body, her legs and buttocks twitching uncontrollably. Just as he thinks he\'s about to suffocate, she collapses onto the
                bed beside him, breathing heavily"
            "They rest for a few minutes. He grabs some tissues from a box by the bed and starts cleaning himself up. She turns to him,
                face flushed, eyes shining"
            m.c "I love our photo sessions [i.oname]. You\'re so good at this"
            i.c "Being [i.oname] for you [m.c.name] turns me on so much"
            "She snuggles into his neck, her arm across his slender body as she pulls him against her. They doze, tired
                but happy"

            "He wakes to her stroking his cheek. He meets he smiling eyes"
            m.c "You look so lovely, so perfect as a girl [i.oname]. Why don\'t you try being a girl all the time?"
            "He tidies a strand of her hair behind her ear"
            i.c "I\'m not ready for that [m.c.name]. I\'ll admit dressing as a girl is exciting but I think my
                friends and family would be appalled and, at the end of the day, I\'m a guy who likes girls"
            m.c "Have you ever had sex with a guy?"
            "[i.c.name] frowns"
            i.c "No! I\'m not into guys"
            m.c "You don\'t know until you try it"
            "[m.c.name] smirks at him, her eyes twinkling as she strokes his chest. Her hand slowly inching downwards until she
                cups his balls"
            m.c "You loved having that big, thick toy in your mouth. Wouldn\'t you like so suck on a real cock? Having
                a nice big man cum in your mouth would look so hot and you\'d enjoy it so much"
            "Despite himself, he feels himself getting hard. [m.c.name] grasps his cock and starts to wank him slowly"
            i.c "I\'m straight [m.c.name]! There\'s no way I\'d go with a guy"
            m.c "Part of you seems to like the idea"
            "With a grin she slides on top of him. The thought of [i.oname] having sex with a man has obviously got her
                excited and she guides his penis between her legs"
            "Her eyes flicker as she mounts him, her big body pinning him to the bed"
            "He gives a little moan and smooths his hands over her big soft buttocks, squeezing her gently, before grabbing her tits and
                using his thumbs to tease her big nipples"
            "She rides him slowly. Their sex has been urgent, desperate up to now and having her fuck him slowly
                like this adds another delicious dimension to their love-making"
            "He\'s so aroused as her warm, moist vagina caresses his cock. Being underneath her feels so right. She looks like a
                goddess with her flushed, pretty face and big, bounteous body bouncing deliciously as she pushes him deep inside her"
            i.c "You\'re so beautiful [m.c.name]. I\'m such a lucky guy"
            m.c "Mmm. Remember you\'re [i.oname]. I want you to always be a girl when you\'re with me, made up nicely and wearing
                pretty, girly clothes"
            "He groans at her words. The idea is so deviant, so tempting"
            "She increases the pace gradually. He matches her thrusts and they are soon grunting and gasping as their passion rises. She\'s
                riding him hard and he pushes into her as she impales herself on him, his nails digging into her buttocks, urging her on"
            "Eyes shut, he tries to hold himself back for her but having his cock deep in her warm, welcoming body is so pleasurable, he
                soon starts to twitch, ramming himself into her as he cums hard again, writhing underneath her"
            "As his body spasms, it drives [m.c.name] to her climax. She lets out a series of little moans before groaning loudly, her eyes rolling back
                in her head and she almost passes out, slumping forward onto him"
            "They lie together panting"

            "She grabs a tissue and rolls off him, heading to the toilet. He relaxes on the bed, drained. After a few seconds, he cleans
                himself up, takes off his tights and camisole and dresses in his jeans and teeshirt once again. He\'s removing his
                make up when [m.c.name] gets back"
            "She starts getting dressed. Despite the pervy things they\'ve been doing, he feels closer to [m.c.name], comfortable in her
                presence. They work well together and the sex is fabulous"
            m.c "I\'ll load up the pics and video tonight. They will be sensational!"
            "She stands behind him as he rubs his lipstick off with a tissue"
            i.c "You always make me look so pretty and so naughty [m.c.name]. My fans will love them"
            "She strokes his head, smiling and caressing his ear"
            m.c "Will you come as [i.oname] next time?"
            "He stands up and holds her around her thick waist"
            i.c "If that\'s what you want"
            "She hugs him back, her mesmerising blue eyes happy"
            m.c "You want it too [i.c.name]. Admit you love being [i.oname]"
            i.c "I do. I love being a pretty girl for you"
            m.c "Why don\'t you take some girly clothes to try on?"

            python:
                for item in item_lookup:
                    if item.name == "Girly Clothes from Maki":
                        i.add_item(item)

            "She helps him to pick out an outfit. It\'s skimpy and slutty and he knows he\'ll love wearing it"
            m.c "Mmm. I know you don\'t like the idea of being with guys but just think about it. I can always set up a little shoot"
            "He gulps and lowers his eyes. He nods slowly. They have a final kiss before he leaves"

            $ i.loathing += 4
            $ i.libido = i.dec_value(i.libido, 4)
            $ m.level += 1
            $ m.countdown += 1
            # Set timer (increased at end of day)
    elif m.level == 4:
        "The traffic on his OnlyFans site has gone wild. There\'s a lot of appreciaton out there for [i.oname] as well
            as a lot of lust"
        # Message window
        call phone_start(0) # blue phone
        $ phone_too = "Maki"

        # this brings up the message, first slot is the name, and second is the content
        # notice how it has _start at the end, the first one is special as there are no delays before it. use this for the first message
        # first param is the avatar (see bPhone.rpy for these)
        # second param is the of who sent the message (me would be the person who owns the phone)
        # third param is the message
        # same format for message_start and message
        # Need to work out how to do emojis

        call message_start("makiA", m.c.name, "Have you looked at your site [i.oname]? Your public love you!")
        call message_reply("Yes. They do really like me being so naughty")
        call message("makiA", m.c.name, "You look so hot!")
        call message("makiA", m.c.name, "It makes me all excited watching you push that big toy in your boy-pussy")
        call message("makiA", m.c.name, "Wanna do some more shots? We can make some exclusive content that people pay a bit extra for. We\'ll make a fortune")
        call message_reply("Err... Yeah! Sounds good. I\'ll come round today")
        call message("makiA", m.c.name, "I hope you\'re remembering your promise...")
        call message_reply("Of course. I\'ll be all dressed up and ready for action")
        call message("makiA", m.c.name, "Ooo. Can\'t wait!")

        call phone_end(0)
        # Normal window
        # show i dress
        "After showering and checking his body for any stray hair, he shaves carefully, making his skin as smooth as possible.
            Next, he puts on his make up. He\'s been practicing and his eye-liner, lipstick and foundation are perfect.
            After squeezing into a tight pink blouse and short pink and white checked skirt, he combs his hair and puts on earrings and his nose-ring"
        "He pouts at the pretty girl in the mirror. He feels so good, so deviant. He grabs his sunglasses and sneaks out of
            his flat. Fortunately none of his flatmates are around. He really does not want them to know about [i.oname]"
        "Hoping his helmet doesn\'t mess up his hair too much, he jumps on his scooter and goes to [m.c.name]\'s house"
        # scene maki's house
        scene m_house
        show screen control_bar(m)

        "He hops off his scooter, takes off his helmet and spends a couple of minutes tidying his hair. [m.c.name] opens
            the door with a big smile on her face. She looks gorgeous in a tight, green dress that hugs her generous curves"
        show i fem at right
        show m green at left
        i.c "Hi [m.c.name]"
        m.c "Wow! You're so lovely as [i.oname]. We need to hurry up and do those photos. I\'m not going to be able to keep my
            hands off you for long"
        "She grins and they hug tightly. All of a sudden they are kissing hard, his erection pressing into her big, soft
            tummy. He nuzzles into her neck, kissing her ear as he gropes her big bum"
        i.c "I want you so much"
        "Her eyes flicker with lust"
        m.c "Mmm. But we can't. Not yet. I\'ve said you\'re going to do a private show in an hour and you need to learn your lines"
        "He smiles, hugging her round her thick waist"
        i.c "My lines? I thought I had a non-speaking part"
        "She giggles"
        m.c "Not this time. Come on, let's get started"
        "They walk downstairs hand in hand. He\'s intrigued as to what she has in store"
        scene m_basement
        show i fem at right
        show m green at left
        "There\'s a bed set up in front of the camera with four toys on the pillow, including the
            silver vibrator and purple toy [i.c.name] played with before. She\'s added a thicker pink
            toy that [i.c.name] thinks looks far too big for him and a realistic looking cock with balls"
        i.c "These look nice"
        "He sits on the bed, hooking his hair behind his ear and stroking the fake penis"
        m.c "Would you like to wear this?"
        "She holds out a bra with the small cups filled with gel"
        i.c "Oh yes. I\'d love to look like a proper girl"
        m.c "Put it under your blouse and it will give you a nice feminine shape"
        "He smiles and takes off his blouse. She helps him put on the bra and adjusts it before he puts his blouse back on again.
            Looking down, he admires his fake boobs stretching the tight top. They look perky and so sexy"
        m.c "Why don\'t you look in the mirror [i.oname]?"
        "He goes over to the mirror to enjoy his new shape. Pulling back his shoulders, he turns to one side then the other, smoothing
            his palms over his new curves, his eyes sparkling with excitement"
        i.c "I look so good. So feminine. So girly"
        "She stands behind him, grinning, her hands slip around his waist"
        m.c "It won\'t take us long to make enough money for a boob job [i.oname]. We could always plump up your bum too"
        i.c "Surgery seems a big step [m.c.name]. I, I don\'t think I\'m ready for that"
        "She kisses his shoulder as he frowns"
        m.c "It\'s only a minor operation and you so love being a girl [i.oname]"
        i.c "There\'d be no going back. I\'d have to tell my parents and my friends. They might hate me, reject me"
        "She cuddles him from behind, squeezing him against her soft body"
        m.c "I\'m sure your true friends would accept the new you. Just think how good you\'ll feel with some nice A or B cup
            boobs"
        "She stokes her fingers between his legs. He\'s so big and hard"
        i.c "It\'d feel so good. It\'s just such a big change for me"
        m.c "Why don\'t we see what your fans think of your new shape?"
        "He smiles and nods before climbing on the bed. She gets behind the camera as he shakes back his hair and arches his back
            once more. The perfect little femboy with his long smooth legs, gentle curves and pretty, innocent face"
        "She hands him a piece of paper"
        m.c "I\'ve put together a little script. You don\'t have to follow it word for word but try to memorise the main points"
        i.c "It\'s very rude"
        "He giggles"
        m.c "It\'s meant to be. I\'m sure [i.oname] loves being naughty and slutty"
        i.c "Mmm. She does. Really slutty"
        "[m.c.name] spends some time setting up the cameras and making sure the lighting is good and clear while [i.c.name] learns his lines"
        m.c "Ok. Two minutes to go. Ready?"
        i.c "Yes. Let\'s get going"
        "He grins broadly and kneels on the bed as [m.c.name] counts down. She snaps her fingers and starts the video with a close-up of [i.c.name]\'s
            face. He starts speaking in a soft, high feminine voice"
        i.c "Hello everyone, welcome to my private show. Thank you all for joining and I hope you enjoy yourself"
        i.c "It\'s so exciting having all you guys watching me. I hope your cocks are going to get all big and hard at the thought of fucking
            my pretty little mouth and tight little boy pussy"
        "He flutters his eyelashes and picks up the realistic looking dildo, stroking it against his cheek"
        i.c "I\'ve never sucked a cock but I think it would be so lovely. I do want to become an expert cock-sucker so I need to practice"
        "He licks slowly round the tip of the dildo, his eyes half-shut before taking it in his mouth. He sucks it slowly, gradually
            pushing it deeper and deeper until it's right at the back of his throat, making his eyes water slightly"
        "After a couple of minutes sucking noisily, he pulls it out. It's glistening with his saliva"
        i.c "Mmm. Do you think that would turn you on having me suck you like that? I wouldn\'t mind if you grabbed my hair and fucked
            my face so long as you weren\'t too rough"
        "With a gasp, he put the cock in his mouth once more, relaxing his throat to take it so deep"
        i.c "Ooo. This is getting me so excited"
        "As the camera pulls back, he flicks his hair behind his ear and takes off his skirt. His pink frilly knickers are straining against his
            huge erection. He smiles naughtily"
        i.c "Just look at how excited my girl-cock is thinking about giving you a blow-job"
        "He untangles his panties and pulls them off. Picking up the vibrator, he turns it on and holds it against his penis, letting out a little
            groan as the humming toy stimulates him"
        i.c "I\'d like to do this with you. Getting you all excited before you take me. Oh yes!"
        "He throws his head back and writhes on the bed. Picking up the fake penis, he puts it in his mouth once more. [m.c.name] gives him
            the thumbs up from behind the camera. She\'s grinning broadly, enjoying him being so filthy and slutty"
        "Dropping the vibrator and taking the purple toy, he squirts some lube on the end before turning his back to the camera raising himself on his knees. He wriggles
            his cute little bottom, his face serious as he looks back at the camera"
        i.c "I\'m desperate to have a nice big guy use my tight little boy-pussy. I like my toys but I really want to have a real cock thrusting into me hard. It
            would be so exciting. So lovely"
        "With one hand he pulls his buttock to one side, giving the camera a good view of his smooth, hairless crack. His other hand pushes the smooth tip of
            the dildo into his anus, probing it gently"
        "After a few seconds, he presses the tip harder against his back entrance. The thick toy squeezes past the tight little ring and,
            with a groan, he starts easing it deep inside him, his eyes shut as he enjoys himself"
        i.c "Mmm. It hurts a little but I like that. I want to feel used, to be a little sore after you\'ve fucked me and have your cum dripping out of my boy-pussy"
        "[m.c.name] zooms in to catch every detail of the thick dildo stretching his anus as he fucks himself, his balls hanging down between his slender, slightly spread
            legs and his rock hard cock"
        "She pans round to his pretty face, his eyes half-shut, his pretty mouth open and breathing heavily"
        "He pops the big fake cock between his lips once more, sucking greedily as he pumps the thick toy into his anus"
        "After a couple of minutes he rolls onto his back. Still with the toy deep inside him, he holds the vibrator against his cock
            once more as he continues to bugger himself with the other dildo"
        "[m.c.name] hand is between her legs, rubbing herself as she enjoys his wanton display"
        "His head thrown back, he\'s gasping for air, his eyes screwed tight shut as his climax approaches. It only takes a few seconds
            before he lets out a long groan, his hips jerking as he spurts ropes of cum onto his pretty pink blouse"
        "He lies still, eventually opening his eyes and grinning naughtily at the camera. He scoops up a blob of his gooey cum with his finger. Grinning,
            he pops his finger in his mouth and swallows it down"



        "[m.c.name] and [i.c.name] have sex after more explicit shots"
        # Shorter version of 2
    elif m.level == 5:
        # P has sex with two guys
        # M and P spend time together afterwards
        # Reduce lib, increase loath
        "[i.c.name] is used by two guys before sex with [m.c.name]"
        $ m.level += 1
    elif m.level == 6:
        # P and M review pics and have sex
        $ m.level += 1
    else: #m.level = 7
        "Random explicit scene (Solo, Sex with guy, Sex with guys)"

    return

    label maki_ans_1:
        m.c "I suppose it will keep interest in your sites if we refresh the pictures but something a little more
            spicy would really increase your income"
        i.c "It doesn\'t feel right. I\'m a boy and I don\'t want to be seen as a girl"
        show m sultry at left
        m.c "Maybe you just need a little more practice to get comfortable with the idea"
        scene m_basement
        show i fem at right
        show m at left
        "They go inside. [m.c.name] carefully turns [i.c.name] into [i.oname]. He poses once more as a girl, smiling coyly
            at the camera, throwing his head back and laughing, sucking his finger sensually. He\'s become a very sensual femboy
            model"
        "[m.c.name] encourages him, delighting as he embraces his feminine side. After perhaps half an hour of photos in various
            outfits [m.c.name] declares she has enough pictures. Before he changes back to being a boy, she hugs and kisses him. They hold
            the kiss just a little bit too long"
        m.c "You were great [i.oname]! If you show a little more next time we'll have money flowing in"
        i.c "You really think so? People do seem to like the pictures of [i.oname]"
        show m sultry at left
        m.c "That\'s because you\'re so hot"
        "He changes and goes home, at one level ashamed at posing as a girl again but he knows [m.c.name] will do a great job,
            his fans will really enjoy the pictures and he\'ll get money to pay [k.c.name]\'s rent"

        $ i.loathing += 2
        $ i.libido =i.dec_value(i.libido, 2)

        return

    label maki_ans_2:
        m.c "Your last set was fabulous. Sexy and beautiful. Maybe we could try a couple more outfits"
        i.c "Would I be stripping again?"
        show m sultry at left
        m.c "Of course. Your fans want to see your lovely body. It\'s not going to be a problem is it?"
        "[i.c.name] lowers his eyes and shakes his head. He wonders why he\'s getting a little hard"
        scene m_basement
        show i fem at right
        show m at left
        "They go down to the basement. [m.c.name] carefully turns [i.c.name] into [i.oname]. He poses once more as a girl, smiling coyly
            at the camera, throwing his head back and laughing, sucking his finger sensually. He\'s become a very sensual femboy
            model"
        "[m.c.name] encourages him, delighting as he embraces his feminine side. After perhaps half an hour of photos in various
            outfits [m.c.name] declares she has enough pictures. Before he changes back to being a boy, she hugs and kisses him. They hold
            the kiss just a little bit too long"
        m.c "You were great [i.oname]! If you show a little more next time we'll have money flowing in"
        i.c "You really think so? People do seem to like the pictures of [i.oname]"
        show m sultry at left
        m.c "That\'s because you\'re so hot"
        "He changes and goes home, at one level ashamed at posing as a girl again but he knows [m.c.name] will do a great job,
            his fans will really enjoy the pictures and he\'ll get money to pay [k.c.name]\'s rent"

        # Set trigger to collect additional money
        # Self-loathing check
        $ i.loathing += 3
        $ i.libido =i.dec_value(i.libido, 3)

        return

    label maki_leave:
        i.c "I\'m still coming to terms with what happened last time"
        m.c "Well I think you enjoyed yourself last time"
        i.c "Yes, er, no. I don\'t know. Look, I need to think some more about it"
        m.c "OK. Don\'t think too long. We don\'t want your fans to stop subscribing"
        "He nods and slinks away"
        $ self.libido += 3

        return
