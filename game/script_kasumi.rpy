label choose_Kasumi:
    # Kasumi becomes more and more dominant as Player becomes submissive. Main attributes Femboy, Anal Whore, Pain Slut
    # Player options: Cuddle, have sex, submit, worship body, lick feet
    # Kasumi options: Comfort, Sexual dominance, pegging, feminisation, CBT, scratching, biting, big dildo
    # Need to keep track of Kasumi's money and pay her rent
    # Kasumi initially can comfort Player and reduce self-loathing. Her increased dominance can have the opposite effect
    # Player owns up to Kasumi when he wants to become a femboy
    show screen control_bar(k)
    $ k.gapcnt = k.gap

    if k.level == -1:
        # Intro to P and K having romantic time together
        scene ik_walk
        show i at right
        show k at left
        "[i.c.name] meets [k.c.name] on the campus and they go for a walk by the river"
        "It\'s a lovely day and they stroll together hand in hand. [k.c.name] looks so pretty and
            she flirts and giggles as they enjoy each other\'s company"
        k.c "I\'m so lucky having such a handsome boyfriend who helps me out so much!"
        i.c "And I\'m so lucky to be going out with such a beautiful girl"
        "He hugs her and they kiss, slowly, lovingly"
        i.c "We could go back to your place and do some studying"
        "[k.c.name] smiles"
        k.c "And what sort of studying did you have in mind?"
        i.c "I have to learn to appreciate the female form for my course"
        k.c "We\'d better get on with it then"
        scene bg ks_bedroom
        show k happy at left
        show i happy at right
        "Laughing they walk to [k.c.name]\'s flat. Hurrying through the door they head to the bedroom and quickly
            fall onto the bed together. They hug and kiss, their cheerfulness turning quickly to passion as they
            hurriedly undress one another"
        "He hugs her to him, enjoying the feel of her slender, warm naked body against him, her firm breasts pressing
            into his chest. She strokes his bottom, massaging him gently, encouraging him to love her"
        "She lies back on the bed, spreading her legs, offering herself to him. He\'s so turned on, looking down at this
            beautiful girl, her pretty face flushed with desire for him, her long, black hair tangling over the bed"
        "He tenderley places his hand on her small bush, his fingers stroking through her sparse, wiry hair and rubs
            her labia with his thumb. She\'s so wet"
        k.c "Love me [i.c.name]"
        "She strokes his cock. He\'s hard as a rock"
        i.c "Just try and stop me"
        "He carefully lies on top of her and [k.c.name] wraps her arms around him as he guides himself into her. He\'s gentle at first,
            feeling himself stretch her. They are both breathing hard and they kiss passionately before he starts riding her a little harder"
        "They both start to moan and groan. His pace gets faster and faster and she writhes underneath him, her hands clamped on his buttocks
            pulling him into her. He tries to hold back as her body starts to quiver, her face flushed as her moans become lounder and more urgent"
        "Eventually her body spasms and she cries out as her orgasm sweeps through her body. He cums at the same time, letting himself go and groaning
            loudly as he empties himself inside her"
        "As they rest, he can feel her vagina twitching against his softening cock. Eventually he rolls off her"
        i.c "That was wonderful [k.c.name]"
        k.c "Mmm. I love having you on top of me, in me. My handsome guardian angel"
        "They kiss once more before cuddling up and dozing in each other\'s arms"
        k.c "You\'d better go [i.c.name]. I really need to get up early and I won\'t get any sleep with you here"
        "[i.c.name] smiles"
        i.c "I\'d hope not"
        "Sighing, he gets up and starts to get dressed. She watches him, admiring his slender body. They have a final big hug and extended kiss
            before he heads back to his flat"
        $ k.level += 1
    elif k.level == 0:
        # Shorter version
        # K asks P to visit M to piok up ring
        scene bg ks_bedroom
        show k happy at left
        show i happy at right
        "Once again [i.c.name] and [k.c.name] rush back from college, burst into [k.c.name]\'s flat and tumble into the bedroom"
        "As they hurry to undress, [k.c.name] kneels down in front of [i.c.name] and, taking his erect cock in her hand,
            kisses it firmly before stroking it with her cheek. [i.c.name] groans"
        i.c "That feels so good"
        k.c "A little treat for my wonderful boyfriend"
        "She licks him around the tip before taking the head in her mouth and sucking him slowly. The sensation
            is so wonderful and [i.c.name] throws his head back and moans as he strokes her hair"
        "With a little pop, [k.c.name] releases him"
        k.c "All ready for action?"
        i.c "God, yes!"
        "They get on the bed and he quickly mounts her. She grabs his bum, pulling him inside her. He penetrates her slowly, with long, deep
            thrusts as she starts to whimper, her excitement rising"
        "After they\'ve been making love for a few minutes, they\'re both so turned on and he\'s having to hold himself back. He wants to try something different
            before he cums"
        i.c "Can we do it from behind?"
        k.c "Mmm yes! I love the idea of you taking me hard like that"
        "He pulls out, letting her turn onto her hands and knees. Her pussy is glistening with her juices and her labia engorged. It looks so hot and he guides
            his erection into her warm, welcoming sex. She gives a little sigh as he easily pushes in to his full length. She rocks back against him, enjoying having
            his big, hard cock inside her"
        "He\'s soon pumping into her hard, his hips moving faster and faster. She responds, pushing herself onto him. Their moans and groans fill the room. He grabs
            her slender thighs firmly and, with a series of very quick thrusts, pushes himself over the edge. She cums even before him, with a satisfied \'Yessss\!\'"
        "They writhe together as cums inside her for what seems like minutes before collapsing onto the bed and cuddling, breathing heavily. They rest for a few seconds"
        k.c "That was great. You were so masterful"
        "She rubs his nose with her crooked finger"
        "He grins, happy to have satisfied his wonderful girlfriend. They rest for a few minutes"

        # Maybe have Phone ping here

        "Eventually her phone pings and she picks it up, resting on her elbow"
        k.c "Do you remember [m.c.name]. The ginger girl at the party"
        i.c "Err..."
        "She punches him playfully"
        k.c "You remember all right. You couldn\'t take your eyes off her"
        k.c "Anyway, she says she has a present for us. She called it \'something for the happy couple\'"
        i.c "That\'s very nice of her. Does she come from a rich family?"
        k.c "I don\'t know. She always has nice things and tells stories about holidays abroad. I guess she
            must have money from somewhere"
        i.c "Can I see it?"
        k.c "She said to pop round and pick it up but it's on the other side of town and, as you have your scooter and it's
            a present for both of us, I thought you could fetch it. She said she\'s in most afternoons"
        i.c "Sure, just give me her address"
        "[k.c.name] reaches for her phone and messages [i.c.name]"
        k.c "And before you ask, you\'re not getting her number"
        i.c "But I don\'t want to go all the way over there and her not to be in"
        "[k.c.name] frowns"
        k.c "I suppose..."
        "She begrudgingly messages [i.c.name] [m.c.name]\'s number before they have another hug and he has to leave"

        $ k.level += 1
        $ m.level = 0

    elif k.level == 1:
        scene ik_cafe
        show i at right
        show k at left
        "[i.c.name] meets up with [k.c.name] at a cafe near the college and they sit across the table from each other holding hands"
        k.c "[m.c.name] gave me our present"
        "He pulls out the jewellery box from his pocket. [k.c.name]\'s eyes open wide"
        "She takes the box and opens it, admiring the golden pair of rings, hers small, with an intricately carved band and \'D\' engraved on the bezel. His
            is larger and plainer with \'S\' and the band worked to look like links in a chain"
        k.c "Wow!"
        i.c "They must be worth a fair bit. I tried not to take them but [m.c.name] insisted"
        k.c "What are \'S\' and \'D\'?"
        i.c "[m.c.name] said we had to find out"
        "[k.c.name] purses her lips"
        k.c "I can\'t think. Never mind, they are lovely. Let\'s put them on\!"
        "Smiling, they slip them onto their right ring finger. It\'s a real squeeze to get past his finger joint"
        i.c "Mine is quite tight. It will be hard to get off again. Maybe I could get [m.c.name] to adjust it"
        "[k.c.name] frowns playfully"
        k.c "And why would you want to take it off?"
        "He smiles back at her. They kiss. As they leave the cafe, she takes a selfie with him holding their rings
            together in front of the camera. \'True Love\'"
        "The ring feels a little strange on his finger, almost as if it's shrunk slightly and become even tighter. As they
            walk to [k.c.name]\'s flat, he turns several times to admire her. He\'s so lucky to be with [k.c.name]. He\'s glad he can help
            her out with her rent and would do anything for her"
        scene bg ks_bedroom
        show i happy at right
        show k happy at left

        "Back at her place they are soon in bed again, kissing and cuddling. With a cute giggle she slides down his body and
            gives his cock a little peck, making him gasp. Next, she wraps her lovely, long hair around his cock, stroking him
            exquisitely as she grins up at him"
        k.c "Do you like that honey?"
        i.c "It feels wonderful [k.c.name]"
        k.c "I love it when you\'re big and hard and ready to take me"
        "She takes him in her mouth, sucking him slowly, licking the end of his member with her tongue"
        i.c "Oh God [k.c.name]. That\'s so good! It turns me on so much!"
        k.c "Mmm. It turns me on too. I want you in me! Now!"
        "With a big grin, he clambers on top of her. She opens her legs to receive him and they are soon fucking hard, him
            thrusting himself into her, [k.c.name] responding, impaling herself on his cock"
        "After a couple of minutes, he pulls out and helps her turn on her front, he pussy glistening with her excitement as
            he guides his cock into her once more"
        "Their rutting becomes more frenzied, his hips pump into her even harder and faster She braces herself against
            him. They are both panting and groaning. She cums first, screaming as her climax spasms through her body. This
            drives him over the edge and he lets out a long groan as his cock spurts his seed deep inside her"
        "They spoon together as they come down, [i.c.name] cuddling into [k.c.name]/'s back. They are both so happy and content
            that they\'ve found someone to love"

        $ k.countdown = 0
        $ k.level += 1

    elif k.level == 2:
        "[k.c.name] have sex. [k.c.name] is more demanding"
        # Similar to 0
        # Reduce lib and loath
        # P could steal clothes
        # Stays here until timer increases

    elif k.level == 3:
        "[k.c.name] rides [i.c.name] and bites his lip after orgasm"
        # K becomes more demanding, is on top, bites Ps lip
        # Reduce lib and loath but not by so much
        # P could steal clothes
        # P fem check
        # Again waits for timer

    elif k.level == 4:
        "[k.c.name] scratches [i.c.name] hard and bites his shoulder"
        # Sex now optional
        # K scratches and bites P
        # Reduce lib, increase loath
        # P could steal clothes
        # P fem check
        # Maybe enforced recovery time
        # Timer again
        # Could have another level here:Beating and kicking

    elif k.level == 5:
        # Sex now optional
        # K ties up P and tortures him
        # Reduce lib, increase loath
        # Maybe enforced recovery time
        # Not increased until final Maki level
        "[k.c.name] ties [i.c.name] up and tortures him"

    elif k.level == 6:
        "[k.c.name] wants a proper man and finishes with [i.c.name]"
        # K breaks up with P
    return
