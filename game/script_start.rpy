label initgame:
    $ valid_name = False
    while not valid_name:
        $ player_name = renpy.input("Please enter your characters name (at least three characters)", default = "Hari")
        $ player_name = player_name.strip()  # Remove leading/trailing spaces
        if player_name.isalpha() and len(player_name) >= 3:
            $ valid_name = True
        else:
            "Please enter a valid name with at least three alphabetic characters."

    $ i.c.name = player_name
    return

label intro:
    # User's appearance
    show i at right
    "[i.c.name] is a [i.description]. He wears [i.top], [i.trousers] and [i.shoes]. His hair is [i.hair]"
    # User's college life
    "[i.c.name] studies archaeology at College Number 12. He is quite a lazy student but finds the work
    enjoyable and easy"
    # User's job delivering pizzas
    "On Tuesdays and Thursdays, [i.c.name] has a job delivering pizzas so he can make some extra cash"
    # User's beautiful girlfriend Kasumi
    show k at left
    "[i.c.name] has a girlfriend, [k.c.name]. She is a [k.description] who is [k.attitude]. She is [k.body]"
    # User's relationship with Kasumi
    "It is the first serious relationship for [k.c.name] and [i.c.name] and they are so in love"
    # User's happy life.
    "Everything is going well for [i.c.name]. He has an interesting course, enough money to live on and
        a beautiful girlfriend"
    return

label game_start:
    scene bg party
    # User has encounter with Maki
    "[i.c.name] and [k.c.name] are at a garden party. It\'s a sunny day and everyone is having a good time"
    show m sultry at right
    "They are holding hands and occasionally gazing into each other\'s eyes. A girl who [i.c.name] hasn\'t seen before
    approaches them. She is a [m.description]"
    show k happy at left
    k.c "Hi [m.c.name]! It\'s a lovely day for a party. This my boyfriend, [i.c.name]"
    hide k
    show m sultry at right
    m.c "Hi [k.c.name]. So this is your gorgeous new guy?"
    "She looks at [i.c.name], her blue eyes smiling. There\'s something fascinating about her that draws him in, her wide smile,
        her beautiful hair and her big, heavy body, encased in her [m.dress]"
    i.c "Err, hello.  Nice to meet you [m.c.name]"
    show m happy at right
    "She gives him a half-smile, noticing him checking out her breasts. His eyes snap back to her face."
    m.c "Well [k.c.name] is a lucky girl going out with a pretty boy like you. I expect I will see you around"
    "She walks away slowly, giving [i.c.name] a good view of her big, sumptuous rump"
    hide m
    i.c "She\'s very, er, confident"
    show k cross at left
    k.c "Yes. She certainly seems to be popular with boys too"
    "[k.c.name] frowns and slaps his arm"
    k.c "You certainly seemed to like her. You couldn't take your eyes off her"
    i.c "I\'m sorry [k.c.name]. You know I only have eyes for you"
    hide k
    "They make up quickly and are soon mooning at each other again. The party lasts until mid afternoon before people
    begin to drift away. A couple of times, [i.c.name] catches [m.c.name]\'s eye and her naughty smile causes him to blush
    slightly and look away"
    "Eventually [i.c.name] and [k.c.name] head back to her flat"

    scene bg ks_flat
    "They stumble into the flat in each other\'s arms, kissing gently. They have just started sleeping together and they are both
        looking forward to some fun. It\'s so exciting for [i.c.name] having [k.c.name]'s slender, warm body in his arms. [k.c.name]\'s
        mobile rings. [k.c.name] untangles herself from [i.c.name] and picks up, frowning"
    show k sad at left
    k.c "Oh no! This is awful"
    "She puts her hand to her mouth, her big eyes open wide. The person on the other end jabbers away."
    k.c "OK, OK. Do you want me to come home?"
    "There\'s more excited burbling from the phone. [k.c.name] hangs up, rubbing her forehead"
    i.c "What\'s the matter?"
    k.c "My dad has lost a lot of money in a business deal. We're broke"

    scene bg ks_sitting_room
    "She walks through to the sitting room and flops on the sofa, tears in her eyes"
    k.c "I\'m going to have to leave [i.c.name]. I can\'t affort to stay"
    i.c "I can help you [k.c.name]. I have some money and I\'m earning good money at the pizza shop"

    show k at left
    show i at right
    k.c "That\'s very sweet of you but my rent and bills are £450 a month"
    i.c "I\'m sure I could get close to that [k.c.name]. I have a bit of money saved too"
    k.c "Really? But I couldn\'t. You work so hard for it. I don\'t want to live off you"
    i.c "I love you [k.c.name]. If it means you\'ll stay then I\'ll do whatever it takes"

    show k happy at left
    k.c "You really are a wonderful boyfriend"
    hide k
    hide i
    "They kiss, slowly, gently. Eventually their passion starts to rise. [i.c.name] stands up and
        helps [k.c.name] to her feet. They walk to the bedroom where they undress and get into bed. He
        is slow and gentle with her, stroking her soft skin, caressing her lovely pert breasts and rubbing
        his fingers slowly between her legs"
    "Eventually he mounts her. She hugs him close, her big brown eyes fixed on his, gazing at her hero, her saviour.
        They make love, he carefully and tenderly enters her and their bodies move together gracefully. He cums
        first, groaning as the climax hits him. This drives her over the edge and, with a high-pitched squeak she quivers
        beneath him"

    scene bg ks_bedroom
    "She doesn\'t let him go that night. [i.c.name] is tired after his exertions but he sleeps badly. [m.c.name]\'s
    enigmatic smile fills his dreams along with the image of her full figure straining at her dress"
    "He wakes confused. He has the perfect girlfriend. Why does the thought of [m.c.name] bother him so much?"
    "Rolling over in bed, he finds [k.c.name] is gone and there is a note on the pillow"

    call screen note_screen("Going to college to see if they can help me out with some cash. Love you so much, K")

    return
