label AN_start:

    $ renpy.movie_cutscene(AN_movie_intro)

    body john AN_sayaka underwear
    body sayaka AN_john uniform

    pause 2
    play music AN_bgm_welcome_to_this_world fadein 4
    pause 1

    "Divine punishment."
    "Ever heard of it? It's the kind of thing that happens when you've fucked up really bad."
    "Some say it doesn't exist, others do. But can you really blame anyone for thinking how they do? After all, you've either experienced it, or you haven't."
    "I don't really believe in it personally, but exactly what else could have happened?"
    "I don't know what I am being punished for. I don't even know if I am the one being punished. The only thing I know is that something divine happened that day."
    "That day was at the start of our final school year, our debut as seniors on Tina Koya High."
    "The 8th of August is the date where it all began."

    stop music fadeout 2
    pause 1.5

    title "8th of August" "The first day"

    $ renpy.sound.set_volume(0.25)
    play sound [AN_sfx_alarm] loop
    pause 2

    think "Hmm..."

    pause 1

    think "An alarm?"
    think "Did I set an alarm yesterday? Mom totally did for me, didn't she?"

    scene bg sayaka bedroom day
    $ screenfilter.blur = 20
    show black
    hide black with dissolve

    "I opened my eyes with hesitation. I was still tired, but surprisingly enough I didn't feel like complete crap after staying up too late."
    "I tried finding my phone to my left but..."
    think "Has there... always been a wall on my left-hand side?"

    $ screenfilter.blur = 10

    think "Why are my bedsheets... pink...?"

    $ screenfilter.blur = 0

    think "Wait, where the hell am I?"

    $ renpy.sound.set_volume(1)

    "The alarm was still ringing, now with full volume, and as I sat myself up in the bed I was in, - which clearly wasn't mine either, - I started to panic just a little."
    john "{size=-5}Did I drink or something yesterd-{/size}"

    with hpunch
    $ renpy.sound.set_volume(0.1)

    think "Wh- Is that me speaking?"
    john "One, two, three... Why do I..."
    "I was thoroughly confused by this point."
    john "{size=-3}H- Hello? Is there anyone else here?{/size}"
    think "Okay this is freaky. This isn't my voice. And those aren't my hands... Or my hair...!"
    "I rushed out of bed."

    show bg sayaka bedroom day:
        ease 0.5 zoom 2.0 xalign 0.8

    think "A mirror. Mirror. Come on, there has to be a mirror in here!"

    show bg sayaka bedroom day:
        ease 0.5 zoom 2.0 xalign 0.1

    "I opened a closet hoping to find one in there."

    scene AN_bg sayaka room dressing room with dissolve
    outfit john underwear
    outfit AN_sayaka underwear
    show AN_sayaka b_28 at offscreenleft, faceright:
        alpha 0.0
    show john b_28 at centerright, faceleft:
        alpha 0.0

    "Luckily, there was a large mirror inside."
    "One look confirmed my suspicion, but somehow also made it worse."

    show john b_28 at center:
        ease 0.75 alpha 1.0
    show AN_sayaka b_28 at left:
        ease 0.75 alpha 0.65
    with ease

    john "Sayaka?!"

    show john b_27
    show AN_sayaka b_27

    john "I'm Sayaka?!"

    show john b_22
    show AN_sayaka b_22

    john "{size=-5}What the fuck is happening... I'm John, right?{/size}"

    show john b_17
    show AN_sayaka b_17

    think "Okay, assess the situation."
    think "I'm John Davis. Not Sayaka. For some reason I must have become her and am now in her room."
    "That's right. This wasn't a dream. If it were I would have woken up from this nightmare a just earlier."
    think "...How the hell does someone just suddenly {q}become{/q} someone else..."
    "Sayaka was the complete arch nemesis of one of my closest friends, Katrina, and heavily bullied another one of my friends, Kyoko."

    show john b_22
    show AN_sayaka b_22

    "Just about the worst person to somehow magically become..."

    show john b_3
    show AN_sayaka b_3

    think "But..."

    show john b_0
    show AN_sayaka b_0

    "I kept staring into the mirror..."
    think "I'm... Sayaka..."

    show john b_1 blush
    show AN_sayaka b_1 blush

    "As I began to understand that this wasn't a dream and that I was suddenly in full control of one of the best looking girls in school, I fully blushed with her face."

    scene bg sayaka bedroom day with dissolve
    $ renpy.sound.set_volume(1)
    play sound sfx_lockpick
    show john a_17 blush at left, faceright:
        alpha 0.0
    show john at centerright with ease:
        ease 0.5 alpha 1.0

    "But I pushed that aside for later. My - or, Sayaka's alarm - had been ringing like crazy. And unless everything changed, Tina Koya had the first school day of my senior year today."
    "Sayaka was also a senior starting today."

    show john a_6 at faceleft

    think "Come to think of it, if I'm her, is she me?"
    think "Please tell me she's not me..."

    show john b_5

    "If she really was turned into me, then I should talk to her first thing in the morning. Which means going to school as early as I can."

    show john b_0:
        ease 1 xpos 0.65

    "I picked up the phone that had been buzzing and saw that it was unusually early. More than an hour until school starts, actually."

    show john a_21

    john "{size=-5}Jeez, how early does this girl get up...{/size}"

    show john a_13

    "To my disappointment, she had her phone on lock with a code. The simple 1-2-3-4 code didn't work here, so I gave up trying to guess it and put it down."
    think "This confirms that I'm not secretly Sayaka having a mental breakdown who believes she is actually John, right? I would have known her code if I am her."

    scene black with dissolve
    outfit john uniform

    "Thankfully, getting dressed wasn't {i}that{/i} difficult. It appears she had put her school uniform aside for today."

    play sound AN_sfx_clothes1

    john "And, there, we..."

    play sound AN_sfx_clothes2
    scene bg sayaka bedroom day
    show john b_1 at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    extend " go."
    "I had some weird thoughts whenever I happened to touch her boobs. I didn't imagine it to feel the way it did, and it also felt a bit like overstepping some boundaries."

    show john b_3 at faceright

    "Either way, I didn't want to bother having to consider her hair or make-up (which she used a-plenty), or changing her underwear..."

    show john a_24

    think "Even though I wouldn't mind taking a proper pea-"

    show john a_3

    extend " Oh for crying out loud, focus! This isn't the time to be fascinated being stuck as one of the most horrible people on earth!"

    scene black with dissolve
    play sound sfx_door_close
    scene AN_bg sayaka hallway day
    show john a_6 at left, faceright:
        ease 1 xpos 0.5
    with dissolve

    "As I got out of her room, the next hurdle began to be apparent."

    show john a_13:
        faceleft
        pause 0.5
        faceright

    think "Where exactly do I go...?"

    show AN_bg sayaka hallway day behind john:
        ease 0.75 zoom 2.0 xalign 0.4
    show john at Position(pos=(0.40, 1.0), anchor=(0.5, 1.0)), faceleft with ease:
        easein 0.25 yanchor 0.98
        easein 0.25 yanchor 0.96
    show john at Position(pos=(0.40, 1.0), anchor=(0.5, 0.96)), faceleft

    "This house looked absolutely enormous. It was hard to tell, but I had to be a story up since I saw stairs leading down."

    scene black with dissolve
    scene bg sadie bathroom day
    show john b_11 at center, faceright:
        alpha 0.0
    with dissolve
    play sound sfx_door_open
    show john at center:
        ease 0.5 alpha 1.0

    "After looking around a bit more, I managed to find the bathroom."

    show john at faceleft

    john "Even her bathroom is massive..."

    show john b_1 at centerright, faceright with ease

    "I thought that I might as well brush my teeth. It felt like something I should do right now."
    "I didn't like going anywhere with a bad feeling in my mouth, so I grabbed the only pink toothbrush which I assumed was hers and shrubbed away."

    show john b_25

    think "Actually, thinking about it, I'm using freaking Sayaka's toothbrush..."
    think "If I weren't her then I would probably puke."

    scene black with dissolve
    scene bg sayaka kitchen day
    show AN_saki a_0 at left, faceleft
    show john b_5 at right:
        alpha 0.0
    with dissolve
    show john at Position(pos=(0.60, 1.0), anchor=(0.5, 1.0)), faceleft with ease:
        ease 0.5 alpha 1.0

    "I found my way to the kitchen after going through the, once again, massive living room area and found a woman with pink hair, just like Sayaka, standing there."

    show john b_2

    john "Uhm... Good morning."

    show AN_saki a_4 at faceright
    pause 1
    show john b_7
    show AN_saki a_9

    AN_saki "You're early. Grab some cereal if you're hungry, I don't have time to make you anything."
    john "Uh... Okay."
    "This had to be her mom. Or her sister if she had one, but I doubted that she would be a sister after what she just said."
    AN_saki "I'm going to be late today again. You know where the cup-noodles are."








































    placeholder
