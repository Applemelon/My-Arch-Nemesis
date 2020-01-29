label AN_initited:

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

label AN_day_1:

    title "8th of August (Monday)" "The first day - John"

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
    play music bgm_dreams_become_real

    think "Wh- Is that me speaking?"
    john "One, two, three... Why do I..."
    "I was thoroughly confused by this point."
    john "{size=-3}H- Hello? Is there anyone else here?{/size}"
    think "Okay this is freaky. This isn't my voice. And those aren't my hands... Or my hair...!"
    "I rushed out of bed."

    $ renpy.sound.set_volume(0.05)
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

    stop music fadeout 2.5
    show john b_28 at center:
        ease 0.75 alpha 1.0
    show AN_sayaka b_28 at left:
        ease 0.75 alpha 0.65
    with ease

    john "Sayaka?!"

    #SKIP
    show john:
        faceleft
        alpha 1.0
    show AN_sayaka:
        alpha 0.65

    show john b_27
    show AN_sayaka b_27

    john "I'm Sayaka?!"

    show john b_22
    show AN_sayaka b_22

    john "{size=-5}What the fuck is happening... I'm John, right?{/size}"

    play music bgm_covert_affair
    show john b_17
    show AN_sayaka b_17

    think "Okay, assess the situation."
    think "I'm John Davis. Not Sayaka. For some reason I must have become her and am now in her room."
    think "...Somehow..."
    "That's right. This wasn't a dream. If it were I would have woken up from this nightmare just earlier."
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

    #SKIP
    show john:
        alpha 0.0
    show john:
        alpha 1.0

    "Sayaka was also a senior starting today."

    show john a_6 at faceleft

    think "Come to think of it, if I'm her, is she me?"
    think "Please tell me she's not me..."

    show john b_5

    "If she really was turned into me, then I should talk to her first thing in the morning. Which means going to school as early as I can."

    show john b_0:
        ease 1 xpos 0.65

    "I picked up the phone that had been buzzing and saw that it was unusually early. More than an hour until school starts, actually."

    #SKIP
    show john:
        xpos 0.65

    show john a_21

    john "{size=-5}Jeez, how early does this girl get up...{/size}"

    show john a_13

    "To my disappointment, she had her phone on lock with a code. The simple 1-2-3-4 code didn't work here, so I gave up trying to guess it and put it down."
    think "This confirms that I'm not secretly Sayaka having a mental breakdown who believes she is actually John, right? I would have known the code to her phone if I am her."

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
    "The skirt in particular felt... Well, wrong. But it was something I could live with."

    show john b_3 at faceright

    "Either way, I didn't want to bother having to consider her hair or make-up {i}(which she used a-plenty){/i}, or changing her underwear..."

    show john a_24

    think "Even though I wouldn't mind taking a proper peak-"

    show john a_3

    think "Oh for crying out loud, focus! This isn't the time to be fascinated being stuck as one of the most horrible people on earth!"

    scene black with dissolve
    play sound sfx_door_close
    scene AN_bg sayaka hallway day
    show john a_6 at left, faceright:
        ease 1 xpos 0.5
    with dissolve

    "As I got out of her room, the next hurdle began to be apparent."

    #SKIP
    show john:
        xpos 0.5

    show john a_13:
        faceleft
        pause 0.5
        faceright

    think "Where exactly do I go...?"

    #SKIP
    show john:
        faceright

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

    #SKIP
    show john:
        alpha 1.0

    show john at faceleft

    john "Even her bathroom is massive..."

    show john b_1 at centerright, faceright with ease

    "I thought that I might as well brush my teeth. It felt like something I should do right now, it was part of my own morning routine after all."
    "And besides, I didn't like going anywhere with a bad feeling in my mouth, so I grabbed the only pink toothbrush which I assumed was hers and shrubbed away."

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

    "I found my way to the kitchen after going through the, once again massive, living room area and found a woman with pink hair, just like Sayaka, standing there."

    #SKIP
    show john:
        faceleft
        alpha 1.0

    show john b_2

    john "Uhm... Good morning."

    show AN_saki a_4 at faceright
    pause 1
    show john b_7
    show AN_saki a_9

    AN_saki "You're early. Grab some cereal if you're hungry, I don't have time to make you anything."
    john "Uh... Okay."
    "This had to be her mom. Or her sister if she had one, but I doubted that she would be a sister after what she just said."

    show AN_saki a_4

    AN_saki "I'm going to be late today again. You know where the cup-noodles are."

    show AN_saki at offscreenleft, faceleft with ease:
        ease 0.5 alpha 0.0
    play sound sfx_door_close
    pause 0.5
    show john b_4

    "With that, she just left. Without a goodbye, a wave, without anything."
    think "Jeez, I hope she isn't always this cold."

    show john b_13

    "Strangely enough I didn't feel hungry at all. I could probably buy tons of food later with the amount of money Sayaka supposedly has. Right now, figuring out what's going on by finding myself at school is key priority."

    show john b_3:
        ease 3 xpos -0.5

    "Without further worry I left the house with her backpack on me."

    scene black with dissolve
    scene bg sayaka house day
    show john a_0 at Position(pos=(0.60, 1.0), anchor=(0.5, 1.0)), faceleft:
        alpha 0.0
    with dissolve
    play sound sfx_door_not_open
    show john at center with ease:
        ease 0.5 alpha 1
    play sound sfx_forest
    $ renpy.sound.set_volume(0.5)

    "Hurdle number two for today was once more figuring out where the hell I am."

    #SKIP
    show john:
        alpha 1

    "I didn't have the faintest idea where Sayaka lived. I was basically on some random street in the middle of nowhere."

    show john b_1 at faceright

    think "At least the weather is nice."

    show john at faceleft

    "All I could do is guess one of the two directions this road goes."

    show john b_0

    think "She {i}does{/i} walk to school, right?"

    show john b_3:
        ease 3 xpos -0.5
    $ renpy.sound.set_volume(0.25)

    "Instead of brooding over what to do I just picked what looked right and walked down the road. With luck, I would end up in a place I knew which I could use for reference."

    stop music fadeout 1.5
    play sound AN_sfx_silence
    $ renpy.sound.set_volume(1)
    scene black with dissolve
    scene AN_bg road 1 day
    show john b_0 at Position(pos=(0.40, 1.02), anchor=(0.5, 1.0)), faceleft
    with dissolve
    pause 1
    play music bgm_fast_talkin

    cornelia "Saya?! Hey!"

    show john a_5 at faceright:
        easein 0.3 yanchor 1.00

    "I was still in an unfamiliar environment, but I heard someone shout out to me."

    show john a_6

    "Someone who sounded annoyingly much like someone I occasionally interacted with."

    show cornelia b_8 at offscreenright, faceleft
    show john a_13
    show cornelia at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0)) with ease

    cornelia "Saya...? What are you doing here?"

    show john a_30

    john "Uh, heading to school?"

    show cornelia a_8

    cornelia "But... Without me?"
    "For some reason, she was on the verge of crying."

    show john a_0

    "I never thought I would be about to see Cornelia of all things crying over... This. I always thought she was okay with anything as long as she got to be the dog of Sayaka."

    show john a_15

    john "Do you, uh... Want to walk to school with me?"

    show cornelia b_3
    show john b_7 at faceleft with hpunch:
        ease 0.2 xpos 0.36 ypos 1.0
        ease 0.3 ypos 1.02

    cornelia "What the fuck do you think?! I've waited for you every day in the last two years and now you decide you are okay just going to school alone?!"
    "I didn't know if this was some kind of pent up anger she was releasing on me or what exactly it was. All I knew was that she was angry and sad at the same time."
    "It sure made me jump, though."

    show cornelia a_8

    "But she soon realized she was talking to her chief in command."

    show cornelia b_4
    show john b_17

    cornelia "I- I- I mean, it's- You're okay to do so, you're you, after all. But can you at least... you know, tell me before you want to change anything about our morning schedule...?"

    show john b_6

    john "Ugh, honestly, whatever, I don't want to deal with this right now. Let's just go then."

    show john b_1

    "True, I really didn't want to deal with anything right now, but I realized that I wouldn't be lost if I just followed her."

    show cornelia b_9

    "She wouldn't be leaving me alone unless I straight up pushed her away, but even I wasn't that heartless, and she was of use after all."

    show cornelia b_5
    show john b_0

    cornelia "Ooo~~okay."

    show john b_5

    "And now she was just waiting."

    show cornelia a_5

    "Standing there."

    show john b_6

    "Looking at me."

    show john a_0

    cornelia "Aren't we going?"

    think "Is she waiting for me to take the lead?"

    show john a_26

    think "She is totally waiting for me to take the lead..."

    show john a_16

    john "Ah, yes. I just thought... How about this: Today, because it's a new school year, you should take the lead."

    show john a_13
    show cornelia b_2

    "She began giggling as if she heard something hilarious."

    show john a_6

    john "I'm being serious."

    show cornelia a_7

    cornelia "...You are?"
    john "Come on, we need to get there as quick as possible."

    show cornelia a_8

    cornelia "O- Okay, let's go then, I guess!"

    stop music fadeout 1.5
    scene black with dissolve
    scene bg road day
    show john b_0 at center, faceleft
    show cornelia b_1 at centerleft, faceleft
    with dissolve
    show john:
        center
        block:
            ease 0.6 yanchor 0.99
            ease 0.8 yanchor 1.00
            repeat
    show cornelia:
        centerleft
        block:
            easein 0.4 yanchor 0.99
            easein 0.5 yanchor 1.00
            repeat
    play music bgm_hackbeat

    "Underway, Cornelia started various conversations of gossip about other students. Even talking about some students I didn't even know existed."

    show cornelia b_2
    show john b_29

    "All I could do is nod and go {q}Ah, yeah{/q} and such."

    show cornelia b_6

    "Cornelia noticed something was up, but never brought it to attention."

    show john b_13

    "Whether this was considerate friendship or her way of staying out of trouble was something I could only guess."
    cornelia "By the way... You didn't apply any make-up today? I thought this was an important day for you."

    show john a_8

    think "Well, shoot, she is on to me."

    show john b_16

    john "Heheh, I, uh... Just didn't feel like it, you know?"

    show cornelia a_3 at faceleft:
        ease 0.2 yanchor 1.00
    show john b_27:
        ease 0.5 yanchor 1.00

    cornelia "Didn't feel like it? Aren't you supposed to be the greatest beauty of the seniors?"

    show john b_19

    john "Oh, lay it off already. I can't deal with something like that right now."

    show john a_17
    show cornelia a_5

    cornelia "Yeah, you can't deal with {i}anything{/i} right now apparently. But excuse me for asking you. You've been hella weird today, you know that, right?"

    scene black with dissolve
    show bg school entrance day:
        zoom 2.0 xalign 0.8 yalign 0.8
    show cornelia a_5 at centerright, faceleft
    show john b_6 at right, faceleft behind cornelia
    with dissolve
    show john:
        right
        easein 0.6 yanchor 0.99
        easein 0.8 yanchor 1.00
    show cornelia:
        centerright
        easein 0.4 yanchor 0.99
        easein 0.5 yanchor 1.00

    "As was my luck, we arrived at the school gates before having to talk more to her about whatever she even talks about."

    show john b_0

    "There weren't a lot of people. Everyone who was passing by were people I didn't know, with some few familiar faces among them."

    show cornelia at faceright

    "I instinctively reached down to my pocket for my phone to check the time, but naturally I didn't have any pockets right now."

    show john a_6

    "Also, I just noticed I forgot bringing her phone."

    show john b_5

    john "Cornelia, what's the time?"

    show cornelia a_6

    cornelia "Why are you calling me- Ugh, whatever, sec."

    show cornelia a_5

    cornelia "It's seven thirty-six."

    show john a_13

    john "So 24 minutes left."
    john "Please go ahead and find us some spots at the entrance ceremony."

    show cornelia a_2

    cornelia "Hah, if you're going to ask me for a favor then I guess there is no helping it."

    show cornelia b_0

    cornelia "But then what are you going to do in the meantime?"

    show john b_18

    john "Just do it."

    show cornelia b_6
    show john b_17

    cornelia "Alright then. Jeez, you're moody today."

    show john a_0
    show cornelia a_5 at center, faceleft with ease:
        ease 0.75 alpha 0.0
    hide cornelia

    "Choosing to once more ignore her statement, I placed myself leaning up a wall and waited."

    show john a_13

    "And waited."
    "I couldn't check the time because I had no phone or watch on me, but as a sudden flood of people appeared, I knew it was close to ten minutes left until we had to meet at the ceremony."

    show john a_0
    show sayaka a_16 at left:
        alpha 0.0
    outfit sandra suit
    accessory sandra set glasses
    show sandra b_3 at offscreenleft:
        alpha 0.0

    "Then, finally, I saw myself approach."

    show bg school entrance day:
        ease 1 zoom 2.0 xalign 0.1
    show john at offscreenright with ease
    show sayaka at center:
        pause 0.25
        ease 0.5 alpha 1.0
        block:
            easein 0.7 yanchor 0.99
            easein 0.7 yanchor 1.00
            repeat
    show sandra at centerleft:
        pause 0.25
        ease 0.5 alpha 1.0
        block:
            easein 0.6 yanchor 0.99
            easein 0.8 yanchor 1.00
            repeat
    with ease

    "Together with my mom, that is."

    #SKIP
    show sayaka:
        alpha 1.0
    show sandra:
        alpha 1.0

    think "Great..."

    show sayaka a_15

    "I thought of how to approach them, but the moment my own body saw me, it sprinted towards me."

    stop music fadeout 0.5
    show bg school entrance day:
        ease 0.5 zoom 2.0 xalign 0.6
    show sandra b_8 at offscreenleft:
        ease 0.5 alpha 0.0
    show sayaka a_7 at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0))
    show john a_27 at right
    with ease
    play music bgm_just_nasty

    sayaka "{b}{i}YOU!{/i}{/b}"

    show john a_31

    think "Yep, she's pissed."

    show sandra at centerleft with ease:
        ease 0.5 alpha 1.0
    show sayaka a_16
    show john a_0

    sandra "John, what are you shouting for?"

    show sayaka at faceleft
    show sandra b_4

    sayaka "Fucking nothing!"

    show sayaka at faceright

    sayaka "You! We're going to talk!"

    show john a_5

    john "{size=-5}Hey, at least be just a little polite.{/size}"

    show john a_2

    john "I'm sorry Ms. Davis, but I'm borrowing him for a minute or two!"

    show john a_10
    show sandra b_5

    sandra "Sayaka? I didn't know you and John interacted."

    show sayaka a_7 at faceleft

    sayaka "This is a special occasion!"

    show sayaka at faceright
    show john a_0

    sayaka "Now get a move on, hippie!"

    show sandra b_3
    show sayaka a_16:
        easein 3.25 xpos 1.5
    show john b_6:
        pause 1
        faceright
        easein 2.75 xpos 1.5

    john "Alright, alright."
    "She had grabbed me by my hand and straight up yoinked me in the opposite direction of where all the other students were headed."

    stop music fadeout 3
    show sandra a_6

    sandra "{i}Sigh...{/i} I wonder what happened..."

    scene black with dissolve
    scene bg school garden day
    show sayaka a_5 at left, faceleft
    show john a_0 at centerright, faceleft
    with dissolve
    play music bgm_pulse_rock

    "She lead me to the garden of the school. With everyone soon attending the entrance ceremony, there was nobody around."
    "And she made sure of that before erupting at me like a volcano."

    show sayaka a_7 at faceleft:
        ease 0.5 xpos 0.4

    sayaka "Explain. Right now! Are you that bitch's pet John?!"

    show sayaka a_16
    show john a_5

    john "Sayaka, calm down."

    show sayaka a_4

    sayaka "Calm down?! Are you for real?! How am I supposed to be calm when you're trying to steal my fucking life right in front of me!"

    show sayaka a_15
    show john b_7

    john "Steal your life?"

    show sayaka a_7

    sayaka "I've been calling my phone for half a fucking hour now and it went to {i}MY OWN{/i} voicemail {b}EVERY TIME!{/b}"
    think "Well, I already thought as much, but she isn't the cause for this swap between us then?"

    show sayaka a_16
    show john b_5

    john "I didn't do anything. I woke up and I find out I'm you for god knows what reason."
    john "But it sure sounds like you didn't have anything to do with it either."
    sayaka "Oh, please. Someone like you would be begging to be me. Of course you have something to do with this!"

    show john a_3

    john "Listen here, you stuck-up sissy. I would rather spend eternity walking around as a WcDonalds employee than have to live your pathetic life of bullying for a single day."

    show sayaka a_15

    john "Yeah, so what if you look good? But you are still rotten to the core."

    show sayaka a_14
    show john a_5

    sayaka "Hohohoh, okay, someone like you tries to badmouth me? Of course that's the only thing you're good for like the absolute bottom feeder you are. You probably spend your life, like, playing video games and doing absolutely nothing all day."

    show sayaka a_16

    sayaka "I bet if laughter really is the best medicine there is, then reading your life story could be curing the world right now as we are {b}fucking speaking!{/b}"

    show john a_32

    think "Why did I ever think I could cooperate with this woman."

    show john a_17

    john "Fuck you too. If you like insulting me so much, then how about we just stay like this until dear John over yonder my sight goes ahead and apologizes to the tyrannical bitch."

    show john b_16

    john "You value your reputation, right? Do you want to see me fuck it up into an unrepairable state, or would you rather figure out how to reverse this shit?"

    show sayaka a_7

    sayaka "You wouldn't even dare. You're fucking dead if you attempt anythi-"

    show sayaka a_15
    show john a_0

    "She stopped in her tracks as if realizing something."

    show sayaka a_7

    sayaka "Did you touch me?"

    show john b_11

    john "Did I wha-"

    show sayaka a_4 at faceleft with hpunch:
        easein 0.35 xpos 0.5
    show john b_27

    sayaka "{b}DID YOU FUCKING TOUCH ME?!{/b}"

    show sayaka a_15
    show john b_19

    john "What do you think?! I was in a hurry to get to school to figure out what's going on myself! And it is kind of hard getting clothes on without touching my own body! Or would you rather I come in underwear?"

    show sayaka a_16

    john "And are you just constantly angry or something? Jesus H. fucking Christ, can we stop screaming at each other and fix this?!"

    show john b_18

    john "I've already told you that I absolutely hate you! If I could swap with anyone then you would be my very last pick!"

    show sayaka at faceleft:
        easein 0.5 xpos 0.45
    show john b_17

    sayaka "Are you seriously trying to make me believe you didn't do this shit?"

    show john b_19

    john "YES! OH MY GOD, YES!"

    show sayaka a_15
    show john b_17

    sayaka "Hngh- Then- "

    show sayaka a_7 at faceleft

    extend"{b}{size=+5}AGH!{/size}{/b}"

    show AN_asset bucket at Position(pos=(0.25, 1.1), anchor=(0.5, 1.0)):
        zoom 0.35
        alpha 0.0
        ease 0.25 alpha 1.0
    show sayaka at centerleft with ease
    play sound AN_sfx_kick
    show AN_asset bucket:
        ease 1 ypos 0.1 xpos -0.2 rotate -90
    with hpunch
    pause 0.75

    "She turned around and kicked a bucket with no holding back. It was clear as day that Sayaka was absolutely livid."

    hide AN_asset bucket
    show sayaka a_20

    "She stood there, probably venting her rage inside her head for a few seconds."

    show sayaka a_21
    show john a_6

    "And when I say {q}a few seconds{/q}, I mean, she sure took her sweet time."

    show john a_0
    show sayaka a_16

    "When she was finally done, she took a deep breath."
    sayaka "{size=-7}Okay. Relax, Sayaka. You're the one in control. You're the queen of this stupid school. Good things are to come.{/size}"

    show sayaka at center, faceright with ease

    sayaka "Phew. Okay, fuck it. I don't believe you, but I'm not going to stay like this, so let's just find a way to go back to normal."

    show john a_1

    john "Good, now if-"

    show sayaka a_7 at Position(pos=(0.6, 1.0), anchor=(0.5, 1.0))
    show john b_27 at Position(pos=(0.75, 1.05), anchor=(0.5, 1.0))
    with ease
    with hpunch

    sayaka "And if you're lying to me, then kiss goodbye to everything you love. Get it?"

    show john b_28
    show sayaka a_16

    john "Ow, fuck! Calm your tits, I'm not lying! And it's clear as day that you aren't either. So someone must have done this!"
    sayaka "Obviously."

    show john b_8

    john "Now could you please get your hands off me? You've established that you're the physically strong one here."

    show sayaka at Position(pos=(0.5, 1.0), anchor=(0.5, 1.0)), faceleft with ease

    sayaka "Hmph..."

    show john b_18 at Position(pos=(0.75, 1.0), anchor=(0.5, 1.0)) with ease

    john "You know, that really hurt."

    show john b_17
    pause 1

    "...Not really much of an apology coming from her, is there? She really hit me hard on my shoulder, even though she probably didn't intend to use that amount of force."

    show john a_0

    john "...Anyways, I'm guessing what we're left with is that someone must have done this."

    show sayaka a_5 at faceright

    sayaka "Or something."
    john "Something?"

    show sayaka a_16

    sayaka "It sure as fuck isn't a coincidence that {i}we{/i} were swapped, but even a preschooler would know that this could just by chance be a coincidence."

    show john a_5

    john "You mean, we just happened to magically get swapped randomly?"

    show sayaka

    sayaka "What else, moron?"

    show john a_32

    "I clenched my fist at her constant jabbing but endured it for now. I would be sure to get back at her in some way, but that's for when we actually know what triggered this."

    show john a_13

    john "Okay, so something, or someone, caused this."
    "..."

    show sayaka a_20
    show john a_27

    sayaka "Seriously? That's it? You really can't think of anything else?"

    show john b_18
    show sayaka a_21

    john "Like what?"

    show john b_17

    sayaka "Who did this? Why they did this? How they did this? What caused it? Anything actually helpful?"

    show john a_6

    john "Then let's hear your {i}oh so wise{/i} opinion."

    show sayaka a_16

    sayaka "If someone did this, they would have to be close to us for them to be interested in actually doing this, right?"

    show john a_16

    john "Which just about rules in, what, possibly the entire school?"

    show sayaka a_19

    sayaka "If you could let the people who know a thing or two about actually thinking with their heads talk, you would get that it rules out many more."

    show john a_13

    sayaka "Loads of jealous bitches are after me, I'm at the top of the food chain after all. But why anyone would want to mess with a shipwreck like you is beyond me."

    show john a_14

    john "That's a very humble way of saying that you're someone everyone in school hates looking at."

    show sayaka a_5
    show john a_15

    sayaka "As if you could understand how it is to be the alpha. Having loads of jealous vixens after me is part of the job, after all."

    show john a_6

    john "Yeah, no, you're just a d-bag towards everyone."

    show john a_0

    john "But you're saying that more people would be after you than me?"

    show sayaka a_16

    sayaka "Yes, and that includes that orange slut of yours you call a friend, and maybe Nerdy McNerd."

    show john b_17

    john "Could you {i}not{/i} try to bully people when trying to talk?"
    sayaka "..."

    show john b_27

    john "...What?"

    show sayaka a_21

    sayaka "...John, explain to me why I am not wearing any make-up."

    show john b_28

    john "Wha- Why is that a worry?! We've got bigger issues at hand!"

    show sayaka a_24

    sayaka "Oh my god, this is the end of me..."

    play sound sfx_bell
    show john b_17
    show sayaka a_15 at faceleft

    "We had both lost track of time entirely, but the school bell, which was supposed to be a signal that indicates that everyone should be seated right now in the school hall, broke our conversation completely."

    show sayaka a_16 at faceright
    show john b_18

    john "Shit, we're going to be late on the one day we can't be late on."

    show john b_17

    sayaka "Meet me here at lunch again. And you better fucking show up."

    show john a_32

    john "Alright, alright."

    show john b_22:
        easein 1.5 xpos 0.6
        block:
            easein 0.5 yanchor 0.99
            easein 0.7 yanchor 1.00
            repeat
    show sayaka at faceleft:
        easein 1.5 xpos 0.35
        block:
            easein 0.6 yanchor 0.99
            easein 0.8 yanchor 1.00
            repeat

    "As tough as it was to admit, Sayaka must be a bit more organized. The only thing I could think of was that someone must have done this."
    "Despite her burning anger which could rival the sun itself, she had some ideas of things to think about."

    show john b_17

    "Unless I wanted to be bested by this bird-brain, I would have to think of some things as well."

    stop music fadeout 3
    scene black with dissolve

    "With that, we silently rushed to the ceremony together."

    play music bgm_flutey_funk
    show AN_bg auditorium no podium at center:
        zoom 1.1
    show abby a_0 at Position(pos=(0.5, 0.7), anchor=(0.5, 1.0)):
        zoom 0.6
    show AN_asset podium at Position(pos=(0.5, 0.925), anchor=(0.5, 1.0))
    with dissolve

    "When we arrived, Principal Luten had already started her speech."

    show abby a_1

    "It is a pretty customary thing to me at this point now that I've heard it twice already, since I'm now a senior."

    scene black
    show AN_bg auditorium
    show alex a_3 at left, faceright:
        zoom 0.75
    show greg a_6 at centerleft, faceright:
        zoom 0.75
    show sayaka a_16 at centerright, faceleft:
        zoom 0.75
        alpha 0.0
        pause 0.5
        ease 0.5 alpha 1.0
    show john b_25 at right, faceleft:
        zoom 0.75
        alpha 0.0
        pause 0.75
        ease 0.5 alpha 1.0
    with dissolve
    "We caught the mean look of a few of the teachers as we entered the auditorium."

    #SKIP
    show sayaka a_16:
        alpha 1.0
    show john b_25 at right, faceleft:
        alpha 1.0

    hide alex
    hide greg
    with dissolve
    show leona a_5 at left, faceright:
        zoom 0.75
    show jack a_8 at centerleft, faceright:
        zoom 0.75
    with dissolve

    "Other teachers who knew us well were on the other hand surprised to see us entering together."

    show jack:
        ease 0.5 alpha 0.0
    show leona:
        ease 0.5 alpha 0.0
    show AN_bg auditorium:
        ease 0.5 zoom 2.0 xalign 0.8 yalign 0.8
    show sayaka at center:
        faceright
        ease 0.5 zoom 1
    show john at centerright:
        ease 0.5 zoom 1
    with ease
    pause 0.25
    show john b_11

    sayaka "{size=-7}Whatever you do, don't fucking tell any of our friends about this. You go join my clique until lunch. Got it?{/size}"

    #SKIP
    show sayaka:
        faceright
        zoom 1
    show john:
        faceleft
        zoom 1

    john "{size=-7}We aren't telling anyone?{/size}"

    show sayaka a_7

    sayaka "{size=-5}Oh for fu- ...I'll tell you why later.{/size}"

    show sayaka a_16:
        faceleft
        ease 1 alpha 0.0 xpos 0.1

    sayaka "{size=-10}Fuckin' idiot...{/size}"

    hide sayaka
    show john a_6

    "I heard her last comment and decided to keep my comeback for later. One of the teachers told me to seat myself already."

    hide john with dissolve
    show AN_bg auditorium:
        ease 1.25 zoom 2.5 xalign 0.2 yalign 0.9
        pause 1.5
        ease 1.25 xalign 0.8
        pause 1.5
        repeat

    "I scanned the auditorium for Cornelia that I sent ahead to secure some seats. Since she expected me to sit with her, she would probably have space for me."
    "But it was difficult to find her right off the bat because of her height. I saw a lot of blondes, but none with twin-tails like her."

    outfit irene uniform
    show AN_bg auditorium:
        ease 0.5 xalign 0.8
    pause 0.25
    show cornelia a_7 at right, faceleft
    show irene b_4 at center, faceleft
    show john b_5 at offscreenleft, faceright behind cornelia, irene:
        alpha 0.0
    with dissolve

    "Despite that, I luckily found her quite fast because she chose seats in the far back, and also mostly because the towering Irene was sitting there as well."
    "Cornelia was looking my way when I spotted her, which means she probably spotted me talking with Sayaka."

    show AN_bg auditorium:
        ease 0.4 xalign 0.65
    show cornelia at offscreenright:
        ease 0.5 alpha 0.0
    show irene at centerright:
        ease 0.5 alpha 0.0
    show john at centerleft:
        ease 0.5 alpha 1.0
    with ease

    "I went through the many people that sat in my way to the spot she reserved for me. For some reason, people made space for me as if I were royalty."

    show john b_6:
        alpha 1.0

    think "The perks of being the queen bitch, huh?"

    show AN_bg auditorium:
        ease 2.5 xalign 0.8
    show john b_1:
        ease 2 xpos 0.7
        pause 0.25
        faceleft
    show cornelia a_6 at Position(pos=(0.9, 1.0), anchor=(0.5, 1.0)):
        pause 1.5
        ease 0.5 alpha 1.0
    show irene at center:
        pause 1.5
        ease 0.5 alpha 1.0
    pause 2.5

    cornelia "Sayaka, what the hell did that dweeb want from you?"

    #SKIP
    show irene:
        alpha 1.0
    show cornelia:
        alpha 1.0
    show john:
        xpos 0.7
        faceleft
    show AN_bg auditorium:
        xalign 0.8

    show john b_5 at faceright
    show cornelia a_2

    cornelia "He didn't blackmail you or some weird shit, right?"

    show john at faceleft
    show cornelia a_0
    show irene at faceright

    irene "Corny, can you shut the fuck up? I'd like to know where Luten is going to send us for today."

    show john a_6
    show cornelia b_6

    cornelia "Get that stick out your ass already. Who cares about Luten's speeches anyways?"

    show irene b_2

    "While the two were bickering, I had seated myself between them, and just about caught the most killer stare from Irene that was meant to be directed towards Cornelia on the other side of me."

    show irene b_7 at faceleft

    "All I managed to catch from Irene as a follow-up was a silent {q}Urgh{/q} as she voluntarily abrupted the bickering."

    show irene b_4
    show john a_5
    show cornelia b_5

    "Luten explained the usual, just like the last two years."

    show john a_30

    "But, now I realized that there would be another issue. We all received a mail or letter which told us what class we were assigned to."

    show john a_32

    "I was assigned to the E class, but how am I supposed to know what class Sayaka was assigned to? I couldn't just follow someone else since they might be assigned to another homeroom teacher entirely."

    show john b_13

    think "So I have to contact Sayaka somehow again... She doesn't know where I should go either."

    scene black
    show AN_bg auditorium no podium at center:
        zoom 1.1
    show abby a_1 at Position(pos=(0.5, 0.7), anchor=(0.5, 1.0)):
        zoom 0.6
    show AN_asset podium at Position(pos=(0.5, 0.925), anchor=(0.5, 1.0))
    with dissolve

    abby "...As for the seniors, we welcome you back to Tina Koya once more. The same words we gave for the freshmen and juniors apply to you as well. And please treat our new students well!"
    abby "Just like freshmen and juniors, I am going to list which homeroom teacher belongs to what class. So please pay attention to what homeroom teacher you will be having this year."

    show abby a_5

    "She then listed the different classes and which homeroom teacher they have."
    abby "Before we let you go free, does anyone have any questions?"

    pause 0.5
    show abby at faceleft
    pause 0.5
    show abby a_1

    abby "Yes, over there?"

    scene black
    show AN_bg auditorium:
        zoom 2.5 xalign 0.2 yalign 0.9
    show sayaka a_5 at centerleft, faceright
    with dissolve

    sayaka "Principal Luten, what if I'm stupid and forgot what class I'm in?"
    think "Ah, good thinking Sayaka. But the self-jab really wasn't required here."

    scene black
    show AN_bg auditorium no podium at center:
        zoom 1.1
    show abby a_1 at Position(pos=(0.5, 0.7), anchor=(0.5, 1.0)), faceleft:
        zoom 0.6
    show AN_asset podium at Position(pos=(0.5, 0.925), anchor=(0.5, 1.0))
    with dissolve

    abby "If you don't know what class you are in, check in with me here afterwards. I have a list of all classes and it's students here."

    show abby a_5 at faceright

    abby "Anything else?"

    stop music fadeout 2

    title "8th of August (Monday)" "The first day - Sayaka"

    scene black
    show AN_bg auditorium:
        zoom 2.5 xalign 0.2 yalign 0.9
    show sayaka a_2 at centerleft, faceright
    with dissolve
    play music bgm_dub_feral

    think "Great, now I have to try and pose like this twerp in front of the princibitch too."

    show sayaka a_16

    "My mood wasn't the greatest. Of all the people this stupid thing could happen with, it had to be that backstabber's boyfriend."
    "He would be sure to screw up everything I've worked for in my life. If someone was responsible for this, then they would have hell to pay."

    show sayaka:
        ease 0.5 alpha 0.0 xpos 0.1
    show AN_bg auditorium:
        ease 0.5 xalign 0.5
    pause 0.25
    show abby a_5 at Position(pos=(0.55, 1.0), anchor=(0.5, 1.0)), faceright
    show eric a_0 at Position(pos=(0.75, 1.0), anchor=(0.5, 1.0)), faceleft
    show maria a_4 at Position(pos=(0.90, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    "Luten finished answering the few questions people had and I, along with a couple other idiots who genuinely didn't know which class they would be in, asked her to know."

    pause 0.5
    show maria a_1:
        faceright
        easein 2 xpos 1.4
    show eric a_4:
        faceright
        easein 2 xpos 1.25
    show sayaka:
        pause 0.75
        ease 0.75 alpha 1.0 xpos 0.3

    sayaka "Excuse me?"

    #SKIP
    show sayaka:
        alpha 1.0 xpos 0.3

    show abby a_0 at faceleft

    abby "Hm?"
    abby "Ah, John. I'm a bit surprised for you not to know about your class name considering the position of your mother."

    show sayaka a_8

    "That's right. Ms. Davis was this twerp's mom. I didn't have anything against her, she was actually pretty cool."

    show sayaka a_16

    sayaka "Yeah yeah, just tell me what class I am in."

    show abby a_3

    abby "Excuse me?"

    show abby a_5
    show sayaka a_5

    sayaka "{i}Please{/i} tell me what class I am in, principal Luten."
    "The guy probably acted like a wannabe-saint normally, which would throw her off."

    show abby a_0

    "Luten looked at me a bit suspiciously. Like, just tell me, woman."

    show abby a_5

    abby "Your homeroom teacher is Ms. Williams. You're in class B. Go get a copy of your mail if you've lost it from her before the day is over."
    think "Great. Knowing the idiot he probably would have gotten his own class name wrong anyways."

    scene black with dissolve

    "Finally knowing, I would have to act the part in that class for the moment."
    "There was no way I would ever let that bitch Katrina know about this opportunity to get at me, and I would make sure that John wouldn't have a chance to either."

    stop music fadeout 4

    sayaka "{size=-5} Ugh, I can only shudder at having to live like a guy.{/size}"
    think "But I can fix this. Everything is going to work my way eventually. If it can happen once, it can happen twice."

    scene black
    show bg school hallway day:
        zoom 1.25 xalign 0.9
    show sayaka a_16 at centerright, faceleft
    with dissolve
    play music bgm_investigations

    "I got angry when some people just crossed right past without letting me through. Normally I'd assert my dominance, but the only dominance I could establish like this would be dominance over a chicken coop."

    show sayaka at faceright

    sayaka "{size=-7}Why did this have to happen with this guy...{/size}"

    show sayaka at faceleft

    sayaka "{size=-7}It could at least have been Mike or Brad, or someone who isn't an absolute lame-ass.{/size}"

    accessory connie set glasses
    show connie b_4 at centerleft, faceleft:
        alpha 0.0
        ease 0.5 alpha 1.0
    show sayaka a_5

    "Either way, I finally got around to finding Ms. Williams and John's class."

    #SKIP
    show connie:
        alpha 1.0

    show connie at faceright
    pause 0.5
    show connie b_0

    connie "Ah, there you are John. With you it finally makes it 28. Looks like everyone is here."

    show connie a_1 at faceleft

    connie "Follow me and I'll show you our homeroom."

    show connie b_1:
        ease 2 alpha 0.0 xpos -0.2

    "Ms. Williams was chill too. It's just, all those puns she tries to make are like, really painful to listen to."
    "I heard rumors about some idiot giving her a book about puns once. And if I ever were to find out who defiled that woman so badly, I would for sure put an end to them."

    show sayaka:
        ease 1 xpos 0.6
        block:
            easein 0.7 yanchor 0.99
            easein 0.8 yanchor 1.00
            repeat
    accessory kiyoshi set glasses
    show kiyoshi a_2 at centerright behind sayaka:
        faceleft
        alpha 0.0
    accessory kyoko set glasses
    show kyoko a_0 at right:
        faceleft
        alpha 0.0

    think "That would make me a bit of a savior too, wouldn't it?"

    show kiyoshi at Position(pos=(0.45, 1.0), anchor=(0.5, 1.0)):
        ease 0.5 alpha 1.0
        block:
            easein 0.7 yanchor 0.99
            easein 0.9 yanchor 1.00
            repeat
    show kyoko at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)):
        ease 0.5 alpha 1.0
        block:
            easein 0.6 yanchor 0.99
            easein 0.7 yanchor 1.00
            repeat
    with ease
    show sayaka a_15

    kiyoshi "Ah, John, it is good to see you. We were afraid the panourgians had finally made their move."
    think "Oh yeah..."
    think "{b}That{/b} guy."

    show kiyoshi a_1
    show sayaka a_16

    kyoko "Didn't you mention that a move would logically only be made during the winter?"
    think "Oh my god, don't tell me I have to talk with these losers..."
    kiyoshi "You know how it is. To strike when we are most unprepared is to strike the strongest."

    show sayaka a_7
    show kiyoshi a_4
    show kyoko b_3

    sayaka "What the fuck are you even talking about?"

    show sayaka a_16

    think "Please don't tell me I have to be in the same homeroom class as them..."
    "Well, they looked worried at my outburst for a while, obviously, but the little nerd soon after brightened up again."

    show kyoko a_8

    kyoko "We're in the same homeroom class, John!"

    show kyoko b_1

    think "Great."
    think "Just. Great."

    show kiyoshi a_6

    kiyoshi "I'm sure the seventh letter I sent to the principal must have made her reconsider the synergy we have between us three and finally have us in the same homeroom."

    show kiyoshi a_1
    show sayaka a_2

    think "It is totally weird to see them completely off-guard though. They don't even realize it's me."

    show sayaka a_5

    think "They don't... Realize...? Oh."

    show sayaka a_3
    show kyoko b_0

    sayaka "{size=-7}Heh... Heheh...{/size}"

    show sayaka a_17

    think "I can have some fun with this. It's the least that the twerp owes me in exchange for being magnificent me."
    kyoko "John, you alright?"

    show sayaka a_13

    sayaka "Eh- What? Why shouldn't I be? Heh, I'm just getting a lot of good ideas right now. Like, really good ideas."

    show sayaka a_17

    kyoko "Uh... Alright?"

    show kiyoshi a_6

    kiyoshi "Do any of those ideas include new strategies for our lady situation, maybe?"

    show sayaka a_20
    show kyoko b_3

    sayaka "Ew, fuck no! Don't even try to start this shit with me."

    show sayaka a_16:
        easein 1 xpos 0.2 alpha 0.0
    show kyoko b_4:
        pause 1
        ease 0.5 yanchor 1.0
    show kiyoshi a_4:
        pause 1.5
        faceright
        ease 0.5 yanchor 1.0
    pause 1.5

    "Both of them looked at each other with a bit of confusion when I walked away from that creep."

    scene black with dissolve
    scene bg classroom 1
    show sayaka a_5 at Position(pos=(0.25, 1.15), anchor=(0.5, 1.0))
    show connie b_0 at right, faceleft
    with dissolve
    pause 2
    show sayaka a_16 at Position(pos=(0.25, 1.15), anchor=(0.5, 1.0)) with hpunch

    think "Gah! Effing {i}BORING{/i} having to listen to Ms. Williams talking all day long."
    "We had to write our names on a paper so she could remember the names of people she didn't have in previous years."
    "I was so close to writing my real name and not fucking John's."

    show sayaka a_7

    sayaka "{size=-10}Fuck this entire day.{/size}"

    show sayaka a_16

    "I got easily irritated when things didn't go my way as they are supposed to. But I would go full-throttle at anything right now if something went even further the wrong way or annoyed me."

    show connie a_0

    "And I would go especially crazy towards his idiot friends."

    show sayaka a_9

    think "Okay, I hate them. But keep your focus."

    show sayaka a_5
    pause 1.5

    think "...I hope he doesn't fuck up everything I've built in my life within a single day..."

    stop music fadeout 1.5
    scene black with dissolve
    play sound sfx_bell
    scene bg school garden day
    show sayaka a_16 at centerleft, faceleft
    with dissolve
    play music bgm_highlight_reel

    "When lunch finally came around, I only managed to get out of Pervoshi's sight by telling him I had to go play video games or some shit."

    show sayaka:
        faceright
        ease 1 xpos 0.4

    "I don't freaking know what John does when he isn't at lunch. I don't freaking care either."

    show sayaka:
        faceleft
        ease 1 xpos 0.3

    "I've been in the garden for five minutes now, but John still wasn't here."

    show sayaka:
        faceright
        ease 1 xpos 0.4
    show john b_22 at offscreenright:
        faceleft

    think "Oh, he better not be creeping himself out with my body right now..."

    show sayaka:
        faceleft
        ease 1 xpos 0.3

    "Just the thought of that retard being able to do anything with my beauty crept me out to no ends."

    show sayaka at faceright
    show john:
        faceleft
        ease 1.5 xpos 0.6

    "Honest to god, I would probably have broken down if he didn't show up a minute or so later."

    #SKIP
    show john:
        xpos 0.6

    show sayaka a_7 at center with ease

    sayaka "About fucking time you came."

    show sayaka a_16
    show john b_21

    john "Hey. Sorry, I had to take care of something first."

    show sayaka a_15
    show john b_27

    sayaka "Excuse me? Take care of what? Did you actually feel me up or some shit?!"

    show john a_17

    john "Don't gross me out here, your mutt Cornelia kept on clinging on to me until I told her to screw off. Seriously, how do you get rid of her?"

    show sayaka a_5

    "Oh, of course. She existed. I had to rub myself on my forehead since I knew Corny would become a pain in the ass at some point."
    sayaka "{i}Sigh... {/i} That bitch does everything except fuck off when I tell her to."

    show sayaka a_16

    sayaka "And I hope you didn't tell anyone about this for your own sake."

    show john a_13

    john "Well, no. I find it hard to just tell people without preparing, but why aren't we telling anyone again?"
    think "This idiot still hasn't figured out why...?"
    sayaka "It's effing obvious. If someone caused this swap, then we don't know who it is."

    show john a_6

    john "That's a given."

    show john b_5

    john "But why are you so afraid of telling the one responsible? What difference would it make if we tell them or not?"

    show sayaka a_5

    sayaka "It's obviously not because I'm afraid of telling the one responsible. It's because if I tell someone who isn't responsible, they can attack me."
    sayaka "I'm not trusting anyone in this school. As soon as they know a weakness, they will exploit me and take my position at the top."

    show sayaka a_16
    show john b_3

    sayaka "If we admit this to anyone, then not only am I practically announcing that I lost this fight that they started, but I also give people the opportunity to take everything from me. And I'm not fucking losing, like, ever. Got that drilled into your head?"
    sayaka "You're going to help me find literally any clue you can. And I'm not taking no for an answer."

    show john a_26

    john "{i}Sigh...{/i} Fine. Our interests are the same so I don't see why I shouldn't help..."

    show john a_6
    show sayaka a_7

    sayaka "Stop making that face with my face!"

    show john a_32
    show sayaka a_16

    john "..."
    think "This absolute dickhead is making me look like a complete idiot."

    show john b_18

    john "But! One thing before you continue commanding me around like one of your shitty friends: We are on equal footing here. If you're going to treat me like your underling then I'm going to do my own thing, get it?"

    show john b_16

    john "I'd like to think that I am better than you though, so I don't mind going along with what you're saying. But there are lines that you should not cross."

    show john b_15
    show sayaka a_3

    sayaka "Oh man, your attempt at being humble is just {i}too{/i} sweet."

    show sayaka a_17
    show john a_5

    john "Also, we both hate each other, but could we treat each other with just a bit of respect until this thing is over? Like normal human beings?"

    show sayaka a_16

    think "As if I could treat anyone who wants to affiliate with Katrina a respectful or decent human, hah."
    sayaka "Whatever. First off, let's figure out what could have triggered this. Tell me what you did yesterday."

    show john b_6

    john "Well, I did a lot of things, actually."

    show sayaka a_7
    show john b_7

    sayaka "Watch me care for how active you are in your boring life. Just tell already."

    show john a_32
    show sayaka a_16

    "He rolled his eyes as if trying to play smart."

    show john a_6

    john "First off, you're hungry, right?"
    sayaka "I am {i}not{/} going to act as your pathetic girlfriend and go buy lunch with you if that is what you're hoping."

    show john a_3

    john "I just bought two sandwiches before coming here, so can you calm the fuck down with your assumptions?"

    show john b_17

    "He took out the food he purchased {i}with MY{/i} money and handed me one."
    think "What guy isn't going to take advantage of me like this anyways? He might be lying to himself, but he isn't going to lie to me."
    think "I bet he is thinking to himself that this is bringing us closer like some shitty 90's movie."

    stop music fadeout 2

    title "8th of August (Monday)" "The first day - John"

    play music bgm_marty_gots_a_plan
    scene bg school garden day
    show sayaka a_16 at center, faceright
    show john a_31 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    think "Phew, if she found out I was checking her out in the mirror before going here..."

    show john a_6

    "Yeah, the Cornelia story was fake, so what? I look like some girl out of a dream, and confessing to myself in a mirror is something I'm in my full right to do."
    "...Actually, it sounds kind of sad to do that."
    "But at least she bought the excuse and calmed down after being handed something to eat."
    "I couldn't imagine how bad things would get if she intentionally started to sabotage my life, but just the possibility meant that I have to be careful."

    show john b_3

    "Going along with her {q}ideas{/q} or whatever you call them was in my opinion the wisest decision."
    "Being Sayaka for a bit of time could be fun, but for it to be permanent or anything close to it is a big no-no."

    show john b_1

    john "So anyways, you asked about what I did the day before, right?"

    outfit AN_john noshirt
    scene black with wipecircle
    scene bg main room day
    show AN_john a_11 at centerright, faceleft
    show AN_asset grain
    with wipecircle

    john "{i}Hm, I started by getting out of bed of course, I think that was at about twelve in the morning.{/i}"

    show AN_john a_5

    sayaka "{i}Twelve? You call that in the morning? Seriously? I can't imagine you're the kind of guy to go to parties.{/i}"

    show AN_john a_0:
        ease 1.5 xpos 0.5

    john "{i}I, uh, was staying up late playing games.{/i}"

    show AN_john a_5 at faceright

    sayaka "{i}Pfft!{/i}"
    "I didn't know why, but she started laughing all of sudden. Not the good kind of {q}yeah that's pretty funny{/q} kind of laugh, but the mocking kind of."
    sayaka "{i}I'm not even surprised at how boring your life has to be if you're playing effing video games on a saturday night, {b}pfhaaahahaha{/b}~{/i}"

    show AN_john a_16

    john "{i}Yeah, real funny. I thought you wanted to know what I did yesterday, but here you are interrupting the short time we have to talk.{/i}"
    sayaka "{i}~ahaah, yeah. I think you may be right for once.{/i}"
    "I intentionally waited until she was completely silent. I hoped it would send her a message."

    outfit AN_john casual
    scene bg main kitchen day
    show AN_john a_0 at Position(pos=(0.3, 1.15), anchor=(0.5, 1.0)), faceright
    show AN_asset grain
    with dissolve

    john "{i}So, as I was saying, I got up, ate breakfast, then-{/i}"
    sayaka "{i}What breakfast? Cereal? If yes, what cereal?{/i}"
    john "{i}No, my mom prepared fresh buns for us.{/i}"
    sayaka "{i}Ah, one of those {q}perfect{/q} family type situations you see in movies then.{/i}"
    john "..."
    sayaka "{i}What?{/i}"
    john "{i}Oookay, moving on...{/i}"

    scene bg main livingroom day
    show AN_john a_5 at Position(pos=(0.7, 1.2), anchor=(0.5, 1.0)), faceleft
    show AN_asset grain
    with dissolve

    john "{i}After that I watched some TV... until at about three, I think.{/i}"

    show AN_john a_2 at faceright

    john "{i}Then Kyoko called me to come over, or well, I asked to because I still had a few things to do from the homework we had.{/i}"

    outfit kyoko casual
    scene bg kyoko bedroom day open
    show AN_john a_1 at offscreenright, faceleft
    show kyoko a_0 at center, faceleft
    show AN_asset grain
    with dissolve
    show AN_john:
        pause 0.5
        ease 0.75 xpos 0.7
    show kyoko:
        pause 0.5
        faceright
        pause 0.75
        ease 0.25 xpos 0.6

    john "{i}We did some final checks on uh... Math and english, I think?{/i}"

    show AN_john a_0
    show kyoko a_8

    sayaka "{i}Why is it relevant for me to know what classes you suck at?{/i}"

    show kyoko a_6:
        faceleft
        ease 0.75 xpos 0.4
        ease 0.5 ypos 1.1
    show AN_john:
        faceleft
        ease 0.75 xpos 0.4
        ease 0.5 ypos 1.1

    john "{i}Wasn't it you who wanted to know as much as possible?{/i}"
    sayaka "{i}Whatever. Go on.{/i}"

    outfit kyoko uniform
    outfit sandra casual
    accessory sandra set
    scene bg main kitchen dusk
    show AN_john a_0 at Position(pos=(0.3, 1.15), anchor=(0.5, 1.0)), faceright
    show sandra b_9 at Position(pos=(0.5, 1.15), anchor=(0.5, 1.0)), faceleft
    show holly b_0 at Position(pos=(0.7, 1.15), anchor=(0.5, 1.0)), faceleft
    show AN_asset grain
    with dissolve

    john "{i}I stayed there until dinner where I went home and had some soup.{/i}"

    scene bg main room dusk
    show AN_john a_3 at Position(pos=(0.4, 1.15), anchor=(0.5, 1.0)), faceleft
    show AN_asset grain
    with dissolve

    john "{i}Then I played until about one in the night and went to bed.{/i}"

    scene black with dissolve
    scene bg school garden day
    show sayaka a_5 at center, faceright
    show john b_5 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    john "And... That's pretty much it, I think."
    "I couldn't help but question if she was happy with this choppy explanation of my day. If I hadn't told her that we were limited on time I'm sure she would have done her best to insult me after every sentence."

    pause 0.75
    show john a_27
    show sayaka a_7 at faceleft with hpunch

    sayaka "{b}{size=+5}AGH!{/size}{/b} That has {i}NOTHING{/i} in common with what I did!"

    show sayaka a_16
    show john a_30

    "Seeing Sayaka frustrated was a weird feeling, she was usually so asserting and hard-headed."

    show john a_6

    think "Wait, I'm not actually giving her credit, am I?"
    think "I have to remember this is still Sayaka, the number one bitch in this school."

    show sayaka a_7 at faceright
    show john a_0

    sayaka "What about the people? Who else did you meet aside from your mom and that nerd?"

    show sayaka a_16
    show john b_18

    john "That nerd? Address Kyoko properly if you want to ask me something like that, as a first."

    show john b_17
    show sayaka a_7

    sayaka "Fucking fine. Who else besides your mom and Kyoko?"

    show sayaka a_16
    show john a_13

    john "Sayaka, I don't keep tabs on {i}everyone{/i} I see on the streets. I can't remember any familiar faces aside from them and my sister. Kyoko's parents weren't even home."

    play sound sfx_bell
    show john b_7 at faceright
    show sayaka a_5

    "To further frustrate her, the bell rung, signaling the end of lunch."

    show john at faceleft
    show sayaka a_24

    sayaka "{size=-5}Great. Time is already over... I can't believe I'm doing this...{/size}"

    show sayaka a_16 at Position(pos=(0.6, 1.0), anchor=(0.5, 1.0)) with ease

    sayaka "Here."
    "She handed me three pages with loads of notes scribbled on them."

    show sayaka at center with ease
    show john b_11

    "They contained some words that were entirely unfamiliar to me."

    show sayaka a_7

    sayaka "Don't get the high idea that I'm giving you consent to anything. But if I don't look the part, then I won't be someone everyone looks up to."

    show sayaka a_16

    "There were various things like {q}Saffleur{/q} and {q}Heybelline{/q}. All sounded kind of like shampoo or some stuff..."

    show john b_18

    john "Wait, this isn't-"

    show john b_17

    sayaka "It's my daily routine. You got a problem with that?"

    show john b_18

    john "{i}{q}Shampoos to use...{/q} {q}Apply skin oils like this...{/q} {q}{b}How to use pads-{/b}{/q}"

    show john b_19 blush with hpunch
    show sayaka a_2

    john "Sa- Sayaka, are you fucking insane?!"

    show john b_17 blush

    "As I asked that question I caught a glimpse of something I wasn't supposed to see."

    show sayaka a_26
    show john b_27 blush

    sayaka "Don't get the wrong idea here."

    show sayaka a_30

    sayaka "Your job is to keep my popularity and reputation. Which includes maintaining my body."

    show john b_27
    show sayaka a_27

    sayaka "And yeah, I'm on my period, and I won't tolerate you not handling it."
    sayaka "Nothing else matters. And unless something changes, then-"

    show john b_22

    sayaka "..."

    show sayaka a_7
    show john b_5

    sayaka "You know what? Fuck that. Fuck you John. Yeah, you get to enjoy the me-time that is supposed to be only for me. But if I even get a hint of suspicion that you did something that {i}wasn't{/i} written in these notes..."

    show john a_1
    show sayaka a_16

    john "Then I'm dead. I get it."

    show john a_5
    show sayaka a_5

    "Rotten as she may be, I could sympathize just a bit with her. She must not like this at all."
    "Still, the part of me that couldn't sympathize would have wanted to mock her further, but kicking her further down would just make things worse."

    show sayaka a_27

    sayaka "Now... Don't be late to my class, if I don't get good grades, then..."

    show sayaka a_2:
        ease 1 xpos 1.2
    show john b_5 behind sayaka:
        pause 0.5
        faceright

    "I would have wanted to write a few notes to her too, but... She stormed off after I confirmed her intentions of murder if I did anything she didn't like."

    show john b_4

    think "I just hope she holds her part of the deal. If she wants me to act like her she better has to get along with Kat and the others."
    john "{i}Sigh{/i}, I hope this works out..."

    stop music fadeout 4
    scene black with Dissolve(1.5)
    pause 1

    title "9th of August (Tuesday)" "Day 2 - Sayaka"

    outfit sayaka noshirt
    $ renpy.sound.set_volume(0.25)
    play sound [AN_sfx_alarm] loop
    pause 1.5

    think "..."

    pause 0.5
    $ renpy.sound.set_volume(1)
    play sound sfx_lockpick
    pause 1.5
    scene bg main room day shut
    show sayaka a_2 at Position(pos=(0.75, 1.0), anchor=(0.5, 1.0)), faceright
    with dissolve
    pause 1

    "We didn't swap back..."
    sayaka "..."

    show sayaka a_7 at faceleft:
        transform_anchor True
        ease 1.5 rotate -30 yanchor 0.7

    sayaka "You, {size=+10}STUPID-{/size} MHGHH-"
    "I screamed into the pillow."

    show sayaka a_2

    think "This cannot really be happening..."
    think "I don't want to live as this loser anymore...."

    show sayaka a_9

    think "Please just turn me back..."
    think "And that loser gets to enjoy being me..."

    show sayaka a_11

    "I vented again by screaming in his stupid pillow."

    outfit sandra pajamas
    accessory sandra set bedhead
    show sandra b_7 at offscreenleft, faceright
    play sound sfx_door_open
    show sandra at left with ease
    show sayaka a_2

    sandra "John? John are you alright?"

    show sandra b_6

    sandra "Goodness gracious, I thought you were being attacked by a robber or something, the way you're shouting this early..."

    show sayaka a_5:
        faceright
        ease 1 rotate 0

    sayaka "Ugh, {size=+5}I'm fine...{/size}"

    show sandra b_2

    sandra "...You sound really angry about something."

    show sayaka a_16 at faceleft

    sayaka "I said I'm fine!"

    show sayaka a_5 at faceright
    show sandra b_5

    think "At least I have the perk of someone worrying about me this early in the morning."
    sandra "Uhm... Alright then. I'm going to go prepare breakfast then, since I'm up now."
    sayaka "...Okay."

    show sandra b_4 at offscreenleft, faceleft with ease
    play sound sfx_door_close
    pause 0.5

    "Despite my frustrations I took the morning a bit easier today. I was fucking furious yesterday, just as much as I was confused."
    "Waking up in a completely different and shoddy house than the one I went to sleep in, and then waking up late too, because this idiot kept playing games all night long for some reason. I don't think anyone would be able to keep their cool after that."
    "Going to bed early was after all one of my secrets to having the edge over the others. Any wrinkles or signs of insomnia were fatal for my image."
    "That aside, I couldn't stand how he reeked. It became just a tad too gross for me after all, so I took a quick bath before I went to bed, even though it was the grossest thing I had ever done."

    show sayaka at centerright, faceleft with ease

    sayaka "{i}Sigh...{/i} I should better get moving, huh..."

    show sayaka:
        ease 1.5 xpos 0.5

    "To top it all off, he only had three pairs of uniforms... How does he live like this?"
    "Two pairs were still clean, and I told Ms. Davis to clean the used uniform as soon as possible."
    "It almost felt like having talking to your own maid, but your maid is your mom instead. Weird."

    play sound AN_sfx_clothes1
    hide sayaka with dissolve
    outfit sayaka uniform
    play sound AN_sfx_clothes2
    show sayaka a_5 at center, faceleft with dissolve

    "I put on one of the spare uniforms, which was way easier to do than the girl's uniform."

    scene black with dissolve
    scene bg main kitchen day
    show sayaka a_5 at Position(pos=(0.8, 1.1), anchor=(0.5, 1.0)), faceright
    show sandra b_0 at centerleft, faceleft
    with dissolve

    "Afterwards, I made it down to the kitchen, which still was like, nothing, compared to ours."
    "I thought a teacher made bank when working their job, or maybe Ms. Davis just sucked at using money. Not like it matters."
    "I could take comfort in the fact that I wasn't pressed for time. Having to schill out time to make John look good with combed hair or some shit was something I totally was never, ever, going to do voluntarily."
    think "But he better apply like, some makeup today."
    "..."
    think "At least Ms. Davis makes some really good breakfast."

    show sandra b_3

    sandra "By the way, you're up quite early today, aren't you?"

    show sayaka a_2 at faceleft
    pause 0.5

    sayaka "Of course, I'm not wasting my life playing video games all night right now."

    show sandra b_5 at faceright

    sandra "What's this? My little boy is finally going to take a bit of responsibility?"

    show sayaka a_6

    sayaka "About time, yes."

    show sandra b_9 at faceleft
    show sayaka at faceright

    "I finished the, quite frankly delicious, slice of toast she had made me."
    think "Man, that guy must be enjoying her food every single day..."
    think "When I get back I should totally have Daddy hire someone like her."
    think "It depends on whether I am actually hungry or not though... I'm usually never hungry in the morning."
    think "Agh, who cares, I'm sure he would do that for me."

    show sayaka a_5 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)) with ease
    show sayaka at faceleft

    sayaka "I'm going. I want to meet with someone again."

    show sandra b_3 at faceright

    sandra "You're going already? I'm preparing some eggs since you were so stressed yesterday, and today too."

    show sayaka a_2

    sayaka "Huh? You cook for breakfast?"

    show sandra a_1

    sandra "Well now, it's not {i}THAT{/i} uncommon, is it?"

    show sayaka a_6
    show sandra a_0

    "I couldn't last remember when Daddy cooked something for me last time... It must be because Ms. Davis has more than enough time to spend."

    show sayaka a_5

    think "I don't usually get anything for breakfast in the first place though, and I already had something..."

    show sayaka a_17

    think "Oh yeah! It's not me who gets fat when I eat anything right now. Brilliant!"

    show sayaka a_0 at Position(pos=(0.8, 1.1), anchor=(0.5, 1.0)) with ease
    show sandra b_9:
        pause 0.75
        faceright
        ease 1.5 xpos 0.5

    "I put down the bag and seated myself again. Usually if I was hungry, it wouldn't be anything a nice bowl of cereal couldn't fix. But I wouldn't mind getting some tasty carbs free of charge."

    show sandra:
        ease 1 yanchor 0.9

    "I would normally only have something like this on trips with the girls."

    show sandra a_2

    sandra "So, you wanna talk about what's troubling you?"

    show sayaka a_5

    sayaka "Huh? Nothing."

    show sandra a_4

    sandra "Nothing?"
    "I shook my head with a frown. Like she would care about my problems. She is probably just trying to dig into me - or, well, her son - to get something on him like parents usually are."

    show sandra a_0

    sandra "Something personal then? I won't try to force my help on you, but you know that I am great at listening."

    show sayaka a_2

    sayaka "Sure, you do your thing."

    show sandra a_5

    sandra "...?"

    show sayaka a_0 at faceright

    "I finished my plate. I wasn't late yet, but I still had to make sure this guy didn't fuck up everything again."

    show sayaka at right with ease
    show sandra b_4:
        ease 0.5 center

    "I left the table, but Ms. Davis still kept me from going."

    show sayaka a_5 at faceleft

    sandra "John, sorry, but before you go, could you do the dishes today? I have to meet earlier than normally for a quick meeting, and if I have to do my usual routine I don't think I'll make it in time."

    show sayaka a_2

    sayaka "The dishes? Why do I have to do those?"

    show sayaka a_16

    think "Me? Do the dishes? The hell does this woman think I am?"

    show sayaka a_24

    think "Why do I have to put up with this..."

    show sandra b_3
    show sayaka a_19

    sayaka "{i}Tch...{/i} Fine. Whatever."

    show sandra b_5

    sandra "{size=-5}You're in a real cheery mood today, huh.{/size}"

    show sandra b_9
    show sayaka a_5

    sandra "Remember that Natsumi is coming over after school today."

    show sayaka a_2

    sayaka "Uh... Yeah."
    think "Who the hell is that now? Does he have a secret fuckbuddy or something?"

    show sandra b_1

    sandra "Love you sweetie. I'll be upstairs for a few minutes."

    show sandra:
        faceleft
        ease 1.5 xpos -0.2

    sayaka "A- Alright."

    show sayaka a_16:
        pause 0.25
        ease 1 xpos 0.35

    think "Man, just talking to someone is exhausting when you just got up..."

    show sayaka a_5 at Position(pos=(0.35, 1.0), anchor=(0.5, 1.0))

    "I took a look at the dishes that were laid out."

    show sayaka a_24

    think "Do they expect that I, like, actually do this?"

    show sayaka a_2

    think "I've never done this in my life..."

    show sayaka a_16

    "I decided to just do it. There is no way that I can't live as John Davis, I may be one of luxury and status, but that does not mean that I am unable to do these mundane things that he can."
    "Even then, I despised having to do this, but Ms. Davis would probably flip completely if I didn't do it."

    scene black with dissolve
    scene bg main house day
    show sayaka a_5:
        centerright
        faceright
        block:
            ease 0.6 yanchor 0.99
            ease 0.8 yanchor 1.00
            repeat
    show carrie a_1 at center, faceright:
        alpha 0.0
    with dissolve

    "I finally finished doing this stupid chore and went to the streets. I remembered the path from yesterday, so with my skills it should be no issue getting back to school well on time."

    show carrie behind sayaka:
        ease 0.5 alpha 1.0 xpos 0.58

    carrie "Hello John!"

    #SKIP
    show carrie:
        alpha 1.0

    show sayaka a_4:
        faceleft
        linear 0.25 xpos 0.79 yanchor 1.02
        ease 0.5 yanchor 1.0

    think "Wh- What?!"
    "Some girl was all of a sudden breathing down my effing neck like some crazy bitch."

    show carrie a_0
    show sayaka a_15

    carrie "Are you well and good?"
    sayaka "Who the fuck are you now?"

    show carrie a_2

    carrie "Huh? I'm your close friend Carrie, right?"

    show sayaka a_7

    sayaka "My close frie- What? I've never seen you at scho-"

    show sayaka a_1

    sayaka "I mean, yeah, my close friend..."

    show sayaka a_2
    show carrie a_3

    sayaka "Heh...?"
    think "Seriously, this girl is giving me the creeps for some reason."

    show carrie a_9

    carrie "So?"

    show sayaka a_5

    sayaka "...So...?"

    show carrie a_18

    carrie "Is all well?"

    show carrie a_17
    show sayaka a_7

    sayaka "Do you think all is well? Nothing is fucking well here."

    show carrie a_13

    sayaka "I feel like I want to take something and just effing strangle it. I can't stand this shit anymore."

    show sayaka a_15

    sayaka "Which, uh- Has absolutely something with me to do, yeah! Because John Davis is an idiot, and that is me."

    show carrie a_13 at faceleft

    carrie "{size=-8}Is this my chance...?{/size}"

    show sayaka behind carrie
    show carrie a_1:
        faceright
        ease 0.25 xpos 0.6

    carrie "John, if there is anything I can do, I am here to support you!"

    show sayaka a_16

    sayaka "Right. I am totally grateful for your {i}really{/i} generous offer, but I doubt a creep like you can help me with the actual problems I have."

    show carrie a_15:
        ease 0.25 xpos 0.55

    carrie "C- Creep?!"

    show carrie a_13
    show sayaka a_5

    carrie "Am I.. A creep?"
    think "This girl is freaking nuts."

    show sayaka a_17

    think "All the more reason to use her."

    show sayaka a_1

    sayaka "Yes. But! We are close friends, right?"

    show sayaka a_17

    sayaka "And do you know what close friends do... Uh, Karen, was it?"

    show carrie a_11
    show sayaka a_5

    carrie "...Carrie."

    show sayaka a_13

    sayaka "Carrie! Yes, it slipped my tongue there. Close friends do what close friends do best. And that is carrying my belongings on the way to school, right?"

    show carrie a_14

    carrie "You want me to... Follow you to... School...?"

    show sayaka a_16
    show carrie a_7

    sayaka "Uh, yes. Do I have to repeat myself or some shit?"

    show carrie a_1

    carrie "Of course! If it can help you then I'd go anywhere!"

    show sayaka a_19

    think "Yep, totally nuts."

    scene black with dissolve
    show bg school entrance day:
        zoom 2.0 xalign 0.15 yalign 0.8
    show sayaka a_5 at center, faceleft
    show carrie a_1 at centerleft, faceright
    with dissolve
    pause 0.75
    show carrie a_15:
        centerleft
        faceleft
        ease 1.5 xpos -0.2
    show sayaka a_8:
        center
        pause 0.5
        faceright

    "After managing to get little miss crackpot to carry my stuff and sending her home again, I waited for John to come around."
    "I never found him when school ended yesterday, and I still had some things to say."

    show sayaka a_16

    "Eventually, I did see him with Corny in tow and-"

    show sayaka a_21
    pause 1.5

    think "What. The. Fuck. Is going on?!"
    title "9th of August (Tuesday)" "Day 2 - John"

    outfit john uniform_pony
    pause 0.5
    show bg school entrance day:
        zoom 2.0 xalign 0.9 yalign 0.8
    show cornelia a_3 at faceleft:
        center
        ease 0.5 yanchor 0.99
        ease 0.6 yanchor 1.00
        repeat
    show john b_0 at faceleft:
        centerright
        ease 0.4 yanchor 0.99
        ease 0.5 yanchor 1.00
        repeat
    with dissolve

    cornelia "You already forgot about the clothes you bought this weekend?"

    show cornelia b_6

    cornelia "You're really turning into some stupid cliche klutz lately."

    show john b_6
    show cornelia b_5

    john "Yeah, yeah, I know..."

    show john b_13
    show sayaka a_21 at left, faceright:
        alpha 0.0

    think "Is she going to be nagging me like this all day...?"
    think "I don't want to go to the pool with some swimsuit I never bought."

    show sayaka:
        ease 1 alpha 1.0 xpos 0.5
    show john:
        faceleft
        ease 0.25 yanchor 1.0
    pause 0.25
    with hpunch
    show cornelia a_7:
        faceright
        linear 0.5 xpos 0.35
    show john b_11

    cornelia "Huh, John? What are you-"

    #SKIP
    show sayaka:
        alpha 1.0

    "Sayaka pushed Cornelia aside as she stomped towards me."

    show john a_32

    think "Shit, I knew this would happen."

    show sayaka a_16:
        ease 0.75 xpos 0.85
    show john b_27:
        faceright
        linear 0.25 xpos 0.6
        pause 0.15
        ease 0.35 xpos 0.7
    show cornelia b_8

    "She grabbed me forcefully without saying a word, steam almost coming out of her head of pure fury."

    show john b_2 at faceleft

    john "Cornelia, please go ahead again today. I think John wants to talk."

    show cornelia a_8:
        ease 0.25 xpos 0.45
    show john b_0

    cornelia "Wha- What's going on?! You think you can just walk around here like you own the place you freaking nerd?!"

    show john b_3
    show cornelia a_5

    john "I'm serious, don't worry about me."

    scene black with dissolve
    scene bg school garden day
    show sayaka a_16:
        faceright
        centerleft
        ease 0.75 xpos 0.6
        faceleft
    show john b_6:
        faceright
        left
        ease 0.5 xpos 0.35
    with dissolve

    "Before long I got pulled so much out of the way, I couldn't see or hear her anymore."
    "She let go her grip by pushing me away from her. We were once more in the garden behind the school."

    show john a_0

    john "So..."

    show sayaka a_21
    show john a_30 with hpunch

    sayaka "{i}{b}SO?!{/b}{/i}"

    show sayaka a_7

    sayaka "What kind of game do you think you're playing here?"

    show sayaka a_20

    sayaka "Is it some kind of game I can join? Are you purposefully ruining my fucking image with... {i}THIS{/i}?"

    show sayaka a_21
    show john b_17

    john "Sayaka, calm down, I know your hair is important to you, but I-"

    show sayaka a_20

    sayaka "But what, John?!"
    sayaka "But what?!"

    show sayaka a_21
    show john b_5

    "I knew she would be pissed the moment when I realized that even with her detailed description of how to take care of her body, there were things I just didn't understand how to do."
    "Not having access to the internet through her phone or computer, which both were password locked, made it even more difficult."

    outfit john casual
    scene bg sadie bathroom day
    show john a_0 at centerright, faceright
    show AN_asset brush:
        zoom 0.25
        xpos 0.6
        rotate -20
        ypos 0.15
    show AN_asset grain as grain
    with dissolve

    "One of my first issues was the brush..."

    show john a_6

    "I was completely unable to tangle it out of her hair, so I had to cut off a tiny section of it in order not to be stuck with a brush in my hair all day long."

    show john b_6
    show AN_asset brush:
        xpos 0.605
        rotate -25
        ypos 0.165

    john "I hope this isn't noticeable..."

    show john b_5

    john "Well, here goes nothing..."

    play sound AN_sfx_scissor
    pause 0.25
    show AN_asset brush:
        easeout 1 rotate -95 ypos 1.2
    pause 0.75
    play sound sfx_whack
    show john b_28:
        ease 0.25 xpos 0.65
    with hpunch

    john "Ah, shit! My foot!"

    show john b_9:
        ease 0.25 xpos 0.62 ypos 0.98
        ease 0.35 xpos 0.61 ypos 1.0
        faceleft
        ease 0.25 xpos 0.64 ypos 0.98
        ease 0.35 xpos 0.65 ypos 1.0
        faceright
        ease 0.25 xpos 0.62 ypos 0.98
        ease 0.35 xpos 0.61 ypos 1.0

    john "Why does that hurt so much?! It's just a fucking brush!"

    show john b_19:
        transform_anchor True
        ease 0.75 rotate -90 xpos 0.5 ypos 1.5
    with hpunch
    play sound sfx_fall

    john "AHH!"
    john "Ow! Fuck!"
    john "Why is there a shampoo bottle on the floor?!"
    john "...Oh wait, that's the one I used."

    scene black with Dissolve(0.25)
    scene bg sadie bathroom day
    show john b_6 at centerright, faceright
    show AN_asset grain
    with dissolve

    "Using her surprisingly hot hair straightener also turned out to be more lethal than i thought..."
    "I, uh... {q}Lightly{/q} burned a section of her hair while using it."

    show john b_28
    show fire:
        zoom 0.35
        xpos 0.625
        ypos -0.05
    play sound AN_sfx_fire_start
    pause 1
    play music AN_bgm_fire_loop

    john "OH FU-"

    show john:
        faceleft
        ease 1 xpos -0.2
    show fire:
        xpos 0.64
        rotate 25
        ease 1 xpos -0.225
    stop music fadeout 1

    john "WATER!"

    play sound sfx_fall
    with hpunch
    pause 1.5

    john "Who put a shampoo bottle on the floor again?!"

    scene black with dissolve

    "Or when I had to... Change her pads..."
    "..."
    "Yeah, I am just going to leave out that mental image so you don't have to witness that bloody battle of mine."
    "..."
    "That sounded really wrong."

    outfit john uniform_badhair
    outfit AN_sayaka uniform_pony
    scene bg sayaka bedroom day
    show john b_25 at centerleft, faceleft
    show AN_asset grain
    with dissolve

    "And when I woke up today, my hair was a complete mess (not surprisingly)."

    show john b_15

    "The only idea to save it was to bind it into a ponytail which disguises most of the problems I had yesterday."
    "Or at least it was the only thing I could think of."

    hide john
    show AN_sayaka b_17 at centerleft, faceleft
    with dissolve
    outfit john uniform_pony
    show john b_17 at centerleft, faceleft
    hide AN_sayaka

    john "..."
    john "My hand is stuck."
    "So, basically what happened can be summed up into one word: {i}{b}Fuck{/b}{/i}."

    scene bg school garden day
    show sayaka a_16 at center, faceleft
    show john b_5 at centerleft, faceright
    with dissolve

    "All of this wouldn't have been an issue if I had someone to help me, but... Her mom essentially told me to {q}deal with it myself{/q}."
    "I could never have expected more of a cold response from a parent than that."

    show john a_20

    john "I know this is something that is difficult to repair, alright?"
    john "I suck at doing your hair and applying whatever else you have to your skin and face, and I'm sorry about it."

    show john a_13

    john "If there is anything I can do to make it up for you-"

    show john a_27
    show sayaka a_22 with hpunch

    sayaka "Ooo~~~ohoho, so you're going that route, huh?"

    show sayaka a_23

    sayaka "Okay, no problems. If that's how we're doing this, I guess I'll see you later then."

    show john a_30 behind sayaka:
        pause 0.35
        faceleft
        ease 0.25 xpos 0.4
    show sayaka a_21:
        ease 1.5 xpos -0.2

    sayaka "Hmph."

    pause 1.5

    "..."
    think "...She... Left...?"

    show john b_27

    think "What the hell just happened?"

    show john b_22

    think "I was sure she would take out a knife at worst or force me to skip school at best..."

    pause 1

    think "I'm getting a bad feeling about this."

    scene black with dissolve
    play sound sfx_running

    "Despite several alarms going off that this was way too unusual, I decided to head to the first class of school anyways."
    "Maybe talking to her is just going to make things worse and this is how she copes with it."
    think "But she really is way too set on this beauty-crap."

    scene bg classroom 4 day
    show cornelia a_4 at Position(pos=(0.25, 1.15), anchor=(0.5, 1.0)), faceleft
    show john a_0 at right, faceleft:
        alpha 0.0
    with dissolve

    "Cornelia was already sitting in her seat when I looked into the classroom."

    show john at centerright:
        ease 0.5 alpha 1.0
    with ease
    show cornelia at faceright
    pause 0.5
    show cornelia a_7

    "As soon as I walked into the classroom, she hurried up to me."

    #SKIP
    show john:
        alpha 1.0
        faceleft

    show cornelia b_8 at Position(pos=(0.25, 1.0), anchor=(0.5, 1.0)) with ease
    show cornelia:
        ease 0.5 xpos 0.5
    pause 0.15

    cornelia "Oh my god, Sayaka, what was up with him? He didn't hurt you, right?"

    #SKIP
    show cornelia at center

    show john a_10

    john "We were just talking. It's no biggie."

    show cornelia b_5
    show john a_0

    cornelia "No, you were clearly not just talking. That face of his wasn't the face of someone who just {q}wants to talk{/q}."

    show cornelia b_8

    cornelia "I am getting totally worried about you, you're doing weird shit all day since school started again..."
    think "Of course she would catch on to me. Apparently Sayaka was being a bitch towards Cornelia normally. And since I usually don't interact with them, it's hard to tell how I should act sometimes..."

    show john a_13

    john "Shush, I'm serious, it's nothing to worry about."

    show cornelia a_6 at faceleft

    cornelia "{size=-5}Hmph, I just want to help...{/size}"

    show john a_32

    think "Cornelia really deserves better than to hang out with this wicked witch."

    hide john
    hide cornelia
    with dissolve

    "School-day was once more normal. Yesterday was almost entirely homeroom, so we had our first classes today."
    think "It's nice to just space out and do classes like I was myself."
    "Luckily, me and Sayaka were both seniors, so I could follow the class like normal."

    scene bg classroom 1
    show jack a_0 at center, faceleft
    with dissolve

    "Best thing even: During Mallory's class just before lunch, I wasn't targeted. Not even once."
    "Which made me feel even better, since Sayaka would be getting a taste of her own medicine when she experienced class with him."
    "I would delight in seeing it happen, but sadly she wasn't in the same history class as me."

    show jack a_1

    "To make up for me missing her reaction to this guy, I dared try to answer one of his questions, and was told I did a good job."

    show jack a_0

    think "Wait, doesn't that mean that this guy is just some pathetic bully who acts on some kind of vendetta...?"
    think "Come to think of it, what even have I ever done against this moron? He clearly doesn't do it because of my personality or {q}inadequate knowledge{/q}, since I'm having classes just fine with him like this."
    "It was food for thought, but I didn't want to waste any more time thinking about him. He didn't deserve it."

    scene black with dissolve
    show bg lunch:
        zoom 2.0 xalign 0.2 yalign 0.35
    show john b_6 at Position(pos=(0.5, 1.15), anchor=(0.5, 1.0)), faceleft
    show cornelia a_1 at Position(pos=(0.3, 1.15), anchor=(0.5, 1.0)), faceright
    show rita b_0 at Position(pos=(0.7, 1.15), anchor=(0.5, 1.0)), faceleft
    with dissolve

    john "{i}Sigh...{/i}"

    show rita b_2

    rita "Girl, you're awfully timid right now."

    show john a_0
    show cornelia a_5

    john "You think?"
    "I was being forced to sit with Sayaka's friends since, well, they kind of pulled me to the table."
    "I barely knew anything about Rita, or the other people I literally didn't even know the names of and luckily didn't bother talking with me."
    cornelia "I'm sure it's because of John."

    show john b_3

    john "Can you drop that already?"

    show cornelia a_3

    cornelia "I know he is doing something shady with you. And not the {i}shady{/i} kind of shady."

    show john a_0
    show rita b_10
    show cornelia a_5

    rita "Ooh, that kind of shady."
    think "They aren't ever going to let this topic die out, are they..."

    show john a_21
    show rita b_0

    "I just gruntled and ate into one of the burgers Cornelia brought us."

    show john a_13
    show cornelia a_1

    "They kept on talking about whatever they talked about, I heard a few mentions of clothes, so that's probably it."
    "I was sure that Sayaka would be absolutely burning with passion if she could talk about it herself, but I really didn't give a damn."

    show rita b_2

    think "Maybe I can sneak off to the bathroom or something..."

    show cornelia a_0
    show rita b_11

    rita "Earth to Saya, helloo~~~o?"

    show john b_11 at faceright

    john "Huh, what?"

    rita "What the hell is up with you? I asked you about the Jevi jeans you bought me as a present last week, but you're dozing off like some cliche airhead on me."
    rita "Besides, why the hell you wearing a ponytail? I thought your {q}hair that resembles the ocean breeze{/q} was your shitty schtick."

    show john b_13

    john "I, uh... Had some accident yesterday with my hair...?"

    show rita a_12
    show cornelia a_5

    rita "{i}Tch, {/i}if I bore you that much I might as well leave for one of the lame-o tables."

    show cornelia a_7
    show john b_11 at faceleft
    show rita b_2

    cornelia "Hey, look at that."

    show rita at faceright
    show john at faceright
    show cornelia a_5
    show katrina a_6 blush at right, faceleft:
        faceleft
        alpha 0.0

    "She caught my attention as she pointed behind me."

    show bg lunch:
        ease 0.5 xalign 0.5 yalign 0.5
    show katrina:
        pause 0.25
        ease 0.5 xpos 0.6 alpha 1.0
    show cornelia at left:
        ease 0.5 alpha 0.0
    show john at centerleft:
        ease 0.5 alpha 0.0
    show rita at center:
        ease 0.5 alpha 0.0
    with ease
    hide john
    hide rita
    hide cornelia

    think "Kat? What is she..."

    show katrina at offscreenleft with ease:
        alpha 1.0

    "Kat sped past and left the lunchroom."
    think "Was she... crying?"

    show bg lunch:
        xalign 0.2 yalign 0.35
    show john b_11 at Position(pos=(0.5, 1.15), anchor=(0.5, 1.0)), faceright
    show cornelia a_5 at Position(pos=(0.3, 1.15), anchor=(0.5, 1.0)), faceright
    show rita b_2 at Position(pos=(0.7, 1.15), anchor=(0.5, 1.0)), faceright
    with dissolve

    rita "Now this is unusual."
    "I spun my head to the table me and my friends normally sat at."

    show bg lunch:
        xalign 0.8 yalign 0.8
    hide john
    hide cornelia
    hide rita
    show kyoko b_4 at centerright, faceleft
    show kiyoshi a_5 at centerleft, faceleft
    show sayaka a_17 at center, faceleft
    with dissolve

    "I could catch a glimpse at Sayaka with..."

    show kiyoshi a_3 at faceright

    "A smile on her face."
    think "That bitch. What did she do?"

    show bg lunch:
        xalign 0.2 yalign 0.35
    show john b_33 at Position(pos=(0.5, 1.15), anchor=(0.5, 1.0)), faceright
    show cornelia a_2 at Position(pos=(0.3, 1.15), anchor=(0.5, 1.0)), faceright
    show rita a_9 at Position(pos=(0.7, 1.15), anchor=(0.5, 1.0)), faceright
    hide sayaka
    hide kyoko
    hide kiyoshi
    with dissolve

    think "There is no way that Kat would storm out of the room crying without something big happening."

    show john b_31:
        ease 0.2 xpos 0.5004
        ease 0.2 xpos 0.5
        repeat

    cornelia "Aa~~haha, the nerd-group is having a fall-out? That's too hilarious, right Saya?"

    show cornelia b_8

    cornelia "Wh- Saya? What's wrong?!"

    show john at faceleft
    show rita b_12 at faceleft

    "I hadn't noticed it myself, but a few tears managed to roll down my face."
    think "Shit, this is probably because I cry faster while in Sayaka's body."

    show john a_20

    think "This has to be completely unnatural for the others to see."
    "I hadn't really paid it much of a mind before, but now I seriously realized that Sayaka held my life in her hands. She could completely cut me off from my friends if she wanted to."

    show john a_35

    "And I was both furious and sad at the thought."

    show rita a_13

    rita "Are you actually crying about this? Christ you're pathetic."

    show cornelia b_3

    cornelia "Hey, don't you dare say that again!"

    show john b_22
    show cornelia b_5
    show rita a_12

    john "It's nothing."

    show cornelia b_3

    cornelia "You keep saying that! That nerd dragged you with him earlier and now this? What's going on Saya?"

    show cornelia b_5
    show john a_15

    think "Alright, Sayaka. If this is how you want to battle..."
    think "If she keeps her reputation by being a massive douchebag, let's see how she likes it when she steps down from this position entirely and gives the spotlight to someone else."

    show john b_16

    john "Something has been going on, but I can't tell you."

    show john at faceright

    john "I could, but this is my way of paying that bitch back for now."

    show john b_17
    show rita b_10
    show cornelia b_0

    "Curiously, they both leaned in as if waiting for some kind of plan."

    show john a_17

    think "It isn't normal for them to breed a plan for revenge, right...?"

    show john a_16 at faceleft

    john "Instead, I'm paying for your food today."

    show cornelia b_5
    show rita b_2
    show john a_15
    play sound AN_sfx_coins

    "While both kept staring at me in wonder of what I just told them, I got out Sayaka's wallet and gave them a chunk of money, way more than what the food costed."

    pause 1.5

    rita "...You're what?"
    john "It's for you. I want to give both of you something but I only have money on me right now."
    "They looked at each other as looked at me as if I had gone insane."

    show cornelia b_6
    show john b_17
    show rita a_8

    cornelia "I don't know what he has done to traumatize you..."
    "She pushed the money back to my side of the table."

    show cornelia b_5

    cornelia "But don't do this to yourself, Saya. You can't give anyone money. If anything, they should be giving it to you!"

    show cornelia b_7
    show john at faceright

    "Rita on the other hand had already pocketed hers."
    "Cornelia looked furious as she saw the last bit of this motion happening."

    show rita a_11
    pause 1
    show rita b_11

    rita "What? She gave it to me."

    show cornelia b_3
    show john a_6

    cornelia "Can't you see that John has traumatized her or some shit?!"

    show rita b_12
    show cornelia b_5

    rita "Who cares? She could just not give it to me while she's traumatized. Not my problem."

    show rita b_2
    show john a_0

    john "Cornelia, it's fine. You can have it. And I'm not traumatized or whatever kind of condition you come up with next."
    john "I just thought during the summer that I was maybe a bit too stuck up for my own good..."

    show rita b_12
    show john a_1

    john "A bit too arrogant too..."

    show cornelia b_6

    john "Oh, and I was a total bitch during the last two years, really an absolute bitch of a devil."

    show john a_12

    john "Very snooty, way too posh, a real toffee-nosed, la-di-da asshole of a bully."

    show john a_2
    show cornelia a_7

    john "You know me, a real whore."

    show john a_30
    show rita b_11

    rita "Alright, that's it, I'm out."

    show john b_13 at faceright
    show rita:
        faceright
        ease 1.5 xpos 1.2

    "It didn't bother me that Rita suddenly felt like leaving. Maybe she felt as if my words were directed at her."

    show john at faceleft

    cornelia "Wha- Why are you leav- Actually, forget that!"

    show cornelia b_3

    cornelia "What the fuck is going on in your head, Saya? You're none of the above!"

    show john a_14

    john "I want to be a better person this year, okay? Like, a real angel."

    show cornelia b_8
    show john a_1

    cornelia "A real angel? Are you... Oh god, you've lost your mind..."

    show cornelia a_6

    cornelia "Alright then, let's just go with this farce of yours."

    show john b_2
    show cornelia a_0

    john "I'll try not to let it be a farce. And it starts with you. Here."

    show cornelia a_5
    show john b_1

    "I once more pushed the money she rejected towards her."
    john "I probably spent some of your money sometime ago without paying you back. And if I didn't, please take it as a gift. We're best friends, right?"

    show cornelia b_7

    cornelia "You- You really think we're best friends?"

    show cornelia a_2

    cornelia "Of course! We're friends, I always knew that. BFFs after all, right?"

    show john b_2
    show cornelia a_1

    john "That's it."

    show john b_6

    think "I think I'm going to puke at the amount of bubbly bullshit I just spewed spontaneously."

    outfit sandra suit
    accessory sandra set glasses
    scene black with dissolve
    scene bg classroom 4 day
    show john a_0 at Position(pos=(0.6, 1.1), anchor=(0.5, 1.0)), faceleft
    show sandra a_0 at left, faceright:
        alpha 0.0
    with dissolve

    think "Okay, I admit. This is actually kind of stupid and a spur of the moment thing."

    show john a_32

    think "I mean, getting payback by being nice is not exactly a conventional payback method, is it?"

    pause 1.5
    show john a_5

    think "I have to talk to her as soon as possible though."
    think "Damn these freaking classes though. I found out I only share one class with her and that's twice a week. And one of them is on a monday, so only saturday remains."

    show sandra:
        ease 0.75 alpha 1.0

    "I was having class with my mom right now, which was calming my nerves a bit."

    #SKIP
    show sandra:
        alpha 1.0

    "Being able to see her here and there was at least something I could do regularly."
    "She already put us into different groups for a group project, even though we were two days into the school year."

    show john a_6

    think "She really has no chill."

    show john a_5
    show sandra:
        ease 0.5 alpha 0.0

    "I barely knew anyone in here apart from Sayaka's group, which, apart from Cornelia, I've barely interacted with so far."

    hide sandra
    show john a_13
    show irene b_3 at centerleft, faceright:
        alpha 0.0
    show allison a_1 at left, faceright:
        alpha 0.0

    "And since my lifeline squirt wasn't around, I would likely have to pair up with complete strangers who knew Sayaka."
    "Although I really didn't want to pretend being all cutesy and sickening like I was earlier to Cornelia."

    show irene at Position(pos=(0.40, 1.0), anchor=(0.5, 1.0)):
        ease 0.5 alpha 1.0
    show allison at Position(pos=(0.25, 1.0), anchor=(0.5, 1.0)):
        ease 0.5 alpha 1.0
    with ease

    irene "You up for us?"

    show irene b_0:
        alpha 1.0
        ease 0.5 ypos 1.1
    show allison a_0:
        alpha 1.0
        pause 0.2
        ease 0.5 ypos 1.1
    show john b_11

    "With Allison in tow, she already sat herself at my table as if she were accepted."

    show irene b_3

    irene "Or do you rather want to be paired with Arnold?"

    show irene b_0
    show john b_6

    john "Oh no, not Arnold. I would never want to do that."

    show john b_0

    think "That came out way too sarcastic and annoyed..."
    irene "We want to pick topic five."

    show allison a_1

    allison "We both had something similar for our exams, so it's going to be a piece of cake."

    show allison a_0

    john "That's reassuring."

    show john a_32

    think "Even though I could probably do any of these topics without a lot of issues. Being the teacher's son in this case really paid off."

    show john b_1

    "Again, I was pleasantly surprised at how... Well, decent these two girls were."
    "Maybe Irene had a bit of an asshole factor in her voice, sounding annoyed all the time, but they just focused on getting as much done as possible for today without really saying much out of the ordinary."
    "Not like I would ever talk with them again if we got our swapping situation fixed, but it's nice to know that not all people are like pinky."

    show allison a_2
    show irene at faceleft

    allison "Oh, I heard you guys were getting new outfits for cheerleading this year!"

    show irene at faceright
    show allison a_0
    pause 1.5
    show john b_13

    john "Cheer... Leading?"

    show irene b_4

    irene "You're still captain?"

    show john b_27

    john "..."

    show irene

    think "Fuck."
    think "I am not doing that. I didn't know she was on the cheerleader team."
    irene "Is that a no?"

    show john b_14

    john "I... guess you will have to wait and see!"

    show irene b_3
    show allison a_3

    irene "Is it really worth it to make this some dumb surprise if you're doing training in, what, 25 minutes?"

    pause 3

    john "25 what now?"

    show irene b_4
    show allison a_6

    irene "You didn't seriously forget that you have cheerleading training today, did you?"

    show john a_8

    think "And this is the part where a benevolent god ends my suffering."

    show john a_6

    "But actually, this was an opportunity to get back at Sayaka, wasn't it?"

    show john b_2
    show irene b_2
    show allison a_3

    john "Uh, you know what? I have to go to the bathroom real quick."

    show irene at faceleft
    show john a_15:
        ease 1 ypos 1.0
    pause 0.75
    show allison a_6
    pause 1
    show irene b_3 at faceright

    irene "You, uh, do that. We're going to pack up anyways now."

    show irene b_4
    show john a_16

    john "Perfect. And don't follow me into the bathroom."

    show allison a_3
    show john a_15

    allison "Why would we do that?"

    show john a_17

    john "Don't girls norma- Whatever, don't wait for me!"

    show john b_18:
        faceright
        ease 1 alpha 0.0 xpos 1.0
    pause 1
    play sound sfx_sliding_door_close
    show irene b_4
    pause 1
    show irene at faceleft
    hide john

    irene "You noticed it too?"

    show allison a_2

    allison "Do you think what Rita told us was serious?"

    show allison a_3

    irene "I thought it was a joke, but she isn't being bitchy at all."

    show irene at faceright

    irene "Something must have happened. That girl doesn't go tame overnight."
    irene "She's suddenly like a completely different person."
    irene "...Maybe it actually worked?"

    show allison a_6

    allison "What worked?"

    pause 1
    show irene b_0 at faceleft

    irene "I'll tell you once we're out of here."

    scene black with dissolve
    scene bg school hallway day
    show john b_5 at center, faceright
    with dissolve

    "I had to confront Sayaka about this cheerleading crap and Katrina."
    "Fortunately, all senior seem to have their own little section of the school for themselves, so all I would have to do is look into the rooms that were in use and hopefully drag her outside quickly."

    scene bg school classroom hallway day
    show sayaka a_16 at centerright, faceleft
    show john b_13 at left, faceright:
        alpha 0.0
    with dissolve

    "That being said, finding her turned out to be easier than expected."

    show john:
        ease 0.75 alpha 1.0 xpos 0.4
    show sayaka a_21

    "For whatever reason, she was just standing in the hall outside one of the classrooms. We both met eyes right then."

    show john b_19:
        alpha 1.0
        xpos 0.4
    show sayaka a_7

    both "What the hell are you doing here?"

    show john b_28
    show sayaka a_20

    both "Huh?"

    show sayaka a_7
    show john b_27

    sayaka "Aren't you supposed be in class or some shit?"

    show sayaka a_16
    show john b_18

    john "I'm excused! And I could ask you the {i}exact{/i} same thing!"

    show john b_17

    sayaka "That jackass of a dickhead Mallory sent me out here for no fucking reason. What the hell is his deal with singling me out all class?!"

    show john a_2

    john "You seriously had Mallory already? A~~ahaha, I could almost feel bad for you."

    show john a_0
    show sayaka a_7

    sayaka "Shut it, clown."

    show sayaka a_16
    show john b_19

    john "No, you better shut it. What the fuck happened at lunch today? Kat stormed out crying while you were grinning!"

    show john b_17
    show sayaka a_17

    sayaka "Hah, she only got what she deserved."

    show john b_18

    john "Sayaka, I'm fucking serious right now. What. Did. You. Say?"

    show john b_17
    show sayaka a_16 at faceright

    sayaka "What do you care? You're better off not associating with that backstabbing whore anyways."

    show john b_19

    john "Backsta- What?! You told me to act like you, yet you attempt to kill off any bonds I have with my friends within a fucking day!"

    show john b_28

    john "All because of your dumb freaking hair!"

    show john b_9

    john "Which isn't even your hair right now!"

    show john b_17
    show sayaka a_20:
        faceleft
        ease 0.5 xpos 0.65
    with hpunch

    sayaka "You better watch what you're saying next. If you ever tell me that that hair right there is yours, you will be entering a circle of hell you didn't know existed yet."

    show sayaka a_21
    show john a_8

    john "Who cares! If you don't fix it, you're going to enter circles of hell you can't even think of yourself! So you better fucking fix what you did."

    show sayaka a_17:
        faceright
        ease 0.75 xpos 0.75
    show john a_17

    sayaka "You can't even figure out how to make threats without copying mine. How cute."

    show john a_35

    think "I swear, if I have to listen to one more word of hers..."

    show sayaka a_16 at faceleft
    show john a_17

    sayaka "And if you think I am ever going to talk with her again, then you are very mistaken. So if you're so buddy buddy with the lowest scum you can find in the trash, why don't you go try your luck with her?"

    show sayaka a_17

    sayaka "I would really like to see you try. And make sure to film it, I would really treasure seeing any attempt you make. Heh."

    show john b_19

    john "That's it. I'm done playing by your rules. You've been nothing more than an absolute maniac who would attempt to ruin the life of someone else over {b}fucking hair!{/b}"

    show sayaka a_16:
        pause 1.5
        faceright
    show john b_17

    sayaka "Still better than whatever you think you are. Hmpf."

    show john b_17 blush

    "I've never been so angry at talking with someone else in my life than now."
    "It's as if she deliberately tries to piss me off."

    show john b_15

    think "Yes, fuck it. I'm telling them right now that we were swapped. Not like she can do anything about it."
    think "She drew the short stick. I've got the better looks and the better personality. Let's see how she strides around with absolutely no friends for the next few days."
    think "Deserves her right for how terrible she is."

    play sound sfx_bell
    show sayaka a_16
    show john a_13

    "As if it was a symbol to end this arguing, the bell rung to signal that the school day is over."

    show bg school classroom hallway day open behind sayaka with dissolve
    play sound sfx_sliding_door_open
    show sayaka:
        ease 0.5 xpos 0.85 alpha 0.0
    show katrina a_6 at centerright:
        faceleft
        alpha 0.0

    "She left me the very moment she heard the bell and fucked off into the classroom."

    show katrina:
        ease 0.5 xpos 0.6 alpha 1.0
    hide sayaka
    show john a_28

    "Thankfully, Kat seemed to be in the same class here, because left the classroom a few seconds after Sayaka entered it again to pick up {i}my{/i} belongings."

    show katrina a_4:
        alpha 1.0
        pause 0.75
        faceright
        ease 1 xpos 1.3
    show john b_27

    "But she pretty much power jogged away into a different direction the moment she saw me."

    show john:
        ease 1.5 xpos 1.5

    "I went after her and called out to her to make sure she noticed me."

    scene black with dissolve
    scene bg lockers day
    show katrina a_4 at offscreenleft, faceright
    show john b_28:
        offscreenleft
        faceright
    with dissolve
    show katrina at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0)) with ease
    show john:
        pause 0.25
        ease 0.5 centerleft

    john "Kat! Hey! Wait!"

    #SKIP
    show john at centerleft

    show katrina a_9

    "She did react to it and threw me a short glance, but immediately decided to ignore me when she saw who was calling out to her."

    show john b_22

    think "Well, no wonder. She doesn't like Sayaka."
    "I had followed her until we reached the locker now."

    show john b_13

    john "Hey Kat, please hear me out."
    katrina "...What?"

    show john b_22

    john "I, uh... I saw what happened during lunch...."

    show katrina a_18 at faceleft

    katrina "Oh yeah? Good. Because this is my declaration of surrender. Congratulations. You got me. Are you happy now?"

    show john b_27
    pause 1

    john "Huh?"

    show katrina a_20

    katrina "I always knew you were a scumbag deep down. But I never thought you would use a strategy that low just to get back at me. You win."
    think "Hold on... What?"

    show katrina a_15

    john "Kat, I don't know what you're talking about... Did- Did John say anything?"

    show katrina a_12

    katrina "Fuck off, Sayaka. Do you want this on video? That's probably what you're thinking, right? You want this on video so that you can {i}treasure{/i} something for once in your life, don't you?"
    katrina "Bring forth your posh-ass camera crew you rented off Bitch-Bay and just get it over with. Else, just leave me alone."

    show katrina a_9

    katrina "I hope you finally got your dumb revenge."

    show katrina a_6:
        pause 1
        ease 1 xpos -0.2
    show john a_27 behind katrina:
        pause 1.35
        faceleft
    play sound sfx_door_slam

    "She slammed her locker and left."

    show john b_22

    "I was lost for words. This wasn't... At all what I expected."
    "I honestly almost felt like crying."

    show john b_22

    think "Dammit, I am too sensitive like this..."
    think "What could that girl even have told Kat for her to react this way?"
    think "It's like a nuke just exploded."
    think "Why did she do this? This motherfucking bitch."

    show john a_20

    "I realized that I was just standing there for a few minutes thinking about what just happened."

    show john b_4:
        ease 2 xpos -0.2

    "With my head down, I just decided to head to Sayaka's home."

    scene black with Dissolve(1.0)

    title "9th of August (Tuesday)" "Day 2 - Night"

    scene bg sayaka kitchen night lights off
    show john b_25 at offscreenleft, faceright
    with dissolve
    play sound sfx_door_open
    pause 0.25
    show john at left with ease
    pause 0.25

    "Just like yesterday, nobody was home."

    show john at faceleft
    pause 0.75
    play sound sfx_lockpick
    show bg sayaka kitchen dusk behind john
    pause 0.5
    show john b_22:
        faceright
        ease 0.75 center

    "Her parents came home after I had gone to bed yesterday."
    "It was the loneliest home I had ever seen in my life."

    pause 1.5

    think "Oh yeah, cheerleading..."

    show john b_6

    "I decided just to say {q}fuck it{/q} to cheerleading at this point. If Sayaka doesn't want to take care of my life, I sure as hell had no obligation to take care of hers."
    "They would have to figure things out without me."

    show john b_25

    think "Not that me being there would be of any help..."
    "I felt extremely hungry when I entered through the kitchen and just wanted to down like four cups of noodles."

    show bg sayaka kitchen dusk:
        ease 0.75 zoom 2.0 xpos 0.1 ypos 0.7
    show john b_17:
        ease 1 xpos 0.8

    "The refrigerator had some cups stored after I rummaged through it."

    show john b_22

    "I really just felt like eating for no discernable reason. Was it because I was sad? Is Sayaka a stress eater and it affects me?"

    show john a_17

    "I decided not to dwell on it. It's not my body. To hell if she has a diet."

    scene black with dissolve
    play music AN_bgm_background_tele
    pause 1
    show bg sayaka livingroom night lights off:
        zoom 2.0 ypos -0.5
    show john a_5 at Position(pos=(0.65, 1.2), anchor=(0.5, 1.0)):
        transform_anchor True
        rotate -5
    show AN_asset spotlight:
        flip
        zoom 3.5
        rotate 180
        ypos -0.5
        xpos 0.1
        block:
            ease 0.4 alpha 0.9
            ease 0.2 alpha 0.8
            ease 0.2 alpha 0.75
            ease 0.2 alpha 0.8
            ease 0.2 alpha 0.75
            ease 0.35 alpha 0.9
            ease 0.3 alpha 0.6
            ease 0.4 alpha 0.9
            ease 0.2 alpha 0.8
            ease 0.2 alpha 0.85
            ease 0.2 alpha 0.8
            repeat
    show black as dim:
        alpha 0.5
    with Dissolve(1)
    pause 2
    play sound sfx_door_open
    pause 1
    show john b_5 at faceleft:
        ease 0.25 rotate 0

    "Seven cup-noodles in and someone finally opened the door."

    #SKIP
    show john at Position(pos=(0.65, 1.2), anchor=(0.5, 1.0)), faceleft
    show AN_jacob a_0 at offscreenleft, faceleft:
        zoom 0.95
        alpha 0.0

    "I was watching TV with a completely empty mind. When I looked at the clock, I saw that it had already become half past eleven in the evening."

    play sound sfx_lockpick
    hide dim
    show bg sayaka livingroom night behind john:
        zoom 2.0 ypos -0.5
    hide AN_asset spotlight
    show AN_asset sayakasofa as sofa behind john:
        zoom 2.0 ypos -0.5
    pause 0.5
    show AN_jacob behind sofa:
        faceleft
        ease 0.75 alpha 1.0 centerleft
    pause 0.25

    AN_jacob "Saya? What are you doing in here?"

    #SKIP
    show AN_jacob:
        alpha 1.0

    show john b_4
    show AN_jacob a_2

    "I really felt like talking to someone and hoped he would sit down just so I could put my mind to something, but instead, he had this contempted look as he saw the amount of food I had eaten today."

    show AN_jacob a_3:
        ease 1.5 right

    AN_jacob "Make sure you clean up after yourself. I'm having someone come over tomorrow."

    show AN_jacob:
        ease 0.75 alpha 0.0

    "..."

    hide AN_jacob
    show john b_25 at faceright

    "What a prick. He didn't even ask me how my day was or anything."
    "I was positive that I had a sad face right now. What a terrible parent..."

    play sound sfx_door_open
    show john b_17 at faceleft
    show AN_saki a_0 at left, faceright behind sofa:
        alpha 0.0
        zoom 0.9

    "Only a minute or two later, the door opened again."

    show AN_saki:
        ease 0.75 alpha 1.0 centerleft

    "Her mom went through the livingroom..."

    show AN_saki a_4

    "Gave me a short glimpse..."

    show AN_saki a_0:
        ease 1.5 alpha 0.0 offscreenright
    show john b_18:
        pause 0.35
        faceright

    "And then she promptly fucked right off without even bothering to say a single word."

    hide AN_saki
    show john a_4

    think "What a miserable family..."

    show john b_4

    "There was no comfort in living here. They had a big TV, comfy sofas, a luxurious kitchen. But for what reason?"
    "They didn't interact, they didn't watch TV together, they didn't eat at the same table and didn't appear to make their own food."
    "The only things I had heard her parents say were six sentences at most in two entire days."
    "This house was like a frozen home. Completely cold with no love. And I deducted this within two days! That's how bad it is!"

    show john b_25

    think "I just want this day to be over..."

    stop music fadeout 1
    scene black with dissolve
    outfit john uniform_badhair_b
    scene bg sadie bathroom day
    show john b_17 at centerright
    show AN_asset brush:
        zoom 0.25
        xpos 0.6
        rotate -20
        ypos 0.15
    with dissolve

    "I wanted to go to bed. My hair was starting to really itch, so I thought I could try to straighten it out a bit with a hair brush."
    "Once again, because of how long her hair is, I got the brush stuck."

    show john b_19

    john "{size=-5}Ugh, fucking brush...{/size}"

    show john b_17

    "At first there was just a bit of resistance, but it just managed to stick so incredibly quickly."
    john "{size=-5}For fuck's sake...{/size}"
    think "Getting this thing out without any help is freaking impossible..."

    outfit AN_saki casual
    scene bg sayaka kitchen night lights on
    show AN_saki a_0 at centerleft, faceright
    with dissolve

    "But that was the thing. Getting help."
    "Yesterday I tried it with her mom, but she didn't bother."
    "Her dad has probably already went to bed from what I heard, so..."

    show john b_5 at offscreenright, faceleft
    show AN_asset brush:
        flip
        zoom 0.25
        xpos 1.2
        ypos 0.2

    think "...I could at least try..."

    show john at right
    show AN_asset brush:
        xpos 0.85
    with ease

    john "H- Hey, mom..."

    show AN_saki a_2

    AN_saki "...What is it? I'm eating."

    show john b_22

    john "Can you please help me get my brush unstuck today...?"

    show AN_saki a_8

    AN_saki "{i}...Sigh...{/i}"

    show AN_saki a_3
    show john b_27

    AN_saki "Go do it yourself, Sayaka. You're not a child anymore."

    show AN_saki a_4
    show john b_28

    john "Wh- But why?"

    show john b_22

    john "But it's just a few minutes to get it out..."

    show AN_saki a_8

    AN_saki "A few minutes of my freetime. We've talked about this before. It's not difficult to understand, even for you."

    show AN_saki a_0

    AN_saki "And stop using your uniform clothes the entire day."
    john "..."

    show AN_saki a_2

    AN_saki "Now go to bed."
    john "..."
    john "Yes, mom..."

    scene black with dissolve
    outfit sayaka casual
    pause 1
    scene bg main room dusk
    show sayaka a_5 at centerleft, faceleft
    with dissolve
    pause 1.5
    show sayaka a_16 with hpunch

    think "{size=+5}UGH!{/size} It's all just stupid fetish porn on these sites!"
    think "I've been looking at this for over an hour now and all of it just garbage!"
    "Really, I was so frustrated. There has to be some way to revert this swap."
    "But of course the internet is full of bullshit with absolutely no real evidence. Even though I tried to be as specific as possible when searching for swaps on the internet, everything was just some stupid fiction."

    show sayaka a_7

    think "This just makes me tick off even more!"

    show sayaka a_5 at faceright

    sandra "{size=-7}John, dinner is ready!{/size}"
    think "Again, like yesterday, Ms. Davis is actually making dinner..."
    sayaka "Yeah, yeah! Coming!"

    show sayaka a_8

    "Yesterday's dinner was actually really nice. It's the type of stuff that we only get when we are in a restaurant or the maid comes over to visit."
    "Daddy once made dinner here and there before he got his promotions, and now I really missed how he made dinner sometimes..."

    show sayaka a_0

    think "Might as well go eat something."

    scene black with dissolve
    outfit sandra casual
    accessory sandra set
    outfit natsumi casual_b
    scene bg main kitchen dusk
    show sandra a_0 at Position(pos=(0.75, 1.15), anchor=(0.5, 1.0)), faceright
    show natsumi a_0 at Position(pos=(0.55, 1.1), anchor=(0.5, 1.0)), faceright
    show sayaka a_0 at offscreenleft, faceright
    with dissolve
    pause 0.25
    show sayaka at left with MoveTransition(0.75)
    pause 1
    show sayaka a_5

    think "Huh?"

    show natsumi at faceleft

    think "Who is that now?"

    show natsumi a_8

    natsumi "Hello John!"

    show sayaka a_2

    natsumi "Can we play games after dinner?"

    show sayaka a_15

    sayaka "Uh- Wha- Uh, sure...?"

    show natsumi a_3

    think "Who the heck is this runt now? John has {i}two{/i} sisters?"

    show natsumi a_11
    show sandra a_9
    show sayaka a_5

    sandra "{i}Sigh...{/i} You immediately ask him before I can say anything, huh?"

    show natsumi a_9 at faceright

    natsumi "Yes! Else you would tell me to leave John alone."

    show sandra a_1
    show sayaka at centerleft with ease
    show sayaka:
        ease 0.25 ypos 1.15

    sandra "Hah, I will need to try outsmarting you next time then."

    show sayaka a_0:
        ypos 1.15
    show sandra a_3

    "I sat down and ate, and boy, was it better than chinese or whatever mom or daddy brought home."

    show sandra a_0
    pause 0.5

    sandra "You seem to be enjoying your food honey."

    show sayaka a_8

    sayaka "Oh, uh, yeah, it's really good."

    show sandra a_5

    sandra "...Say, did something happen in school today?"

    show sayaka a_5

    sayaka "In school?"
    sandra "With Katrina."

    show sayaka a_21
    show natsumi a_0 at faceleft

    "The moment she mentioned her name I got on edge."

    show sandra a_4
    show sayaka a_16

    think "This bitch is probably going to side with her too, just like John."
    sayaka "It was nothing. She got emotional over something and cried. It's whatever."

    show natsumi at faceright
    show sandra a_7

    natsumi "Did someone in Yui's school cry? Why?"

    show sayaka a_5

    think "{i}Yui's{/i} school?"
    sandra "Hmm, alright. From what I heard it sounded a bit more serious though."

    show sandra a_9

    sandra "Oh, and Natsumi, even grown ups can cry, did you know that?"

    show sandra a_1

    sandra "So don't be afraid to do so yourself if you feel sad, right?"

    show natsumi a_9

    natsumi "That's okay, I know that already. Yui cries all the time sometimes when she is alone in her room!"

    show sayaka a_18:
        transform_anchor True
        ease 0.25 rotate 15
        ease 0.5 rotate 5
        ease 0.25 rotate 0
    show sandra a_5
    show natsumi a_0 at faceleft

    "On hearing that I spat out my food almost laughing."

    show sayaka a_10:
        rotate 0

    think "Woo~~owowow, that Yui cries herself to sleep? That's so fucking hilarious, haha."

    show sandra a_2
    show natsumi at faceright

    sandra "You should keep things like that a secret sweetie."

    show sayaka a_6
    show sandra a_3
    show natsumi at faceleft

    sandra "And John, you're not going to be picking up girls if that's how you react to hearing that."

    show sayaka a_10

    sayaka "Heh, sorry-"

    show sayaka a_4

    sayaka "P- Picking up girls?!"
    sayaka "Why would I do that?!"

    show sayaka a_15
    show sandra a_4

    sandra "Don't tell me that you're gay now of all times where you're starting out as a senior."

    show sayaka a_4

    sayaka "No, of course I'm not gay!"
    sayaka "It's just-"

    show sayaka a_16

    think "Screw this woman! Don't think that just because you made me... well, some really good food, that you can have your way with me!"

    show sandra a_1

    think "Is what I'd say, but... I fucking guess John isn't like, gay or something, so I have to play along with liking girls..."
    think "Yuck..."

    show natsumi at faceright
    show sayaka a_5
    show sandra a_3

    natsumi "What is that?"
    sandra "Huh? What's what?"
    natsumi "Gay."

    show sayaka a_15
    show sandra a_8

    sandra "Ah! Nothing! Really, don't say that word."

    show natsumi a_9 at faceleft
    show sandra b_5 at faceleft
    show sayaka a_5

    natsumi "Oo~~okaay."
    sandra "{size=-5}Phew...{/size}"

    show sandra a_0 at faceright

    "And the girl dug back into her food."
    think "Come to think of it, her name was Natsumi, right? So the Natsumi that was supposed to come over here today..."
    think "Why the hell are they taking care of some random kid?"
    think "This family is so weird."

    scene black with dissolve
    scene bg main room night
    show sayaka a_5 at centerleft, faceleft
    with dissolve
    show AN_asset door at offscreenleft:
        zoom 1.25
    show natsumi a_8 at offscreenleft

    "Before I was involved in any more pointless situations I threw my plate on the counter and went back up to hopefully find anything on the internet about this pile of garbage situation I was in currently."
    "It wasn't long before that little runt barged into the room right after."

    play sound AN_sfx_crash
    show AN_asset door:
        ease 1.25 xpos 1.6 rotate 720
    show sayaka a_15:
        pause 0.5
        faceright
        pause 0.75
        faceleft
    pause 1
    show natsumi at left with ease

    natsumi "John, let's play Maria Kart!"

    show sayaka a_16
    show natsumi a_9

    sayaka "Hold up, what are you doing in this room? Shush!"

    show natsumi a_0

    natsumi "Shush?"
    sayaka "I am doing something important here!"

    show natsumi a_7

    natsumi "Eehhh? But you said we could play!"

    show sayaka a_15

    sayaka "What? I did?"

    show sayaka a_2

    sayaka "Was that what you asked me at dinner?"

    show natsumi a_5

    natsumi "Of course, you meanie!"
    think "What... Is this how this guy spends his evenings? Playing games with a... little girl?"
    think "I can endure one day of this, maybe. But this better not happen again."

    show sayaka a_16
    show natsumi a_0

    sayaka "Fucking fine, if it makes you shut up. Go find that stupid game."

    show natsumi a_5

    natsumi "That's not a very nice thing to say, John!"
    natsumi "I will tell aunt Sandra if you keep saying that. Mom said you can't say those things."
    sayaka "Wow, a real friggin' angel over here, huh?"

    show natsumi a_9:
        ease 0.75 xpos 0.8
    show sayaka:
        pause 0.25
        faceright
    pause 0.85
    show sayaka a_5
    show natsumi a_8 at center, faceleft with ease

    natsumi "Here, here! Put it in, quick!"
    "She handed me some old-ass CD that I apparently should be {q}putting in{/q} somewhere."
    "I had no idea where the hell this annoying kid wanted me to place it though..."

    scene black with dissolve
    outfit john underwear
    outfit sayaka noshirt
    pause 1
    scene bg sayaka bedroom night lights off
    show john a_4 at center, faceleft
    with dissolve
    pause 1.5

    "This family is even more rotten than Sayaka herself..."

    show john b_4

    "I asked for help once, with something trivial, even."
    "But I was rejected immediately and given a cold shoulder."

    pause 1.5

    "I said I could see the fun in posing around as Sayaka, but if this is how my life would be for god knows how long..."

    scene black with dissolve
    scene bg main room dark
    show sayaka a_24 at center, faceright
    with dissolve

    "This family is so freaking crazy..."

    show sayaka a_16

    "I have to admit, at least Ms. Davis pays attention to me like this, but having to deal with people who are buddy-buddy all the time is a pain in the ass."
    "This kid, who just {i}had{/i} to be there until late evening especially."

    show sayaka a_9

    "I... wouldn't mind replacing Ms. Davis with my bore of a mom, but..."

    scene black with dissolve
    scene AN_bg fusion room dark
    show sayaka a_16 at centerleft, faceright
    show john b_4 at centerright, faceleft
    with dissolve

    both "I really hope we can swap back soon..."

    scene black with Dissolve(1.5)
    pause 1

    title "11th of August (Thursday)" "Day 4 - John"

    outfit john uniform_pony
    pause 1
    show bg lunch:
        zoom 2.0 xalign 0.8 yalign 0.3
    show john b_1 at Position(pos=(0.17, 1.0), anchor=(0.5, 1.0)), faceright
    show cornelia a_0 at Position(pos=(0.38, 1.15), anchor=(0.5, 1.0)), faceleft behind john
    show irene b_4 at Position(pos=(0.57, 1.15), anchor=(0.5, 1.0)), faceleft
    show allison a_3 at Position(pos=(0.75, 1.15), anchor=(0.5, 1.0)), faceleft
    with dissolve

    john "Here."

    show john a_1:
        ease 0.5 ypos 1.175

    "I handed her one of the sandwiches I bought for lunch."

    show allison a_1
    show cornelia a_4

    cornelia "...Thanks..."

    show john b_0

    cornelia "So you were serious about last day..."
    john "I usually forced you to do things for me, right?"

    show cornelia a_7
    show allison a_0

    cornelia "You didn't force me! I just did it because you're you."

    show john b_14
    show cornelia b_4

    "Who would have thought that showing kindness to someone would make them feel awkward."

    show john b_0

    "Cornelia was really insistent on not having been used by Sayaka, which is probably worse than knowingly being used."
    "Being a bit more level-headed now and not acting on the spur of the moment that unfolded two days ago, I realized that being nice to Cornelia probably wasn't going to result in payback towards Sayaka for what she did at all."
    "I doubted that she'd even care to be honest."
    "But I might as well try to establish a friendly relationship with her if things aren't changing anytime soon."
    "She is a nice girl anyways, at least when she isn't being an asshole with Sayaka nearby."

    show cornelia a_5 at faceright

    irene "I never thought I would see the day where you of all people do literally any work for someone."

    show allison a_1

    allison "It is really refreshing to see."

    show irene b_0
    show allison a_0

    irene "It is."

    show cornelia b_2
    show john b_0

    cornelia "It is Sayaka, after all!"

    show cornelia b_1
    show irene b_4

    irene "Yeah, yeah, we get it."
    irene "Changing topic, have you heard the rumor?"

    show cornelia a_0

    cornelia "About Michelle?"

    show john a_0

    irene "You believe it?"

    show cornelia at faceleft

    john "Wait, what rumor?"

    show irene b_3
    show cornelia at faceright

    irene "You don't know one of the big rumors going around? They are saying that Michelle suddenly decided to transfer schools."

    show john a_17
    show cornelia b_1

    cornelia "One way or another, not having to deal with that snake is something I am glad about."
    think "What? Why would Michelle transfer to another school?"

    show cornelia a_0 at faceleft
    show irene b_4

    john "It's the Michelle that hangs out with Katrina?"

    show cornelia at faceright

    irene "That's the one."

    show allison a_3

    allison "She is in our homeroom, or was supposed to be."

    show irene b_7

    irene "But she hasn't showed up at all and apparently cut off all contact with everyone."

    show john b_0
    show irene b_4
    show allison a_0

    john "That's... Odd..."

    show cornelia a_6

    cornelia "Who knows what goes on in her head."
    think "Michelle lives in the area and from the one or two evenings where Kat dragged me to her house to play DnD with them, I heard that her parents had jobs in town too."
    think "There is no other high school in town and as far as I know, she doesn't have a boyfriend either..."

    show john a_6
    show cornelia a_1

    think "Agh, who cares, it's just a rumor, and I have my own problems right now."

    show cornelia a_0 at faceleft
    show allison a_3
    show john a_1:
        ease 0.5 ypos 1.0

    john "Anyways, I have to go talk to someone, so I'll be leaving."

    show cornelia a_3

    cornelia "Don't tell me you're going to be talking with John again."

    show john a_0

    john "No, I'm not. And why do you care about me talking with him?"

    show irene b_3
    show cornelia a_0 at faceright

    irene "You've been talking with that twerp?"

    show cornelia b_6

    cornelia "She's been talking with him way too much lately!"

    show john b_6

    cornelia "I told her to tell us if she needs help dealing with him but she insists she doesn't need help."

    show john b_18
    show cornelia b_5 at faceleft

    john "Because I don't, so get off my back already."

    show irene b_0
    show john b_17

    irene "5 bucks she wants to make a move on Mike now that she's trying to reform herself like she's a fairy godmother."

    show allison a_1
    show cornelia at faceright

    allison "Ooh, I think it's going to be Brad!"

    show allison a_0
    show cornelia a_6

    cornelia "{i}Sigh...{/i}"

    show cornelia b_0 at faceleft

    cornelia "Saya, for real, if-"

    show john a_6

    john "If you're trying to tell me that I should ask you or someone for help again, then help me god, I'm taking that fucking sandwich with me."

    show cornelia b_8

    cornelia "What?! I haven't even eaten half of it yet!"
    john "Exactly."

    show cornelia b_6

    cornelia "Ugh, you better not end up in a bad situation."

    show john a_1

    john "Hey, I got things under control."
    cornelia "Fine..."

    show john b_5 at faceleft:
        pause 0.25
        ease 1 xpos 0.5
    show bg lunch:
        ease 1.5 zoom 1.0 xalign 0.5 yalign 0.5
    show cornelia:
        ease 0.75 zoom 0.9
    show irene:
        ease 0.75 zoom 0.9
    show allison:
        ease 0.75 zoom 0.9
    pause 0.01
    hide cornelia
    hide irene
    hide allison
    with Dissolve(0.75)

    "Who would have thought that little Cornelia is this protective of Sayaka."
    think "I wonder if the love is mutual the other way around?"

    show john b_6

    think "Nah, who am I kidding, Sayaka would leave that girl on the pavement in the rain if she could."

    show john b_5

    "Cornelia didn't even get angry at me for skipping out on the cheerleading I was supposedly the captain of now either."
    "It did, however, make her worry at least twice as much about whether something was going on with Sayaka's life behind the scenes."

    show kyoko a_0 at offscreenright, faceleft:
        alpha 0.0
    show kiyoshi a_2 at right, faceleft:
        alpha 0.0
    show katrina a_5 at centerright, faceright:
        alpha 0.0

    "Which in turn kind of makes her more of a pain to deal with. But at least it's well-meant pain."

    show john:
        faceright
        ease 0.75 xpos -0.2 alpha 0.0
    show bg lunch:
        ease 0.75 zoom 2.0 xalign 0.8 yalign 0.8
    show kyoko:
        faceleft
        ease 0.75 right alpha 1.0
    show kiyoshi:
        faceleft
        ease 0.75 centerright alpha 1.0
    show katrina:
        ease 0.75 center alpha 1.0

    "Anyhow, my goal was to try and approach either Kyoko or Kiyoshi now."

    #SKIP
    show kyoko:
        alpha 1.0
    show kiyoshi:
        alpha 1.0
    show katrina:
        alpha 1.0

    "Their fascination with sci-fi had to make it possible for them to at least make this swap a possible thing that could happen."
    "And of course, Sayaka wouldn't want to have lunch with them, so only Kat was with them currently."

    show john:
        ease 0.75 xpos 0.5 alpha 1.0
    show bg lunch:
        ease 0.75 zoom 1.0 xalign 0.5 yalign 0.5
    show kyoko:
        ease 0.75 offscreenright alpha 0.0
    show kiyoshi:
        ease 0.75 right alpha 0.0
    show katrina:
        ease 0.75 centerright alpha 0.0

    "Buuuut, if Kat is there, there is no way we could have a real conversation."

    #SKIP
    show john:
        alpha 1.0

    hide katrina
    hide kiyoshi
    hide kyoko

    "It would just end like it did last time."

    show john b_15 at faceleft

    "There is a solution for every problem, however. And my solution in this case would be Brad."

    show john a_24
    show brad a_1 at left:
        alpha 0.0
    show eric a_1 at offscreenleft:
        alpha 0.0

    think "Man, I'm sounding like a real detective hatching a plan or something."

    show john b_15:
        ease 0.75 xpos 1.2 alpha 0.0
    show bg lunch:
        ease 0.75 zoom 2.0 xalign 0.2 yalign 0.4
    show brad:
        faceleft
        ease 0.75 xpos 0.4 alpha 1.0
    show eric:
        faceright
        ease 0.75 xpos 0.3 alpha 1.0

    "He was sitting together with a few guys I couldn't recognize and Eric."

    show brad a_0:
        xpos 0.4
        alpha 1.0
    show eric a_4:
        xpos 0.3
        alpha 1.0

    "But considering how I currently looked, approaching him and getting to talk with him likely wouldn't be an issue."
    think "Well, time to put on my gameface."

    show john b_2:
        ease 0.5 xpos 0.65 alpha 1.0

    john "Hey guys."

    show brad a_4 at faceright
    show eric a_0
    show john b_1

    "Some had already seen me approaching, but none probably thought I wanted to talk to them."

    show brad a_1

    "They greeted me, almost in unison. Quite the pretty pack of popular guys were here."
    brad "What's up."

    show brad a_0

    eric "Hey."
    john "Brad, can I talk to you alone for a minute?"

    show brad a_4
    show eric a_4

    brad "Me?"
    john "Yeah, you."

    show brad a_5 at faceleft
    show john b_29
    show eric a_7

    "They murmured quietly about how I was going to confess to him or some crap, but Brad himself looked a bit more surprised than anything."

    show brad a_7 at faceright

    brad "Uh, sure, why not."

    show eric a_0
    show brad a_5 at faceleft

    eric "Bah, you shouldn't. You know her."

    show john b_13

    brad "It's alright. Be right back guys."

    scene black with dissolve
    scene bg school passage day
    show john b_1 at centerleft, faceleft
    show brad a_3 at center, faceleft
    with dissolve
    pause 0.5
    show john at centerleft, faceright

    "He followed me out of the lunch area where we talked mostly in private."

    show john b_3

    john "I'll make it quick. I need you to do me a favor."
    brad "Name it."
    john "Can you bring me Kyoko or Kiyoshi from where John normally sits?"

    show brad a_4

    "Once more he had a surprised look on his face, which quickly turned to a more annoyed one."
    brad "I could, and probably would..."
    brad "But does this have anything to do with your attitude towards that girl?"

    show john a_0

    john "Kyoko?"
    brad "We all know your relationship with that group."

    show john a_5

    john "Brad, I'm not trying to be mean-spirited at all, I know I've been an absolute bitch towards her, but I genuinely need to talk to her, and ideally Kiyoshi too."

    show brad a_6

    brad "Hmm..."
    "He thought it through for a good minute. I couldn't really blame him either, no way he wanted to get caught up in this mess."

    show brad a_3

    brad "Alright. But if you're lying, you know what happens. Be right back."

    show john b_5

    john "Oh, and don't tell them I sent you. And, uh, make sure Kat doesn't follow them."

    show brad a_4

    brad "Got it."

    show brad:
        ease 0.5 alpha 0.0 xpos 1.0
    show kyoko a_3 at right, faceleft:
        faceleft
        alpha 0.0
    show kiyoshi a_0 at centerright, faceleft:
        faceleft
        alpha 0.0

    "He wandered off..."

    hide brad
    pause 1
    show kyoko:
        ease 0.5 centerright alpha 1.0
    show kiyoshi:
        ease 0.5 center alpha 1.0

    "And sure enough, both of them appeared a minute later."

    show kiyoshi a_5:
        alpha 1.0
    show kyoko a_4:
        alpha 1.0

    "When they realized that it was me who had sent Brad, it startled them both a bit."

    show kyoko a_7
    show john b_1
    show kiyoshi a_0

    john "Hey. Can we talk for a sec?"

    show john b_0

    kyoko "What do {i}you{/i} want?"

    show kiyoshi a_6

    kiyoshi "I cannot believe it. Could it be that you finally realize my love towa-"

    show john b_6
    show kiyoshi a_4

    john "Okay, stuff it Kiyoshi. I just want to talk with you both."

    show kyoko a_0
    show john b_5

    "One after another, I got surprised looks from them. This must be so unlike Sayaka to them."
    john "Sorry to pull you out from mealtime."

    show kiyoshi a_2

    kiyoshi "Anything for you."

    show kyoko a_2

    kyoko "Just spit it out. What do you want now?"

    show kyoko a_0
    show john b_13

    john "Alright, alright. I just want to know what John told Kat last day?"

    show kyoko a_7
    show kiyoshi a_0

    kyoko "Why do {i}you{/i} want to know that?"

    show john b_11

    kyoko "Don't you already know?"

    show john b_5

    john "No, I don't, but Kat sure made me believe that I am supposed to when I talked to her after what happened."

    show kyoko a_2
    show kiyoshi at faceright

    kyoko "Cut the bullshit Sayaka. I'm leaving."

    show kyoko:
        faceright
        ease 0.5 right alpha 0.0
    show john a_4

    "And that, she did. Quite without a warning."

    show john b_4

    think "Given her mood, I don't think she wants to hear me out, huh?"

    show kiyoshi at faceleft

    john "Great. I didn't even get to tell her."

    show john b_5
    show kiyoshi a_1

    kiyoshi "Get to tell her what? About your confession to me?"

    show kiyoshi a_2

    kiyoshi "It would be my honor to accept it after a long fought battle for your heart."

    show kiyoshi a_1
    show john a_14

    john "At least you're dependant."

    show john a_31

    john "Even though it's because of the way I look..."

    show john b_12

    john "Could you at least tell me then?"

    show kiyoshi a_0
    show john b_1

    kiyoshi "Ah, about this tuesday? I believed you had told J-man about it?"

    show john b_18

    john "I haven't told him anything! I have no idea what happened when Kat got sad all of a sudden!"

    show john b_17
    show kiyoshi a_3

    kiyoshi "It would appear that the plot only thickens, in that case."

    show kiyoshi a_4

    kiyoshi "Hmm, but I believe I can do you this favor in response to getting over your fear of loving your one and only."

    show john a_32

    think "Kiiinda beginning to see why people get the urge to slap him."

    show john a_0

    kiyoshi "J-man has, apparently, managed to achieve full friend-zone with you according to himself during the holidays."
    kiyoshi "In addition, he has shared everything about himself and our group to you. I would not have minded if he talked positively about yours truly to sell my image to you, but there is quite a lot of sensitive information we share and treasure."

    show john a_27

    john "You mean that he has told me things about you guys?"

    show kiyoshi a_5

    kiyoshi "Yes...? However, if you do not have a clue about this, I wonder why he told us that."

    show kiyoshi a_3

    kiyoshi "Nonetheless, it was a disappointing act when he started insulting Kat over and over, and furthermore telling us you would want to make the situation even worse."

    show john b_28
    show kiyoshi a_0

    john "Wha- Seriously?"

    show kiyoshi a_2

    kiyoshi "I could not lie to you, oh angel of my life."

    show john b_27
    show kiyoshi a_1

    think "So she actually {i}intended{/i} to make sure I would seem like messing with them if I tried talking to them?"
    think "Which means that if I told them I was the actual John, they would only write it off as further pouring salt in the wound after having {q}acquainted{/q} myself with Sayaka over the holidays."
    think "I mean, fuck, there is no way that I couldn't clear up this... {q}Misunderstanding{/q}, but the fact that she even tried to do it is what makes me even more furious."

    show john b_3 blush

    think "She is literally trying to burn my bridges to even get my friends to listen to me!"

    show john b_17 blush

    kiyoshi "Dearest, you appear to be going red. Is it a fever? Should I carry you to the nurse's office?"

    show john b_5

    john "Oh, no no, please, I'm fine. I'm just... Angry."
    john "Thanks for telling me. You still believe in sci-fi and aliens and all that crap, right?"

    show kiyoshi a_6

    kiyoshi "Oh? Could it be that it is a secret passion of yourself too?!"

    show john b_6

    john "So you believe in that stuff, right?"

    show john b_25

    kiyoshi "Of course not! I do not believe, I know!"

    show john b_0
    show kiyoshi a_1

    john "Uh... Yeah, that's fine too."

    show john b_13

    john "So would you believe me if I said that I was actually John?"

    show kiyoshi a_4

    kiyoshi "...John? What do you mean?"

    show john b_5

    john "I am John, and the John you talked to yesterday was Sayaka. Me and Sayaka have had our bodies swapped."

    show kiyoshi a_4

    "It took him awhile to process that information, but for some reason he eventually got around to the idea."

    show kiyoshi a_5

    kiyoshi "J-man?!"
    kiyoshi "Is that you?!"

    show john b_1

    john "Yeah, it's me."
    kiyoshi "By all that is alien, I cannot believe you managed to find a high tech alien device that would let you freely alter anyone as you desire!"

    show kiyoshi a_0
    show john b_6

    john "...That's... No, I don't have a thing like that."

    show john a_3

    john "Also, why the hell do you believe me so quickly?!"
    john "I had like at least ten different facts ready to tell you to prove to you I'm the real deal!"

    show john a_17
    show kiyoshi a_2

    kiyoshi "My friends obviously would not try to deceive me."

    show john a_6

    think "That's... not how it works."

    show kiyoshi a_6
    show john a_0

    kiyoshi "Hey, so that means you get to see the lovely Sayaka naked?"

    show kiyoshi a_1
    show john b_5

    john "Uhm, well, yeah... But-"

    show kiyoshi a_2

    kiyoshi "Score for you, J-man!"
    kiyoshi "You really picked the delicate target for your shenanigans! Please tell me how to do it!"

    show kiyoshi a_1
    show john b_27

    john "It's not something I did! I just woke up as her four days ago without any warning."

    show kiyoshi a_3

    kiyoshi "So a mystery swap... Maybe we could research this to be able to replicate it."

    show john b_0
    show kiyoshi a_0

    john "Oh, yeah we could. I want to go back as soon as possible."

    show kiyoshi a_5

    kiyoshi "Go back? Are you a madman? This is the golden opportunity to claim the rank of number one beauty!"

    show john a_5

    john "Kiyoshi, living as her is a nightmare."

    show kiyoshi a_0

    kiyoshi "...So I can have dibs on her?"
    john "For all I care, sure, as long as I get back to being myself."

    show kiyoshi a_6

    kiyoshi "It is settled then! The plan is in motion!"

    show john a_0

    john "What plan?"
    kiyoshi "The plan to get me a smoking hot girlfriend, J-man!"

    show john b_6

    john "No that's not the plan at all."

    show kiyoshi a_0

    kiyoshi "We weren't talking about getting me a smoking hot girlfriend?"

    show john b_3

    john "We were talking about having me become myself again."

    show kiyoshi a_1

    kiyoshi "Ah! I must have gotten carried away."
    john "...Right."

    show john b_5

    john "And can you please try to convince the girls to believe me too? Sayaka must have tried to keep me from telling you guys, but probably didn't anticipate your... Uh... Personality."

    show kiyoshi a_2

    kiyoshi "Of course. When have I ever let you down?"
    think "Yeah I don't want to answer that."

    show kiyoshi a_0
    show john b_15

    john "Thank god someone believes me. See you later man."
    kiyoshi "I wish you all the best on your explorations!"

    scene black with dissolve
    show bg lunch:
        zoom 2.0 xalign 0.2 yalign 0.6
    show john b_1 at centerleft, faceright
    with dissolve

    "It felt like something had been lifted off my chest. Knowing someone else knew who I really was would be a big help."

    show bg lunch:
        ease 10 xalign 0.8
    show john:
        block:
            ease 0.6 yanchor 0.98
            ease 0.7 yanchor 1.0
            repeat

    "Knowing that Kiyoshi wouldn't try to hit on me was really just the icing on the cake."
    "At least I hoped he wouldn't."
    "Like, really hoped."

    show cornelia a_8:
        faceright
        centerright
        ypos 1.10
        alpha 0.0
    show irene b_3:
        faceright
        center
        ypos 1.10
        alpha 0.0
    show allison a_5:
        faceleft
        right
        ypos 1.10
        alpha 0.0

    "It would only become better if Kyoko and Kat would come around eventually as well. At least there would be no misunderstandings possible anymore if they witnessed Sayaka's anger management issues in my body."

    show bg lunch:
        ease 0.5 xalign 0.8
    show cornelia:
        ease 0.5 alpha 1.0
    show irene:
        ease 0.5 alpha 1.0
    show allison:
        ease 0.5 alpha 1.0
    show john b_0:
        ease 0.4 yanchor 1.0

    "But... Uh, Cornelia is apparently having a breakdown."

    #SKIP
    show irene:
        alpha 1.0
    show cornelia:
        alpha 1.0
    show allison:
        alpha 1.0

    show irene at faceleft

    cornelia "-she's being blackmailed, oh god she's being blackmai-"

    show allison a_3
    show irene b_5

    irene "Fucking really, Sayaka?"

    show john b_11

    irene "Kiyoshi?"
    cornelia "-oh god she's being blackmailed, oh god she's being blackmailed, oh go-"

    show irene b_3

    irene "Cornelia has been like this for three freaking minutes now!"

    show allison a_4

    allison "Hey, hey, it's okay... She's back."

    show cornelia at faceleft

    john "Wha-?"

    show allison a_5
    show irene b_4:
        ease 0.4 xpos 0.7
    show cornelia b_3:
        ease 0.5 center
    with hpunch

    cornelia "Fuck! Saya! What are you doing?! What are they doing to you?!"

    show john b_5
    show allison a_3

    john "...I... Was in the bathroom...?"
    cornelia "You absolutely terrible liar! We all saw you taking those two space-nerds with you and returning with- Ew! Kiyoshi!"

    show john a_6:
        ease 0.75 ypos 1.1
    show cornelia b_5

    john "I was just talking with him, why is that a big deal?"

    show irene b_3

    irene "Are you seriously asking why it's not a big deal to be seen talking privately with the prime predator of the school?"

    show irene b_4
    show cornelia at faceright
    show john a_0

    irene "Do you actually have the hots for him?"

    show cornelia a_8 at faceleft

    cornelia "Please say no, please say no, please say no-"

    show john b_6
    show allison a_0

    john "Why the hell would I be into him? If anything then Brad, or Mi-"

    show john b_19

    john "Wait, fuck no!"

    show cornelia a_4
    show john b_7

    think "Why did I just think of Brad or Mike as boyfriends?!"
    think "Am I suddenly gay or something?!"

    show allison a_1

    allison "Aw come on Irene, she can like who she wants, can't she?"

    show irene b_7 at faceright
    show john b_5
    show cornelia at faceright
    show allison a_0

    irene "In every other scenario, yes. But this is Kiyoshi. I wouldn't wish that for her, even despite... You know."

    show irene b_4 at faceleft
    show cornelia a_5 at faceleft

    cornelia "I am {i}not{/i} leaving you out of sight anymore! From now on, it's back to you being normal Saya! I can't stand this!"

    show john b_0

    john "...So I can't be nice to you?"

    show cornelia a_7

    cornelia "...Yes, you can! But..."

    show cornelia a_8

    think "At this point she is probably struggling to find an excuse to both be treated nice and things going back to how they were before I became Sayaka."

    show john b_23

    john "{size=-5}Heh...{/size}"

    show cornelia b_6

    cornelia "What are you laughing at? This is serious, Saya!"

    show john a_31

    john "Oh, nothing... Just nothing..."

    scene black with Dissolve(1.5)

    title "11th of August (Thursday)" "Day 4 - Sayaka"

    outfit sayaka uniform
    pause 0.5
    show AN_bg library day:
        zoom 2.0 yalign 0.5 xalign 0.55
    show sayaka a_2 at centerleft, faceleft
    with dissolve
    pause 0.5

    "I was currently reading all of the books I could find in the school library that had even a slight similarity on people suddenly changing personalities, but fuck."
    "There were like three, and all of them absolutely boring. Turned out none of them were similar to my swap."

    show sayaka a_5

    think "At least I've ended up not having to sit with the circle of losers today."

    show sayaka a_16

    think "That would only have made this day even worse."

    show sayaka a_5

    "The library was a place where I went to, like, once in my life. Some people even forget that this thing exists."
    "Only time I've been here was when Ms. Clark forced us to do some throwaway projects and presentations here."
    "But ultimately, even if it was a very small glimmer of hope, this was a real waste of time."

    show sayaka a_24

    think "Who would have thought that I, Sayaka Sato, would be staying late at school voluntarily..."

    show sayaka a_5
    show sayaka:
        ease 0.75 ypos 1.1
    show AN_sonya a_3 at offscreenright:
        faceleft
        alpha 0.0
    show sadie a_0 at right:
        faceleft
        alpha 0.0

    think "...I could really go for some shopping right now..."

    show sayaka at faceright
    show AN_sonya:
        ypos 1.1
    show sadie behind AN_sonya:
        ypos 1.1

    "I just laid with my face down on the desk for a minute or two until two girls came crashing into the library with their conversation."

    show AN_bg library day:
        ease 0.5 xalign 0.9 yalign 0.6
    show sayaka:
        ease 0.6 alpha 0.0 offscreenleft
    show sadie:
        ease 0.6 centerright alpha 1.0
    show AN_sonya:
        ease 0.6 right alpha 1.0
    pause 0.4

    AN_sonya "-you sure? I thought that thing was her thing."

    hide sayaka

    think "Gah, just fuck off already and let me have my peace for a bit..."

    show sadie a_3

    sadie "It totally was! I reckon something must'a changed."
    AN_sonya "Did you try talking to her about it? I'm sure she would freak out like crazy if we just gave the position to you without asking her..."
    think "Wait, I know those voices."

    show AN_sonya a_0

    think "Sadie and Sonny?!"
    think "I know them from cheerlea-"
    think "..."
    think "Cheerleading!"
    think "Fuck! I forgot all about that! And that dumbhead probably didn't go to it!"

    show sadie a_1

    sadie "Of course not. Do y'all think I have the guts to ask 'er something like that? What if she jus' forgot going and goes all ape on me? I'd be roast."

    show sadie a_0
    show AN_sonya a_1

    AN_sonya "Hah, you're gonna be in so much trouble if Sayaka simply forgot about it."
    think "If I forgot?"

    show sayaka a_5 at offscreenleft:
        alpha 0.0

    "It clicked. The selection of the cheerleading captain was each half year, and if I wasn't there yesterday for the first round of training..."

    show sayaka:
        easein 0.75 centerleft alpha 1.0

    "This was the last straw for today. I fumingly, but still trying to keep my temper, walked over to them to make sure."

    show sadie a_2
    show AN_sonya a_3

    sayaka "Hey girls. Who did you say was the cheerleader captain now?"
    AN_sonya "Huh? Who are you?"

    show sadie a_0

    sadie "Ooh! I've seen 'em before! They always hanging out with that Kiyoshi fella'!"

    show AN_sonya a_3

    AN_sonya "Ew, that guy."

    show sayaka a_16

    sayaka "Just tell me."

    show AN_sonya a_0

    AN_sonya "Chill. It's been Sayaka for two years now, but we elected Sadie-Lynn here yesterday."

    show AN_sonya a_1

    AN_sonya "You into cheerleader captains?"
    sayaka "Fuck off, Sonny. Not in the mood."

    show sadie a_5
    show AN_sonya a_5

    AN_sonya "Wha- You know me?"

    show sayaka at faceleft

    think "John keeps humiliating me, huh?"

    show AN_sonya a_3
    show sadie at faceright

    AN_sonya "Did you tell him about me?"

    show sadie a_2

    sadie "Honest to god, never heard 'em talk before."

    show AN_bg library day:
        ease 0.75 yalign 0.5 xalign 0.55
    show sayaka:
        ease 0.75 center
    show AN_sonya:
        ease 0.5 xpos 1.05 alpha 0.0
    show sadie:
        ease 0.5 right alpha 0.0

    think "Hah, you think I'll just sit here and do nothing?"

    hide AN_sonya
    hide sadie
    show sayaka a_5

    think "..."
    "I was about to leave the library before I stopped to think about this."
    "He deserved it for doing something terrible to my life, right?"

    show sayaka a_16

    "Like hell I would let that bitch Sadie have my spot as the captain for the most prestigious group in this school."
    "This was his fault!"

    show sayaka a_2

    "But for some reason this felt like a rabbit hole that would only go deeper."
    think "..."

    show sayaka a_16

    sayaka "Nah, fuck it, he deserves it."

    scene black with Dissolve(1.0)
    outfit sayaka uniform_c

    title "12th of August (Friday)" "Day 5 - John"

    show bg school entrance day:
        zoom 2.0 xalign 0.8 yalign 0.8
    show cornelia a_3 at centerright, faceright
    show john b_6 at right, faceleft
    with dissolve

    cornelia "-and no matter what, you have to put make-up on tomorrow! Got it? You are {i}not{/i} embarrassing yourself anymore."

    show cornelia a_2

    cornelia "I'll make sure of it!"

    show john b_23

    john "Heh, got it chief."

    show john a_32

    think "Man, what's her deal with upholding Sayaka's honor?"

    show cornelia a_0

    think "It's borderline worrying."

    show john a_6
    show cornelia a_5

    cornelia "Girl, did you even sleep yesterday? You've been rubbing your eyes since we got here."

    show john a_19

    john "Of course I did."

    show john a_32

    john "My eyes just itch a lot even though I went seriously early to bed."
    "My eyes were actually itching since yesterday. They have for a couple days now, but it's getting worse every day. It's been a pain no matter if I had them closed or not."

    show john a_6

    "It was a weird feeling. I got enough sleep this night, an entire nine hours actually, but still, I get this feeling there is something in my eyes at all times, and touching my eye while it's open hurts even more."

    show cornelia at faceleft

    cornelia "Hm, alright."

    show cornelia b_0

    cornelia "...Wait, is that...?"

    show john b_17

    think "Hold on..."

    pause 2
    show john b_28
    show sayaka b_5 at left, faceright:
        alpha 0.0

    think "...{size=+10}What?!{/size}"

    show bg school entrance day:
        ease 0.75 xalign 0.5 yalign 0.8
    show john:
        ease 0.5 xpos 1.05 alpha 0.0
    show cornelia:
        ease 0.5 xpos 0.9 alpha 0.0
    show sayaka:
        faceleft
        pause 0.2
        ease 0.55 centerleft alpha 1.0

    "Without even looking back at Cornelia I raced towards this smug-ass bitch who was minding her own business."

    #SKIP
    show sayaka:
        alpha 1.0
        centerleft

    show john b_19 at right
    show cornelia b_8 at offscreenright

    "She dyed my hair fucking PINK!"

    show john:
        ease 0.5 xpos 0.6 alpha 1.0
    show cornelia:
        pause 0.4
        ease 0.75 xpos 0.65 alpha 1.0

    cornelia "Saya- Wait, Sayaka!"

    show sayaka b_15 at faceright

    john "What the hell do you think you're doing?!"
    "She finally noticed me waltzing her way and was shocked at first."

    show sayaka b_17

    "But then a small grin formed on her face."

    show john b_17

    "She enjoyed this. She revels in this."

    show john b_19

    john "When the fuck did I give you permission to dye my hair pink?!"

    show cornelia b_5
    show john b_3

    sayaka "Oh? I thought you enjoyed messing with hair, so I just thought you'd be okay with pink hair and dyed it to make you happy, you know?"

    show john b_19

    john "Fuck no you didn't, you did this to piss me off!"

    show john a_17

    cornelia "Saya, what did he do?"

    show sayaka b_7
    show john
    show cornelia b_0

    sayaka "He fucked up my hair! That's wha-"

    show sayaka b_4

    sayaka "I- I mean..."
    "The charade of keeping this secret was out by now anyways, thanks to Kiyoshi, but obviously I hadn't told Sayaka about that."

    show sayaka b_16

    "She was still concerned about keeping up appearances even though our lives were taking a freaking skydive for the worst."

    show sayaka b_7

    sayaka "{b}She{/b} messed up her hair! Can you believe it?!"

    show cornelia b_6
    show sayaka b_16

    cornelia "...Saya has been walking around like that for four days now, so what do you care?"

    show sayaka b_7
    show cornelia a_7

    sayaka "But it's terrible! The hair is terrible! Fuck you for messing up my hair!"

    show john a_3
    show sayaka b_16
    show cornelia a_8

    john "Well fuck you too for dying mine in acid pink!"

    show john b_3

    cornelia "...Wha...?"
    sayaka "Come on Corny I'm sick of- I mean, fuck you too, Corny! Not Corny, Cornelia! You're an absolute bitch!"

    show john b_18

    john "Go suck a big one already."

    show john b_3

    sayaka "Hmpf, fucking perv."

    show sayaka:
        ease 0.5 xpos 0.4 alpha 0.0

    "..."

    hide sayaka
    show john b_4

    john "{size=-5}{i}Sigh{/i}... Christ, is she never done fucking my life up over unimportant things?{/size}"
    think "At this point I don't even care anymore."

    show cornelia b_8

    cornelia "What was that?"

    show john b_0 at faceright

    john "Huh? Oh. Corneli-"

    show john b_8

    john "Wait, did you listen to this entire argument?!"

    show cornelia b_5

    cornelia "Yeah I fucking did, what was this all about? Why did you talk about your hair all weird?"

    show john b_7

    john "Well, that is... Becaa~~use... Ah crap, I can't come up with anything."

    show john b_6

    john "I might as well tell you. That right there was your bitch-ass friend Sayaka."

    pause 1
    show cornelia b_6

    cornelia "...Who? You?"

    show john b_3

    john "No, John right there is Sayaka."
    cornelia "... Is that, like, a metaphor?"

    show john b_5

    john "No no, that was Sayaka, in John's body. And I'm John, in Sayaka's body. We got swapped about... Four, five days ago?"
    cornelia "..."

    show cornelia a_3

    cornelia "...What?"

    show cornelia a_0
    show john b_6

    john "Ah, fuck it. Just forget it, it's a pain to have to explain this to you."

    show cornelia a_8

    cornelia "I- I'm sorry Saya, but I don't get what you're telling me at all..."

    show john a_32 at faceleft

    think "Can't really expect anyone (except maybe Kiyoshi) to grasp the concept of two people swapping bodies, huh?"

    show john a_6

    john "Let's just get to P.E. already."

    show cornelia a_1

    cornelia "Uh, yeah, sure!"

    scene black with dissolve
    outfit john gym_pony
    body cornelia AN_cornelia
    outfit cornelia gym
    outfit anuja gym
    outfit izuna gym
    outfit brad gym
    scene bg school gym day
    show john a_27 at center, faceleft
    show cornelia a_11 at centerright, faceleft
    show anuja a_0 at offscreenright, faceleft behind john
    show izuna a_0 at offscreenright, faceleft behind john
    show brad a_0 at offscreenright, faceleft behind john
    with dissolve
    pause 1.5

    "What. Did. I. Just. See."

    show john at faceright

    cornelia "Saya, are you alright?"

    show cornelia a_14
    show anuja:
        easeout 6 offscreenleft

    cornelia "You haven't said a word since we entered the school."
    think "How am I supposed to say anything when the first thing I do is get dragged through the girl's locker room completely unnoticed?!"

    show john a_8
    show brad:
        pause 1
        ease 6 offscreenleft
    show izuna:
        ease 6 offscreenleft

    think "It completely crossed my mind that I was going to see every girl in this class in underwear!"

    show john a_15

    "Those were things I would like to say as a response, but given how she would probably panic when she realized I saw her in her sports bra, I kept my mouth shut as tight as possible."

    show alex a_0 at left, faceright:
        alpha 0.0

    "Not that I was entirely fazed given that I've seen Sayaka naked more than plenty of times now. Cornelia really doesn't top that."

    show alex:
        ease 0.5 alpha 1.0 xpos 0.2
    show john a_0 at faceleft
    show cornelia a_0

    alex "You guys, we're outside!"

    scene black with dissolve
    outfit kiyoshi gym
    outfit rita gym
    outfit AN_harry gym
    show bg school exterior day:
        zoom 2.0 xalign 0.8 yalign 0.7
    show alex a_0 at Position(pos=(0.15, 1.0), anchor=(0.5, 1.0)), faceright
    show kiyoshi a_1 at Position(pos=(0.4, 1.0), anchor=(0.5, 1.0)), faceleft
    show anuja a_0 at Position(pos=(0.5, 1.0), anchor=(0.5, 1.0)), faceleft
    show john a_0 at Position(pos=(0.6, 1.0), anchor=(0.5, 1.0)), faceleft
    show cornelia a_0 at Position(pos=(0.7, 1.0), anchor=(0.5, 1.0)), faceleft
    show AN_harry a_0 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)), faceleft
    show rita b_0 at Position(pos=(0.9, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    think "Huh, so Kiyoshi has the same P.E. class as me."

    show john a_10

    think "I didn't know that, but that's great!"

    show john a_0

    think "Only issue is that I still have this blondie watching my every step..."
    think "Ahh, who cares."

    show alex a_3

    alex "You guys are slow at changing! But it looks like we're all here now."

    show alex a_0

    alex "We're doing groups of four today to play some good old fashioned street hockey!"
    alex "I know you guys are tired of doing exercises almost all the time, so we'll start slow this year!"

    show alex a_9

    alex "And also, {size=-5}while I sure hope I won't regret doing this{/size}, I'll pick six captains at random who will choose three other people in turns, since it seems we are exactly 24 today."

    hide alex
    hide kiyoshi
    hide anuja
    hide john
    hide cornelia
    hide AN_harry
    hide rita
    with dissolve
    show john a_0 at centerright:
        faceleft
        alpha 0.0

    "Ms. Hawkins then ordered us to form a straight line so she could randomly pick the captains."

    show bg school exterior day:
        ease 0.75 xalign 0.6
    show cornelia a_4 at right behind john:
        faceleft
        alpha 0.0
    show john:
        pause 0.5
        ease 0.5 alpha 1.0

    "Of course, as my terrible luck would have it, I was put into the position as one of the captains."

    #SKIP
    show john:
        alpha 1.0

    show cornelia:
        ease 0.5 alpha 1.0

    cornelia "Hey, Saya..."

    #SKIP
    show cornelia:
        alpha 1.0

    show john at faceright

    "Cornelia tugged my t-shirt from behind me and had almost puppy-like eyes."

    show cornelia a_22

    cornelia "You'll still pick me, right? Even if I've annoyed you recently."
    think "Ah hell, I sure can't say no to that."

    show john a_14

    "In response, I nodded towards her before I went out of the line."

    show cornelia a_12:
        ease 0.75 alpha 0.0
    show john a_1:
        faceleft
        ease 1 xpos 0.25
        pause 0.25
        faceright

    think "At least I know two people I want in my group now. Maybe I'll pick Brad or someone else I know if they are left by the end."

    #SKIP
    show john:
        xpos 0.25
        faceright

    show alex a_3 at Position(pos=(0.55, 1.0), anchor=(0.5, 1.0)):
        faceleft
        alpha 0.0

    "So the thing about Kiyoshi and Cornelia was, I knew they were both absolutely terrible at sports. I also knew that Sayaka, surprisingly, at least had a bit of a knack and a fit body for it, but never really bothered to take it seriously."

    show alex:
        ease 0.5 alpha 1.0
    show john a_0

    alex "Sayaka, you need to pick next."

    #SKIP
    show alex:
        alpha 1.0

    show john a_10
    show cornelia a_1:
        ease 0.5 alpha 1.0

    john "Oh, of course! Cornelia, come over here."

    show cornelia a_2:
        alpha 1.0

    cornelia "Yes, Saya!"

    show cornelia a_1:
        ease 0.75 xpos 0.1
        pause 0.25
        faceright
    show kiyoshi a_1 at Position(pos=(0.75, 1.0), anchor=(0.5, 1.0)) behind john:
        faceleft
        alpha 0.0
    show AN_harry a_0 at Position(pos=(0.85, 1.0), anchor=(0.5, 1.0)) behind john:
        faceleft
        alpha 0.0
    show rita b_2 at Position(pos=(0.95, 1.0), anchor=(0.5, 1.0)) behind john:
        faceleft
        alpha 0.0

    "She sure is happy about something as trivial as this. Which was made apparent as she merrily trotted her way behind me."

    #SKIP
    show cornelia:
        xpos 0.1
        faceright

    show alex at faceright
    show kiyoshi:
        ease 0.5 alpha 1.0
    show AN_harry:
        ease 0.5 alpha 1.0
    show rita:
        ease 0.5 alpha 1.0

    "Sure enough, nobody picked Kiyoshi. His terrible skills at being sceptical about things and sports has really come through in the last 24 hours."

    #SKIP
    show kiyoshi:
        alpha 1.0
    show AN_harry:
        alpha 1.0
    show rita:
        alpha 1.0

    show cornelia a_12
    show john a_0 at faceleft

    cornelia "Hey, Rita is still free. We should pick her."

    show john a_28 at faceright
    show cornelia a_1

    john "Sorry, but I'll take Kiyoshi."

    show cornelia a_11
    show rita b_11
    show AN_harry a_3
    show alex a_3 at faceleft
    show john a_10

    "Naturally, everyone reacted to that."

    show rita b_12
    show kiyoshi a_2:
        ease 0.75 xpos 0.375
        pause 0.25
        faceright

    kiyoshi "Naturally, J-man. Or should I be calling you S-girl now?"

    show kiyoshi a_3:
        xpos 0.375
        faceright
    show cornelia a_19

    kiyoshi "That does not roll off the tongue as much."

    show kiyoshi a_4

    cornelia "...What?"
    kiyoshi "Sgirl maybe?"

    show john a_6

    kiyoshi "No, that sounds too much like {q}squirrel{/q}..."

    show john a_13
    show kiyoshi at faceleft

    john "Could you stop giving me names?"

    show kiyoshi a_6

    kiyoshi "Nicknames are imperial for a lasting friendship, Sayohn!"

    show cornelia a_3
    show john at faceleft

    cornelia "What, the fuck Sayaka?"

    show kiyoshi a_1 at faceright

    cornelia "I thought we talked about this yesterday!"

    show rita b_3
    show alex at faceright
    show john at faceright
    show cornelia a_0

    rita "Why would you pick that fuckhead over me?!"

    show alex a_2

    alex "Rita! Watch your tongue!"

    show rita b_11
    show alex a_6
    show cornelia a_5

    "On second thought, this generated a bit more tumult than expected."

    show alex a_3

    kiyoshi "{size=-5}Say-girl...? No... Girl S maybe?{/size}"
    alex "Mike, please choose someone so we can start talking about something else."

    show john a_2
    show cornelia a_8
    show AN_harry a_5
    show rita b_3

    "And just to piss Rita off even more, I chose some random boy I had never really talked to before when it was my turn again."

    show john a_1
    show rita:
        faceright
        ease 0.75 xpos 1.2
    show AN_harry at faceright

    "Picking him over her was worth it so much because of her reaction."

    show john a_5

    rita "{size=-7}I can't believe she is choosing fucking Kiyoshi and Harry over me!{/size}"

    show kiyoshi a_0

    rita "{size=-7}Fuck her!{/size}"

    show AN_harry a_3 behind kiyoshi:
        faceleft
        ease 0.75 xpos 0.5
        pause 0.25
        faceright
    show alex:
        pause 0.25
        ease 0.5 xpos 0.7

    john "Okay... It's not like I chose to leave her on a deserted island or something. Way to overreact."

    show kiyoshi a_2

    kiyoshi "Girls nowadays can be difficult to deal with."

    show kiyoshi a_3

    kiyoshi "Believe me, I know."

    scene black with dissolve
    scene bg school exterior day
    show cornelia a_14 at Position(pos=(0.2, 1.0), anchor=(0.5, 1.0)), faceright
    show john a_32 at Position(pos=(0.4, 1.0), anchor=(0.5, 1.0)), faceleft
    show kiyoshi a_0 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)), faceleft
    show AN_harry a_6 at Position(pos=(0.6, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    cornelia "-and just for one second, I thought that maybe you wouldn't piss off everyone else again, but then you do this!"
    cornelia "Ugh, did you just completely lose your mind all of a sudden?!"
    "I got the full lecture of how to be a part of the {q}famous clique{/q} once more. I've noticed that every time I get one from her, she just sounds more and more desperate."

    show john a_6

    think "Maybe I should try not to burn my own bridges on this one actually..."

    show AN_harry a_7

    AN_harry "Uh, hi, by the way. I don't think we've ever really talked to each other."

    show cornelia a_5
    show john a_5 at faceright

    think "Oh yeah, the guy."
    "He kind of stood out since he was pretty small for a guy."
    "He was in some of my classes, but that's about all I know."

    show john a_10

    john "Hey. It's Harry, right?"

    show AN_harry a_8

    AN_harry "Yeah. Just to make sure, is it alright for you to pick me instead of Rita? She looked really upset..."

    show cornelia a_7
    show john a_0 at faceleft

    cornelia "Of course it's not alright!"

    show cornelia a_8

    cornelia "You're like a completely different person. I get that you told me you wanted to be nice or whatever bullcrap you tried to convince me with, but now I'm starting to believe something is seriously wrong with you."
    cornelia "Rita is going to be absolutely livid, Saya!"

    show john a_5
    show cornelia a_5
    show AN_harry a_3

    john "Who cares? If she gets upset about this then she isn't worth being called a friend."

    show cornelia a_8

    cornelia "Wh- What?"
    cornelia "It's not like I'm getting mad about it like her, it's just, you know."

    show cornelia a_22

    cornelia "I'm not upset about it, I just think you're doing something really bad."

    show john a_6

    john "Cornelia, you're my friend because you're not a bitch like the others."

    show cornelia a_11
    show john a_0

    "She sighed. Really, all she ever thought about was keeping her friendship status with Sayaka intact."

    show cornelia a_0
    show john a_13

    john "And if you want to keep it that way then stop worrying about it. Unless you fuck up majorly I'm cool with you."

    show cornelia a_8

    cornelia "Uhm... What does fu-"
    john "Fucking up majorly includes things you wouldn't do if you were considerate towards other people. Got it?"

    show AN_harry a_8 at faceright

    AN_harry "{size=-5}Are they having a moment or something?{/size}"

    show kiyoshi a_2

    kiyoshi "It's like watching a documentary."

    show kiyoshi a_1
    show AN_harry a_3 at faceleft
    show cornelia a_1

    cornelia "O- Okay. Got it."

    show cornelia a_0

    cornelia "But still, I know you don't really like them, but didn't you say that hanging out with them is important for our image?"

    show cornelia a_5 at faceright

    "I was about to answer before she realized she likely said something private to the two onlookers standing next to us."

    show cornelia a_3

    cornelia "What are you two gawking at? If you've got time listening to us you may as well go get the equipment for us."

    show AN_harry a_11
    show john at faceright
    show cornelia a_5

    AN_harry "Ah, well, not really gawking or anything. I thought we would all go get the hockey equipment together."

    show AN_harry a_3 at faceright
    show kiyoshi a_6

    kiyoshi "Harry, Harry, Harry... We cannot let the ladies do the dirtywork, now can we?"
    AN_harry "I really thought we could."

    show AN_harry at faceleft
    show kiyoshi a_1
    show john a_0 at faceleft

    john "It's okay to talk in front of them. Either way, I really want you to get better along with Kiyoshi."

    show cornelia a_6

    cornelia "What?! No fucking way."

    show john a_30

    john "I want to hang out with him more often, and I'd feel bad leaving you with those other people you call {q}friends{/q}."

    show cornelia a_7

    cornelia "Hold on. You're not actually dating him, are you?"

    show john a_13
    show kiyoshi a_0

    john "Ew, fuck no."

    show john at faceright
    show AN_harry at faceright
    show kiyoshi a_3

    kiyoshi "That's a negative from me as well. S-girl would never be qualified to pass {q}Kiyoshi's Womanly Exam{/q}."

    show kiyoshi a_0
    show john a_6
    show cornelia a_11

    john "Womanly what-now?"

    show kiyoshi a_6

    kiyoshi "I am glad you asked!"
    john "{size=-5}I didn't ask anythi-{/size}"

    show john a_5

    kiyoshi "{q}Kiyoshi's Womanly Exam{/q} is a qualification process in which I, Kiyoshi the examiner, examine the bodily structure and personal integrity of a woman I will date."

    show kiyoshi a_2

    kiyoshi "Naturally, there are many skills that need to be tested. The physical exam will require measuring tape, glue, 16 pounds of flour-"

    show AN_harry a_2
    show john a_32
    show kiyoshi a_1

    AN_harry "You force girls that want to date you to go through an exam?"
    kiyoshi "I do not force anyone. They would take it themselves."

    show kiyoshi a_2
    show AN_harry a_8

    kiyoshi "Anyways, as I was sayi-"

    show cornelia a_3
    show john a_0 at faceleft
    show AN_harry a_3
    show kiyoshi a_0

    cornelia "You want me to be friends with this lunatic?"

    show john a_30
    show cornelia a_14

    john "He really isn't that bad once you get to know him."

    show john a_30 at faceright

    john "...I think."

    show cornelia a_0
    show kiyoshi a_2
    show AN_harry at faceright

    kiyoshi "If the dear Cornelia would like to fulfill an application, I'd be happy to print one out later today."

    show cornelia a_19
    show alex a_3 at right:
        faceleft
        alpha 0.0

    cornelia "Not. Fucking. Happening."

    show kiyoshi a_0:
        faceright
        ease 0.5 xpos 0.65
    show AN_harry:
        ease 0.5 xpos 0.5
    show john a_0:
        ease 0.5 xpos 0.35
    show cornelia a_5
    show alex:
        ease 0.5 alpha 1.0
    pause 0.25

    alex "Team Sayaka! We're waiting for you!"

    show john a_7

    "We had been so absorbed in the conversation that we didn't notice how every other team was just waiting for us at this point."

    show john a_2

    john "Ah! Sorry Ms. Hawkins!"

    show john a_10

    john "Let's go get the hockey equipment, guys."

    scene black with dissolve
    pause 1

    title "12th of August (Friday)" "Day 5 - Sayaka"

    pause 1
    scene bg classroom 1
    show jack a_0 at centerright, faceleft
    with dissolve

    jack "Now, is there {i}anyone{/i} in here who is able to tell me anything about Charles Philippe?"

    show jack a_8
    show sayaka b_5 at Position(pos=(0.2, 1.1), anchor=(0.5, 1.0)):
        faceright
        alpha 0.0

    jack "...Nobody?"

    show jack a_9
    show sayaka:
        ease 0.5 alpha 1.0

    jack "...How about you, John? Got anything {q}wise{/q} to share with us about this topic since you so seemingly believe you do not need to pay attention?"

    show sayaka b_2:
        alpha 1.0

    sayaka "Huh? Wh-What?"

    show sayaka b_16

    "What actually is his deal here?"
    "I looked away for ten seconds and already he starts fucking singling me out again!"
    sayaka "Don't know."

    show jack a_0

    jack "I believe I made it perfectly clear that this was homework assignment for today, didn't I?"
    sayaka "No it wasn't. We had to read a text from some documentalist."

    show jack a_1

    jack "That was the assignment for the class. But of course your inferior head wouldn't be able to keep track of me telling you to research this topic last class."

    show sayaka b_7

    sayaka "You never told me anything like that!"

    show sayaka b_16
    show jack a_0

    "To add fucking insult to injury, the entire class was humoring themselves as if this was some kind of circus. Nobody was defending me, at all!"
    "Why is any of this happening? What did I ever do to that fuckface?"
    jack "I made it very clear. So I am expecting a report on Charles Philippe's rule this tuesday. Just to make sure you actually do something for once, {i}pinky{/i}."

    show jack a_9

    jack "Oh, and be sure to add in a section that retrospects on why it is important to listen to your teacher. Maybe you could make advancements by yourself where even the best would fail to teach you."

    show sayaka b_20

    sayaka "I already have two reports for tuesday that you gave me two days ago!"

    show jack a_3
    show sayaka b_16

    jack "Am I to assume you would like one more, this time about proper behavior in class?"

    show sayaka b_24

    sayaka "I- N- No."

    show jack a_0
    show sayaka b_16

    jack "As I thought. Moving on."

    show jack:
        ease 0.5 alpha 0.0

    "Fuck. Him. Fuck. Him."
    "If I could I would punch him right in his stupid grinning face right now."
    "Is he always like this towards John?"

    show katrina a_9:
        center
        ypos 1.1
        faceright
        alpha 0.0

    "How the hell did John manage to piss this jerk off this hard? Like, how?"

    show katrina:
        ease 0.5 alpha 1.0

    "And his stupid girlfriend Katrina isn't even saying anything!"
    "If you want to be a true friend for once then fucking do something about this!"

    scene black with dissolve
    outfit brad uniform
    show AN_bg library day:
        zoom 2.0 xalign 1.0 yalign 0.5
    show sayaka b_24:
        center
        faceleft
        ypos 1.1
    with dissolve

    think "Sigh... Okay, just keep it cool. No more flipping out."

    show sayaka b_16

    "In the end, that excuse of a teacher sent us to the school library to prepare for {i}another{/i} report we would have to do in his class."
    "We even had to present it. And based on what I had seen so far, no matter what effort I put into it, he would be scum towards me no matter what."
    "So as if I'd bother working on that. I was instead spending time clinging on to the hope that some book around here may tell me anything about my situation."
    "I'd been here three days already, reading some garbage books from god-knows what kind of pathetic authors, and I'm already getting totally sick of it."

    show brad a_0 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)) behind sayaka:
        faceleft
        alpha 0.0

    "I was almost half considering just conceding and praying to god or something, but as if that would help."

    show brad:
        ease 0.5 alpha 1.0

    brad "Got room for one more at the table?"

    #SKIP
    show brad:
        alpha 1.0

    show sayaka b_2 at faceright

    think "Huh?"

    show sayaka b_5

    think "Oh, it's Brad."
    think "What does he want from a twerp like John?"
    sayaka "Yeah, sure."

    show brad a_7:
        ease 0.5 ypos 1.1

    brad "Thanks. I saw what you're reading. That's some weird stuff you're gonna talk about in front of Jack."

    show sayaka b_16

    sayaka "Oh, this? I'm just trying to read some books to figure out something completely unrelated. I couldn't give less of a shit about that jerk."

    show brad a_4

    brad "Uhuh. {q}Spiritual Bond{/q}... Didn't know you were into the... Metaphysical stuff and books like that, or what do you call it?"

    show brad a_1
    show sayaka b_2

    brad "What are you trying to figure out? I'm not into spirits and such, but you know I'm a great advisor, heh."

    show sayaka b_5
    show brad a_0

    sayaka "I really doubt you would be interested. Or even know anything about this."
    brad "That just piques my interest even more. Come on, you starting a new religion or something?"

    show sayaka b_24 at faceleft

    sayaka "{i}Sigh{/i}... Alright, because it's you..."

    show sayaka b_5

    sayaka "How do I even explain this so you get it..."

    show sayaka at faceright

    sayaka "Something that isn't possible happened. And I don't know how it happened or who or what did it."

    show brad a_3

    sayaka "So I've been trying to read any book about some sci-fi bullshit I could find but I'm getting nowhere with this."

    show brad a_4

    brad "Something impossible? Doesn't that just mean it is possible?"

    show sayaka b_16

    sayaka "Obviously. But I want to know how it happened, hence why I am reading this. But even after reading the first few pages I know this one's a dud as well."

    show brad a_5

    brad "But you don't want to share what happened?"
    sayaka "Fuck no. Only me and someone else can know about this."

    show brad a_1

    brad "Ah well, too bad."

    show brad a_0
    show sayaka b_2

    brad "But it sounds interesting. More interesting than whatever Mallory has planned for us."
    brad "Honestly I don't really know what else to tell you. Sounds to me like you're into something weird."

    show sayaka b_16

    sayaka "It totally is."

    show sayaka b_5
    show brad a_1

    brad "You know, when I was in middle school, Zoey did some weird-ass stuff too."

    show brad a_4

    brad "Oh, you know Zoey, my sister, right? She started here as a freshman this year."

    show sayaka b_2

    sayaka "I think I saw some yellow runt telling everyone she was your sibling or something yesterday."

    show brad a_7

    brad "She did?"

    show brad a_1

    brad "Hah, that's sweet of her."

    show brad a_0

    brad "Anyways, her shenanigans are really annoying sometimes, I wouldn't say that her pranks were out of this world or anything impossible like you claim your problem to be, but I grew to like it when she did something stupid."

    show sayaka b_24

    sayaka "God, it's so cliche to say that I can turn this into something positive."

    show sayaka b_16
    show brad a_7

    brad "I know, but cliche stuff is cliche because it's normal, right?"

    show sayaka b_5

    sayaka "And man, you really swoon over your sister, don't you?"

    show brad a_1

    brad "Can't help it."

    show brad a_4

    brad "Oh, and uh... Nice hair you got there...?"

    show sayaka b_16

    sayaka "Drop it, I know it's stupid."
    brad "Did you lose a bet?"
    sayaka "I tried to get back at someone but now I'm stuck with this ridiculous color."

    show sayaka b_24

    sayaka "{size=-5}It doesn't fit me at all right now...{/size}"

    show brad a_1
    show sayaka b_2

    brad "Was it Kat?"

    show sayaka b_7
    show brad a_4

    sayaka "Katrina? Fuck no. Why would you think that?"

    show sayaka b_16
    show brad a_6

    brad "Ah, you know, with the rumors going around and all..."

    show sayaka b_2

    think "The rumors?"

    show sayaka b_5

    sayaka "What rumors?"

    show brad a_5

    brad "About you and Kat."

    show sayaka b_16

    sayaka "I don't give a shit about her."

    show brad a_3

    brad "Man, you guys got into that bad of a fight?"
    sayaka "Let's not make this about her. What is the rumor?"

    show brad a_5

    brad "You know, you and Kat are seen as the {q}nerdy{/q} couple of the school, so you guys causing such a big fallout in the lunchroom has sparked all kinds of people to speculate."

    show sayaka b_5

    sayaka "So it's just that? Speculation?"

    show brad a_7

    brad "I don't really spend a lot of time thinking about rumors, man. Someone has started saying you made her cry deliberately, which I really don't buy."
    think "Of course you wouldn't buy it if it was {i}John{/i} you were talking to."
    think "The wettest noodle of them all."

    show brad a_0

    brad "Sorry about whatever went down, I know you guys liked each other."

    play sound sfx_bell
    show brad a_4

    "And thankfully, the bell rang for lunch just in time for me not having to deal with talking about that bitch anymore."

    show brad a_1

    brad "Damn, I took all your time now."
    brad "If you aren't studying for Mallory's torture lessons during his class then it must be pretty important, whatever you're doing."

    show sayaka b_0
    show brad a_0

    sayaka "It's okay. I needed someone to talk to."

    show brad a_1

    brad "Stressed week?"

    show brad a_0
    show sayaka b_10

    sayaka "Oh, you wouldn't know."

    show sayaka b_0
    show brad a_7

    brad "Hey, if you want, you can come along with me to our table during lunch. In case you're still not getting along with your friends."

    show sayaka b_5

    "Brad had never been this nice to any of the girls I knew, yet he was being a complete bro to freaking John of all people?"

    show sayaka b_15

    think "He isn't actually, like, secretly popular amongst the cool guy group, is he?"

    show sayaka b_6

    sayaka "Uhh... Sure, I think I'll take you up on the offer."

    show sayaka b_2

    sayaka "Better than sitting around doing nothing."

    show brad a_0

    brad "Cool. Let's jet."

    scene black with dissolve
    show bg lunch:
        zoom 1.5 xalign 0.8 yalign 0.95
    show sayaka b_0 at centerright, faceleft
    show brad a_0 at center, faceleft
    with dissolve

    "The last two days during lunch had been excessively boring."

    show sayaka b_5

    "I could barely afford my regular sandvich with the money John had and standing in line was a real pain."
    "Having Corny go fetch the food was what I always did. She would do it without asking."
    "But with John's shitty popularity I would barely be able to command anyone around."

    outfit rita uniform
    show sadie a_5 at Position(pos=(0.35, 1.0), anchor=(0.5, 1.0)):
        faceright
        alpha 0.0
    show rita b_11 at Position(pos=(0.55, 1.0), anchor=(0.5, 1.0)):
        faceright
        alpha 0.0
    show irene b_3 at Position(pos=(0.75, 1.0), anchor=(0.5, 1.0)):
        faceleft
        alpha 0.0
    show allison a_3 at Position(pos=(0.9, 1.0), anchor=(0.5, 1.0)) behind irene:
        faceleft
        alpha 0.0

    "Anyways, I might as well check up on whether the idiot has done anything stupid this time."

    show sayaka b_2:
        ease 0.5 xpos 1.2 alpha 0.0
    show brad:
        ease 0.5 xpos 0.95 alpha 0.0
    show bg lunch:
        ease 0.5 zoom 2.0 xalign 0.6 yalign 0.7
    show sadie:
        pause 0.25
        ease 0.5 alpha 1.0
    show rita:
        pause 0.25
        ease 0.5 alpha 1.0
    show irene:
        pause 0.25
        ease 0.5 alpha 1.0
    show allison:
        pause 0.25
        ease 0.5 alpha 1.0

    "While following Brad, I threw a look towards my table."

    #SKIP
    show sayaka:
        alpha 0.0
    show brad:
        alpha 0.0
    show sadie:
        alpha 1.0
    show irene:
        alpha 1.0
    show rita:
        alpha 1.0
    show allison:
        alpha 1.0

    "But my body wasn't there...?"

    hide sayaka
    hide brad

    "Neither was Corny."
    think "Are they late or something? It's already been three minutes and everyone else is there."
    brad "Hey, John..."
    sayaka "What?"
    brad "Did... Kiyoshi actually manage to score Sayaka...?"
    sayaka "Huh?"

    outfit john uniform_pony
    body cornelia cornelia
    outfit cornelia uniform
    outfit kiyoshi uniform
    show bg lunch:
        pause 0.25
        ease 0.5 xalign 0.1 yalign 0.65
    show sadie:
        ease 0.5 alpha 0.0
    show rita:
        ease 0.5 alpha 0.0
    show irene:
        ease 0.5 alpha 0.0
    show allison:
        ease 0.5 alpha 0.0
    show john a_6:
        centerleft
        faceright
        ypos 1.1
        alpha 0.0
    show cornelia a_6:
        center
        faceleft
        ypos 1.1
        alpha 0.0
    show kiyoshi a_2:
        left
        faceright
        ypos 1.1
        alpha 0.0

    "He pointed towards a completely different table in the back."

    show john:
        ease 0.5 alpha 1.0
    show cornelia:
        ease 0.5 alpha 1.0
    show kiyoshi:
        ease 0.5 alpha 1.0
    hide sadie
    hide rita
    hide irene
    hide allison

    "It was a bit hard seeing anything since Brad had the height advantage, but there they were."
    "John, Corny, and fucking Kiyoshi."
    think "What the?"
    think "Why the hell is he sitting with that perv?!"

    scene black with dissolve
    pause 0.5

    title "12th of August (Friday)" "Day 5 - John"

    show bg lunch:
        zoom 2.0 xalign 0.05 yalign 0.65
    show john a_0:
        center
        faceleft
        ypos 1.1
    show cornelia a_5:
        centerright
        faceleft
        ypos 1.1
    show kiyoshi a_2:
        centerleft
        faceright
        ypos 1.1
    with dissolve

    kiyoshi "Since yesterday I read three different light novels I found about the subject of swapping on the internet."
    kiyoshi "They were valuable research material, but ultimately, I do not believe in reincarnation, magic, or anything like that."

    show john a_6
    show kiyoshi a_1

    john "...Dude, why are you reading light novels?"
    john "That's fiction."

    show kiyoshi a_2

    kiyoshi "Wee~~~ell... Mostly because I got really drawn into the stories and ended up reading until three in the night yesterday."

    show kiyoshi a_1
    show john a_0 at faceright
    show cornelia a_15

    cornelia "I'm sorry, but what are you two clearly-not-somehow-dating-for-god-fucking-knows-what-reason people talking about?"

    show john b_18
    show kiyoshi a_4
    show cornelia a_14

    john "We aren't dating!"

    show john b_17

    kiyoshi "What you're suggesting is preposterous!"

    show john b_19

    john "Seriously, just imagining being with him romantically is disgusting."

    show john a_17
    show kiyoshi a_3

    kiyoshi "Extremely so. Bros don't do that."

    show kiyoshi a_0
    show cornelia b_23

    cornelia "Yeesh, I get it."
    cornelia "Apparently you're in on this... Weird swapping thing too."

    show cornelia b_17

    cornelia "But why are you suddenly so... Normal? Seriously, it freaks me out."

    show john b_25 at faceleft
    show cornelia b_18

    "Cornelia had a point on that one."
    "Kiyoshi was usually flirty as all hell around girls, especially Sayaka and Cornelia."

    show john b_23

    think "Well, {i}flirty{/i} is a generous way of saying it..."

    show john b_25

    "It's nice that he immediately accepted my story without thinking twice about it, but I half expected him to be flirty with me now as well."
    "Which luckily hasn't happend."

    show john b_27

    "Maybe he is actually more reliable than I thought?!"

    show john b_0
    show kiyoshi a_3

    kiyoshi "Normal?"
    kiyoshi "I am not normal, mind you. I am special."

    show cornelia b_11
    show kiyoshi a_0

    cornelia "Yes. Vee~~ery special."

    show john at faceright
    show cornelia a_0

    cornelia "Saya are you sure you don't want to go back to the other girls...?"

    show john b_2

    john "Relax. We're just sitting with Kiyoshi for today, we can sit with them tomorrow."

    show john b_1

    john "Kat and Kyoko apparently still don't want to talk about this, so it's good to catch up with him once in a while."

    show john a_20

    "And the entire Kat and Kyoko thing was a shame. I was sure they would relax at some point and not be pissed at me, or Kiyoshi for taking my side, but for now they didn't want to talk with us."

    show cornelia a_4
    show john b_5

    cornelia "If you say so..."

    show cornelia a_22

    cornelia "{size=-10}This week has been so fucking weird...{/size}"

    show john at faceleft
    show kiyoshi a_2
    show sayaka b_16 at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0)) behind john:
        faceleft
        alpha 0.0
    show brad a_5 at left behind kiyoshi:
        faceright
        alpha 0.0

    kiyoshi "It is good to hear that you also treasure our friendship."

    show kiyoshi a_1
    show sayaka:
        ease 0.5 alpha 1.0

    sayaka "Excuse me?"

    #SKIP
    show sayaka:
        alpha 1.0

    show cornelia b_28:
        ease 0.5 xpos 0.85
    show john b_11
    show kiyoshi a_0
    with hpunch

    cornelia "Eep!"

    show cornelia b_26
    show john at faceright

    "Someone suddenly poked me on my shoulder."
    "When I turned around, queen asshole was on time to surely nag me again."
    sayaka "What are you doing? With him? At the same table?"

    show cornelia b_17
    show john b_0
    show sayaka at faceright

    cornelia "Jeez, don't scare me like that, asshole!"

    show cornelia b_18
    show sayaka at faceleft

    john "Sayaka, I'm just eating lunch with my friends. Are you going to forbid me from doing that as well now?"

    show sayaka b_7

    sayaka "Uh, hello?! Yes?! Anyone but him! Did you tell them about us?"

    show sayaka b_16

    john "Of course I did. They both know we swapped."

    show sayaka b_20
    show cornelia b_26

    sayaka "You... Absolute... AAGH!"

    show john b_25

    sayaka "Is it so hard to do simple tasks like {q}don't interact with weirdos{/q}?!"

    #SKIP
    show brad:
        ease 0.5 alpha 1.0

    show kiyoshi a_4
    show cornelia b_31

    sayaka "Why are you doing this?! You're just ruining my reputation!"

    show sayaka b_21
    show brad a_4

    "Sayaka's half-way shouting was now garnering a bit of attention."

    show sayaka b_15:
        faceright
        pause 0.5
        faceleft
        pause 0.5
        faceright
    show john b_13

    "Attention that she noticed."

    show sayaka at faceleft

    "Even though the attention on us three was aplenty already because the number one girl in school was sitting with the most despised guy among the girls."

    show sayaka b_21

    sayaka "{size=-5}Why can you not do ONE thing properly?{/size}"

    show john b_17
    show cornelia b_5

    brad "Uh, John?"

    show john b_18
    show brad a_5

    john "You're not exactly keeping it a secret yourself in this public space either."

    show sayaka b_15
    show john b_17

    sayaka "...!"

    show john a_17

    john "You know he is actually willing to help try to reverse the swap."

    show sayaka b_16

    sayaka "Oh spare me the formalities, I know you're probably just as much of a sick perv as him and want to take advantage of this."

    show cornelia b_29
    show john b_0

    cornelia "Hold on."

    show sayaka at faceright

    "The girl that was pretty much sinking into her chair out of confusion finally spoke up."

    show cornelia b_31

    cornelia "Is... Is this entire swap thing actually a real thing?"

    show sayaka b_7

    sayaka "No! No swaps, no nothing! I'm Dumbass Davis and he is Sayaka Sato!"

    show sayaka b_16 at faceleft
    show john b_6

    john "You know that you can trust her, right?"

    show sayaka b_21

    sayaka "N-"

    show cornelia b_11
    show john b_23

    think "Heh, if you answer no here it would make you look bad, wouldn't it?"

    show john b_31

    john "As I tried telling you this morning, yes, me and Sayaka swapped bodies for some reason."

    show brad a_4

    cornelia "..."

    show cornelia a_22
    show sayaka b_16 at faceright

    cornelia "But that shouldn't be possible..."

    show john b_27
    show sayaka b_15

    brad "Oh damn, I think I've heard something I shouldn't have heard."

    show sayaka at faceleft
    show john at faceleft

    john "Huh? Brad?!"

    show cornelia a_20

    think "What the heck is he doing here? I hadn't noticed him at all."

    show john b_13 at faceright

    john "Uh... Guess someone else is in on it then."

    show brad a_5

    brad "Was that the {q}impossible{/q} thing you told me about then, John?"

    show sayaka b_16

    show john a_13 at faceleft

    john "{i}Sigh{/i}... She, or he, whatever, is Sayaka, not John."

    show brad a_4

    brad "Whoah. So I was talking to Queenie all the time?"
    brad "That's trippy."

    show john a_6

    think "He is... unusually accepting as well."

    show sayaka b_20
    show john b_0 at faceright
    show cornelia b_31

    sayaka "Fine! Anyone else want to know?!"

    show sayaka b_15

    sayaka "{size=-5}Wait, did you just call me Queenie-{/size}"

    show john b_3
    show sayaka b_16

    john "Sayaka, chill. Let's just put all the stuff we've done behind us and actually get help on this, alright?"

    show sayaka b_7

    sayaka "Alright?! You probably still haven't lifted a finger trying to figure out how to swap back!"

    show john b_19
    show sayaka b_16

    john "I got Kiyoshi to help us!"

    show sayaka b_7
    show john b_3

    sayaka "Bullshit! I bet you've been oggling all over me ever since you told him!"

    show sayaka b_16
    show cornelia a_22

    cornelia "Uhm... I think he {i}is{/i} trying to help..."

    show sayaka b_21 at faceright
    show john b_6
    show cornelia a_8

    "Sayaka turned her absolute fury towards Cornelia now."
    think "Boy, this girl is a living volcano..."

    show sayaka b_20
    show brad a_3

    sayaka "You're siding with them now, Corny?!"

    show sayaka b_16
    show cornelia b_32

    cornelia "Wha- N- No! Im not siding with anybody! Everything they've talked about for lunch was how they want to figure out how to swap back or something!"

    show john b_0
    show kiyoshi a_1
    show cornelia b_31
    show sayaka b_5

    sayaka "...They did?"

    show sayaka at faceleft
    show john b_18

    john "If the first thing you do wouldn't be yelling at us, then you would know that Kiyoshi wants to help us."

    show john b_17

    john "Considering how desperate you are to swap back, I'd say you should say thank you to any help you can get, especially from someone as... Uh... Unorthodox as Kiyoshi."
    john "You know, the nerd who knows a thing or two about weird stuff?"

    show kiyoshi a_3
    show john a_5 at faceleft

    kiyoshi "Hey, what I am researching are legitimate theories."

    show john a_0
    show kiyoshi a_0

    john "Legitimate, but also weird."

    show sayaka b_2

    sayaka "...Are you actually willing to help us then? Without being your usual shitty self?"

    show kiyoshi a_2

    kiyoshi "I very much plan to, oh maiden in need of ai-"

    show kiyoshi a_1
    show sayaka b_16
    show john at faceright

    sayaka "Yeah yeah, whatever. Fine then."

    show john b_1

    "For the first time, I was able to calm her down, if even a little. Be it with the help of two other people, but still, we've tamed the dragon."

    show brad a_7
    show kiyoshi at faceleft
    show cornelia b_0
    show sayaka b_5
    show john b_0 at faceleft

    brad "Uh, so yeah, good luck to you guys."

    show sayaka b_16

    sayaka "Ugh, you heard everything, didn't you?"

    show brad a_1

    brad "Sorry, it was just a bit too interesting to listen for me to just bail out of the conversation."

    show brad a_5

    brad "But you and Sayaka have switched places then?"

    show cornelia b_17
    show john at faceright
    show sayaka b_2 at faceright
    show kiyoshi a_0 at faceright

    cornelia "Seriously, this isn't a prank, right?"

    show cornelia b_18
    show kiyoshi a_1

    kiyoshi "They very much have. I am sure you have both taken notice to how they act very differently now."

    show kiyoshi a_6
    show john at faceleft
    show sayaka at faceleft

    kiyoshi "For example, John's body over there is for some unexplainable reason secretly attracted to me now."

    show kiyoshi a_1
    show sayaka b_16
    show john a_32

    sayaka "I am not attracted to you, you fucking perv."

    show kiyoshi a_2

    kiyoshi "Denial is the sweetest way of showing love."

    show cornelia a_0
    show brad a_0
    show john a_0
    show sayaka b_5

    brad "Hmm..."

    show brad a_1

    brad "I'll buy it. But I'm also hungry. See you guys later."

    show john a_14

    john "See ya."

    scene black with dissolve
    show bg lunch:
        zoom 2.0 xalign 0.05 yalign 0.65
    show john a_0 at Position(pos=(0.6, 1.1), anchor=(0.5, 1.0)), faceleft
    show cornelia a_5 at Position(pos=(0.8, 1.1), anchor=(0.5, 1.0)), faceleft
    show kiyoshi a_1 at Position(pos=(0.2, 1.1), anchor=(0.5, 1.0)), faceright
    show sayaka b_5 at Position(pos=(0.4, 1.1), anchor=(0.5, 1.0)), faceleft
    with dissolve

    sayaka "So exactly {i}what{/i} have you looked at so far? Any books? Articles?"
    kiyoshi "I have only dabbled in a few light novels so far. These stories turn out to be quite expansive in some cases."
    kiyoshi "The methods of swapping here are typically connected to an event or mere coincidence."

    show kiyoshi a_2

    kiyoshi "But it is too soon to make any firm conclusions. Besides, this phenomenon has opened up the doors for an entirely new genre for me."

    show kiyoshi a_1
    show john a_6
    show sayaka at faceright

    john "Like I said, light novels are fiction. They don't help."

    show sayaka b_16

    sayaka "Are you kidding me? Of course they help! Would you not categorize what {i}really happened{/i} to us as fiction under normal circumstances?"

    show john a_0

    john "Well, if you put it like that..."
    sayaka "If anything, we might get ideas on what to do in order to swap back."

    show sayaka b_5 at faceleft

    sayaka "And I fucking hate to say it, but please help me by looking for clues. Your weirdo-factor actually would come in useful for once."
    "Sayaka was being sincere towards Kiyoshi for once. I bet it helped being able to communicate with him because she has my body."
    "With him not creeping out on her, he was being much more normal towards her and all."

    show kiyoshi a_6

    kiyoshi "Anything for my darling in peril."

    show john a_31

    think "Or maybe I just imagined him being more normal."

    show kiyoshi a_0
    show john b_0

    kiyoshi "It is a shame though. I would imagine that Kyoko would love to have a closer look at this phenomena as well."

    show john b_4
    show sayaka at faceright

    john "Yeah, I kind of hoped they would get around to realizing this is a thing by now."

    show sayaka b_16
    show cornelia b_18

    sayaka "You want to tell {i}those{/i} two as well?"

    show john b_7

    sayaka "Aren't you fine with this guy just knowing? Or are you going to tell the entire fucking school?"

    show cornelia b_17
    show john b_13 at faceright

    cornelia "I agree, you should keep this between us."

    show cornelia b_24

    cornelia "And especially far away from them."

    show john a_26
    show cornelia b_14

    john "What is your deal with Kat and Kyoko anyways?"

    show john a_6 at faceleft

    john "I get why you don't like Kiyoshi since he's Kiyoshi..."

    show kiyoshi a_5

    kiyoshi "Hey, I don't like the way you phrase your descriptions of me today, J-girl."

    show kiyoshi a_0
    show john a_13

    john "But what have they ever done to you two?"

    show cornelia b_26
    show sayaka b_5
    pause 1.5

    cornelia "...Uhm..."

    show cornelia a_11
    show sayaka b_16
    show john b_0 at faceright

    "Cornelia looked at Sayaka as if asking for permissions."

    show john at faceleft

    "I know that Sayaka and Kat have a background, so maybe she knows a bit about it. But without Sayaka's permission she probably won't say a word."

    show cornelia a_4

    sayaka "No. Go be buddy-buddy with gingerface and that nerd if you want to. But don't drag me into it!"
    sayaka "Actually, don't be buddy-buddy with them at all while you're posing as me."

    show john b_18

    john "God, you don't ever get it, do you?"

    show john a_17

    sayaka "Get what?!"

    show john b_18
    show cornelia a_0

    john "How absolutely bitchy you are. Can't you talk about them normally with us and tell us what your issue is instead of this bullshit?"

    show sayaka b_7
    show john b_17

    sayaka "Fuck you. I didn't ask for any of this to happen!"

    show sayaka b_16

    sayaka "Also, why have you been rubbing your eyes all this time?"

    show john a_13

    john "Huh?"
    "Ah. I was doing it subconsciously at this point, but my eyes had become {i}really{/i} itchy now."

    show john b_4

    john "I don't know, it hurts like hell and I was going to ask you anyways."

    show sayaka b_5
    show cornelia b_0

    john "Sometime yesterday it suddenly started itching, and whenever I touch my eyes it hurts like hell."
    sayaka "When you touch your eyes...?"

    show sayaka b_16
    show john b_5

    sayaka "Did you not clean my co-"

    show sayaka b_15
    show john b_6

    "She just stopped herself midway during her sentence, as if not wanting to be heard."

    show sayaka b_5:
        ease 0.5 xpos 0.45

    sayaka "{size=-5}Did you not clean my contact lenses properly?{/size}"

    show john a_13

    john "Contact lenses?"

    show sayaka b_16

    sayaka "Shh!"

    show cornelia b_11

    cornelia "Oh yeah, that's right! When did you last clean them?"

    show kiyoshi a_4

    kiyoshi "{size=-5}My darling uses contact lenses?{/size}"

    show john a_5

    john "..."

    show john a_30

    john "Clean them...?"
    "Sayaka uses contact lenses?"
    "I've literally not even once noticed or heard anything about that."

    show kiyoshi a_1

    kiyoshi "Ah, you are supposed to clean those every day, J-girl."

    show john b_27
    show sayaka b_7

    sayaka "Seriously?! I even gave you  list of things to do!"

    show john b_28
    show sayaka b_16

    john "You gave me seven pages to read through!"

    show john b_27
    show sayaka b_7
    show cornelia b_24

    sayaka "Did I not make it clear to read through all seven pages?!"

    show sayaka b_16

    john "..."

    show john b_17

    john "Maybe..."

    show sayaka b_25

    sayaka "Oh my fu-"

    show sayaka b_7:
        ease 0.5 ypos 1.0

    sayaka "Come with me you fucking noodle brain."

    show sayaka b_16:
        ease 0.25 xpos 0.5
        pause 0.25
        faceleft
        pause 0.25
        ease 0.75 xpos 0.2 alpha 0.0
    show john b_28:
        pause 0.25
        faceright
        ease 0.25 ypos 1.0
        pause 0.25
        ease 0.75 xpos 0.285 alpha 0.0
    show kiyoshi a_0:
        pause 1
        faceleft

    "With that, she yanked me up and dragged me out of the lunchroom."

    scene black with dissolve
    scene bg school bathroom day
    show sayaka b_16:
        centerright
        faceleft
        alpha 0.0
    show john b_11:
        right
        faceleft
        alpha 0.0
    pause 0.5
    play sound sfx_door_close
    show sayaka:
        ease 0.5 center alpha 1.0
        pause 1
        faceright
    show john:
        pause 0.5
        ease 0.5 centerright alpha 1.0
    pause 0.5

    "She dragged me into the women's bathroom."

    #SKIP
    show john:
        centerright
        alpha 1.0
    show sayaka:
        center
        faceright
        alpha 1.0

    "Not that there was anything wrong with being here in my current situation, but..."

    show john b_18

    john "Why do we have to go in here together? If anyone sees me being in here together with a girl, it's going to spread rumors like wildfire!"

    show john b_17

    sayaka "Who cares about you. You need to remove the lenses right now so just deal with it."
    john "We could've just have done this in the boy's bathro-"

    show sayaka b_7
    show john b_27

    sayaka "Are you fucking stupid?! What if someone caught me being in there? Rumors would spread like wildfire!"

    show john a_6
    show sayaka b_16

    think "..."
    sayaka "Now get your ass to the mirror!"

    show john b_25

    john "Fine..."

    show john:
        ease 0.5 xpos 0.5
    show sayaka:
        ease 0.25 xpos 0.375

    think "If it would remove this terrible itch then I'd put up with her shit."

    show john b_0
    show sayaka b_5 at faceleft

    sayaka "Good. Now put a finger on your lower eye-lid and look up."

    show john a_6

    john "I do what?"

    show sayaka b_16 at faceright

    sayaka "Those instructions were, like, the {i}simplest{/i} instructions ever."

    show john a_32

    john "Well excusez moi, Ms. Perfect, but I've never done this before."

    show sayaka b_24 at faceleft
    show john a_0

    sayaka "{i}Sigh{/i}..."

    show sayaka b_16 at faceright

    sayaka "Finger under your eye-lid."

    show john b_0:
        transform_anchor True
        ease 0.75 rotate 5 ypos 1.05

    john "Alright."

    show john b_13
    show sayaka at faceleft

    "Really, something so simple should not be this terrifying."
    "Sayaka's nails were, despite me not taking care of them at all, long and lethal to the eye."
    "If I jerked my finger upwards, I would practically pierce my eye."

    show sayaka b_5

    sayaka "Now look up."
    sayaka "The lens should slide down. Then you can grab it."

    show john b_28

    john "I what?! Grab it with these nails?!"

    show sayaka at faceright

    john "Oh god this feels weird as fuck!"

    show sayaka b_7
    show john b_27

    sayaka "Stop crying you baby! Just pick it and take it out!"

    show john b_11

    "Easier said than done. Her nails were a thing, and I honestly have absolutely no idea of how not to mutilate my eyes like this."

    show sayaka b_5 at faceleft

    sayaka "Just use the... What's the word for it..."

    show john b_26
    show sayaka at faceright

    john "Oh god I can feel it slowly sliding down under my eyelid!"

    show john b_27
    show sayaka b_7

    sayaka "Pinch it out already! Use your... fingerprint-place of the finger!"

    show sayaka b_16
    show john b_28

    john "What the fuck is the fingerprint-place of the finger?!"

    show sayaka b_20

    sayaka "Pinch it between your fingers! How hard can it be?!"

    scene black with dissolve
    pause 1

    title "12th of August (Friday)" "Day 5 - Zoey...?"

    scene bg school hallway2 day
    show zoey a_0 at centerleft, faceleft
    show mel a_7 at center, faceleft
    with dissolve

    zoey "Oooh! And a burger place too! My great bro told me all about it!"

    show zoey b_2

    zoey "You're gonna be totally flabbergasted at their food!"

    show zoey b_0
    show mel b_0

    mel "Sounds like you have this place mapped out fine, girl."

    show mel a_2

    mel "You know, burgers are somewhat of a specialty in my home-"

    show zoey b_6
    show mel a_0

    zoey "Wait... Do you hear that?"

    show mel a_7

    mel "Huh?"

    show zoey b_4

    zoey "From in there."

    show zoey a_2:
        ease 0.75 xpos 0.2
    show mel a_8:
        ease 1 xpos 0.35

    mel "I can't hear anythin-"

    show mel a_7
    show zoey a_3

    sayaka "{size=-7}Just let me get it myself already!{/size}"
    sayaka "{size=-7}You fucking suck at this!{/size}"

    show mel a_8

    john "{size=-7}N- No! Don't do it like that!{/size}"
    john "{size=-7}Oh god it's even further in now! Get it out!{/size}"
    mel "...Are they... Doing it in there?"

    show zoey a_4 at faceright

    zoey "Of course. This school really is just like Brad explained it."

    show zoey a_2 at faceleft
    show mel a_6

    john "{size=-7}Oh my god! I finally got it out!{/size}"
    john "{size=-7}Wait, no. Now it's stuck to my fingers! This stuff is sticky as hell!{/size}"

    show zoey a_4 at faceright

    zoey "Students are bold and full of youth here. It was a great idea to go to this high school."

    show zoey a_2

    mel "I'm really starting to regret entering this school if this is what happens in the first week..."

    show zoey a_3

    zoey "We should give them our respect and leave them alone."

    show mel a_6

    mel "...Yeah..."

    show mel:
        faceright
        ease 0.75 center alpha 0.0
    show zoey:
        ease 0.75 centerleft alpha 0.0

    sayaka "{size=-7}Fucking finally!{/size}"
    sayaka "{size=-7}Now take out the other one.{/size}"
    john "{size=-7}...There's another one?!{/size}"
    sayaka "{size=-7}In the other eye, you fucking idiot.{/size}"

    scene black with dissolve
    scene bg school hallway day
    $ screenfilter.blur = 2
    show black
    show sayaka b_5 at Position(pos=(0.6, 1.0), anchor=(0.5, 1.0)), faceright
    show john b_3 at Position(pos=(0.4, 1.0), anchor=(0.5, 1.0)), faceright
    hide black
    with dissolve
    pause 1

    john "Seriously, I can't see anything."

    show sayaka b_16

    sayaka "And that won't change after telling me three fucking times about it! I get it, my eyesight is shit. Can we move on to something else? Or just not talk anymore, preferably?"

    show john b_5

    john "Fine. Can you tell me the code to your phone then?"
    sayaka "Why, so you can go snoop around on even more personal stuff?"

    show john b_17

    john "So I can use your fucking phone. I'm only able to take calls right now."
    sayaka "Got anything else interesting you want to do with it?"

    show john b_18

    john "Well, yes, call you in case I need to know something. Or order take-out since your parents don't do a single thing all day except tell me how uninterested they are in me. Oh wait, they don't even bother telling me that."

    show john b_17
    show sayaka b_21 at faceleft

    sayaka "Listen here, you little piece of shit."

    show john b_27

    sayaka "You can make fun of everything else and make me look like a circus clown, but if you dare say anything bad about mom and daddy, then you can kiss your ass goodbye. Got it?"
    "Whoah, she shifted tone entirely. This must be a touchy subject, even for her."

    show sayaka b_16
    show john b_25

    john "Jeez, fine."

    show john b_18

    john "Still, could I at least have my own phone so I can do anything interesting during the entire day? All I have is TV right now."

    show sayaka at faceright
    show john b_17

    sayaka "You want {q}Sayaka{/q} to have {q}John's{/q} phone? No way. Besides, I can't trust you with anything that resembles a camera while you're in control of me."

    show john b_22

    john "Can't you at least put a little trust in me? It's not like I'm planning to tear your life down."
    sayaka "No."

    show sayaka b_5

    sayaka "Now fuck off, we're already five minutes behind for classes because you spent eternity trying to get contact lenses off."
    think "Just when you think you can get along with her, she blasts you with a nuke of hostility..."
    think "I don't think I'll ever be able to have a normal conversation with her."

    scene black with Dissolve(2.0)

    title "Later on the same day..."

    $ screenfilter.blur = 0
    outfit AN_john uniform_c
    show AN_asset main bathroom night mirror as mirror
    show AN_asset main bathroom night cut mirror as bg
    show AN_john b_5 behind bg:
        alpha 0.5
        faceright
        center
    show sayaka b_5 at centerright, faceleft
    with dissolve
    pause 1.5

    sayaka "..."

    show sayaka b_25
    show AN_john b_25

    sayaka "Argh! Why the fuck did I dye my hair with this stupid color?!"

    scene black with Dissolve(1.0)

    title "13th of August (Saturday)" "Day 6 - John"

    $ screenfilter.blur = 2
    outfit AN_harry uniform
    scene bg school classroom hallway day with dissolve
    play sound sfx_sliding_door_open
    scene bg school classroom hallway day open
    pause 0.5
    show cornelia a_5:
        center
        alpha 0.0
        faceleft
    show john b_6:
        centerright
        alpha 0.0
        faceleft
    show AN_harry a_8:
        right
        alpha 0.0
        faceleft
    with dissolve
    show cornelia:
        ease 0.75 centerleft alpha 1.0
    show john:
        pause 0.25
        ease 0.75 center alpha 1.0
    show AN_harry:
        pause 0.5
        ease 0.75 centerright alpha 1.0
    pause 1.5

    john "Bah, Mallory's class is still as boring."

    #SKIP
    show john:
        alpha 1.0
        center
    show cornelia:
        alpha 1.0
        centerleft
    show AN_harry:
        alpha 1.0
        centerright

    show john b_25
    show cornelia a_17 at faceright
    show AN_harry a_3

    cornelia "Boring? It's fucking lametown in there. I'm starting to get sick of listening about torture chambers for the 3rd year in a row."
    cornelia "Like you'd think he actually has a personal dungeon at home."

    show john b_2
    show cornelia a_1

    john "Heh, wouldn't surprise me."

    show john b_1 at faceright
    show cornelia a_0
    show AN_harry a_11

    AN_harry "Well, thanks for having me in your project group."

    show AN_harry a_0

    AN_harry "It's usually always a pain to do these on my own."
    "After meeting him in that P.E. session, it turned out that this Harry guy was actually pretty chill to talk with."
    "When I saw how he had nobody to talk to during Mallory's class, I invited him over to work with Cornelia and me on our project, which he happily accepted."

    show cornelia a_1

    "Not even Cornelia was against it, it looked like she liked him too, even if he had a reputation of being quite the loner."
    cornelia "Tell us when you're done with your stuff."

    show AN_harry a_1

    AN_harry "Will do. See you guys later, and have a good weekend."

    show AN_harry a_0:
        faceright
        ease 1 offscreenright alpha 0.0

    "We waved him goodbye and we went on our way to talk with Sayaka over lunch again."

    scene black with dissolve
    scene bg school hallway day
    show cornelia b_0 at centerleft, faceleft
    show john b_1 at center, faceleft
    with dissolve

    john "Hm, at least Mallory doesn't torture me personally anymore, which is a nice change of pace."

    show cornelia a_11

    cornelia "Torture-what now?"

    show john b_3

    john "Ah, I guess you wouldn't know. Mallory kept bullying me or something when I was in front of him as John, but when he thinks I'm Sayaka he treats me like all the others. It's really weird."

    show cornelia b_9

    cornelia "Huh..."

    show john b_5
    pause 1.5
    show cornelia b_23

    cornelia "Hey, Saya..."

    show john b_13
    show cornelia b_5

    john "What's up?"

    show cornelia a_11 at faceright

    cornelia "Were you guys serious about what you said yesterday? About... Uh, swapping bodies or something."

    show john b_7

    think "Hm? I thought we already had her on board with this."

    show john b_3
    show cornelia a_0

    think "She is the exact opposite of Kiyoshi on this I guess. Well, I can respect her being sceptical about this entire thing."

    show john a_14

    john "Yes, I'm actually John on the inside. Even Sayaka told you yesterday, right?"

    show cornelia b_24
    show john a_10

    cornelia "Hm... Right."

    show john b_1

    cornelia "It's just really freaky thinking that I'm {i}not{/i} talking with the real Saya right now."

    show cornelia b_5
    show john b_2

    john "Hey, I totally get it. Cornelia, if it were you who swapped with Kyoko or something, I would probably take at least a week or two before I believed it."

    show john b_29

    john "I'm not judging you or anything for not believing it outright."

    show cornelia b_4

    cornelia "Right."

    show john b_0
    show cornelia b_24

    cornelia "It's still really weird that you're not calling me Corny with that voice though."
    john "You want me to?"

    show cornelia b_23

    cornelia "No, no, if you did then I'd think you were really Saya."

    show cornelia b_24

    cornelia "Unless you're playing some elaborate prank on me and you {i}are{/i} Saya."

    show cornelia b_0
    show john b_11
    show irene b_4 at Position(pos=(0.9, 1.0), anchor=(0.5, 1.0)):
        alpha 0.0
        faceleft
    show allison a_3 at Position(pos=(0.975, 1.0), anchor=(0.5, 1.0)):
        alpha 0.0
        faceleft
    show rita b_11 at Position(pos=(1.05, 1.0), anchor=(0.5, 1.0)):
        alpha 0.0
        faceleft

    irene "Hey!"

    show irene:
        ease 0.5 alpha 1.0 xpos 0.7
    show allison:
        ease 0.75 alpha 1.0 xpos 0.8
    show rita:
        ease 1.0 alpha 1.0 xpos 0.9
    show john at faceright
    show cornelia at faceright

    irene "You two!"

    #SKIP
    show irene:
        alpha 1.0
        xpos 0.7
    show allison:
        alpha 1.0
        xpos 0.8
    show rita:
        alpha 1.0
        xpos 0.9

    show cornelia a_1

    cornelia "Oh, it's Irene and the others."
    "I noticed that as well. But this time she was accompanied by four or five other girls, including Allison and Rita."
    "All of them were part of Sayaka's group, I believe?"
    "All I knew about them was that they talked to themselves at the same table as me and Cornelia."

    show john a_10

    john "Hey, what's up."

    show irene b_1

    irene "You going to ditch us again for the weirdo guys?"

    show john a_14

    john "For today too, yeah. Sorry, we'll talk another time I guess."

    show john a_0
    show cornelia a_5
    show irene b_8
    show rita a_22

    irene "Heh, thought as much. Be sure not to bore yourself to death hanging out with those losers."

    show cornelia a_8
    show irene:
        ease 0.75 alpha 0.0 xpos 0.4
    show allison a_0:
        ease 0.75 alpha 0.0 xpos 0.5
    show rita:
        ease 0.75 alpha 0.0 xpos 0.6
    show john:
        pause 0.75
        faceleft
    show cornelia:
        pause 0.85
        faceleft

    john "Uh... Thanks...?"

    pause 1.5
    show cornelia b_8 at faceright

    cornelia "{size=-5}Saya, we should go to their table today.{/size}"

    show john a_6

    john "Huh? Why?"

    show cornelia b_17

    cornelia "{size=-5}Did you not see what just happened? That was a complete power move on you right there!{/size}"

    show john b_6
    show cornelia b_14

    john "If you're whispering you might as well call me by my real name."

    show john a_13

    john "Also, what? She simply asked us if we were gonna spend lunch together and I told her we had stuff to do."

    show cornelia b_23

    cornelia "Ugh, you don't get it!"
    cornelia "She is trying to take the lead of our friend group into her own hands now that you're wasting time with loser town!"

    show john b_12
    show cornelia b_24

    john "Eh... I'm sure you're just overreacting. Irene seems nice enough to not be doing something as petty as that."

    show cornelia b_23
    show john b_13

    cornelia "Fine. Just... Be sure to keep Saya's status up, okay?"

    show cornelia b_5 at faceleft
    show john b_0

    "If Cornelia was right, it might just make Sayaka even more angry."
    "Not that I really care, but I've felt increasingly uncomfortable being in her shoes for a long time now, with her only actual friend to talk to being Cornelia."

    scene black with dissolve
    scene bg school stairs day
    show cornelia b_5 at center, faceleft
    show john b_4 at centerright, faceleft
    with dissolve

    "Now that I started to think about it, I've barely even spoken to her parents even though I've countless times tried striking up {i}some{/i} kind of conversation with them, if they are even home. But they completely ignore her."
    john "{size=-10}Sigh...{/size}"
    think "And this crappy vision..."
    think "Not having glasses or contact lenses is going to be the end of me."

    show john b_5

    "Every day just made me want to swap back even more, even though some would probably kill to some hot chick."
    "It's one of those things where it's fun for the first few days, but gets incredibly boring as time passes."

    show john b_0

    john "Hey, Cornelia."

    show cornelia b_0

    cornelia "What's up?"

    show john b_4

    john "What does Sayaka do in her spare time?"

    show cornelia a_14 at faceright

    cornelia "What she does?"

    show cornelia a_11 at faceleft

    cornelia "I don't know what she does at home, but we typically go shopping."

    show john b_0

    john "Ah yeah, you've asked me to go shopping a few times already."

    show cornelia a_14 at faceright

    cornelia "Why are you asking?"

    show john a_32

    john "Because I'm bored whenever I go home. All I can do is watch tele and they only have like 5 crappy channels to watch."

    show john a_21

    john "She refuses to give me her password for her phone and computer, and there is no console or anything I can use."

    show cornelia a_11
    show john a_20

    cornelia "Hmm... I see."

    show cornelia a_10

    cornelia "Do you want to try shopping?"

    show john a_0
    show cornelia a_1

    "Well, of course I didn't want to."
    "It's shopping. The most boring thing you can do in your free time."

    show john a_32

    "But with today being a half-day, there were still a good twelve hours or so before the day ended, so sitting around doing nothing for so long made the offer more enticing."

    show john a_14

    john "Yeah, screw it. Sure. We should ask Sayaka to tag along as well."

    show john a_5
    show cornelia a_3

    cornelia "No we shouldn't. Your reputation is already hitting fucking spikes on the bottom of a hole. No way you're going to be seen in public with an actual low-life like John as well."

    show cornelia a_5

    cornelia "And besides, she already has enough to worry about. I'll make sure you don't end up doing something she doesn't want to, like buying clothes from some shitty brand."

    show john a_6

    john "You know I'm here, right?"

    show cornelia a_6

    cornelia "Like I care, you already know I think you're a loser."

    show john a_14

    john "That's hurtful."

    show cornelia a_1

    cornelia "You better prove me wrong then. Let's go after we've talked with Saya."

    show john a_1

    john "Sure."

    scene black with dissolve
    pause 0.5
    scene bg lunch
    show sayaka a_8 at Position(pos=(0.4, 1.1), anchor=(0.5, 1.0)), faceleft
    show kiyoshi a_10 at Position(pos=(0.2, 1.1), anchor=(0.5, 1.0)), faceright
    with dissolve

    sayaka "What else?"

    show kiyoshi a_1

    kiyoshi "Headbutts."

    show sayaka a_5

    sayaka "Alright. Head... Butts..."
    "Huh. I never imagined I'd see the day come."
    "Sayaka sitting at the same table as Kiyoshi, alone, and they were talking with each other."

    show john b_0:
        alpha 0.0
        right
        faceleft
    show cornelia b_13:
        alpha 0.0
        centerright
        faceleft

    "She had a small notebook she was writing in. Definitely related to swapping us back."

    show cornelia:
        ease 0.5 xpos 0.6 alpha 1.0
    show john:
        pause 0.25
        ease 0.5 xpos 0.8 alpha 1.0

    cornelia "Hey Saya."

    #SKIP
    show john:
        xpos 0.8
        alpha 1.0
    show cornelia b_1:
        xpos 0.6
        alpha 1.0

    show sayaka at faceright

    sayaka "Hm? Oh, Corny."

    show sayaka a_16

    sayaka "And you."

    show cornelia a_1:
        ease 0.5 ypos 1.1
    show john a_34:
        ease 0.65 ypos 1.1

    john "I feel very welcome."

    show kiyoshi a_7
    show sayaka a_5 at faceleft
    show john a_0
    show cornelia a_0

    kiyoshi "J-girl and Corny! Good timing to arrive."

    show sayaka a_5 at faceright
    show cornelia a_19
    show kiyoshi a_16

    cornelia "Don't ever call me Corny again."

    show cornelia a_5

    kiyoshi "I see. Perhaps you're more of a {q}{i}Nelia{/i}{/q} kind of girl?"

    show cornelia a_14
    show john a_31

    cornelia "Don't call me by any of your nicknames!"

    show kiyoshi a_12

    kiyoshi "Cornelia it is!"

    show john a_5
    show cornelia a_5

    john "And could you at least settle on a name for me instead of changing it every time we meet? Not that I'd be against you just calling me by my name as well."

    show sayaka a_16 at faceleft
    show kiyoshi a_0

    sayaka "Who cares about nicknames. You got anything else?"

    show kiyoshi a_4

    kiyoshi "I am afraid that this was it for now. But even if these methods end up without success, I've found a treasure trove of material that I can research during the weekend."

    show kiyoshi a_6

    kiyoshi "If you know what I mean by that, J-S-Girl."

    show john a_6
    show sayaka a_5
    show cornelia a_15

    "For some reason he was winking with one of his eyes towards me, even though it was clear as day that the two girls saw him doing the gesture and knew exactly what he meant."
    sayaka "You mean you've found some sicko porn somewhere?"

    show kiyoshi a_16

    kiyoshi "It is not si- ...Uhhh... Noo...?"

    show john a_5
    show cornelia a_6

    sayaka "As long as I don't have to read that shit and you find methods that could swap us back, whatever."

    show sayaka at faceright

    john "You're finding ways to re-enact the swap?"

    show cornelia a_5

    sayaka "Yes. We can try some of them right after we leave here."

    show kiyoshi a_1

    john "Mind if I ask what we're trying?"
    sayaka "{i}Sigh... {/i} Yes..."

    show sayaka a_16

    sayaka "But just so your brain understands the circumstances, I am {b}only{/b} doing these things to hopefully turn things back to normal. Kapish?"

    show john a_13

    john "Yeah yeah."

    show sayaka a_5

    sayaka "So far we have drinking the same cup of water, ingesting each other's DNA... And, uh... {size=-5}Kissing...{/size} And headbutting each other."

    show john a_10
    show cornelia a_7

    john "Oh. Sounds goo-"

    show john a_3

    john "{i}Kissing?!{/i}"
    cornelia "No way you would make out with him, Saya!"

    show sayaka a_16

    sayaka "{size=-5}Shut the fuck up, both of you. If you're going to talk about something this gross then do it quietly! People are listening to everything we're saying!{/size}"

    show john a_8:
        faceright
        pause 0.75
        faceleft
        pause 1
        faceright
    show cornelia a_8

    "I instinctively looked around, and sure enough, there were some who had their attention on us. Not many, but some."

    show john a_9
    show cornelia a_0

    "Starting rumors like this would be bad right now."

    show john a_17 at faceleft

    "Even though plenty rumors are probably making their rounds already."
    john "Still, even if we were in death's stranding I'd never imagine that you of all people would actually agree to that."

    show sayaka a_7

    sayaka "Do I look like someone who wants to do that?"
    sayaka "As I said, this is only for us to turn back."
    sayaka "And as if it's not bad enough with it being you, kissing myself is weird as fuck. So don't think I'm doing it for fun or because I would enjoy it."

    show john a_27
    show sayaka a_16

    "Oh yeah. That would mean me kissing myself as well."
    "Shit, is that considered gay? Technically?"

    show john a_8

    "Besides, my first kiss would be with myself!"

    show john a_30
    show kiyoshi a_18

    kiyoshi "Good on you S-man, if I could be in your shoes I'd take the offer."

    show john a_27
    show kiyoshi a_6

    john "Who are you talking to now with that nickname? Me or Sayaka?"
    kiyoshi "You, obviously."

    show sayaka a_5 at faceleft
    show john a_0
    show kiyoshi a_17

    sayaka "If I was stuck as Kiyoshi I think I'd jump off a cliff the moment I had the opportunity."

    show john a_11
    show sayaka at faceright

    john "Hey hey, you just said something positive about me!"

    show cornelia a_6
    show sayaka a_16
    show john a_10
    show kiyoshi a_0

    sayaka "I said that between Nazi Germany and North Korea, I would rather want to live in North Korea."

    show john a_15

    sayaka "North Korea being you in case you missed the analogy. Which means you are a terrible choice of residence."

    show john a_31
    show cornelia a_4

    john "Man you're just brimming with humor."

    show john a_0
    show sayaka a_5

    cornelia "Okay, we get it. You hate each other. Now here."

    show kiyoshi a_1

    "She shoved a glass of water that she got just earlier when we bought food to the middle of the table."

    show cornelia a_5

    cornelia "I didn't drink anything yet. So try your drinking thing."
    "Both of us chugged a sip. Drinking from a glass of water is supposingly not a very difficult thing, but it was still awkward as all hell doing this."

    show sayaka a_16

    sayaka "This feels way too fucking intimate all of a sudden."

    show john a_17
    show cornelia a_14

    john "Ditto."

    show cornelia a_15

    cornelia "And you two want to try kissing each other when youthink {i}this{/i} is intimate?"

    show sayaka a_7
    show cornelia a_14

    sayaka "Oh shut up, bitch."

    show john a_5
    show cornelia a_5 at faceright
    show sayaka a_16

    john "Wait, so what did this actually accomplish? I am pretty sure we didn't drink from the same cup last sunday."

    show sayaka a_5
    show cornelia at faceleft

    sayaka "Maybe we accidentally drank from the same bottle or something a week earlier. Who knows. The only thing that matters is whether it works or not."

    show john a_0

    "Still, my hopes were not exactly sky high for this to work."
    john "I don't suppose this would take effect immediately, would it?"
    sayaka "I don't know. With luck we are back to ourselves when we wake up tomorrow."

    show sayaka at faceleft
    show kiyoshi a_2

    kiyoshi "Actually, the novel I read had the main characters swap immediately. I can only assume it was because of the DNA exchange of saliva entering the-"

    show kiyoshi a_0
    show sayaka a_16
    show cornelia a_8

    sayaka "And that's just about as much as I want to hear about that, thank you very much."

    show cornelia a_5
    show sayaka a_5 at faceright

    cornelia "Anything else you want to try now? I remembered something we need to talk about later, Saya."
    sayaka "What is it now?"

    show cornelia a_4

    cornelia "Well, you know, the party."

    show sayaka a_2

    sayaka "Party?"

    show john a_13

    john "The party?"

    show kiyoshi a_6

    kiyoshi "Aha! The party!"

    show kiyoshi a_7
    show cornelia a_6

    kiyoshi "What party?"

    show kiyoshi a_1
    show sayaka a_20

    sayaka "Oh shit! The party in two weeks!"

    show sayaka a_15
    show cornelia a_5

    cornelia "Yes, that one."
    sayaka "Fuck! We can't cancel that!"

    show john b_5

    john "Wait, party?"

    show sayaka a_16
    show john a_15

    sayaka "...Ugh, you're just going to have to deal with it."

    show john a_16
    show cornelia at faceright

    john "What party?!"

    show cornelia a_0
    show john a_17

    cornelia "Sayaka's monthly party."

    show john a_7

    john "You do parties each month?"

    show cornelia a_3
    show john a_30

    cornelia "Have you not noticed that Saya hosted parties every month last year?"

    show kiyoshi a_11
    show cornelia a_5 at faceleft
    show sayaka a_5 at faceleft

    kiyoshi "Ahh, yes. I've tried entering numerous times."

    show kiyoshi a_9

    kiyoshi "But somehow I never manage to get in."

    show cornelia a_6
    show sayaka a_16
    show john a_0

    sayaka "Because you aren't invited you knobhead."

    show sayaka a_5 at faceright
    show cornelia a_0 at faceright
    show kiyoshi a_0
    show john a_13

    john "Is this like... Some kind of {q}popular people{/q} party you got going on?"
    sayaka "Yes. Now you know why you don't know this exists."

    show john a_6

    john "Oof."

    show john a_0
    show sayaka a_19

    sayaka "You have to ask permission from mom and daddy to host it on Saturday two weeks from now."

    show john a_8

    john "Wait, wait, wait. I am not hosting any parties, lady."

    show sayaka a_5

    john "I've barely even been to any!"

    show sayaka a_16

    sayaka "I will arrange everything if we haven't swapped back by then. All you need to do is do what I tell you to do."

    show john a_17

    sayaka "If I don't host these parties, people will start thinking lowly of me."

    show cornelia a_5

    cornelia "Exactly."

    show john a_3
    show sayaka a_5

    john "Alright, alright. As long as I don't have to do anything."

    show john a_6

    sayaka "Good."

    show sayaka at faceleft
    show cornelia at faceleft
    show kiyoshi a_6

    kiyoshi "Could it be that the invitation I've been looking for for months might be showing itself to me now?"
    sayaka "No."

    show kiyoshi a_15

    kiyoshi "Worth a try. Hey John, you will help me sneak in, right?"

    show john a_6

    john "You're on your own here bud."

    show kiyoshi a_3

    kiyoshi "Tough blow, J-man."

    show john a_5

    john "You'll get used to it."

    show john a_0
    show sayaka at faceright
    show cornelia at faceright
    show kiyoshi a_0

    john "Anyways, you got anything else we need to do before we leave?"

    show sayaka a_8

    sayaka "Headbutting."

    show cornelia a_14 at faceleft
    show john a_26

    john "Headbutting? You think we could have swapped because we headbutted each other?"
    john "When have we ever headbutted each other?"

    show john a_6
    show sayaka a_16

    sayaka "Who cares. I'm going to headbutt you. Get ready, and make sure I don't hit something important!"

    show john a_32

    john "Ugh, fine."

    scene black with dissolve
    pause 1
    scene bg neighborhood2 day
    show john b_9:
        center
        faceright
        block:
            ease 0.9 yanchor 0.99
            ease 1.3 yanchor 1.00
            repeat
    show cornelia b_1 behind john:
        centerright
        faceright
        block:
            easein 0.8 yanchor 0.99
            easein 1.2 yanchor 1.00
            repeat
    with dissolve

    john "Agh, this still hurts!"

    show cornelia b_0
    show john b_8

    john "Why did she have to headbutt me like we're in a deathmatch? She still doesn't get how strong she can hit now that she has my physique at all!"

    show cornelia b_25
    show john b_11

    cornelia "I'm sure you deserved it."

    show john b_19
    show cornelia b_1

    john "As if! I've been putting up with her shittalk for way too long! If anyone deserves a headbutt, it's her."

    show john b_17
    show cornelia b_24

    cornelia "Yeah yeah, I get it, you're all bark and no bite."

    show john b_33

    john "You don't get fed up with her at all?"

    show john b_31
    show cornelia b_17

    cornelia "Unlike you, I'm able to see Saya for what she is. A good friend and a great leader."

    show cornelia b_6
    show john b_11

    cornelia "So when you're done whining about all your issues then maybe you could see just how fucked up this is for her."

    show cornelia b_24

    john "Oh come on, her life is far from perfect."

    show cornelia b_17

    cornelia "But she still remains positive and gets to call herself the queen of school."
    cornelia "Your life is probably all peachy peachy with a nice family and all, but we don't all have that, Mr. Perfect."

    show cornelia b_23

    cornelia "Don't just think she is respected and feared by people for no reason."

    show john b_13
    show cornelia b_5

    john "Well- Yeah, it's just..."

    show john b_22

    "Well she did have a point. Her parents basically didn't exist and her friends were for the most part all entirely artificial."

    show john b_5

    john "Even if she may have it hard here and there, she isn't the only one, you know."

    show cornelia b_24

    cornelia "You wouldn't understand what she has gone through anyways."

    show john b_1

    john "I guess I wouldn't. Either way, I don't want to spend the entire afternoon in another heated discussion. I've had enough of that lately."

    show cornelia b_0

    john "You were going to take me to the mall, right?"

    show cornelia b_1

    cornelia "Yup! They are currently selling some of the new Goopy skirts. We have to try some!"

    show john b_6

    john "...Goopy...?"

    show cornelia b_17
    show john b_27

    cornelia "You don't know Goopy?!"

    show cornelia b_23

    cornelia "They make some of the most fashionable clothes and handbags!"

    show john b_6

    cornelia "Jeez, are you living in the last year or something?"

    show cornelia b_5

    john "It would seem I still have much to learn about this world."

    scene black with Dissolve(1.5)
    $ screenfilter.blur = 0

    title "14th of August (Sunday)" "Day 7 - Sayaka"

    outfit sayaka casual
    scene bg main room day
    show sayaka a_5:
        centerleft
        faceleft
        ypos 1.1
    with dissolve
    pause 1
    show sayaka a_2

    sandra "{size=-5}Honey, Kiyoshi is here!{/size}"

    show sayaka a_0

    sayaka "Coming!"

    show sayaka a_5:
        ease 0.75 ypos 1.0

    "Yeah... So this is me in a situation I never thought I'd find myself in."
    "Kiyoshi - yes, that Kiyoshi - visiting my home for the time being."
    "He promised to read up more about possible swap methods me and John could do and practically invited himself over, saying {q}It's fine because he would {i}technically{/i} be visiting John{/q}."

    show sayaka a_24

    sayaka "{i}Sigh...{/i}"

    show sayaka a_2

    "Were it not for my current situation I never would have let that freak near me, yet here he is, being more reliable than crappy John."

    scene black with dissolve
    outfit kiyoshi casual
    scene bg main livingroom day
    show kiyoshi a_1 at centerright, faceright
    show sandra a_1 at right, faceright
    show sayaka a_8:
        offscreenleft
        faceright
        alpha 0.0
    with dissolve
    pause 0.25
    show sayaka:
        ease 1.0 centerleft alpha 1.0
    pause 0.75
    show kiyoshi at faceleft
    show sandra a_9
    pause 0.25

    kiyoshi "Aha! {i}John{/i}, how nice to see you."

    #SKIP
    show kiyoshi:
        centerright
        faceleft

    sayaka "Yeah yeah, whatever. Come with me."

    show kiyoshi a_2:
        ease 0.75 center

    kiyoshi "Naturally."

    show kiyoshi a_1 at faceright
    show sandra b_9 at faceleft

    sandra "Oh, John, before I forget, there will be some fruit salad later. Leona is coming over and we are making some."

    show sayaka a_0

    sayaka "Sure. Sounds delicious."

    show kiyoshi at faceleft
    show sayaka a_8

    sayaka "Now come on, we've got a lot to cover today."

    scene black with dissolve
    pause 0.5
    scene bg main room day
    show sayaka a_5:
        centerleft
        faceright
        ypos 1.1
    show kiyoshi a_15:
        centerright
        faceright
    with dissolve
    pause 0.5
    show kiyoshi a_14:
        pause 0.25
        faceleft
        pause 1.5
        faceright

    kiyoshi "I must say, you've made an effort to keep this room clean."

    show kiyoshi a_1 at faceleft

    sayaka "Of course I have. The day I woke up there was shit everywhere in here."

    show sayaka a_16

    sayaka "I can't live with that."

    show sayaka a_2

    sayaka "Anyways, let's not beat around the bush. You found anything interesting?"

    show kiyoshi a_6:
        ease 0.5 ypos 1.1

    kiyoshi "Ah yes. I can say that I am plenty proud of the info I've gathered yesterday."

    show kiyoshi a_0

    kiyoshi "I don't assume anything has happened since you gave John one of the most aggressive headbutts I've seen yet?"
    sayaka "Nothing."
    kiyoshi "Hm, that eliminates one of the three main tropes."

    show kiyoshi a_1

    kiyoshi "In... What do you call it nowadays... Modern literature-"

    show sayaka a_5
    show kiyoshi a_0

    sayaka "In manga, not modern literature."
    kiyoshi "Yes, as I said, in {i}modern literature{/i}, the big three swapping methods seem to be physical traumatic contact between two heads, kissing, and finally, lightning."

    show sayaka a_32

    sayaka "Lightning? I think I've heard about that. Two people struck by lightning and something happens, right?"

    show kiyoshi a_9
    show sayaka a_5

    kiyoshi "Exactly. Since it would seem kissing is out of the question for now..."

    show sayaka a_16
    show kiyoshi a_13

    sayaka "Of course it is! To begin with we never kissed each other anyways."

    show kiyoshi a_15

    kiyoshi "It never hurts to try, you know."
    sayaka "Absolutely fucking yes it does."

    show kiyoshi a_9

    kiyoshi "Ah well. I guess John's first kiss will have to wait then."

    show sayaka a_7

    sayaka "You're trying to make me kiss him so he can have me as his first kiss?"

    show sayaka a_16
    show kiyoshi a_8

    kiyoshi "I am a great wingman, aren't I?"
    sayaka "Ugh, fuck you."

    show kiyoshi a_1

    kiyoshi "Anyhow, I have lots of other things you can try before attempting to electrocute both of you at the same time."

    show sayaka a_5

    "..."
    "The guy had ideas, that was for sure."
    "Magic spells, falling down stairs, brain swap during surgery, body swap potions, voodoo puppets, taking a shower at the same time, speaking someone's name three times in a mirror..."
    "And all other kinds of insane shit he could come up with on the fly."
    "Whether those ideas were rational or not was another thing entirely."

    scene black with dissolve
    pause 1

    "But the main question we had to ask ourselves was still the same."
    "Is this a question of {q}Why did it happen{/q}, or is it a question of {q}Who did it{/q}."
    "It would be ideal if this happened by accident. If I could replicate it, then everything would go back to normal."
    "I would be able to build up my reputation again, to live life as a winner and be, well, me."
    "On the other hand, if this was caused by someone and I couldn't replicate it myself..."
    "I would be at the mercy of whoever tries to destroy my life."

    scene bg main room day
    show sayaka a_5:
        centerleft
        faceright
        ypos 1.1
    show kiyoshi a_0:
        centerright
        faceleft
        ypos 1.1
    with dissolve

    kiyoshi "Now, with all the quibble out of the way, let me give you my final thoughts on what truly happened between you and John."

    show sayaka a_15

    sayaka "You got even more?"
    kiyoshi "Of course. And I think you will find this to be the most probable cause."

    show sayaka a_5
    pause 1

    kiyoshi "Aliens."

    pause 1
    show sayaka a_33

    sayaka "...Aliens?"

    pause 1

    kiyoshi "Aliens."

    show sayaka a_7

    sayaka "Why the fuck would aliens swap me and that nerd?"

    show sayaka a_16
    show kiyoshi a_7

    kiyoshi "You see, I've long been gathering evidence on alien life. I believe you two were chosen as an alien experiment to swap the souls of two humans."

    show kiyoshi a_17
    show sayaka a_5

    kiyoshi "Or maybe..."

    show kiyoshi a_6

    kiyoshi "Or maybe it was an accident when the aliens altered the reality on earth!"
    kiyoshi "That's it!"

    show sayaka a_33

    sayaka "..."

    show sayaka a_16
    show kiyoshi a_1

    sayaka "How does that help me swap back?"

    show kiyoshi a_0

    kiyoshi "It... Uh, doesn't. However, if we could make contact with these aliens, perhaps we could make a deal with them."

    show sayaka a_5
    show kiyoshi a_1

    kiyoshi "What do you say we go make some crop circles?"

    show sayaka a_16

    sayaka "I am not making crop circles with you, Kiyoshi."

    play sound sfx_knock
    show sayaka a_5 at faceleft
    show kiyoshi a_0

    "Just as this discussion ended, Ms. Davis knocked on the door."
    sandra "The salad is ready, boys."

    show sayaka a_12

    sayaka "Thanks!"

    show kiyoshi a_1
    show sayaka a_0 at faceright

    sayaka "I'm hungry. Let's put this off for now."

    show kiyoshi a_2
    show sayaka a_5

    kiyoshi "It has been a while since I have had something from Ms. Davis."

    show sayaka a_10:
        ease 0.75 ypos 1.0
    show kiyoshi a_1:
        pause 1.5
        ease 1 ypos 1.0

    sayaka "She makes really good food, trust me."

    show sayaka a_15

    think "...Wait."
    think "I'm not getting along with him, am I?"

    play sound sfx_door_open
    show sayaka a_21:
        faceleft
        ease 1 xpos 0.0 alpha 0.0
    show kiyoshi:
        pause 0.5
        ease 1 xpos 0.4 alpha 0.0

    "I shuddered from the thought and left to eat something."

    scene black with dissolve
    pause 0.5
    outfit leona casual_b
    scene bg main livingroom day
    show leona a_1:
        centerright
        faceright
        xpos 0.6
        ypos 1.15
    show sandra a_1:
        centerright
        faceright
        xpos 0.8
        ypos 1.15
    show sayaka a_0:
        alpha 0.0
        center
        faceright
        xpos 0.2
    show kiyoshi a_1:
        alpha 0.0
        center
        faceright
        xpos 0.0
    with dissolve
    pause 0.5
    show sayaka:
        ease 0.5 alpha 1.0 xpos 0.3
    show kiyoshi:
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.1
    pause 0.5
    show sandra a_0
    pause 0.25
    show leona at faceleft

    sayaka "Hello Ms. Winters."

    #SKIP
    show sayaka:
        alpha 1.0
        xpos 0.3
    show kiyoshi:
        alpha 1.0
        xpos 0.1

    show leona a_4

    leona "Good afternoon you two."

    show leona a_1

    leona "Help yourselves to some."
    "She pointed to two extra bowls they had laid out for us."

    show sayaka a_6

    "Ms. Winters was one of the teachers I respected the most, if I had to mention one in particular."
    "She didn't do all kinds of bullshit in her classes like some others would and did her job."
    "For that, she would definitely be my pick as my favorite teacher."
    "To think that she was close enough to Ms. Davis on a personal level to hang out with her though..."

    show sayaka a_0
    show kiyoshi a_2 behind sayaka:
        ease 0.75 xpos 0.45

    kiyoshi "Don't mind if I do."
    sayaka "We'll take it back to my room."

    show sandra b_1 at faceleft

    sandra "Aw, but we were hoping to talk lots and lots about school and grades with you."

    show sayaka a_15
    show sandra b_9

    sayaka "Wait, really?!"

    show sayaka a_5
    show leona a_4
    show sandra b_0

    leona "She's messing with you. Go enjoy it if you don't want to hang out with the old ladies."

    show kiyoshi a_6
    show leona a_1
    show sandra b_9

    kiyoshi "To be honest, I would not be against staying here with you two ladi-"

    show sayaka a_16:
        ease 0.25 xpos 0.325
        pause 0.25
        faceleft
        pause 0.25
        ease 0.5 xpos 0.225
        pause 0.25
        ease 0.5 xpos 0.125
        pause 0.25
        ease 0.5 xpos 0.025
    show kiyoshi a_5:
        transform_anchor True
        pause 0.5
        ease 0.25 rotate -5 ypos 1.03
        ease 0.5 xpos 0.35
        pause 0.25
        ease 0.5 xpos 0.25
        pause 0.25
        ease 0.5 xpos 0.15
    show leona a_6
    show sandra b_5

    sayaka "Don't you dare start with this again. We're going back to my room."

    show sayaka a_5 at faceright
    show kiyoshi a_6 at faceright

    kiyoshi "Ah, I see. Well, anyone would be jealous if the Kiymaster chose someone else to talk with. May it be another day!"

    show sayaka a_16:
        faceleft
        ease 1 xpos -0.05 alpha 0.0
    show kiyoshi:
        ease 1 xpos 0.05 alpha 0.0
    show leona a_7
    show sandra b_8

    sayaka "Oh just shut it, you."

    leona "Uh, yeah. See you later."

    show sandra b_1

    sandra "{size=-10}You think he still has a crush on you?{/size}"

    show sandra b_0
    show leona b_8 at faceright

    leona "S- S- Sandra! Don't say that!"

    scene black with dissolve
    pause 0.25
    scene bg main room day
    show sayaka a_24:
        faceright
        centerleft
        alpha 0.0
    show kiyoshi a_4:
        faceright
        left
        alpha 0.0
    with dissolve
    play sound sfx_door_open
    show sayaka:
        ease 0.75 centerright alpha 1.0
    show kiyoshi:
        pause 0.5
        ease 0.5 centerleft alpha 1.0

    sayaka "For god's sake..."

    show sayaka a_16 at faceleft
    show kiyoshi a_0

    sayaka "You know, you could actually be tolerable to talk to..."

    show kiyoshi a_1

    kiyoshi "Hm? Have I perhaps broken through to you?"

    show kiyoshi a_4

    sayaka "If, you would stop doing this pathetic excuse of an attempt at flirting and frankly creepy shit you're doing, that is."

    show kiyoshi a_3

    "God, this guy. Now he looked confused at me."
    kiyoshi "Uhm, what are you talking about?"

    show sayaka a_7
    show kiyoshi a_16

    sayaka "You!"
    sayaka "I never imagined even once that I would have this conversation with you!"

    show kiyoshi a_5

    sayaka "But apparently it's needed for you to face fucking facts. You're disgusting, you know?"

    show kiyoshi a_11
    show sayaka a_16

    kiyoshi "Aha, don't say it like tha-"

    show sayaka a_7
    show kiyoshi a_0

    sayaka "I am fucking serious!"
    sayaka "All you do is jump from one girl to the next like a perverted dog in heat!"

    show kiyoshi a_4

    sayaka "I think I've slapped you and pepper sprayed you at least 50 times now and you still don't get it!"
    sayaka "Girls don't like it when you're trying your mating rituals! Why don't you get it?!"

    show sayaka a_16

    kiyoshi "..."

    show kiyoshi a_0

    kiyoshi "I would not per se say that I made any moves on any of the ladies downstairs though."

    show sayaka a_7

    sayaka "That's totally besides the point!"
    sayaka "How many times do you need to have an anchor smacked across your face before you finally take the hint?"

    show sayaka a_25
    show kiyoshi a_5

    sayaka "Nobody wants to be {q}flirted{/q} at by some dipshit!"

    show sayaka a_16

    kiyoshi "..."
    "Finally, it seems he takes offense to me."

    show kiyoshi a_4
    show sayaka a_2

    sayaka "{i}Sigh...{/i} Look..."
    sayaka "I am not going to lie. I am not against being friends with you. You seem reliable and trustworthy, unlike many other people."

    show sayaka a_5

    sayaka "But the moment you start thinking with your dick you become such a massive turn-off."

    show sayaka a_2

    sayaka "Get it?"

    show kiyoshi a_3

    kiyoshi "...Kind of?"
    kiyoshi "You are not mad at me then?"

    show sayaka a_16
    show kiyoshi a_0

    sayaka "I am angry as fuck at you right now. But it's not the {q}Fuck you{/q} kind of angry, it's the dissapointment kind of."

    show sayaka a_5

    sayaka "But... Look. You're helping me by spending your time. I can't pay you back in money, but what if I gave you some actual tips on how to get into a girl's pants?"

    show kiyoshi a_5

    sayaka "Not only would it help you, but also all the girls who have to listen to your constant barking."

    show kiyoshi a_14

    kiyoshi "You'd do that?"

    show sayaka a_3

    sayaka "I am the master matchmaker in this school for a reason after all."
    sayaka "Even finding some random nerd for you should be a breeze."

    show sayaka a_17
    show kiyoshi a_8

    kiyoshi "That would be a gift I would never be able to refuse."

    show kiyoshi a_11
    show sayaka a_5

    kiyoshi "I would need to give you my extensive list of research that has helped me create {q}Kiyoshi's Womanly Exam{/q} then!"

    show kiyoshi a_1
    show sayaka a_16

    sayaka "What the hell is that?"

    show kiyoshi a_2

    kiyoshi "Ah, you see: This is a kind of qualification process in which I examine the bodily structure and personal integr-"

    show sayaka a_20

    sayaka "{i}Not listening!{/i}"

    scene black with dissolve
    pause 0.5
    scene bg main house dusk
    show kiyoshi a_2 at right, faceleft
    show sayaka a_0 at centerleft, faceright
    show sandra b_0 at left, faceright
    with dissolve
    pause 0.75
    show kiyoshi a_1:
        faceright
        ease 0.75 alpha 0.0 offscreenright
    pause 0.5
    scene black with dissolve
    play sound sfx_door_open
    scene bg main entrance day
    show sandra b_9:
        alpha 0.0
        offscreenleft
        faceright
    show sayaka a_0 behind sandra:
        alpha 0.0
        left
        faceright
    with dissolve
    pause 0.25
    show sandra:
        pause 0.25
        ease 1.0 alpha 1.0 centerleft
    show sayaka:
        ease 0.75 alpha 1.0 center
    pause 0.85
    play sound sfx_door_close

    sandra "He looked happier than usual."

    #SKIP
    show sayaka:
        alpha 1.0
        center
    show sandra:
        alpha 1.0
        centerleft

    show sayaka a_2 at faceleft

    sayaka "Kiyoshi?"

    show sayaka a_5

    sayaka "I just promised him something."

    show sandra a_1 at faceleft

    sandra "Oh? And what would that be?"

    show sayaka a_6
    show sandra a_0

    sayaka "It's not something I'm planning on telling you."

    show sandra a_2

    sandra "Ah darn. For a moment I thought it was because you gave him your console."

    show sayaka a_5

    sandra "I didn't think I'd see the day where you of all people would give it away for free."

    show sayaka a_2

    sayaka "He just... Asked for it."
    "He did. But it wasn't specifically him who wanted that video game thing."
    "Apparently John had nothing to do all day, so rather than him doing weird shit in my body, I'd let him play on that thing instead. He did ask Kiyoshi to bring it to him now that he was here anyways."

    show sayaka a_5

    "I did make it perfectly clear that absolutely {i}nobody{/i}, especially my parents, should ever find out about it."
    "And it wasn't like I'd ever use it myself, so while we were swapped, he could have that piece of junk."

    show sandra a_4

    sandra "I know I've asked this at least ten times this week but are you sure you're alright John?"
    sandra "It's just so unlike you to suddenly go to bed early and study."

    show sandra b_3 at faceright

    sandra "Not that I'm complaining."

    show sayaka a_6

    sayaka "It's fine. It's just for a week or two, I hope."

    show sandra b_4

    sandra "You hope?"

    show sandra b_5

    sandra "Is this one of those challenges I've read about on the internet?"

    show sayaka a_10

    sayaka "Wha- No no, none of that. I just... felt like it..."

    show sayaka a_0
    show sandra b_3

    sandra "..."

    show sandra b_9

    sandra "In that case, if you don't want to play games, do you want to watch a movie after dinner?"

    show sayaka a_5

    sayaka "A movie?"
    "Now she's piqued my interest."

    show sayaka a_0

    sayaka "What kind of movie?"

    show sandra b_0

    sandra "Anything you'd like."

    show sayaka a_5
    show sandra b_9

    think "Huh... Well, if John gets to act however he wants in front of the people I know, I'm sure I should be allowed to watch some crappy teen movie."

    show sayaka a_12

    sayaka "I'd love to. And if there is still some of your fruit salad left, we totally should have some while watching. That stuff was just delish."

    show sandra b_1

    sandra "Now that's a promise."

    scene black with dissolve
    pause 1

    title "15th of August (Monday)" "Day 8 - Sayaka"

    outfit sayaka uniform_c
    show bg school entrance day:
        zoom 2.0 xalign 0.2 yalign 0.8
    show carrie a_0:
        left
        faceright
        pause 0.5
        block:
            ease 1.2 ypos 1.02
            ease 1.0 ypos 1.0
            repeat
    show sayaka a_5:
        centerleft
        faceright
        pause 0.5
        block:
            ease 1.3 ypos 1.02
            ease 1.1 ypos 1.0
            repeat
    with dissolve

    carrie "It is nice weather today, isn't it?"

    show sayaka a_32

    sayaka "Uh, sure."

    show carrie a_15

    carrie "..."

    show sayaka a_16
    show bg school entrance day:
        ease 5 xalign 0.3

    think "Ugh, it'd be best if that psycho would just do as she is told instead of trying to talk."
    "It's not like she wasn't useful though, she carried my stuff around and somehow managed to be around to carry my stuff home as well at the end of the day."

    show sayaka a_5

    think "Which makes you think about what she even does the entire day."

    show cornelia b_8:
        alpha 0.0
        faceleft
        right

    think "Not that I care."

    show carrie a_2:
        ease 0.5 ypos 1.0
    show sayaka:
        faceleft
        ease 0.5 ypos 1.0

    sayaka "Alright, my stuff."

    show carrie a_15

    carrie "Here you go."

    "It wasn't {i}that{/i} heavy of a backpack that I had to carry around, but if I had the service available, I wouldn't let it go to waste."

    show cornelia:
        ease 0.75 alpha 1.0 centerright
    show bg school entrance day:
        ease 0.5 xalign 0.3

    cornelia "{size=-5}Saya!{/size}"

    #SKIP:
    show cornelia:
        alpha 1.0
        centerright

    show sayaka a_2 at faceright
    show carrie a_2

    carrie "..!"
    "I saw Cornelia running towards me, and behind her was John who..."

    show cornelia b_21
    show sayaka a_21

    outfit john uniform_pony_pants
    accessory john set glasses
    show john b_15:
        alpha 0.0
        offscreenright
        faceleft

    cornelia "Saya, please don't get angry now! I told him this would ruin your reputation but he insisted that it wasn't a big deal, and-"

    show sayaka a_7

    sayaka "...What the fuck is he wearing?!"

    show bg school entrance day:
        ease 0.75 xalign 0.8
    show carrie:
        ease 0.75 offscreenleft alpha 0.0
    show sayaka:
        ease 0.75 xpos 0.2 alpha 0.0
    show cornelia a_8:
        ease 0.75 xpos 0.4 alpha 0.0
    show john:
        pause 0.25
        ease 0.5 centerright alpha 1.0

    "Not like I couldn't tell it by myself though."

    #SKIP:
    show john:
        centerright
        alpha 1.0
    hide sayaka
    hide cornelia
    hide carrie

    "He had completely dropped my skirt and went to school in fucking jeans!"
    "Who does that?!"

    show sayaka a_7:
        centerleft
        faceright
        alpha 0.0

    "And he was using glasses too!"

    show sayaka:
        ease 0.5 center alpha 1.0
    show john b_0

    sayaka "You prick!"

    show john b_2
    show sayaka a_16:
        alpha 1.0
        center

    john "Why hello there."

    show john b_10

    john "Do you at least want to hear me explain why I'm using jea-"

    show john b_27
    show sayaka a_20

    sayaka "I won't let you explain shit! You're going to go home {i}right now{/i} and change back to what I always wear!"

    show john a_17
    show sayaka a_21

    john "Dude, people can hear us talking."

    show sayaka at faceleft
    show cornelia b_14 behind sayaka:
        left
        faceright
        alpha 0.0
    show carrie a_13 behind cornelia:
        offscreenleft
        faceright
        alpha 0.0

    "Luckily I was able to grasp myself before becoming completely angry. We were in front of the school, of course there would be people watching."

    show sayaka at faceright
    show carrie:
        ease 0.75 alpha 1.0 left
    show cornelia:
        ease 0.5 centerleft alpha 1.0

    "But it's not like that fucking matters now anyways! What are people going to think when they see a supposed beauty queen looking like a geek from some pervy magazine?"

    show john a_13

    john "Look, I {i}really{/i} hate wearing skirts, and since it seems we're going to be stuck for a long while, I thought-"

    show john a_0
    show sayaka a_7

    sayaka "Thought what?!"

    show sayaka a_16
    show john a_32
    show carrie a_10

    "He paused a moment in shock and promptly gave me {i}those{/i} eyes that this prick always gives me, as if he thinks he is above me."

    show john a_5

    john "I thought that I'd like to feel just a bit comfortable. No offense, but your life is boring to me and your clothing sucks to wear."

    show sayaka a_7

    sayaka "Are you even trying to figure out how to swap back?!"

    show sayaka a_16
    show john b_18

    john "How am I supposed to?! I don't have access to the most basic human right nowadays which is internet because your chummy ass refuses to let me access your computer or phone!"

    show sayaka a_7
    show john b_17
    show cornelia a_8 at faceleft

    sayaka "Because you'd abuse the hell out of access to those things!"

    show cornelia b_8 at faceright
    show sayaka a_16

    cornelia "...G- Guys, calm down-"

    show john b_19

    john "But you wouldn't abuse access to {b}my{/b} phone by digging through it to find all kinds of dirt on it?! I bet you've already browsed through every single conversation I've had with my friends on there!"

    show john b_17
    show sayaka a_20
    show cornelia b_26 at faceleft

    sayaka "How fucking dare you accuse me of anything!"

    show john a_3
    show sayaka a_21

    john "Oh I dare to accuse you very much you communist bitch!"

    show john a_26
    show carrie a_13
    show cornelia at faceright

    john "Also, what the fuck is Carrie doing here?!"
    carrie "Huh?"

    show cornelia b_3 with hpunch
    show sayaka a_15 at faceleft
    show john a_30

    cornelia "{i}{b}{size=+5}GUYS!{/size}{/b}{/i}"

    show sayaka a_7
    show john a_3
    show cornelia b_26

    both "What?!"

    show sayaka a_16
    show john a_17
    show cornelia a_8

    cornelia "{b}Everyone{/b} is staring at us!"

    show john a_5:
        pause 0.5
        faceright
        pause 1.0 faceleft
    show sayaka a_5:
        pause 1.0
        faceright

    "We both looked around, and sure enough, an absolutely massive crowd had formed around us."

    show sayaka at faceleft

    "Almost similar to the kinds of crowds that gather in a ring around a fist-fight in a school in one of those teen movies."

    show john a_4
    show sayaka at faceright

    john "Uh..."

    show cornelia a_5

    john "Okay, I'll admit, I'm sorry, but I'm not going back home to change now."

    show sayaka a_16
    show john a_5

    sayaka "Yes, you are."

    show john b_19
    show cornelia a_11

    john "Seriously, who are you to decide after just randomly dying my hair pink."

    show sayaka a_7
    show john b_17

    sayaka "You deserved it!"

    show cornelia b_17
    show sayaka a_16

    cornelia "Oh my fucking-"

    show cornelia b_3

    cornelia "Both of you, come with me, right now!"

    show cornelia b_18:
        ease 2 xpos 1.2
    show sayaka a_15:
        transform_anchor True
        faceleft
        pause 0.75
        ease 0.25 rotate 5
        ease 1.5 xpos 1.2
    show john b_27
    pause 1
    show john b_28:
        transform_anchor True
        ease 0.25 rotate 5
        ease 1 xpos 1.2

    "Corny grabbed both our sleeves and had a look on her face that was a mix between anger and embarrassment."

    show carrie a_16

    sayaka "Carrie, go home, I have shit to do!"

    scene black with dissolve
    pause 0.5
    scene bg school garden day
    show john b_6:
        offscreenleft
        xpos -0.35
        faceleft
        transform_anchor True
        rotate 5
    show sayaka a_7:
        offscreenleft
        xpos -0.37
        faceleft
        transform_anchor True
        rotate 5
    show cornelia b_24:
        offscreenleft
        faceright
    with dissolve
    pause 0.25
    show john:
        ease 1.5 centerright
        faceleft
        ease 0.25 rotate 0 ypos 1.0
    show sayaka:
        pause 0.75
        ease 0.6 centerleft
        ease 0.25 rotate 0 ypos 1.0
        faceright
    show cornelia:
        pause 0.25
        ease 1.0 center
    pause 1

    "Corny dragged us away from the crowd, coincidentally to where I dragged John the first few times."

    #SKIP
    show john b_4:
        centerright
        rotate 0
        faceleft
    show sayaka a_16:
        centerleft
        rotate 0
        faceright
    show cornelia a_14:
        center
        faceleft

    "When there was nobody else in sight, she released her grip from our clothes and stood in place for a few seconds."

    show cornelia a_3

    cornelia "What are you two doing?!"

    show john b_7
    show cornelia a_14
    show sayaka a_5

    john "Wha-"

    show cornelia a_5

    cornelia "You are both making us look like complete idiots!"

    show sayaka a_7
    show john b_0

    sayaka "I am making us look like idiots?! Look at this dickhead who is making me look like one alre-"

    show cornelia b_3
    show sayaka a_15
    show john b_11

    cornelia "Don't you think I've told him how absolutely stupid he is already for doing this?!"
    cornelia "Do you really think telling him to go fuck himself is going to change anything?!"

    show cornelia b_14
    show sayaka a_4
    show john b_15

    sayaka "Wh- Why are you talking back to me?!"

    show sayaka a_15

    "This guy was just grinning because Corny of all fucking people dared to talk to me like a superior or something."

    show sayaka a_21

    think "I swear, when we swap back..."

    show sayaka a_16
    show cornelia a_4 at faceright
    show john b_13

    cornelia "Can you guys just, for once, not argue in front of each other?"

    show sayaka a_7
    show cornelia b_5 at faceleft

    sayaka "How am I supposed to-"

    show sayaka a_15
    show cornelia b_3

    cornelia "Hey!"

    show cornelia b_17

    cornelia "Don't say another word!"

    show cornelia b_14
    show sayaka a_21
    show john b_11

    sayaka "You- But- "

    show sayaka a_20 at faceleft
    show john b_2

    sayaka "{b}{i}ARGH!{/i}{/b}"

    show sayaka a_24
    show cornelia at faceright

    think "Fuck!"

    show cornelia b_17
    show john b_11
    show sayaka a_16

    think "I know she's right, keeping up this bullshit is only going to make me look like an equal to that idiot."

    show john b_21
    show cornelia b_14
    show sayaka at faceright

    "He himself looked content being able to get away without anything happening though..."

    show cornelia a_5 at faceleft
    show john b_25

    think "I need my payback on this, and I'm so going to get it soon, just you wait."
    cornelia "Are we fine?"
    sayaka "Urgh, yes! Fine! Do whatever you want!"

    show john a_24
    show cornelia at faceright

    john "I was fine from the beginning."

    show sayaka a_7
    show cornelia at faceleft

    sayaka "You-"

    show sayaka a_16
    show cornelia b_23
    show john a_31

    cornelia "Good! Then we're all going to our classes. Alright?"

    show john a_13
    show sayaka a_5
    show cornelia b_24

    sayaka "...Alright, fine."

    show john a_11

    john "Sure."

    show john a_10

    "I felt a bit calmer now, maybe Corny talking back turned out to be the best for me."
    "Before leaving, I got a glimpse of his face. He smiled, clearly enjoying seeing me beaten."

    show sayaka:
        faceleft
        ease 3 xpos -0.2
    show john a_13

    "I knew that this was his own pathetic way of getting payback at me for using that stupid dye on his hair. I need to figure out some way to get at him that would hit him good."

    show john a_1
    show cornelia a_11 at faceright

    john "See you at lunch then...?"

    show cornelia at faceleft

    sayaka "{size=-5}Whatever.{/size}"

    show cornelia a_19

    cornelia "...Sigh..."

    scene black with dissolve
    pause 1

    title "16th of August (Tuesday)" "Day 9 - Sayaka"

    outfit kiyoshi uniform
    pause 1
    scene bg lunch
    show sayaka a_5:
        center
        faceright
        ypos 1.1
    show cornelia a_0:
        centerright
        faceleft
        ypos 1.1
    show kiyoshi a_17:
        centerleft
        faceright
        ypos 1.1
    with dissolve

    sayaka "So, any ideas?"

    show cornelia a_4

    cornelia "Really, do you think it's a good idea to do anything...?"

    show cornelia a_5

    cornelia "I mean, it would just end up becoming a loop of both of you wanting payback..."

    show sayaka a_16

    sayaka "No, I need it. I cannot live knowing that that moron is able to pose around as me with those clothes."
    cornelia "I guess as long as we keep an eye on him to make sure he doesn't do something stupid..."

    show sayaka a_5

    "Normally, I would consult everyone at my former table to figure out some way to really put someone back into their place somehow."
    "If people annoyed me to no end, they would end up facing me and my group unless they kissed my feet."

    show sayaka a_16

    "But things were different now. John was wearing my face and the only help I had was Corny."

    show sayaka a_5 at faceleft

    "And, well, Kiyoshi, who was currently somehow reading something on his phone while also eating lunch."

    show cornelia a_12
    show sayaka a_2

    cornelia "Well, got anything in mind?"

    show sayaka a_5 at faceright
    show cornelia a_1

    sayaka "I need something that degrades him even further than where he already is."
    sayaka "Something that he wouldn't notice so that he doesn't get the idea to do the same thing to me."

    show sayaka a_2

    sayaka "I don't know. I already fucked up his friendship with Katrina and Kyoko. Those are pretty much the only girls he talks with, so..."

    show cornelia a_11

    cornelia "Girls?"

    show cornelia a_0
    show sayaka a_3

    sayaka "Wouldn't it be hilarious to see his chances of ever getting another girlfriend smother away? Heh, that's a good thought."

    show cornelia a_7
    show sayaka a_5

    cornelia "You want to neuter yourself...? While in his body?"

    show sayaka a_20
    show cornelia a_20

    sayaka "What?! No!"

    show sayaka a_16

    sayaka "Don't joke about that, I'm not... Doing that!"

    show cornelia a_0
    show sayaka a_5

    "I took a bite out of my sandwich and thought about hard it."
    sayaka "I don't know, I don't typically ruin my reputation with girls as a guy."

    show cornelia a_12

    cornelia "Ah, so that's what you want to do."

    show cornelia a_22

    cornelia "Uh... Maybe you could wear some weird clothes too...?"

    show cornelia a_0
    show sayaka a_32

    sayaka "Nah, that's too obvious. I need the reputation gone, not just something that might attract someone else."
    sayaka "Hmm... If there was something I could get inspiration from, this would be much easier."

    show sayaka a_2

    sayaka "Do we even have examples of someone in this school who all girls just, like, hate?"

    show cornelia a_4

    cornelia "Hmm..."
    "..."

    show sayaka a_15 at faceleft
    show cornelia b_11

    "...!"
    "As if having the exact same thought, we both looked at the guy sitting at our table peacefully reading."

    show sayaka a_14 at faceright
    show cornelia b_29

    "Both of us pointed at him in silence and then turned to each other."
    sayaka "Oh!"

    show cornelia b_10

    cornelia "We have the greatest weapon right here!"

    show sayaka a_3 at faceleft
    show cornelia b_22
    show kiyoshi a_16

    "He noticed us both staring at him after a while and looked at us with a confused look."

    show kiyoshi a_5

    kiyoshi "...Huh?"

    show kiyoshi a_4

    sayaka "You!"

    show kiyoshi a_5

    kiyoshi "...Me?"

    show sayaka a_17
    show kiyoshi a_9

    sayaka "Tell us how you act around girls!"
    kiyoshi "Wh-"
    "He looked as if he had just seen a ghost or something."

    show kiyoshi a_3

    kiyoshi "Act around girls? Could it perhaps be that you want to entrap the heart of a woman just like I do?"

    show sayaka a_2
    show cornelia b_24
    show kiyoshi a_0

    sayaka "Uh... Yeah, whatever you just said."

    show kiyoshi a_5
    show sayaka a_5

    kiyoshi "Oh no. Could it be that you truly are lesbian?"

    show sayaka a_7
    show cornelia b_0

    sayaka "Wha- No! I just need to give John some payback by having all girls see him like they see you, you kno-"

    show sayaka a_15 at faceright
    show cornelia b_17
    show kiyoshi a_4

    cornelia "Hey, don't tell him the plan! He sides with John after all!"

    show sayaka a_2 at faceleft
    show cornelia b_14
    show kiyoshi a_6

    kiyoshi "Ah, you want to pay back John's misdoings against you by making him a favor? How wholehearted of you."

    show sayaka a_33
    show cornelia b_6

    "..."
    sayaka "...Yeah, that."

    show kiyoshi a_12

    kiyoshi "Could this perhaps be a part of my training then?"

    show sayaka a_2
    show cornelia b_24

    think "His training...?"

    show sayaka a_32

    think "Oh yeah, I did promise him to {i}flirt better{/i} or something..."

    show sayaka a_6

    sayaka "Uh, yes, I want to try out how you approach girls first, you know."

    show cornelia b_23
    show sayaka a_2 at faceright
    show kiyoshi a_0

    cornelia "What is this {q}training{/q} I just heard about?"

    show kiyoshi a_14
    show sayaka a_5 at faceleft
    show cornelia b_31

    kiyoshi "My dear Sayaka has promised me to learn how to approach girls properly, as it seems my previous attempts have been fruitless."

    show kiyoshi a_1
    show cornelia b_27
    show sayaka at faceright

    cornelia "Pfft, really?"

    show cornelia a_2

    cornelia "You're gonna teach him how to talk with girls?"

    show sayaka a_16
    show kiyoshi a_2

    "Man, this bitch was giggling to herself because of that stupid promise."
    "She sure had a mind of her own now that she was spending time with John, huh?"

    show cornelia a_12
    show sayaka a_5
    show kiyoshi a_4

    cornelia "But honestly, you must have done something crazy to him. I know you're a guy for the time being, but he is like, not even paying attention to me."

    show cornelia a_10

    cornelia "Kind of like a tamed animal if you ask me, haha."

    show sayaka a_32 at faceleft
    show cornelia a_2

    think "Huh, she is actually kind of right."
    think "Normally he'd be all over any girl he sees."

    show cornelia a_1
    show kiyoshi a_3

    kiyoshi "What do you mean?"

    show kiyoshi a_4
    show sayaka a_5

    sayaka "She means that it's weird that you're not trying to get into her pants."

    show cornelia a_3

    cornelia "H- Hey! Don't even try to make me imagine that picture in my head!"

    show cornelia a_5
    show kiyoshi a_3

    kiyoshi "Why would I want to go out with Cornelia?"

    show sayaka a_2
    show cornelia a_11
    show kiyoshi a_4

    "..."

    show cornelia b_8

    cornelia "...What?"

    show cornelia b_11

    think "He just said something weird."

    show kiyoshi a_11

    kiyoshi "I mean, you aren't exactly girlfriend material."

    show kiyoshi a_1

    cornelia "..."

    show cornelia b_3

    cornelia "...WHAT?!"

    show sayaka a_10
    show kiyoshi a_0

    sayaka "Pffftt..."

    show cornelia b_18

    sayaka "Aa~~~~ahahahaha..."

    show sayaka a_13

    sayaka "Oh my god, for real?"

    show cornelia b_32

    cornelia "Hey! Don't laugh at that!"

    show cornelia b_28

    cornelia "And what do you mean I'm not {q}girlfriend material{/q}?!"

    show kiyoshi a_14
    show cornelia b_32

    kiyoshi "According to {q}Kiyoshi's Womanly Exam{/q}, Cornelia lacks the following."
    kiyoshi "Strike one: She is unusually flat."

    show cornelia b_29
    show sayaka a_14

    kiyoshi "Strike two: Her personality is quite shallow and from observations, not very feminine."

    show cornelia b_3

    cornelia "Wh- Wai-"

    show cornelia b_8

    kiyoshi "Strike three: Too short. Although it is important that the height does not exceed the Kiyoshi, the girl must be at least able to see above high quality kitchen counters."

    show sayaka a_13 at faceright

    "Corny had a face of absolute terror on her. There was no stopping this, the number one perv of the school was saying that she, of all people, wasn't good enough for him."

    show kiyoshi a_7
    show cornelia b_29
    show sayaka a_6 at faceleft

    kiyoshi "Strike four: The examinee is not in the least attracti-"

    show cornelia b_28
    show sayaka a_14
    show kiyoshi a_4

    cornelia "{b}STOP! OH MY GOD, STOP!{/b}"

    show kiyoshi a_5
    show cornelia b_29

    kiyoshi "Huh? What's wrong?"

    show cornelia a_3
    show sayaka a_1
    show kiyoshi a_4

    cornelia "What's wrong?! Are you kidding me?! You've been hitting on me {i}EVERY TIME{/i} I see you, and now you're telling me I'm ugly!"

    show sayaka a_13
    show cornelia b_18

    sayaka "-ahahah, yeah, that's kinda true, actually..."

    show kiyoshi a_3

    kiyoshi "Of course I would, you were with the lovely Sayaka after all."

    show cornelia a_8
    show sayaka a_2
    show kiyoshi a_4

    cornelia "...Wait, so you're saying that every time you were hitting on us, you were only hitting on Saya?"

    show kiyoshi a_9
    show sayaka a_6

    kiyoshi "Of course. Wasn't that clear?"

    show cornelia a_20

    cornelia "What?!"

    show sayaka a_13
    show cornelia b_8

    sayaka "Pfffft-"

    "This was so hilarious, so much that I slammed the table with my hand in sheer laughter."

    show kiyoshi a_0
    show cornelia b_3

    cornelia "I absolutely {i}refuse{/i} to accept that you, of all people, are telling me that!"

    show cornelia b_28

    cornelia "You don't realize there is a charm to smaller girls?!"

    show cornelia b_29
    show kiyoshi a_17

    kiyoshi "Charm? There is no charm about that. There needs to be something else, and I do not see that in you."

    show cornelia a_8
    show sayaka a_14

    cornelia "Wha- Why- You..."

    show sayaka a_10

    sayaka "-ahahah, this is killing me..."

    show kiyoshi a_4
    show cornelia b_8

    cornelia "He- Hey, stop l- Laughing!"

    show sayaka a_13

    "Kiyoshi's confused look just made this so much better, but knowing that lunchtime wouldn't last forever, I finally managed to get a grip on myself again."

    show sayaka a_1

    think "Although this probably is one of the funniest things I could ever think of."

    show sayaka a_13

    sayaka "Oh- Okay, but really, tell us what it is you do whenever you try to talk with girls."

    scene black with dissolve

    title "17th of August (Wednesday)" "Day 10 - Sayaka"

    pause 1
    show AN_asset grain
    show sayaka a_5:
        center
        faceleft
        xpos 0.65
    show kiyoshi a_6:
        center
        faceright
        xpos 0.35
    with dissolve

    kiyoshi "{i}So, first of all, you must find your target. Ideally, try to approach her in seclusion.{/i}"

    show sayaka a_32
    show kiyoshi a_4

    sayaka "{i}Seclusion...? Really?{/i}"

    show kiyoshi a_3

    kiyoshi "{i}Anything wrong?{/i}"

    show kiyoshi a_0
    show sayaka a_16

    sayaka "{i}It just sounds so fucking creepy when you say it like that.{/i}"

    show kiyoshi a_11

    kiyoshi "{i}Uh, well... Approach her while she is alone, then?{/i}"

    show sayaka a_5
    show kiyoshi a_4

    sayaka "{i}I don't think it gets better now that you've imprinted that word into my brain.{/i}"
    kiyoshi "{i}Uh...{/i}"

    show kiyoshi a_17

    "He discreetly cleared his throat before continuing."

    show kiyoshi a_11

    kiyoshi "{i}First of all, declare that your heart is hers!{/i}"

    scene AN_bg dullschool rear day
    show zoey a_2 at centerleft, faceright
    show sayaka a_17 at centerright, faceleft
    with dissolve

    "Heh, the plan was simple. Go and ask loads of girls out and get rejected in order to start rumors of John confessing to {i}everyone{/i}."
    "As long as I was him, I didn't want to be ostracized by everyone, so acting exactly like Kiyoshi was out of the question."
    "But that didn't mean that I couldn't give off the aura of some creep who wanted every girl he sees."
    "I had basically prepared for every situation right now, and if I prepare for something, things {i}never{/i} go south."

    show zoey a_3

    zoey "So, what's up?"
    "This was Zoey, Brad's sister who just recently started going here as a freshman."

    show sayaka a_5

    "Since she was Brad's sister, I knew she would be among the popular girls, even if she looked a bit... Uh, childish, I guess."

    show sayaka a_17

    "Which also means that having her start rumors among freshmen she's sure to impress would result in a bingo for me."

    show sayaka a_9

    think "Alright, Kiyoshi-gameface on."

    show sayaka a_6

    sayaka "You know, I've noticed you."

    pause 1
    show zoey a_7

    zoey "...Huh?"

    show sayaka a_0

    sayaka "Amongst all the... New girls, you stand out to me."

    show zoey a_2

    zoey "..."

    show zoey a_3
    show sayaka a_5

    zoey "....Huh?"

    show sayaka a_3

    think "She's completely dumb-founded..."
    think "Guess Kiyoshi's moves really do completely alienate every girl he talks to."

    show sayaka a_0

    sayaka "Would you please go out with me?"

    show zoey a_2 blush
    pause 1.5
    show zoey b_4 blush

    zoey "...S- Seriously?!"

    show sayaka a_5

    sayaka "It would be my, uh... Utmost pleasure, I think... And-"

    show zoey a_0

    zoey "Okay, sure."
    sayaka "-it would pain my hea-"

    show sayaka a_16

    sayaka "{b}What?{/b}"

    show zoey b_3:
        ease 0.75 xpos 0.6
    show sayaka a_15 blush:
        pause 0.5
        ease 0.5 xpos 0.75

    zoey "I know a really good place we could go eat something! You like burgers, right?"

    show sayaka a_4 blush

    sayaka "Uh... S- Sure...?"

    show zoey b_0
    show sayaka a_15 blush

    zoey "You want to go this Sunday at twelve? It comes as a bit of a surprise that one of Brad's friends likes me, but this sounds exciting."

    show sayaka a_18 blush
    show zoey b_6

    think "What the hell are those puppy eyes?! Why can't I just-"

    show sayaka a_11 blush

    sayaka "No- I mean- Y- Yeah, why not, I guess...?"

    show zoey a_1

    zoey "Cool, talk to you later then!"

    show zoey b_2:
        faceleft
        ease 0.75 xpos 0.4 alpha 0.0
    show sayaka a_15 blush

    think "..."

    show sayaka a_4 blush

    sayaka "{size=-5}What the fuck...?!{/size}"

    show sayaka a_14 blush

    think "O- Okay, that was just one girl who seemed to accept anyone, hah, nothing to worry about, I can just... Tell her it was a joke later on..."

    scene black with dissolve
    pause 0.5
    show AN_asset grain
    show sayaka a_5:
        center
        faceleft
        xpos 0.65
    show kiyoshi a_6:
        center
        faceright
        xpos 0.35
    with dissolve

    kiyoshi "{i}It is also important to make sure you properly convey your feelings.{/i}"

    show sayaka a_32

    kiyoshi "{i}Love is the most powerful force in the universe!{/i}"

    show kiyoshi a_18

    kiyoshi "{i}Besides several panourgian inventions, including death rays, that is.{/i}"

    show sayaka a_2
    show kiyoshi a_16

    sayaka "{i}So, what, you just tell someone you love them?{/i}"

    show kiyoshi a_15

    kiyoshi "{i}Exactly.{/i}"

    show sayaka a_16

    sayaka "{i}That's exactly the same advice you gave me just earlier! How is telling someone you love them and telling someone that your heart is theirs any different?!{/i}"

    scene AN_bg dullschool rear day
    show emily a_5 at centerleft, faceright
    show sayaka a_16 at centerright, faceleft
    with dissolve

    "Alright, talking with a freshman who didn't know better was a mistake."
    "Juniors already know John and how boring he is, if they even knew him, and the only one I really knew a lot about was this chick that always did announcements on mondays."
    "She hung out with Katrina occasionally, so she had to know how lame John is."

    show sayaka a_24

    think "Okay, gameface back on."

    show sayaka a_1

    sayaka "I am {i}so{/i} happy that you decided to take your time to see me."

    show emily a_0
    show sayaka a_0

    emily "You asked to talk, so obviously it's the least I can do for you John."

    show emily a_1

    emily "So, what did you want to talk about? It sounded serious."

    show sayaka a_5

    sayaka "Well, you see, for the longest of times I've tried to hold this back..."

    show sayaka a_3

    think "Damn, I'm so good at acting."

    show sayaka a_11

    sayaka "But... I really do think I truly love you."

    show emily a_5
    show sayaka a_6

    emily "...Eh?!"

    show emily a_6 blush
    show sayaka a_2

    emily "{b}EHH?!{/b}"
    emily "Really?! For real?!"

    show sayaka a_9

    sayaka "Yes, I understand if you feel like I am boring and bland, so let us just leave it at th-"

    show sayaka a_5
    show emily a_3 blush

    emily "What? Really? I think you're a great guy John!"

    show sayaka a_16

    sayaka "You think what now?"

    show emily a_4

    emily "For real, I thought you liked Kat since you two are together, but now I feel kind of..."

    show emily at faceleft

    emily "Flustered, I guess?"

    show emily a_6 blush at faceright
    show sayaka a_32

    emily "In a good way, you know!"

    show emily a_5
    show sayaka a_25

    sayaka "No no, for real, you don't have to respond so kindly to me, I'm just doing this becau-"

    show sayaka a_16 blush
    show emily a_3 blush

    emily "Hey hey hey, don't worry about it, I think it takes a lot of courage to say something like that, you know? Being asked out like this is totally every girl's dream!"

    show sayaka a_15 blush
    show emily a_4

    think "Wha- What the hell is up with this girl?! Guys ask girls out like this all the time, don't they?!"

    show sayaka a_4

    sayaka "But-"

    show sayaka a_15 blush
    show emily a_7 at faceleft

    emily "I like you a lot too, so if you want to hang out together sometime where we aren't the five of us like always, I think it would be really fun."
    think "Who the hell are {q}the five of us{/q}?!"

    show emily at faceright

    think "Does this girl actually fucking like John?!"

    show sayaka a_18 blush

    sayaka "Uh... Uhhhh... Y- Yeah. Su- Sure..."

    show sayaka a_15 blush

    think "And why am {b}{i}I{/i}{/b} feeling embarrassed?!"
    think "I want to refuse this, but I feel so fucking embarrassed!"

    show emily a_2 blush

    emily "Sweet! Really, I feel a bit guilty knowing Kat and all, but I'd like to give it a try!"

    show emily a_4 blush

    emily "We'll see each other later, right? Or is there something else on your mind?"

    show sayaka a_14 blush

    sayaka "Uheheh, no...? Heh..."

    show emily a_1 blush

    emily "Give me a call or a text and we'll figure something out! See you later!"
    sayaka "Yeah..."

    show sayaka a_4 blush

    think "Oh my god why."

    scene black with dissolve
    pause 0.5
    show AN_asset grain
    show sayaka a_5:
        center
        faceleft
        xpos 0.65
    show kiyoshi a_7:
        center
        faceright
        xpos 0.35
    with dissolve

    kiyoshi "{i}Most importantly, convey your feelings in a most romantic way.{/i}"
    kiyoshi "{i}The way to a woman's heart is to make her understand that no matter what, she can rely on you and you alone!{/i}"

    show sayaka a_7
    show kiyoshi a_4

    sayaka "{i}That's just telling someone you love them with extra steps!{/i}"

    show sayaka a_16

    sayaka "{i}Is this really it? All you can muster to do when interacting with any woman is to say that you love her in the most roundabout way?{/i}"

    show kiyoshi a_5

    kiyoshi "{i}We- Well, you did mention that my strategy was ineffective...{/i}"

    show kiyoshi a_4

    sayaka "{i}Yeah, well, no shit if this is the only thing you even do...{/i}"
    sayaka "{i}Sigh... I think I've promised to help for something that can't be helped...{/i}"

    scene AN_bg dullschool rear day
    show allison a_24 at centerleft, faceright
    show sayaka a_24 at centerright, faceleft
    with dissolve

    think "Okay, get your fucking grip together."

    show sayaka a_15

    think "Those two were just... Oddballs."

    show sayaka a_17

    think "Yeah, that's it. They are crazy to actually accept a confession from someone like John."

    show allison a_26

    "This time, I wasn't going to fool around with people I didn't know."
    "Once word spread that I had confessed to two people at the same time, he would look like an absolute asshole anyways."

    show sayaka a_3

    "Now, to the main dish. Allison."

    show sayaka a_5

    allison "So, uh... You wanted to talk?"
    "People think she is oh so innocent because of how clumsy and kind she is. But dig deeper into how she acts, and you'll quickly find that she isn't some goodie-two-shoes at all."
    "She's been asked out by more people than me even, and has coldly rejected everyone."

    show sayaka a_17
    show allison a_3

    "This time, I was sure to get someone who would reject me!"

    show sayaka a_16

    think "Also, no more Kiyoshi talk! I'm doing this my own way now."

    show sayaka a_5
    show allison a_24

    sayaka "I'll be honest, I like you. Alright?"

    show sayaka a_30

    sayaka "I... Uh, would like you to go out with me...?"

    show sayaka a_15 blush
    show allison a_25 blush

    think "Wait, what the hell am I saying! I'm getting fucking embarrassed again! Why?!"

    show allison a_18 blush

    allison "Oh... The others joked that you would... Uh, confess to me when you asked me to talk with you."

    show allison a_21 blush
    show sayaka a_5 blush

    allison "So this is kind of embarrassing."

    show sayaka a_17

    think "Alright! Finally someone who sees this guy as a massive joke!"

    show allison a_9
    show sayaka a_5

    allison "Uhm..."

    show allison a_21

    allison "But it doesn't really bother me that you tell me though."

    show sayaka a_10

    sayaka "Ah, understanabl-"

    show sayaka a_7 blush
    show allison a_0

    extend " What."

    show sayaka a_15 blush

    think "She doesn't actually..."

    show allison a_1

    allison "I think you're really cute and interesting, but I can't tell my friends about us if... You do want to go out with me."

    show sayaka a_4 blush

    sayaka "W- Wait, but you've rejected {i}so many{/i} people before! Why would you say yes to me? I'm boring as hell and can't do anything properly-"

    show sayaka a_15 blush
    show allison a_9 blush

    allison "But I like that. You seem really reliable and fun to hang out with."

    show sayaka a_4 blush

    sayaka "He- He does- I mean, I do?"

    show allison a_12
    show sayaka a_15 blush

    allison "I do think that someone asked you to confess to me, maybe Sayaka since you two talk to each other a lot right now."

    show allison a_10 blush

    allison "And when Katrina got mad last week I think something happened. So if you don't really like me then that's okay too."

    show allison a_22 blush at faceleft

    "She shifted in place as if... She really did like the situation she was in..."

    show sayaka a_24
    show allison a_23 blush

    think "How is this even happening..."
    think "This entire thing was such a stupid idea!"

    show sayaka a_15 blush
    show allison a_16:
        faceright
        ease 0.5 xpos 0.5

    allison "I know! We can exchange numbers if you'd like."

    show allison a_23

    allison "If you still want to go somewhere just us two alone then I would be very happy."

    show allison a_0
    show sayaka a_11 blush:
        ease 0.75 xpos 0.75

    sayaka "You, uh... Really don't have to do that."

    show sayaka a_17 blush
    show allison a_11

    allison "Non-sense. I do think you're cute. So if you ever change your mind, please tell me."

    show allison a_21
    show sayaka a_15

    "Without really being able to retaliate, I ended up adding her number, which I already knew, to John's phone."
    "And for some reason, it kinda felt good?"

    show sayaka a_21

    "Don't tell me..."

    scene black with dissolve

    title "18th of August (Thursday)" "Day 11 - Sayaka"

    show bg lunch:
        zoom 2.0 xalign 0.05 yalign 0.65
    show sayaka a_25:
        center
        faceleft
        xpos 0.45
        ypos 1.2
        transform_anchor True
        rotate -10
    show kiyoshi a_4:
        centerleft
        faceright
        xpos 0.2
        ypos 1.1
    with dissolve

    sayaka "I don't fucking get it!"
    sayaka "Why do they all like him?! Why do people like some roadside fodder like John?!"

    show sayaka a_16:
        ease 0.75 rotate 0 ypos 1.1 xpos 0.4
    show kiyoshi a_2

    kiyoshi "I can take it that yesterday's lunch period was a great success for your plans to give J-man a shot with the ladies."

    show sayaka a_4
    show kiyoshi a_1

    sayaka "Yes! No! It's terrible! I couldn't say no to {i}any of them{/i} once they were okay with him {q}liking them{/q}!"

    show sayaka a_16

    "To think one of my plans to ruin someone failed so spectacularly that I didn't even know why I did it in the first place..."
    "If this wasn't basically the taste of defeat then I didn't know anymore."

    show sayaka a_17 at faceright

    "Even then, texting the three people I talked to yesterday was still the ace in my pocket. I had just recently texted them that this was all a joke. No way they wouldn't see him like a scumbag now then!"

    show kiyoshi a_14

    kiyoshi "Ah yes, about this highly fascinating light novel I read just recently-"

    show sayaka a_3
    show kiyoshi a_10

    "I had already texted all of them when we entered the lunchroom, so it was only a matter of time until rumors would spread about him, I bet."

    show kiyoshi a_8

    kiyoshi "Oh, she isn't listening to me."
    kiyoshi "Back to eating I go."

    show kiyoshi a_1
    show sayaka a_5 at faceleft
    play sound sfx_text

    "And speak of the devil, my phone vibrated to signal that I received a message!"

    text start john
    text title "Annoying Citrus"

    msg john "hello. sorry, but yesterday was a bet i lost and i would like to avoid going out with you after all. thanks" instant
    msg zoey "what? why? i still want to take you somewhere even if ti was for fun! im still taking you with me on sunday, alright? it sounds like we could have a lot of fun!"

    text end
    pause 1
    show sayaka a_15

    think "..."

    show kiyoshi a_10

    think "Oh god, this is hell..."

    show sayaka a_24
    show cornelia b_1:
        alpha 0.0
        right
        xpos 0.8
        faceleft
    show john b_1:
        alpha 0.0
        right
        xpos 0.95
        faceleft

    sayaka "{size=-5}Just fucking kill me already...{/size}"

    show sayaka a_16 at faceright
    show cornelia:
        ease 0.75 alpha 1.0 xpos 0.65
    show john:
        ease 0.75 alpha 1.0 xpos 0.8

    "It only took a good two minutes before John and Corny finally showed up, although they looked a bit disgruntled."

    show cornelia b_2:
        alpha 1.0
        xpos 0.65
    show john:
        alpha 1.0
        xpos 0.8

    cornelia "Hey Saya."

    show cornelia b_0
    show sayaka at faceleft
    show john b_0

    sayaka "Whatever..."

    show john b_5

    john "Uh...?"
    john "Is she angry at us?"

    show kiyoshi a_11

    kiyoshi "I believe she managed to get herself too many girls yesterday."

    show cornelia:
        ease 0.5 ypos 1.1
    show john a_13
    show kiyoshi a_1
    pause 1
    show john b_6:
        ease 0.5 ypos 1.1

    john "...I'm not even gonna ask."

    show john b_0

    john "Although the most bizarre thing just happened to us..."

    show sayaka at faceright
    show cornelia b_6
    show john b_5

    cornelia "Yeah, some blonde freshman was staring at us all the time while we got some food."

    show john b_11
    show cornelia b_5

    john "It was really bizarre."

    show cornelia a_6 at faceright

    cornelia "Yeah, we get it, it was bizarre, you've already said that four times now."

    show john b_0

    john "Oh, right, sorry."

    show sayaka a_5
    show cornelia b_0 at faceleft
    play sound sfx_text

    think "Huh? Ah, another message..."

    text start john
    text title "DnD Emily"

    msg john "hello emily, yesterday was just a joke, disregard everything i said" instant
    msg emily "Aw, I thought as much, guess there is still some love for Kat xP"

    text end
    show sayaka a_15
    pause 1.5
    show sayaka a_4
    show john b_27
    show cornelia b_26

    sayaka "{i}{b}AARGH! Fuck this!{/b}{/i}"

    show john b_28

    john "Wo- What is it now?!"

    show sayaka a_16
    show john b_28

    "Corny and John were both startled at my outburst."

    show sayaka:
        ease 0.25 ypos 1.0
        ease 0.5 xpos 0.7
    show john b_7:
        transform_anchor True
        pause 1
        ease 0.25 rotate -3 ypos 1.05
    show cornelia:
        pause 0.5
        faceright
        ease 0.5 xpos 0.55

    "I grabbed John by the collar of his outfit and dragged him along."

    show sayaka at faceleft
    show john b_28

    john "Wait, what did I do now?!"

    show sayaka a_7:
        ease 2.0 xpos -0.4
    show john behind kiyoshi:
        pause 0.1
        ease 2.0 xpos -0.3
    show cornelia:
        pause 0.75
        faceleft

    sayaka "Shut up and come with me."
    john "{size=-5}But what about my food?!{/size} {size=-7}No, wait,{/size} {size=-10}I'm starving!{/size}"

    show cornelia a_11
    pause 1.5
    show cornelia a_14

    cornelia "How are you just calmly still eating your food...?"

    show kiyoshi a_8

    kiyoshi "Ah, I was just wondering if that girl you saw staring at you in astonishment was interested in me."

    show cornelia a_6

    cornelia "Yeah, no."

    scene black with dissolve

    title "18th of August (Thursday)" "Day 11 - John"

    pause 0.5
    scene bg school bathroom day
    show john b_19:
        alpha 0.0
        center
        faceleft
        xpos 1.1
        ypos 1.05
        transform_anchor True
        rotate -3
    show sayaka a_16:
        alpha 0.0
        center
        faceleft
        xpos 0.95
    with dissolve
    pause 0.5
    show john:
        pause 1
        ease 1 alpha 1.0 xpos 0.7
    show sayaka:
        pause 1
        ease 1 alpha 1.0 xpos 0.5

    john "{size=-7}Ow ow ow- Hey, hold up, why are we- {/size}Hey! Why are you dragging me into the girl's bathroom again?!"

    #SKIP
    show john:
        alpha 1.0
        xpos 0.7
    show sayaka:
        alpha 1.0
        xpos 0.5

    show john b_19:
        ease 0.25 rotate 0 ypos 1.0

    john "At least let me check if someone is here!"

    show sayaka a_7 at faceright
    show john b_27

    sayaka "Like I care!"

    show sayaka a_16

    think "Man, what the hell is her deal today?"

    show john a_13 at faceright

    "There was nobody in here again, luckily for me."

    show john b_11

    think "Aren't the girl's stalls usually really occupied with people all the time normally?"
    think "Man, it's so convenient how nobody is here right now so that we can talk in private."

    show john b_0 at faceleft

    john "Alright, alright, we're here."

    show john a_4

    john "Geez, you know that your grip is way stronger right now than normally right? It really hurts when you do something like that."

    show john a_0

    "But really, what did I do now? I thought she was over the entire jeans and glasses thing."

    show sayaka a_7

    sayaka "You're going to a mixer with me."

    show sayaka a_16
    show john b_11

    john "...A mixer?"

    show john b_25

    think "Isn't that..."

    pause 0.5
    show john b_28

    john "{i}{b}WHAT?!{/b}{/i}"
    john "What the hell?! Do you want to go out with me like this?!"

    show john b_27
    show sayaka a_7

    sayaka "Shut the hell up you good-for-nothing!"

    show sayaka a_16

    sayaka "I don't give a crap about you, I just have something to confirm."

    show john b_28

    john "Something to confirm? What the hell are you going to {q}confirm{/q} by going to a mixer with me?!"

    show john b_27

    sayaka "Then you haven't noticed it? When you look at guys?"

    show john b_6

    john "Uh, what am I supposed to notice?"
    sayaka "That they look like boyfriend material?!"

    show john b_27

    #TODO: Add blushes to glasses
    john "Wha-{nw}"

    show john b_28 blush

    extend "What?!"
    think "Wait, why am I getting so flustered by her saying that?"

    show john a_8 blush

    john "N- No! Never!"

    show john a_27

    think "Seriously?!"
    sayaka "I casually talked to some girls yesterday and got embarrased as fuck! And I know for sure that I'm not some lesbie!"

    show sayaka a_7

    sayaka "This entire body swap shit has to be fucking with me, and if it fucks with me, I bet it fucks with your head too."

    show sayaka a_16
    show john a_29 blush

    john "I, uh... Maybe a little bit...?"

    show john a_27 blush

    john "Wait, are you actually dating a girl right now?!"

    show sayaka a_20

    sayaka "Of course not! I'm not lesbian you asshole."

    show sayaka a_16
    show john b_19

    john "But why the hell should I- I mean, why would I go to this mixer thing with you? Why don't you just go yourself?"

    show john b_17

    sayaka "Because I decided you're going too."

    show john a_6

    john "Wow, I don't know what I expected asking Ms. Full-Of-It over here."

    show sayaka a_7

    sayaka "You're going, basta!"

    show john b_18

    john "And I {b}really{/b} don't feel like going, so no thank you."

    show john b_17
    show sayaka a_21:
        faceleft
        ease 0.5 xpos 0.4

    sayaka "Nghh...!"

    show john b_6

    think "Man, she is annoyed like all hell right now."

    show john b_4

    think "Not that I do this to annoy her, I just {i}really{/i} don't want to go do that kind of thing with her."

    show john b_17
    show sayaka a_7:
        faceright
        ease 0.25 xpos 0.55

    sayaka "Fine, if you go, we're even with the glasses and jeans."

    show sayaka a_16
    show john b_18

    john "Seriously? That's your logic? In the first place, you started it because you dyed my hair!"

    show john b_17
    show sayaka a_7

    sayaka "In the first place I did it because {b}you{/b} decided to ditch cheerleading, and still do!"

    show john b_11
    show sayaka a_16

    john "Wait, that's why you did it?"

    show sayaka a_4

    sayaka "You didn't fucking realize until now?!"

    show john b_28
    show sayaka a_21

    john "How am I supposed to?! Hello? You're not communicating with me at all!"

    show sayaka a_20
    show john b_13

    sayaka "Do you really think this is fun for me?! My life being used by someone I hate?!"
    sayaka "Everything I built up, being torn down within a single fucking week because, oh, I don't know, some stupid god decided that this time, I should be the one getting grated by the worst fucking human he could find?!"

    show sayaka a_21
    show john b_19

    john "What? No, I..."

    show sayaka a_20
    show john b_11

    sayaka "You're terrible at dealing with women you prick! Not only that, but now it turns out that I am starting to become a lesbie even though I know I'm not!"

    show sayaka a_4

    sayaka "I don't know what's happening to me! I'm going fucking crazy over this, and you're still fighting against me!"

    show john b_8

    john "Hey- No, Sayaka, I'm- I'm sorry, I didn't mean it like that, it's just, you know..."

    show sayaka a_7

    sayaka "Go to the fucking mixer with me."

    show john b_4
    show sayaka a_16

    think "...Man, I didn't know that this was how she felt. She actually seems completely broken over her sudden change in sexuality..."
    think "Although I feel the same as well."
    "Being attracted to guys even though you know you aren't. It was a feeling that was indescribable."
    "Instincts clashing together, basically. I kind of felt confused, but that was about it, but for her it must be much more serious if she even started pleading to me to go to this thing in her own way."

    show john b_18

    john "{i}Sigh{/i}... Alright..."

    show john b_13

    john "You want to go to make sure we both feel this way, right? No tricks, no dating between us, right?"
    sayaka "Of course."

    show john b_25

    john "Okay, but if I do this, we're even. I get to wear what I want as long as it isn't a clown outfit-"
    sayaka "{size=-5}You're already wearing one...{/size}"

    show john a_32

    john "...As I said, as long as it isn't a clown outfit. Okay?"

    show john a_6

    sayaka "...Fine, have it your way."

    show john b_25

    think "Oh god, what have I even gotten myself into..."

    scene black with dissolve

    title "20th of August (Saturday)" "Day 13 - John"

    pause 1
    scene bg sayaka house day
    show john b_2:
        center
        xpos 0.45
        faceright
    show cornelia a_1:
        center
        xpos 0.75
        faceleft
    with dissolve

    "Ah yes, sweet release. We were done with the half-day at school today and finally had weekend once more."

    show john b_4

    "Tomorrow would be the day where I would go to this dreaded mixer with Sayaka of all people, and it was stressful thinking about it, but sometimes I think it's important not to make her too angry."

    show john a_0
    show cornelia a_2

    cornelia "See you on monday then."

    show cornelia a_1
    show john b_29

    john "Ah, uh... You don't want to come in for a drink or something since your parents arent home and everything?"

    show cornelia a_14

    "She looked at me as if confused about it. For whatever reason she didn't expect this at all."

    show cornelia b_4
    show john b_0

    cornelia "No... It's okay, I don't... Uh, usually just enter her house, you know..."

    show john a_6

    john "Huh? You don't?"

    show john a_13
    show cornelia b_0

    john "Has she never invited you over to just hang out?"

    show cornelia b_17

    cornelia "What? No, of course not! We hang out in the mall and I get to go to her home if we are setting things up for her parties. That's it."

    show cornelia b_14
    show john a_30

    "Well that took a sad turn. I didn't expect them to have a friendship this terrible."
    "What she was saying was essentially that Sayaka never let her just casually visit her, even though they walked to school and back every single day..."

    show john a_13

    john "No, please, if that's the case, I really insist. I'm not Sayaka, remember? Or do you have anything better to do?"

    show cornelia b_21

    cornelia "Well, no, but..."

    show john a_11
    show cornelia b_31

    john "Come on! You get to just casually hang out in her house. Doesn't that sound exciting?"

    show cornelia b_23

    cornelia "If you put it like that, sure, but-"

    show cornelia b_5
    show john b_14

    john "Then make yourself comfortable. Come on, what's the harm?"

    show cornelia b_4
    show john b_1
    pause 1
    show cornelia b_1

    cornelia "...Alright, you win, sure."

    scene black with dissolve
    play sound sfx_sliding_door_open
    pause 2
    play sound sfx_door_open
    pause 1
    play sound sfx_door_close
    scene bg sayaka kitchen day
    show john b_0 at left, faceleft
    show cornelia a_1 at center, faceleft
    with dissolve
    pause 0.5
    show john b_12:
        faceright
        ease 0.5 centerleft

    john "Oh yeah, sorry, this household only has weird juice brands to drink besides water."

    show john b_1

    cornelia "That's okay."

    show john:
        ease 3 xpos 0.8
    show cornelia:
        pause 1.25
        faceright

    "At least I could spend some idle time of the day on talking to Cornelia right now. I actually liked talking to her on occasions now."

    show john a_0

    john "Uh... So let's see... We got apple juice, raspberry juice... Something called lemon water...?"

    show cornelia b_1:
        ease 1 xpos 0.675

    cornelia "Lemon water sounds good."

    show john a_11

    john "Coming right up!"

    scene black with dissolve
    pause 0.5
    play sound sfx_door_open
    scene bg sayaka bedroom day
    show john b_0 at center, faceleft
    show cornelia a_11 at right, faceleft
    with dissolve

    "I did have my console in my room now which helped entertain me, and I managed to break Sayaka's phone lock too, so life was a bit more bearable, with not having anything to do the entire day and all."

    show john b_1 at faceright

    "But still, I did like talking to people, that much hasn't changed despite our swap."

    show john b_0
    show cornelia a_12

    cornelia "It's been so long since I've been in Saya's room... It almost feels like I'm breaking some kind of law, heh."

    show john b_6
    show cornelia a_11

    john "You haven't been to her room? Aren't you guys close friends or something?"

    show cornelia a_6

    cornelia "Well, duh, but this is her {i}private{/i} room. The one she sleeps in and stuff."

    show cornelia b_0:
        ease 0.5 centerright
    show john a_27

    john "Sayaka has more rooms?!"

    show cornelia b_6

    cornelia "...Seriously, you didn't know?"

    show cornelia b_24
    show john a_26

    john "Why would she have multiple rooms? You mean bedrooms?"

    show cornelia b_2
    show john a_6

    cornelia "I can show you later. Really, you live here and you don't even know that."

    show john b_2
    show cornelia b_1

    john "Don't blame me, I haven't had a guide yet."

    show john b_6

    think "What would she even need more than one room for?"
    think "What am I thinking. It's Sayaka. Logic doesn't apply like that."

    show john b_1

    john "But I'm looking forward to learning more about this place."

    show cornelia a_1

    cornelia "I only really know the living room area and where she hangs out when she wants to be in private."

    show john a_0:
        faceleft
        ease 0.75 xpos 0.4
        faceright

    john "Ah yeah, are you for real when you say she never invited you over?"

    show cornelia a_5

    cornelia "Why would she?"

    show john b_11:
        ease 0.5 ypos 1.15

    john "But aren't you guys friends?"

    show cornelia b_5

    cornelia "Of course."

    show cornelia b_0:
        faceright
        pause 1
        ease 0.5 xpos 0.75
        faceleft
        ease 0.5 ypos 1.1

    john "It just doesn't seem like the friendship goes both ways to me..."

    show john a_13

    john "You know, when I think of friends, I think of hanging out on a day off or doing stuff together."

    show cornelia a_0

    cornelia "What we do in our free time is none of your business, you know. Besides, we don't play the same friendship game like you guys do."

    show cornelia a_13

    cornelia "Sayaka has qualities that you can't even understand, and before you came along she had status and power in her image alone."

    show john a_30
    show cornelia a_18

    cornelia "We can't play some kid's game of {q}Hang out and cuddle with your friends{/q} like that."

    show cornelia a_1
    show john a_24

    john "But isn't that exactly what we're doing right now...?"

    show cornelia a_10
    pause 1.5
    show cornelia a_19

    cornelia "...No."

    show cornelia a_7
    show john a_2

    cornelia "Well yes, but you aren't the real Saya!"

    show john a_12
    show cornelia a_0

    john "Haha, you totally do enjoy sometimes just talking, don't you? Having talked to you for two weeks convinced me."

    show cornelia a_8 blush
    show john a_1

    cornelia "Sh- Shut up, I'm only doing this because it's you."

    show john a_14

    john "Heh, sorry."

    show cornelia b_6 blush at faceright
    show john a_1

    "It was really easy to figure out how she feels about certain things."
    "If I had never swapped with Sayaka, I probably never would have seen Cornelia in this kind of light, but she was really not that bad."

    show cornelia b_24 at faceleft

    "The only thing that stood out to me about her was the influence Sayaka was having on her, and I personally didn't think it was the good kind of influence."
    "But whatever, right now I was in charge on that front."

    show john b_0

    think "Actually, all this talk is making me remember about this thing I found some time ago."

    show john a_0
    show cornelia b_5

    think "Maybe it's worth a shot asking Cornelia about it."

    show john b_0

    john "Hey, by the way, I wanted to ask you something."

    show cornelia b_0

    cornelia "Hm?"

    show john:
        faceleft
        pause 0.5
        ease 0.5 ypos 1.0
        ease 0.75 xpos 0.25

    john "I found this thing after rummaging through the room."

    show cornelia b_6

    cornelia "Why have you been rummaging through Saya's room? You know she would never allow that."

    show cornelia b_24


    john "What she doesn't know, doesn't hurt her."
    "After digging through the drawers I found the thing I had been wondering about for a long time."

    show AN_asset picture_frame with dissolve
    show cornelia b_23:
        center
        xpos 0.4

    john "Here."
    cornelia "An old picture?"
    john "Sounds like you don't know what it is either."
    cornelia "Hm, no, never seen it."
    john "I just thought that this girl right here-"
    "I pointed at the little girl to the very left."
    john "Doesn't she look a lot like Kat?"
    cornelia "..."
    john "And this girl on the right looks like Sayaka."
    "Cornelia went silent the moment I mentioned Kat's name."
    cornelia "{i}Sigh...{/i}"

    hide AN_asset picture_frame with dissolve

    cornelia "Look, I'm sure someone out there would appreciate your endless curiosity in the business of someone else..."

    show john at faceright

    cornelia "But this isn't something you're supposed to know about. I don't even know much about it and I'm next to Saya constantly."

    show cornelia b_5
    show john b_4

    john "So you think I should stay out of trying to figure out the beef between Sayaka and Kat?"

    show cornelia b_0

    cornelia "Exactly."

    show john b_13

    john "Ugh, fine. I'm just really curious as to why they hate each other so much..."
    john "I know that they were friends at some point, but something {i}must{/i} have happened, especially if Sayaka keeps this picture hidden."

    show cornelia b_6

    cornelia "You're really bad at letting a topic go just like that, huh?"

    show cornelia b_24
    show john a_14

    john "Seems like it."

    show john a_0
    show cornelia b_5 at faceright

    cornelia "That aside, why does Sayaka have an EksBox in her room...?"

    show john a_11

    john "Oh, you know what it is? Do you have one yourself?"

    show cornelia b_11 at faceleft
    show john a_10

    cornelia "Of course not. You think I'm some kind of nerd who knows about that stuff?"

    show john a_31
    show cornelia b_0

    think "...But She still knows what an EksBox is..."

    show john a_25

    john "Alright, sorry, my bad."

    show john a_10

    john "But do you want to try playing?"

    show cornelia b_24:
        pause 1
        faceright
        pause 1.5
        faceleft

    "She eyed me and the console curiously. It was clear as day that she was conflicted and was really bad at hiding that."

    show john a_14
    show cornelia b_5

    "The moment I had asked her the question I immediately realized that she totally did want to play, if just a little."

    show john a_1
    show cornelia a_1 at faceleft

    cornelia "...No, but you can go ahead if you want to. I'll watch."

    show john b_11

    john "Wouldn't that be boring for you?"
    cornelia "I said it's fine, you only have one controller anyways."

    show john b_13

    john "Alright then."

    show john b_24:
        ease 2 xpos 0.65
        ease 0.75 xpos 0.675 ypos 1.15
    show cornelia:
        pause 1
        faceright

    think "She even knows how controllers look."
    think "Heh, too easy to read."

    show john b_23
    show cornelia a_13

    "I couldn't help but smirk."

    scene black with dissolve
    pause 1
    play music AN_bgm_gaming fadein 1
    scene bg sayaka bedroom dusk
    show john b_17:
        center
        faceright
        xpos 0.5
        ypos 1.15
    show cornelia b_23:
        center
        faceright
        xpos 0.35
        ypos 1.15
    with dissolve

    cornelia "No, no, you're doing it all wrong, you need to first stack up blocks and wait for a straight block to appear."

    show cornelia b_5

    john "Am I not doing that already?"

    show john b_3

    cornelia "You need to wait until you have four height rows before you drop a straight block down there, else you lose the multiplier."

    show cornelia b_6

    cornelia "Geez, I thought you were good at games and even I know more about Dedris than you."

    show john b_17
    show cornelia b_24

    john "Hey, I've never really played Dedris before."

    show cornelia a_0

    cornelia "As if that's an excuse. If you're good at one game then another game gets easier to pick up."

    show cornelia a_1

    cornelia "So if you nerd through tens of games the next one should be ever easier to learn."

    show john b_6

    think "...Why does she know so much about games..."

    show john b_0

    "I only had the games that were installed on my console, so after we got bored of them we started playing some retro games that were already installed when I bought it."
    "And for some reason, Cornelia of all people was tutoring me in how to play them at what is basically competitive level..."

    show john b_11

    john "So are retro games your thing?"

    show cornelia b_6

    cornelia "No games are my thing! And don't miss the middle with the L-block."

    show john b_25

    john "Right..."

    $ renpy.sound.set_volume(0.25)

    think "Geez, she'd rip my hair out if I missed an obvious placement for these blocks."

    show john b_0
    show cornelia a_11
    play sound sfx_kiyoshi_sing

    "Whilst playing, Cornelia's phone started playing her ringtone."
    cornelia "Oh, it's mom-"

    show cornelia a_8

    cornelia "What the hell, it's half past six already?!"

    show john b_11

    think "Oh yeah, we have spent a lot of time just playing games I had."

    play sound AN_sfx_silence
    $ renpy.sound.set_volume(1)
    show john b_5
    show cornelia b_0:
        ease 0.5 ypos 1.0 xpos 0.4
        pause 0.25
        ease 4 offscreenright

    "I kept playing while she went outside the room to talk."

    play sound sfx_door_open

    "Sayaka's parents would probably still be gone for another two or three hours, but hers are maybe wondering where she is."

    play sound sfx_door_close
    show cornelia b_4:
        faceleft
        ease 2.5 centerright
    show john b_0

    "It only took a few minutes before she entered again."

    show cornelia b_0

    cornelia "My parents are preparing dinner, so I'm leaving soon."

    show john a_10
    stop music fadeout 3

    john "Ah, alright."

    show john a_14:
        pause 1
        ease 0.5 ypos 1.0

    john "It is probably enough games for me today anyways."

    show john a_10
    show cornelia b_30

    cornelia "And, uh... And if you want you can come along."

    show john a_29

    john "Huh? Really? Your parents would let me eat over at them?"

    show cornelia b_0
    show john a_0

    cornelia "My mom said that since you invited me to hang out for once they'd like to repay the favor. Something along those lines."

    show john a_13

    john "Hmm..."
    think "Man, when was the last time I had dinner with someone other than myself?"
    "Every day here really was the monotone same. Get home, be by myself and then order something for dinner alone."
    "For the last few days I have been buying my own food to make from a store nearby and ate whatever I wanted to cook, but it just felt like I was living by myself."

    show john b_14

    john "Sure, why not. Don't see a reason why I would refuse."

    show john b_11

    think "Actually, I do have something Sayaka and Kiyoshi want me to read about the swapping thing before monday..."

    show john b_23

    think "Well, that can wait."

    show john b_10

    john "I am going to get changed though before we go. These school clothes just don't work as comfy wear."

    show john b_1:
        faceleft
        ease 1 xpos 0.3
    show cornelia a_7

    cornelia "H- Huh?! You're getting changed?"

    show cornelia b_14

    cornelia "I hope you close your eyes while you don't have any clothes on!"

    show john a_6 at faceright

    john "...Seriously?"
    john "You don't think I've seen her naked before?"

    show cornelia b_17

    cornelia "A guy can't just watch a girl naked whenever he wants!"

    show cornelia b_14
    show john b_6

    john "Yeah, yeah, I get it. But Sayaka gets to see me naked whenever she wants to too, so don't think this is one-sided."

    show cornelia a_3

    cornelia "But you are totally uninteresting physically. Saya is leagues above you in appearance."

    show cornelia a_14
    show john a_32

    john "That's a very roundabout way of telling me I'm ugly..."

    show john a_13
    show cornelia b_5

    john "Besides, we've both already realized that the swap is starting to affect us mentally."
    john "At the start I thought seeing her in her underwear was hot, but nowadays it doesn't even affect me when I see other girls half-naked or whatever."

    show cornelia b_11

    cornelia "That's- That still isn't an excuse for you to go around the girl's changing room, you know?!"

    show john b_6
    show cornelia b_5

    "Earlier yesterday when we had P.E., Cornelia made sure I was the last one in and out of the changing room."
    "For obvious reasons."
    think "And she still hasn't realized that it was me during the first P.E. lesson I had as Sayaka."

    show cornelia a_5
    show john b_0

    cornelia "Fine then, not like I can stop you peeking when you're alone anyways..."

    show cornelia a_8

    cornelia "But.. Are you guys starting to turn into each other?"

    show john a_6
    show cornelia a_22

    john "What does that mean?"

    show cornelia a_8
    show john a_0

    cornelia "Like... Are you starting to become more like Saya then since you, uh... Start seeing girls like a girl? That's what you said, right?"

    show cornelia a_22
    show john b_1

    john "Nah, I don't think it's that extreme. Sayaka said it has to do with hormones or something probably."

    show cornelia a_0

    cornelia "Oh, that makes sense."

    show john b_0
    show cornelia a_14

    cornelia "But really, hurry up, my mom is waiting for us."

    scene black with Dissolve(1.0)
    $ renpy.sound.set_volume(0.5)

    title "21st of August (Sunday)" "Day 14 - John"

    outfit john underwear_badhair
    accessory john set
    $ screenfilter.blur = 2
    play sound AN_sfx_rooster
    pause 1.5
    scene bg sayaka bedroom day
    show black:
        alpha 0.5
    show john b_6:
        faceright
        center
        xpos 0.6
        ypos 1.15
        alpha 0.0
    with Dissolve(1.0)
    pause 1.5

    think "..."

    $ renpy.sound.set_volume(1.0)
    show john:
        ease 0.75 alpha 1.0
    show black:
        ease 0.75 alpha 0.0

    think "Ugh, why do the neighbors have a freaking rooster of all things..."

    show john b_22

    "It was that bliss time of the week where I could just stay in my bed half-asleep, despite Gunnar the Rooster from next door screaming his lungs out."

    show john b_20

    "Sundays were the best, especially if you spent a lot of time just gaming into midnight last day."

    show john b_14

    think "I'm sure Cornelia can be proud of the fact that I finally unlocked hard-mode in Dedris."

    show john b_22

    think "..."
    think "Right, I made the stupid decision to promise going on this date thing."
    john "{i}Sigh...{/i}"

    show john b_6 at faceleft

    think "Glasses, glasses, where art thou."

    show john b_14

    think "There you are."

    accessory john set glasses
    show john b_23
    with dissolve
    $ screenfilter.blur = 0

    think "That's better."

    show john b_6

    think "Man, I would've loved sleeping until like twelve into noon, but Sayaka told me I had to get up as early as possible."
    think "..."

    show john b_25

    think "I should probably get up before she ambushes me while I'm still lying here."

    scene black with dissolve
    outfit john uniform_b_pony_jeans
    scene bg sayaka kitchen day
    show john b_6:
        center
        faceright
        ypos 1.1
    with dissolve
    pause 2
    play sound sfx_bell
    pause 1
    play sound AN_sfx_silence
    pause 0.5
    show john b_11 at faceleft

    think "Oh, that has to be her."

    show john b_6

    think "She's really early..."

    show john:
        ease 0.75 ypos 1.0
        pause 1
        ease 5 offscreenleft

    "I was still munching on my cereal, so I took the bowl with me to the front door."

    scene black with dissolve
    scene AN_bg sayaka frontyard day
    show john b_0:
        right
        faceleft
        alpha 0.0
    with dissolve
    show john:
        pause 0.5
        ease 0.75 alpha 1.0 centerright

    "It was a bit of a hassle since anyone without a key wouldn't even be able to get into this massive complex of a building."

    #SKIP
    show john:
        centerright
        alpha 1.0

    outfit zoey casual
    outfit sayaka winter
    play sound sfx_sliding_door_open
    show carrie a_9:
        left
        faceright
        alpha 0.0
        xpos 0.0
    show zoey a_2:
        left
        faceright
        alpha 0.0
    show sayaka a_16:
        centerleft
        faceright
        alpha 0.0

    "I opened the gate for her and..."

    show john b_6
    show sayaka:
        ease 0.5 center alpha 1.0
    show zoey:
        pause 0.25
        ease 0.5 xpos 0.35 alpha 1.0
    show carrie:
        pause 0.5
        ease 0.5 xpos 0.2 alpha 1.0

    sayaka "Took you long enough."

    show zoey b_1:
        alpha 1.0
        xpos 0.35
    show sayaka:
        center
        alpha 1.0
    show carrie:
        xpos 0.2
        alpha 1.0

    zoey "I knew it, you totally were going to be with this girl today! You shouldn't just lie to girls like that!"

    show carrie a_2
    show sayaka a_24

    carrie "{size=-5}Another rival...{/size}"
    john "..."

    show zoey a_2
    show sayaka a_16
    show john b_19

    john "What the hell are they doing here?"

    show john b_17

    "That blonde girl that kept looking at me during lunch last day and freaking Carrie were with her in tow."

    show sayaka a_7

    sayaka "Not my fault that this annoying girl doesn't want to leave me alone."

    show sayaka a_16 at faceleft
    show zoey a_3

    zoey "We both agreed we would be going to hang out today."

    show sayaka a_7

    sayaka "Did not!"

    show sayaka a_16 at faceright
    show zoey a_2
    show carrie a_16 at faceleft

    john "Wait, you're bringing her to the mixer?"

    show zoey a_3
    show sayaka a_15

    zoey "The mixer? What is that?"

    show sayaka a_4 at faceleft

    sayaka "She is only staying until we're done preparing {i}you alone to go to the aforementioned thing{/i}."

    show john b_6
    show sayaka a_16

    john "...Uh... Am I supposed to agree with what you're sayi-"

    show john b_28
    show sayaka a_15 at faceright

    extend " Ah, I mean, yes, {i}I am the only one going to this thing{/i}...?"

    show john b_26
    show sayaka a_13

    sayaka "{i}Exactly{/i}."

    show john b_27
    show zoey b_6
    show sayaka a_8 at faceleft

    zoey "...What are you guys even talking about?"

    show sayaka a_16

    sayaka "Not something you have to know."

    show zoey b_5
    show carrie a_2 at faceright

    sayaka "Carrie, my things."

    show carrie a_1:
        pause 1
        ease 0.5 xpos 0.35
    show zoey a_2:
        pause 1.25
        ease 0.75 xpos 0.2

    carrie "Yes! Here you go."

    show sayaka a_0
    show john b_11
    show carrie a_14

    sayaka "Thanks, see you later at six."

    show carrie a_15

    carrie "Of course, John."

    show carrie a_1 blush:
        faceleft
        ease 2.5 offscreenleft
    show zoey:
        pause 1.5
        faceleft

    "Unbelievably, she waltzed her way back towards where she lived."

    show zoey at faceright
    show sayaka a_5 at faceright
    show john b_6

    john "Did you actually for real tame this girl?"

    show john b_13

    sayaka "What do you mean {q}tame her{/q}? All I did was make sure she doesn't cause trouble for me."

    show sayaka at faceleft
    show zoey a_7

    zoey "Who was she anyways? She gave me the creeps."

    show john b_25
    show sayaka at faceright

    john "You don't even know half of it. Man, I'm so glad I don't have to interact with her anymore."

    show sayaka a_17
    show john b_11
    show zoey a_2

    sayaka "Bah, you're just missing out on free workforce. All you need to do is throw her a bone and make sure she doesn't get any wrong ideas."

    show sayaka a_16:
        ease 4 offscreenright
    show zoey b_2:
        pause 2
        ease 4.5 offscreenright
    show john:
        pause 2
        faceright
        pause 1
        faceleft
        pause 1.5
        faceright

    sayaka "Anyways, I'm not here to chat about useless stuff. You bought the things I told you right?"
    "Without much of a warning, she just walked through the door as if she owned the place and expected me to follow."

    show john b_6

    "And that girl followed her almost immediately, and I still had no idea who the hell she was or what she was even doing here."

    scene black with dissolve
    scene bg sayaka kitchen day
    show sayaka a_5 at centerright, faceright
    show zoey a_0 at center, faceleft
    show john b_0:
        offscreenleft
        faceright
        ease 1.0 centerleft
    with dissolve

    john "I didn't find the exact shampoo you told me to buy but I found something similar."

    show sayaka at faceleft

    sayaka "That's fine. As long as the eyeliner and lipstick are the exact same."

    show john b_6

    john "...Do you really want me to actually wear that stuff?"

    show zoey a_2

    zoey "You don't use eyeliner normally?"

    show sayaka a_16
    show zoey at faceright
    show john b_11

    sayaka "Yes she does, and yes, I do want you to wear it."

    show sayaka a_5

    sayaka "Now. Let's get down to business"

    show sayaka:
        faceright
        ease 0.75 xpos 0.85
    play sound sfx_door_open

    "She walked up to the fridge, opened it, and found a can of soda that had been lying around for god knows how long."

    show sayaka:
        faceleft
        ease 0.5 xpos 0.7
    show zoey a_3

    sayaka "Here. Me and Sayaka have to talk in private for a bit, so go into the living room and watch some TV while you wait."

    show zoey a_0

    "She handed the blonde the soda, to which the girl smiled."

    show zoey a_1

    zoey "Sure!"

    show zoey a_3

    zoey "But I want to join in on applying her make-up."

    show sayaka a_16

    sayaka "Yeah yeah, scram."

    show zoey b_2:
        ease 3 offscreenright
    show john b_6
    show sayaka a_5:
        pause 1
        faceright
    pause 2
    play sound sfx_door_close
    pause 0.5

    "The girl left the kitchen and closed the door behind her."

    show john b_25
    show sayaka at faceleft

    john "...Care to explain?"

    show sayaka a_16

    sayaka "I can't get rid of her."

    show john b_17

    john "You can't get rid of her? Why is she following you in the first place?"

    show sayaka a_7

    sayaka "She just... Came up to me and told me she liked me and now I'm stuck with her."

    show john b_6
    show sayaka a_16

    john "...So you're saying that within two weeks, you've managed to get some freshman to fanatically like me. For no reason."
    sayaka "Who cares about it? We don't have a lot of time so we need to start doing the make-up and hair."

    show john b_13

    john "I still don't get why she is suddenly attached to you like Carrie, I mean, it really reeks like you're hiding someth-"

    show sayaka a_4

    sayaka "I said, who cares!"

    show sayaka a_25 at faceright
    show john b_25

    think "She is totally hiding something."

    show sayaka a_16 at faceleft
    show john b_18

    john "Who even is she?"

    show john b_17
    show sayaka a_5

    sayaka "...{i}Sigh...{/i} Her name is Zoey and she is Brad's sister."

    show john b_11

    john "Huh..."

    show john b_28

    john "Wait, Brad has a sister?! That Brad?!"

    show john b_27

    sayaka "Yes, that Brad. And she agreed to leave me alone for the rest of the day if she could help out with this, so just, don't question why she's here and everything will be fine."

    show sayaka a_16
    show john b_0

    sayaka "Got that drilled into your brain?"

    show john b_6

    john "Yes, sir."

    show sayaka:
        faceright
        ease 2.5 offscreenright

    think "I was curious what on earth made her stick to Sayaka in the first place, but it doesnt't seem like she wants to talk about it."

    play sound sfx_door_open
    scene black with dissolve
    scene bg sayaka livingroom day
    show zoey a_3 at centerright, faceright
    show sayaka a_16:
        center
        xpos 0.4
        faceright
    show john b_0:
        offscreenleft
        faceright
        ease 2 xpos 0.275
    with dissolve
    show zoey a_2 at centerright, faceleft
    play sound sfx_door_close

    sayaka "We're done talking. If you want to do this then get off your ass and follow us."

    show zoey a_0 at faceleft
    show john b_6

    zoey "Huh? Oh that was fast. Sure."
    think "Seriously, why does this girl even want to be in a 100 meter radius of Sayaka if this is how she treats her..."

    scene black with dissolve
    pause 1
    outfit john underwear_badhair
    accessory john set
    outfit sayaka winter_tshirt
    $ screenfilter.blur = 2
    scene bg sadie bathroom day
    show john b_6:
        centerright
        faceright
        ypos 1.15
    show sayaka a_5:
        center
        faceright
        xpos 0.5
    show zoey a_0:
        centerright
        faceright
        xpos 0.6
    with dissolve

    sayaka "The face cream."

    show zoey b_6:
        ease 0.5 xpos 0.85

    zoey "Uh... What drawer?"
    sayaka "Third from the top on the right."

    show zoey b_0

    zoey "Oh, okay."

    show zoey a_0

    think "..."

    show john b_23

    think "I feel like a doll that's being pampered right now..."

    show zoey:
        faceleft
        ease 0.5 xpos 0.6
    show sayaka a_2

    zoey "Here you go."

    show sayaka a_5
    show zoey at faceright

    "Sayaka was concentrated on putting all kinds of chemicals on my face in the right way."

    show john b_20

    "It just... I don't know, looked weird to see my own body applying stuff to Sayaka's face, while I had control of Sayaka's face and all."

    show john b_6
    show zoey a_3

    "I had looked at myself in the mirror plenty of times during these last two weeks, but this was still bizarre. My face was full of some weird cream she smeared around for the 4th time now."

    show john b_0

    zoey "Do you guys do this often?"

    show sayaka a_2

    sayaka "Often? Uh..."

    show john b_30

    john "N- No, John just... Likes to practice for the future, heh, right, John?"

    show sayaka a_6
    show zoey a_2
    show john b_13

    sayaka "Uh, yeah, sure."

    show zoey a_1

    zoey "Ooh, you want to be some kind of make-up stylist or whatcha call it?"

    show zoey a_0
    show sayaka a_0
    show john b_1

    sayaka "Uhm, yeah, that."
    "It was only for a brief moment, but Sayaka actually nodded in approval to me in the mirror. Almost as if telling me {q}good job{/q}."

    show john b_14

    "It almost felt fulfilling having this girl approve of my genius lie."

    show sayaka a_5
    show john b_29

    john "But don't, you know, tell anyone. It's a secret."

    show zoey b_2

    zoey "My lips are sealed."

    show zoey a_0
    show john b_11
    show sayaka a_8

    sayaka "Good. Now wait 15 minutes for the cream to sink in, then wash your face afterwards."
    sayaka "After that you can take a bath while I fix your hair and then we do the final touches."

    show zoey a_7
    show john b_25

    john "Uh... Sounds good."

    show zoey a_1
    show john b_11
    show sayaka a_5

    zoey "Ahaha, he said he is going to do your hair while you're taking a dip in the water and you're just okay with that?"

    show john b_27
    show sayaka a_15

    zoey "You're so weird. "

    show zoey a_0

    sayaka "..."

    show john b_26

    think "Wait, did she actually say that?"

    show sayaka a_12
    show john b_27
    show zoey a_7

    sayaka "I'm just gonna go make a call real quick."

    show sayaka a_16:
        transform_anchor True
        ease 0.5 rotate 7.5 ypos 1.02

    "She leaned down right next to my ear and started whispering to me."

    show zoey a_2

    sayaka "{size=-8}This is taking too long and I have to do this while you're washing yourself or we're going to be late, so I'm getting this brat away from here with my plan B.{/size}"

    show sayaka a_12:
        ease 0.5 rotate 0 ypos 1.0
    show zoey a_3 at faceleft

    zoey "Huh?"

    show john b_7 at faceleft

    john "Hey, hey, hey..."

    show sayaka a_16:
        faceleft
        ease 4 xpos -0.5

    john "You're not serious right?"

    play sound sfx_door_close

    "She ignored me and got out her phone (well, it's actually my phone but whatever)."

    show john b_0
    show zoey b_4 at faceright

    zoey "What did he tell you?"

    show john b_2

    john "Uh... Nothing..."

    show zoey a_2
    show john b_14

    zoey "..."

    show zoey a_3
    show john b_1

    zoey "You like him too, right? You can't hide that, you guys are way too close."

    show john b_28

    john "W- What? Like him? Me?"

    show john b_11
    show zoey a_2

    zoey "Heck yeah. But I'll let you know, he confessed to me, not you. And I bet you told him to text me what he did."

    show john b_26

    zoey "But I don't give up that easily!"

    show john b_19

    john "What?! He confessed to you? What the hell are you talking about?"

    show zoey b_5:
        faceleft
        ease 0.75 xpos 0.55
    show john b_17

    zoey "Hmpf, so he didn't tell you."

    show zoey b_2 at faceright

    zoey "But yeah, that's right. I'm still trying to figure out why he would suddenly back out again, but even someone who has the guts to do that as a prank is someone I think is really cool."

    show john b_5

    john "Ba- Back up, are you serious? Confessed, like in, tell you he likes you?"
    zoey "Of course."

    show john b_19

    john "Wha- Why would she do tha-"

    show john b_27
    play sound sfx_door_open
    show zoey a_2 at faceleft
    show sayaka a_10:
        faceright
        ease 2 centerleft

    "As I was trying to figure out what the heck she was saying, Sayaka walked back into the bathroom with a smile on her face."

    show john b_6
    show sayaka a_0

    john "...What did you do now?"

    show sayaka a_16

    sayaka "What do you mean by that?"

    show john b_25

    john "You have a smile on your face, that's not a good sign."
    sayaka "Rude."

    show sayaka a_6

    sayaka "Anyways, I'm {i}so sorry{/i} Zoey, but it seems like Brad has business with you and is here in a minute to pick you up, so sadly we will have to part ways now."

    show zoey a_3
    show john b_0

    zoey "Why would Brad come here all of a sudden?"
    zoey "Why do you even know he's coming?"

    show sayaka a_12

    sayaka "Oh, he called me."

    show zoey a_7
    show sayaka a_0

    zoey "But didn't you just walk out to make a ca-"

    show zoey b_1

    zoey "Oh come on!"

    show zoey b_6

    zoey "I just want to spend time with you!"

    show sayaka a_5

    sayaka "Well, boo-hoo, life is unfair."

    show john b_6

    think "Man, it gives an entirely different take on her character if she is being nefarious and it affects yourself positively as a result..."
    think "She just doesn't give a crap about Zoey's feelings at all."

    show zoey b_5
    show john b_0

    zoey "...Fine."

    show zoey a_3 at faceright

    zoey "But I'm not giving him up to you yet."

    show john b_2

    john "Uh... Sure..."

    show zoey:
        faceleft
        ease 4 offscreenleft
    show sayaka:
        pause 2.75
        faceleft
    show john b_25

    think "I don't know if I'm supposed to be happy that Sayaka has made some random girl fall this hard for me or if I should be angry."

    show john b_17

    think "Still, confessed to her? Why on earth would she do that?"

    scene black with dissolve
    pause 1
    play sound sfx_door_open
    scene bg sadie bathroom day
    show john b_6:
        centerright
        faceright
        ypos 1.15
    show sayaka a_5:
        offscreenleft
        faceright
        ease 3 xpos 0.5
    with dissolve

    sayaka "Alright, she's finally gone."

    show sayaka a_16
    show john b_0

    sayaka "Geez was she annoying."

    show john b_6

    john "Right..."

    show john b_13

    john "About what she to-"

    show john b_0
    show sayaka a_5:
        faceleft
        ease 0.5 xpos 0.35

    sayaka "Now get your ass up and wash your face, 15 minutes have long passed. I'm gonna go fill the bathtub and figure out how to fix your hair."

    show john b_7 at faceleft

    john "Were you serious when you said you're gonna do my hair while I'm..."

    show sayaka at faceright

    sayaka "While what? While you're in the tub? You're not supposed to get your hair wet right now anyways and we're running short on time, so yes, I am serious."

    show john b_5

    john "...You don't feel embarrassed at all about doing that...?"

    show sayaka a_2

    sayaka "...About seeing myself naked?"

    show john b_4

    john "Yeah, that..."

    show sayaka a_16
    show john b_0

    sayaka "I've literally grown up with that body, why the hell would I be embarrassed looking at it?"

    show john b_4

    john "..."
    "Man, I thought she would feel just a little bit like me, but for some reason it felt... Just wrong to let her see me without any clothes on."
    "Was I just being weird? Or was the swap affecting me here too?"
    "This is weird..."

    scene black with dissolve
    pause 0.5
    outfit john casual
    outfit sayaka winter
    $ screenfilter.blur = 0
    scene bg sayaka bedroom day
    show john b_1 at left, faceleft
    show sayaka a_5 at centerleft, faceleft
    with dissolve

    john "So, we done with the dress-up?"

    show john a_1 at faceright
    show sayaka a_0

    sayaka "Yep. You finally look like me again."

    show john a_32
    show sayaka a_5

    john "Do I really need to wear contacts though? They are annoying to wear."
    sayaka "Yes, you do."

    show john a_6
    show sayaka a_16

    sayaka "As we agreed, you can wear those shitty glasses again once we're done, but you better not embarrass me in front of the other people or I'm retracting the deal!"

    show john a_13

    john "Yeah, yeah, fine by me."

    scene black with dissolve
    pause 1.5
    scene bg yui house day
    show john b_0:
        center
        faceright
        xpos 0.6
        block:
            ease 0.75 ypos 1.02
            ease 0.6 ypos 1.0
            repeat
    show sayaka a_5:
        center
        faceright
        xpos 0.8
        block:
            ease 0.85 ypos 1.02
            ease 0.65 ypos 1.0
            repeat
    with dissolve

    "After what felt like hours of being baked with what had to be ten different beauty products, I was finally deemed ready to get this thing over with."

    show john b_6

    "Sayaka had somehow arranged this unfathomably quickly and rented some really cliche karaoke room for four."

    show john a_0

    "So I assumed it was going to be a two girls two boys situation, which would feel extremely awkward since I'd {i}have{/i} to interact with us being only four."
    sayaka "And you know exactly how to act, right?"

    show john a_13

    john "Yeah yeah, girly, legs closed, laugh at jokes that aren't funny..."

    show john a_0

    sayaka "And make sure not to spill food."

    show john a_13

    john "And that."

    show john a_26

    john "Shouldn't I actually be giving you demands on how to act too?"

    show john a_6
    show sayaka a_13

    sayaka "Oh come on, anything I do would be a better option than what you would do."

    show sayaka a_6
    show john b_13

    john "Didn't you say that you got nervous around girls?"

    show sayaka a_5

    sayaka "I know how to deal with it now."

    show john a_13

    john "Actually, that reminds me, that Zoey girl mentioned something..."

    show sayaka a_2

    sayaka "Mentioned what?"
    john "Something about you confessing to her."

    show sayaka a_15 blush
    show john b_11

    "Her face went red in an instant as she looked away."

    show john b_6
    #TODO: Add blush to expression below
    show sayaka a_24 blush

    think "Could you make it more obvious that you did something stupid?"

    show john a_6

    john "Not like I'm going to complain about you somehow ending up scoring me a girlfriend or something..."

    show sayaka a_16 blush
    show john a_31

    john "Besides, she's being annoying to {i}you{/i} right now so I really have no idea what you were thinking."

    show sayaka a_4 blush

    sayaka "Shut up, okay?!"

    show sayaka a_15 blush
    show john a_13

    john "Geez, touchy subject or something?"

    show sayaka a_16 blush

    "It was probably something I would have digged further into to get my satisfaction of annoying her a bit, but with this mixer thing coming up I figured that I probably shouldn't tempt the devil."

    scene black with dissolve
    scene AN_bg karaoke bar alt
    show john b_0:
        center
        faceleft
        alpha 0.0
    show sayaka a_5:
        center
        faceright
        alpha 0.0
    with dissolve
    play sound sfx_door_open
    show john:
        pause 1
        ease 0.75 xpos 0.4 alpha 1.0
    show sayaka:
        pause 0.25
        ease 0.75 xpos 0.6 alpha 1.0

    "We arrived at the locale, which was kind of cozy looking."
    "We were just in time, with a minute to spare, but there was nobody else in sight here yet."

    scene black with dissolve
    pause 0.5
    outfit sayaka winter_tshirt
    scene AN_bg karaoke bar alt
    show john a_13:
        center
        faceleft
        xpos 0.8
        ypos 1.1
    show sayaka a_16:
        center
        faceleft
        xpos 0.6
        ypos 1.1
    with dissolve

    "Time ran with us just sitting around for five minutes. I couldn't really be bothered striking up something to talk with Sayaka about, and evidently, neither could she."

    show john b_0

    sayaka "{size=-7}Where the hell are they...{/size}"

    show john a_6
    outfit audrey casual_c
    outfit dominic casual
    show audrey a_0:
        alpha 0.0
        center
        faceright
        xpos 0.4
    show dominic a_5:
        alpha 0.0
        center
        faceright

    think "At least I know who is the more patient one of us two..."

    play sound sfx_door_open
    show sayaka a_5
    show dominic behind audrey:
        ease 0.5 alpha 1.0 xpos 0.35
    show audrey :
        pause 1
        ease 0.5 alpha 1.0 xpos 0.2

    "After ten minutes in total, two people entered the room."

    show sayaka a_0:
        ease 0.25 ypos 1.0 xpos 0.575
    show dominic a_3
    show audrey b_1
    show john b_1

    "Sayaka lit up from her grumpy mood immediately as if nothing were ever wrong and greeted them."

    show dominic a_0
    show audrey b_0

    sayaka "Hello. Great to meet both of you. Dominic and Audrey, I believe it was?"
    audrey "Hey. We're so sorry about the delay."

    show dominic a_2

    dominic "Yeah, hey, the train was delayed so we had to run our pants off, heh."

    show dominic a_0
    show sayaka a_1

    sayaka "Ah, public transport. I totally get what you went through, haha."

    show john b_6

    think "Uh... Has she ever even taken public transport?"

    show john b_0
    show sayaka a_0

    think "Don't tell me she is going to lie all throughout the day."
    sayaka "As you guys already know, my name is John, and this lady over here is Sayaka, the one I talked to you about."

    show john b_14
    show sayaka a_5 at faceright

    john "Oh, yeah, hi."
    "I waved my hand as we introduced ourselves."

    show john b_1
    show dominic b_1
    show sayaka a_0 at faceleft

    dominic "I'm Dominic, glad to meet you."

    show dominic a_0 at faceleft
    show audrey a_1

    audrey "And I'm Audrey."

    show john a_2
    show audrey a_0
    show dominic at faceright

    john "Ah, cool meeting you guys."

    show dominic b_2
    show john a_10

    dominic "Pleasure is all ours."

    show dominic a_2
    show sayaka a_8
    show john a_34

    "He smiled gently at me, but in the corner of my eye I could feel Sayaka feeling physical disgust."

    show john a_1

    "This Dominic guy seemed like a normal guy, so why she'd react like that was really beyond me."

    show john a_31

    think "But then again, this is Sayaka we are talking about."

    scene black with dissolve
    pause 3
    scene AN_bg karaoke bar alt
    show john b_13:
        center
        faceleft
        xpos 0.8
        ypos 1.1
    show sayaka a_0:
        center
        faceleft
        xpos 0.6
        ypos 1.1
    show audrey b_0:
        center
        faceright
        xpos 0.4
        ypos 1.1
    show dominic a_1 behind audrey:
        center
        faceright
        xpos 0.2
        ypos 1.1
    with Dissolve(1.0)

    "It went more smoothly than I thought it would. Sayaka was practically leading the conversation with me just nodding."

    show john b_12
    show dominic a_0

    "Oh, and the magic trick of faking a small smile or laugh when the others said something that was supposed to be funny."

    show john a_32

    "Which quickly became very tiring to do."

    show john b_0
    show sayaka a_5
    show dominic a_5
    show audrey b_9

    sayaka "Actually, I was wondering, do you guys know each other already?"

    show audrey b_0
    show dominic b_0

    dominic "Heh, you guessed right. We are actually both working under an apprenticeship as waiters."

    show dominic a_0
    show sayaka a_2

    sayaka "You can have an apprenticeship as a waiter?"

    show dominic a_2

    dominic "Yep. We both work at cafes that are practically right next to each other."

    show dominic a_0
    show sayaka a_5
    show audrey b_1

    audrey "And we've been friends since pre-school, so it was kinda funny that we ended up both wanting to do the same thing when we grow up and then even ended up in neighboring shops."

    show john b_5

    think "Huh, seems weird to me that they haven't gotten together themselves yet if they have such matching interests. They look like the perfect match."

    show audrey a_0
    show dominic
    show sayaka a_5

    sayaka "Huh, shouldn't you guys have gotten together yourselves yet if you have such matching interests? You really look like you'd be the perfect match for each other already."

    show john b_6

    think "...What, she can read minds now too?"

    show john b_0
    show audrey b_1

    audrey "Hehe, we get that a lot. But we both agreed that we would rather want to be rivals and co-workers in the future if everything goes well."

    show audrey b_0
    show dominic a_2

    dominic "And I wouldn't survive a day with Drey's famous frisbee tray flying everywhere around the house."

    show audrey b_3 at faceleft

    audrey "That has only happened three times."

    show john b_23
    show dominic a_1
    show sayaka a_16

    think "Nah, I take back everything I said before. These guys are {i}too much{/i} of a match."

    show audrey a_3
    show dominic a_0
    show sayaka a_24

    "Sayaka let out a long sigh while Audrey and Dominic were bickering and laughing over what appears to be misfortunes that happened during the job."

    show john b_0:
        transform_anchor True
        ease 0.75 rotate -5
    show sayaka a_5
    show audrey a_0

    john "{size=-5}I'm supposed to feel flustered about Dominic, right?{/size}"

    show john
    show sayaka a_33
    show dominic b_2

    "I almost thought she wouldn't answer since the banter the other two were doing was starting to cool off, but eventually she did respond."

    show sayaka a_16
    show audrey a_6
    show dominic b_5

    sayaka "{size=-5}Yes, but these guys are so basic.{/size}"

    show audrey a_1
    show dominic a_1

    john "{size=-5}Basic?{/size}"

    show dominic a_5
    show audrey b_6 at faceright
    show sayaka a_34
    show john b_11:
        ease 0.5 rotate 0

    sayaka "Aaa~~~anyhow, let's do something. I rented this karaoke room for a reason after all."

    show sayaka a_5
    show audrey b_1
    show dominic a_0

    audrey "Heh, we are going to hear you sing?"

    show audrey b_0
    show sayaka a_3

    sayaka "I'll show you what a future star sounds like, just you watch."

    scene black with dissolve
    pause 1
    accessory sayaka set shadow
    show AN_bg karaoke bar alt:
        zoom 1.5 xalign 0.75 yalign 0.8
    show john a_14:
        center
        faceleft
        xpos 0.45
    show audrey a_1:
        center
        faceleft
        xpos 0.25
    show sayaka a_21:
        transform_anchor True
        center
        faceleft
        xpos 0.65
        ypos 1.2
        rotate -5
    show dominic a_5:
        center
        faceleft
        xpos 0.8
        ypos 1.15
    with dissolve

    "The karaoke actually turned out to be quite fun."

    show john a_10
    show audrey a_0 at faceright

    "I hadn't considered singing with Sayaka's voice before, but it was actually... Really good."

    show john b_0 at faceright
    show dominic a_6
    show sayaka a_24

    "Well, her on the other hand..."

    show sayaka a_21

    sayaka "{size=-8}I can't sing... This body can't sing...{/size}"

    show john a_31
    show sayaka a_24
    show dominic a_2
    show audrey b_6

    "I felt just a tiny bit bad for apparently robbing her of her talent to hit notes, since I knew that I was terrible at it with my actual body."
    "Turns out that the talent of being terrible at singing carries over when you swap with someone."

    show john b_6

    think "But isn't she is having just a bit too much of an existential crisis right now?"

    accessory sayaka set
    show dominic a_0
    show audrey b_0
    show john b_0
    show sayaka a_5:
        faceright
        ease 0.5 rotate 0 ypos 1.15 xpos 0.6

    dominic "You know, I'd pay a pretty penny if you were a performer at a party or something."

    show audrey a_1
    show john at faceleft
    show sayaka at faceleft

    audrey "U-huh!"

    show john b_12
    show audrey a_0

    john "Heh, well, maybe it's a possibility for the future."

    show john b_0
    show audrey b_0
    show sayaka a_33

    audrey "Hey, hey, can I do this one with you as well?"
    "She pointed towards some song I knew. {q}Don't start unbelieving{/q}."

    show john a_24

    think "What a classic."

    show dominic a_2
    show sayaka a_5 at faceright
    show john b_0
    show audrey b_9

    dominic "We're in for a treat now."

    show dominic a_0

    dominic "You know, Audrey actually performs on stage sometimes."

    show sayaka at faceleft
    show john b_12:
        pause 1
        faceleft

    john "What? Really? That's amazing!"

    show john b_1
    show audrey b_7 blush

    audrey "Don't up-play me like that Dom, I only experimented a little once or twice doing it."

    show john b_0 at faceright
    show sayaka at faceright
    show audrey b_4 blush
    show dominic b_2

    dominic "I could invite you to the next time she does her gig if you're up for it."

    show john b_2
    show sayaka a_33

    john "Heh, uh... Maybe."

    show john b_5
    show sayaka a_5 at faceleft
    show audrey a_0 blush:
        faceleft
        ease 1.0 ypos 1.05 xpos 0.2

    think "Crap, is this guy already asking me out for another event?!"
    think "How do I even turn him down? I don't want to go out with a dude!"

    show john b_0 at faceleft
    show audrey a_1:
        pause 1
        faceright
        ease 0.5 ypos 1.0 xpos 0.25
    play sound sfx_device

    "While I had a mild internal panic attack, Audrey turned on the track which brought me back to reality just a bit."

    show john b_4

    think "I probably have to tell him I don't want to meet him again at some point, right?"
    think "But I need to say it in some sort of gentle way to not hurt him..."

    show john b_19

    think "ARGH! Why am I thinking about this like that?!"

    show john b_11:
        pause 1
        faceright
    show audrey b_0
    show sayaka a_16

    sayaka "What, not gonna sing with your beautiful and talented voice...?"

    show john at faceleft

    think "Oh, right, the song."
    "But the way Sayaka said that to me was the most monotone way possible."

    show john b_6

    "She clearly had nothing but spite and jealousy towards me for stealing her spotlight."

    show john b_23

    think "Sorry, heh."

    scene black with dissolve
    pause 0.5
    show AN_bg karaoke hallway day:
        zoom 1.5 xalign 0.7 yalign 0.8
    show john b_0 at center, faceright
    show sayaka a_16 at centerright, faceright
    with dissolve

    "Me and Sayaka had excused ourselves out of the room under the pretense to go get something to drink."
    "Mostly because Sayaka heavily insisted on us doing that for them."
    "But I can imagine that her thirst wasn't the reason for wanting to go out of the room for a minute."

    show sayaka a_7
    show john b_11

    sayaka "Those guys are so fucking lame!"

    show sayaka a_16
    show john b_0

    john "What? Why?"

    show sayaka a_7 at faceleft
    show john b_13

    sayaka "Don't you see it? They are clearly already buddy-buddy with each other and are just finding excuses not to fuck already because they are too scared about what the other one would say!"

    show sayaka a_25

    sayaka "This entire thing is so freaking pointless, how am I supposed to get turned on by someone who is already in the pants of someone else?!"

    show sayaka a_16
    show john b_3

    john "Whoah, whoah, calm down."

    show john a_13

    john "They might hear you, you know..."

    show sayaka at faceright

    sayaka "Urgh, I spent money on this for nothing."

    show john a_30

    john "So... You don't think Audrey is attractive or something?"

    show sayaka a_7

    sayaka "I mean, sure, she's cute and would probably make for a great girlfr-"

    show sayaka a_20
    show john b_11

    sayaka "Oooh fuck no what am I saying?!"

    show sayaka a_7 at faceleft

    sayaka "She's average!"

    show sayaka a_16
    show john b_6

    john "{i}Sigh...{/i} Okay, so you're having another one of your anger fits."

    show sayaka a_7
    show john b_11

    sayaka "It's not-"

    show sayaka a_25 at faceright

    sayaka "Argh! Fine!"

    show john a_6
    show sayaka a_16

    john "...What's fine?"

    show sayaka at faceleft

    sayaka "That I'm pissed! I get it, I was supposed to figure out if I turned lesbian and obviously I am!"

    show john a_0

    sayaka "But what about you? You think that joke of a man is worth anything?"

    show john b_0

    john "Uhm... Well..."

    show john a_4

    think "I guess I looked at him in a bit of a different light...?"
    think "I mean, if he asked me out on a date while I was still a guy then I'd still try to politely tell him something like {q}Whoah, back off{/q} in order to not hurt his feelings too much..."

    show john a_13

    john "It's... Uh... Kind of complicated I think."

    show sayaka a_5

    sayaka "What about the girl? You seemed all giddy-giddy being able to sing with her without holding back."
    sayaka "No perv thoughts at all?"

    show john b_13

    john "I guess not...?"

    show sayaka a_8

    sayaka "You didn't even notice how you managed to ram her tits a couple times while you were so caught up in using {i}my voice{/i} for your own fun?"

    show john a_8 blush

    john "Wait, I did?!"

    show john b_27 blush

    think "Hell, I didn't even notice that. I just went with the flow, Audrey was pretty much a natural born performer which I tried to mirror for fun."

    show john a_0 blush
    show sayaka a_33

    sayaka "I really hope for your own sake that you aren't naturally gay."

    show john b_18

    john "I didn't do that on purpose!"

    show john b_4
    show sayaka a_5

    john "And I'm sorry that I suck at singing..."

    show sayaka at faceright

    sayaka "You better be."

    scene black with dissolve
    scene AN_bg karaoke bar alt
    show sayaka a_34:
        faceleft
        alpha 0.0
        center
        xpos 0.7
        pause 0.75
        ease 0.75 xpos 0.6 alpha 1.0
    show john b_11:
        faceleft
        alpha 0.0
        center
        xpos 0.9
        pause 0.75
        ease 0.75 xpos 0.8 alpha 1.0
    show dominic a_0:
        faceleft
        center
        xpos 0.35
        pause 0.5
        faceright
    show audrey a_0:
        faceleft
        center
        xpos 0.15
        pause 0.75
        faceright
    with dissolve
    play sound sfx_door_open

    "We brought the refreshments to the other two and ended up staying for another hour or so before finally deciding to end the day there."

    scene black with dissolve
    outfit sayaka winter
    outfit audrey casual
    scene bg city walkway day
    show sayaka a_12:
        center
        xpos 0.5
        faceright
    show john b_14 behind sayaka:
        center
        xpos 0.3
        faceright
    show dominic a_2:
        center
        xpos 0.7
        faceleft
    show audrey a_1:
        center
        xpos 0.85
        faceleft
    with dissolve
    show dominic a_0:
        pause 0.5
        faceright
        ease 2 alpha 0.0 xpos 1.2
    show audrey a_0:
        pause 0.4
        faceright
        ease 2 alpha 0.0 xpos 1.35

    "About three and a half hours had passed with them, and I had both their numbers registered on my phone now."

    show john b_1
    show sayaka a_33

    "This entire thing actually went completely different to what my expectations were. I thought this would have been some kind of date where we'd end up kissing or some crap, but it was actually pretty enjoyable."

    show john b_0

    "Well, for one of us at least."

    show sayaka a_5

    john "You're still angry about today?"

    show sayaka a_16 at faceleft
    show john b_11

    sayaka "Oh no, John, I am actually so freaking happy right now. You ended up having loads of fun hanging out with that bitch while I was stuck talking with the other guy about how he tuned his motorbike."

    show sayaka a_5

    sayaka "Just a splendid time."

    show john a_6

    john "...I'll take that as a yes."

    show sayaka a_16 at faceright
    show john a_0

    sayaka "{i}Sigh...{/i} It's just frustrating..."

    show john a_4

    john "..."

    show sayaka a_5 at faceleft
    show john a_10

    john "You... Uh, want to stay a bit longer at your own house? Your parents probably won't be home until ten or so as usual."
    sayaka "It's fine. Your mom was going to make me pancakes today."

    show john a_18

    john "Oh, right..."

    show john a_4

    think "Man, what would I give to get a good meal like yesterday again for dinner..."

    show john b_0
    show sayaka a_2

    think "Which reminds me, I should probably go and stock up on ingredients."

    show john b_14

    "In that moment I decided that I would be making pancakes myself today."

    scene black with dissolve
    pause 0.5
    scene bg neighborhood3 day
    show john b_0 at center, faceleft
    show sayaka a_5:
        centerleft
        faceleft
        pause 1
        faceright
    with dissolve
    pause 0.5

    john "Well, see you tomorrow then."
    sayaka "Yeah yeah."
    sayaka "And don't forget to read the links to those stories I sent you."

    show john b_14

    john "Will do."

    show sayaka:
        faceleft
        ease 4 offscreenleft
    show john b_13

    "She went her own way without looking back, but did wave a hand in the air briefly when we got to the crossing where the roads home forked."

    show john b_1

    think "Huh, she even said {q}see you{/q} in her own roundabout way."
    "Today really was weird. Sayaka seemed to tolerate me at the end there. A real world first."
    john "Hm, maybe things are starting to look better between us, somehow."

    scene black with Dissolve(2.0)
    pause 1

    title "23rd of August (Tuesday)" "Day 16 - Cornelia and Kiyoshi (side story)"

    show bg lunch:
        zoom 2.0 xalign 0.2 yalign 0.5
    show cornelia a_5:
        centerright
        faceleft
        ypos 1.1
    show kiyoshi a_1:
        centerleft
        faceright
        ypos 1.1
    with dissolve
    pause 2

    cornelia "..."

    show cornelia b_6
    show kiyoshi a_0

    cornelia "...They aren't coming, are they?"

    show kiyoshi a_2
    show cornelia b_24

    kiyoshi "Ah, it would appear so."

    show cornelia a_0
    show kiyoshi a_1

    cornelia "...What is Sayaka even doing right now? I know that John is doing that stupid {q}future plans interview{/q} or whatever they call it, but you guys have to do that tomorrow, not today."

    show kiyoshi a_7

    kiyoshi "You must know that this interview can determine your future. After all, this is where you tell your teacher and education supervisor what you would like to do when you get older."

    show kiyoshi a_1
    show cornelia a_19

    cornelia "...Yeah, I kind of know what they do, I just opted not to spend 20 seconds explaining it."

    show cornelia b_24

    cornelia "I've already been in there, but thanks for explaining something I already knew."

    show cornelia b_0
    show kiyoshi a_9

    kiyoshi "Oh. And my sweet Sayaka was going to try out my swapping theory of using the school computers I believe."

    show kiyoshi a_0
    show cornelia b_5

    cornelia "...Computers? How does that make sense?"

    show kiyoshi a_6

    kiyoshi "You see, in the recent piece of {i}modern literature{/i} I read, the two heroes trade bodies when their personal computer files are traded around."

    show kiyoshi a_1
    show cornelia a_11

    kiyoshi "I suggested that perhaps the school has the neural network of each student downloaded with high-tech alien technology, and currently she is researching whether we should continue the pursuit of this theory."

    show cornelia a_15

    cornelia "...What?"

    show kiyoshi a_8
    show cornelia a_11

    kiyoshi "Nevermind, some theories require you to have an excellent skill in thinking to grasp."

    show cornelia a_14
    show kiyoshi a_0

    cornelia "Are you saying I'm not smart enough to understand you?"

    show kiyoshi a_5

    kiyoshi "Uh... No...?"

    show cornelia b_17 at faceright

    cornelia "...Hmph, you better not get used to talking to me like that."

    show kiyoshi a_0
    show cornelia b_18
    pause 2
    show cornelia b_4

    "..."

    show cornelia b_9

    cornelia "...Man, this is boring."

    show kiyoshi a_4

    cornelia "I wish I could sit with some other girls..."

    show kiyoshi a_7
    show cornelia a_11

    kiyoshi "Indeed, if I were to be accompanied at a table with a girl, I would at least expect someone of a higher standar-"

    show cornelia b_3:
        faceleft
        ease 0.25 xpos 0.55
    with hpunch
    show kiyoshi a_5

    cornelia "There! You did it again! You're saying I look terrible!"

    show kiyoshi a_11
    show cornelia b_14

    kiyoshi "What? Not at all, I am just saying that your features are, uh... Inadequate for my tastes."

    show cornelia b_17
    show kiyoshi a_4

    cornelia "Is there really {i}nothing{/i} about me you even find slightly attractive?!"

    show cornelia b_14
    show kiyoshi a_9

    kiyoshi "Well, I would need to think about it before I could give a definite answer."

    show cornelia b_3
    show mina b_3:
        alpha 0.0
        center
        faceright
        xpos 0.8
        ypos 1.25
    show gabriel a_4:
        alpha 0.0
        center
        faceleft
        xpos 1.0
        ypos 1.25

    cornelia "You can't even think of anything from the top of your head?! Seriously?!"

    show bg lunch:
        ease 0.75 xalign 0.5 yalign 0.65
    show cornelia:
        faceright
        ease 0.5 alpha 0.0 xpos 0.35 ypos 1.0
    show kiyoshi:
        ease 0.5 alpha 0.0 xpos 0.1 ypos 1.0
    show mina:
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.6 ypos 1.1
    show gabriel:
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.8 ypos 1.1

    cornelia "What about that girl over there? She is small like me too! Tell me you don't find her attractive either!"

    #SKIP
    show mina:
        alpha 1.0
        xpos 0.6
        ypos 1.1
    show gabriel:
        alpha 1.0
        xpos 0.8
        ypos 1.1

    hide cornelia
    hide kiyoshi
    show mina b_0
    show gabriel a_16

    kiyoshi "Oh, Mina. Yes, she is quite the girl. She may be small, but her personality is one that others should strive to imitate. And her assets are quite in order as well."

    show gabriel a_0

    cornelia "What?! You're even saying my personality is shit!"

    show mina b_1
    show gabriel a_3

    kiyoshi "Oh, uh, not at all. I would definitely say that it is... Unique...?"

    show gabriel a_5:
        faceright
        ease 2 xpos 1.2 alpha 0.0
    show mina b_3

    cornelia "Unique?"

    outfit zoey uniform
    show mina a_0
    hide gabriel
    show zoey a_1:
        alpha 0.0
        center
        faceright
        xpos 1.0
        ypos 1.15
    show mel b_0:
        alpha 0.0
        center
        faceleft
        xpos 1.2
        ypos 1.15

    cornelia "That's seriously the best you can think of?!"

    show bg lunch:
        ease 0.75 xalign 0.8 yalign 0.8
    show mina:
        ease 0.5 xpos 0.5 ypos 1.0 alpha 0.0
    show zoey:
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.7 ypos 1.0
    show mel:
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.9 ypos 1.0

    cornelia "What about her? That girl that's always after Sayaka. She is annoying and even smaller than me."

    hide mina
    show zoey a_0
    show mel a_2

    kiyoshi "Well..."
    cornelia "{q}Well{/q} what?"

    show mel a_0

    kiyoshi "There is a certain charm to her. I cannot describe it. I believe that if Sayaka hadn't tried her luck, I would have tried it myself."
    kiyoshi "Having a girl try to fight for your affection all the time seems like something that happens to an antagonist of an epic story."

    show bg lunch:
        zoom 2.0 xalign 0.2 yalign 0.5
    show cornelia b_17:
        center
        faceleft
        xpos 0.55
    show kiyoshi a_0 at centerleft, faceright
    hide zoey
    hide mel
    with dissolve
    cornelia "For real? Even her?"

    show cornelia b_14
    show kiyoshi a_2

    kiyoshi "She would still be a second pick if uh... That helps."

    show kiyoshi a_1
    show cornelia b_4:
        faceright
        ease 0.5 xpos 0.6
    outfit john uniform_pony_pants
    accessory john set glasses
    show john b_19:
        alpha 0.0
        center
        faceleft
        xpos 0.95

    cornelia "...Seriously, weren't you supposed to get advice from Saya on how to treat girls..."

    show kiyoshi a_0
    show cornelia b_0
    show john:
        ease 0.5 alpha 1.0 xpos 0.8

    john "{i}Hah... Hah... Hah...{/i} Sayaka!"

    show john b_22
    show cornelia b_11

    cornelia "Huh? John? Why are you out of breath?"

    show john b_19

    john "Where the hell is Sayaka?!"

    show cornelia a_5
    show john b_17

    cornelia "What happened? Weren't you supposed to be doing that interview right now?"

    show john b_18

    john "Yes!"
    john "And she filled out her own form for it and everything. But!"

    show cornelia a_0
    show john b_28

    john "What the hell does she mean with {i}{q}I want to be the loving wife of a billionaire in the future{/q}{/i}?!"

    scene black with Dissolve(1.0)
    pause 0.5

    title "24th of August (Wednesday)" "Day 17 - John"

    pause 1
    outfit anuja uniform
    scene bg classroom 2
    show cornelia b_24:
        center
        faceright
        xpos 0.3
    show john b_11:
        center
        faceright
        xpos 0.15
    show katrina a_9:
        center
        faceleft
        xpos 0.6
    show kyoko a_0:
        center
        faceleft
        xpos 0.75
    show anuja a_11:
        center
        faceleft
        xpos 0.9
    with Dissolve(1.0)
    pause 1

    think "Wha-"
    "For some reason, Kat, Kyoko and Anuja were here before I could get out of my classroom."

    show cornelia b_23

    cornelia "What do {i}you{/i} want?"

    show cornelia b_5
    show katrina a_18
    show john b_0

    katrina "Buzz off. I need to talk with her in private."

    show john b_11
    show katrina a_4

    john "Me?"

    show john b_13

    katrina "Yes, you."

    show cornelia b_17

    cornelia "Hell no you aren't-"

    show john a_10
    show cornelia b_0 at faceleft
    show katrina a_18

    john "Hey, Cornelia, it's okay."

    show cornelia a_4

    john "Just you and me?"

    show katrina a_4

    katrina "Yes."

    show john a_14

    john "Fine."

    show john a_10

    "I was hoping for the day where they would finally try to talk with me again. I expected they would come around sooner than this, but better late than never."

    show john a_13
    show cornelia b_0

    john "And {i}don't{/i} start any quarrels with the other two while I'm gone, got it?"

    show cornelia b_24 at faceright

    cornelia "Tch, fine."

    show john a_0

    "Kat looked at me with serious eyes all the time."

    scene black with dissolve
    pause 0.5
    play sound sfx_sliding_door_open
    pause 0.5
    scene bg school classroom hallway day
    show john b_13:
        center
        alpha 0.0
        xpos 0.45
        faceright
        pause 0.5
        ease 0.75 alpha 1.0 xpos 0.55
    show katrina b_7:
        center
        alpha 0.0
        xpos 0.6
        faceright
        pause 0.35
        ease 0.75 alpha 1.0 xpos 0.8
    with dissolve

    "We eventually got to a corner where nobody else was around."

    #SKIP
    show katrina:
        xpos 0.8
        alpha 1.0
    show john:
        xpos 0.55
        alpha 1.0

    "I was honestly interested in hearing what she wanted to talk with me about. Ideally, she'd finally believe me about the swap."

    show john b_14

    john "This looks private enough."

    show john b_0
    show katrina b_2

    john "..."

    show john b_11

    john "Do you, uh... Believe what I said now?"

    show katrina a_2 at faceleft

    katrina "..."

    show katrina a_12

    katrina "John has been doing some screwed up stuff lately, you know that, right?"

    show katrina a_4
    show john b_4

    john "So you still don't believe me..."

    show john b_0
    show katrina a_12

    katrina "Stuff that I know he wouldn't have done."

    show katrina a_17
    show john b_11

    katrina "I know that he liked his hair the way it was, and that he never really was into all of that love-life crap."
    katrina "So to see him suddenly {q}confess{/q} to Emily and that new girl on the same day makes me incredibly sus."

    show katrina a_18
    show john a_14

    john "Ah, ye-{nw}"

    show john b_19

    extend " She did what?!"

    show john b_27
    show katrina a_23

    katrina "None of this is something he would have done."

    show katrina a_12

    katrina "At the same time, you suddenly dress up like a total geek, have the worst hair-do since middle-school and act all nice towards your pathetic group of posh-ups."

    show john b_0
    show katrina b_7

    katrina "So, without any tricks, are you for real the actual John who looks like this bitch right now?"

    show john a_2
    show katrina b_13

    john "Finally, you get it. Yes!"

    show john a_14

    "While I was hoping for her to be a bit more energetic about this, she instead looked kind of sad."

    show john a_0

    "Did I say something wrong now all of a sudden? Was I not supposed to be happy that she finally came around to it?"

    show katrina a_4

    katrina "Just... How did this happen then? Kiyoshi has been spamming us with texts about what he is doing and what happened, but..."

    show john a_4

    john "Well that's the thing, none of us know what happened. It just... Suddenly happened overnight."

    show katrina a_2

    katrina "But why her?"

    show john a_30

    john "I really don't know..."

    pause 1
    show katrina a_6 at faceright

    katrina "{size=-5}Why her...{/size}"

    show john b_4

    john "It's... Sorry, but I didn't have a say in that..."

    show katrina a_7

    "I knew Kat hated Sayaka with an absolute burning passion."
    "Their background was still a mystery to me since they seemed to be close as kids, but Cornelia said I was better off not knowing about this."

    show john b_13

    think "Maybe now I can ask though..."

    show katrina a_14 at faceleft
    show john b_12

    john "Hey, would you mind if I asked what happened between you and her when you were kids?"

    show katrina a_11 blush
    show john b_0

    "Her sad face turned bright all of a sudden."

    show katrina b_9 blush at faceright

    katrina "I would very much mind."

    show john b_11

    john "...Uhm... Why?"

    show katrina a_14 at faceleft

    katrina "Because, Sayaka. That's why."

    show katrina a_2

    katrina "-I -I mean, John. Sorry."

    show john b_4

    "For some reason her voice trembled with embarrassment. So something must have happened that neither Sayaka nor Kat would want me to know."

    show john b_6

    think "{i}Sigh...{/i} Honestly, these guys."

    show john b_5
    show katrina a_14

    john "Then, if you don't mind me asking, do you hang out with Anuja a lot now? I saw that she was with you, and I think I've seen you talk occasionally a lot as well..."

    show katrina a_15

    katrina "It's, uh... It's because of Michelle..."

    show john b_0

    think "Michelle...? Wasn't there a rumor about her at some point?"
    john "Did something happen to her?"

    show katrina b_6

    katrina "{i}Sigh...{/i} Well for one, she's gone insane..."

    show john a_30

    john "Insane? What happened to her?"

    show john a_0
    show katrina a_4

    katrina "Don't you dare tell this to someone else. I'm trusting that you're the real John I know on this."

    show john a_14
    show katrina a_14

    john "Your trust is well placed then."

    show katrina a_2
    show john a_10

    katrina "...One day when she woke up, Anuja found her rolling on the ground with her entire room completely destroyed."

    show john a_30

    katrina "Everything had been thrown around, and everyone says Michelle herself did it, almost as if possessed by some kind of demon."

    show john a_8

    john "...Wha..."

    show john a_30
    show katrina a_21

    katrina "It was so bad that her fingernails were almost entirely ripped off, and... There was blood everywhere on her hands and face when they found her..."

    show katrina a_2
    show john a_27

    john "...Holy shit..."

    show katrina b_4

    katrina "I've heard about it from Anuja and Michelle's parents. Anuja said that when she first saw Michelle like that, Michelle was mumbling as if talking another language entirely..."
    katrina "It freaked Anuja completely to the point where she now has nightmares about it..."

    show katrina b_8

    katrina "And, uh... Well, Anuja now lives with my family for the time being after that."

    show katrina b_9
    show john b_27

    john "..."

    show john b_26

    "What the actual fuck?"

    show john b_27

    "Michelle always seemed like a stable role-student who was organized and had everything in order..."
    "Just how would it ever make sense that she'd just wake up one night and suddenly go mental like that..."

    show john b_4

    "I could only shudder thinking about it."

    show john b_11
    show katrina a_23

    john "Is she okay?"

    show katrina a_2

    katrina "She's supposedly still in the hospital. I haven't heard from her since then. Not even Anuja knows anything."

    show john a_4

    john "...Shit, I'm so sorry to hear that. You two were close friends even though I never really talked to her, right?"

    show katrina a_23

    katrina "..."

    show katrina a_2
    show john a_0

    katrina "It's... Been a tough couple of weeks lately. And I'm sorry I... Didn't believe you at first when you said you were John."

    show john a_10

    john "Hey, I don't blame you at all if that happened without my knowing."

    show john a_14
    show katrina a_23

    john "Besides, the people we've told were all really skeptical about it as well, except for Kiyoshi."

    show john a_10
    show katrina a_16

    katrina "Thanks, but..."

    show john a_0
    show katrina a_5

    "She looked at me for a brief moment in consideration."

    show katrina a_15

    katrina "I'm sorry, I just can't..."

    show katrina b_7

    katrina "You look exactly like her, sound like her, smell like her..."

    show katrina b_11 at faceright

    katrina "{size=-5}...The guy I liked more than anything turned into the girl I hate more than anything...{/size}"

    show john a_5

    "It was a mumble, but I could still hear her clearly."

    show john b_0
    show katrina a_23 at faceleft

    "It came over me that she just said she liked me, probably more than a friend."

    show john b_4

    "But... It just felt kind of... Empty to me for some reason?"

    show john b_2

    john "Is that so... I, uh... Thanks, I guess..."

    show john b_13
    show katrina a_2

    katrina "{size=-8}You guess, huh...{/size}"
    katrina "I don't have any ill will against you, or hate you John..."

    show katrina a_14

    katrina "But I just cannot look at you right now and not hate you."

    show katrina b_2

    katrina "We are still friends, but..."

    show katrina b_3

    katrina "I wanted to tell you that. It's selfish of me to say this, but when you go back to being yourself, please tell me as soon as possible."

    show katrina a_15
    show john b_22

    katrina "But until then, I..."
    "..."
    john "Oh..."

    show john b_17

    think "What is wrong with me?! A girl, Kat of all people, is probably pouring out her heart for me right now, and all I am thinking of is just passive thoughts!"
    "{q}Ah, so that's how it is.{/q}"
    "{q}That's a bummer.{/q}"

    show john b_18

    think "How are any of these thoughts even acceptable in this situation? Is this body really affecting me so much that I feel nothing but apathy for her feelings?"

    show john b_9

    think "Come on, head! Feel sympathy!"

    show katrina b_7
    show john b_13

    katrina "Sorry."

    show katrina a_6:
        pause 1.5
        ease 4 offscreenleft alpha 0.0
    show john:
        pause 2.5
        faceleft

    "She waited a few seconds before walking away."
    "I didn't have a response. I wasn't extremely torn about it. Everything was a mess."

    show john b_4 at faceleft
    show kyoko a_12:
        centerleft
        faceright
        xpos 0.2
        alpha 0.0

    "It was sad, and a tear of regret not being able to respond to her feelings did roll down my cheek, but I didn't know if that was the {q}old me{/q} somehow weeping or not."

    show kyoko:
        ease 0.5 xpos 0.3 alpha 1.0

    kyoko "Are you okay?"

    show john b_11

    john "Huh? Oh, Kyoko."

    show john b_13

    kyoko "I just wanted to make sure you are okay. If Kat and Kiyoshi both believe it's you, then I do too, John."

    show john b_20

    john "Heh, thanks."

    show john b_1

    john "I'm guessing you want to stay with Kat."

    show kyoko a_4

    kyoko "You already know then."

    show kyoko b_8

    kyoko "Yes, she's going through a lot right now, so I think it is best if I stay by her side."

    show john b_20

    john "Makes sense..."

    show kyoko b_3

    kyoko "..."

    show kyoko a_6
    show john b_0

    kyoko "You know, if it really is you, I still consider you as one of my best friends, if that worries you."
    kyoko "Kiyoshi has been texting us a lot about finding a solution to revert this swap of personality that you and Sayaka have experienced, and I'll try giving it a shot to figure out what happened as well."

    show kyoko a_13

    kyoko "If I find or need anything, I will let Kiyoshi know. And I hope everything goes well between you and Sayaka."

    show kyoko a_10
    show john b_14

    john "...Thanks. It helps knowing you're supporting me through this."

    show john b_1
    show kyoko a_1

    kyoko "Heh, don't mention it."

    show kyoko a_10

    kyoko "I'm going to have to run now, we're still in school after all. I'll catch you later at some point."

    show john a_10

    john "Ah, yeah. I hope we can talk more later."

    show kyoko a_8

    kyoko "Me too. Good luck."

    show kyoko a_1:
        pause 1.5
        faceleft
        ease 0.75 alpha 0.0 xpos 0.15
    show john b_1

    "She gave me a really heartwarming smile before leaving."
    think "She knew exactly what Kat would be telling me, didn't she?"

    show john b_14

    "At least I wouldn't go from this spot with nothing but depressing thoughts in my mind. Knowing Kyoko was fine with our situation was a great boost in confidence."

    show john a_1

    think "After all, if someone knows something about mysteries, it's Kyoko."

    show john a_13

    think "Well, Kiyoshi does as well, but his methods are a bit more unorthodox."

    scene black with dissolve
    scene bg school hallway day
    show cornelia b_24 at centerleft, faceright
    show john b_13:
        center
        faceleft
        xpos 0.75
        alpha 0.0
        pause 0.75
        ease 0.75 alpha 1.0 xpos 0.6
    with dissolve
    pause 1
    show cornelia b_6

    cornelia "Finally."

    show cornelia b_24
    show john b_2

    john "Sorry to make you wait. I hope you didn't start anything back here."

    show john b_1
    show cornelia a_5

    cornelia "Of course not. I do have self restraint after all."
    cornelia "But what were you talking about?"

    show john b_12

    john "Just... It's, uh... Private..."

    show john b_13
    show cornelia b_6 at faceleft

    cornelia "Tch, fine. Keep your secrets then."

    scene black with Dissolve(1.0)
    pause 1.5

    title "25th of August (Thursday)" "Day 18 - John"

    outfit john formal_pony
    show bg sayaka livingroom day:
        zoom 2.0 xalign 0.2 yalign 0.5
    show john b_25:
        center
        faceright
        xpos 0.2
        ypos 1.15
    show cornelia b_0:
        centerright
        faceright
    with dissolve
    pause 1

    "So, this supposed party Sayaka was throwing every month without me knowing about it was starting to creep up."

    show john b_0

    "As a result, I ended up bringing Cornelia and Sayaka along with me home."

    show cornelia a_0 at faceleft
    show john a_0 at faceleft

    sayaka "{size=-5}Corny, we need to check the lights in the kitchen.{/size}"

    show cornelia b_2:
        ease 3 offscreenleft
    show john b_25

    cornelia "Coming!"
    "And now they were rushing around the house to check things."

    show john b_23 at faceright

    "You could consider it as a different kind of entertainment. Sayaka had completely forgotten I existed, which made it possible for me to munch on popcorn in the living room while watching TV."
    "I was still feeling a bit melancholic after the talk I had with Kat yesterday, but I felt a bit better after me and Kyoko texted each other about what had been happening on both sides of our friend group."

    show john b_25

    "It was one thing I had thought about a lot recently. I had become way too emotional after swapping with Sayaka, which had to be another side-effect like the liking guys thing."
    "The confrontations with Kat made that obvious."

    show john b_11 at faceleft

    sayaka "{size=-5}The lights are working fine, right?{/size}"

    show john b_6

    cornelia "{size=-5}Uhm... All good, all lights work.{/size}"
    think "But really, they're even checking if all of the 20 small light bulbs in the kitchen work...?"

    show john a_6

    think "And yeah, I checked, there are exactly 20 light bulbs in the kitchen."
    think "Don't blame me, this place is {i}that{/i} boring."

    show john b_23 at faceright

    "But after all, the only response to the situation that came to mind was {q}Ah well{/q} after I dropped another two or three popcorn down into my mouth."

    scene black with dissolve
    outfit sayaka uniform
    scene bg sayaka kitchen day
    show sayaka a_5:
        center
        faceright
        xpos 0.2
    show john b_25:
        center
        faceleft
        xpos 0.45
    with dissolve

    "The peace didn't last long though. Sayaka wanted to check if every formal thing was in check."
    "I had busted my ass off doing what she told me, making sure her parents knew that she was throwing the party (and of course getting permission for it), and all other stuff like alcohol, snacks, you name it."
    sayaka "And you've notified the neighbors?"
    john "Check."
    sayaka "Made sure the pool is getting cleaned tomorrow?"
    john "Check."
    sayaka "And... You've notified Marty about the snacks?"

    show john b_6

    john "Cheee~~~eck."
    "It went on and on."

    scene black with dissolve
    scene bg sayaka livingroom dusk
    show john b_5 at center, faceright
    show sayaka a_5:
        centerright
        faceright
        xpos 0.8
    with dissolve

    "They stayed for a long time. Every little nook was checked, as if fanatic that everything would be perfect."
    "And to that end, I just had to ask."

    show sayaka a_2

    john "Hey, is this really just a regular party?"

    show sayaka a_5 at faceleft

    sayaka "What do you mean?"

    show john b_6

    john "I mean, you are really making a huge deal out of this. Will it really matter if you've made sure there isn't a single speck of dust behind the refrigerator?"

    show john b_11
    show sayaka a_16

    sayaka "Really? You still haven't noticed?"
    john "...Noticed what?"
    sayaka "That this is my last chance of redeeming myself as a public figure?"

    show john b_13

    john "...Public figure?"

    show sayaka a_24

    sayaka "Oh my god, you are just so dense..."

    show sayaka a_7

    sayaka "You've ruined me over these last three weeks. This is my last chance to make sure I'm not perceived as some sort of boring librarian the way you're making me look right now."

    show sayaka a_16
    show john b_17

    sayaka "Unlike you, I actually believe we can swap back. I bet you're having the time of your life as me, so you don't worry too much about the bigger picture as always, but some of us want to right what's wrong."

    show john b_18

    john "Wait, hold up. Don't start thinking I don't want to swap back either here, I've already made it perfectly clear several times that your life sucks."

    show john b_17
    show sayaka a_7

    sayaka "Well if it sucks so much then why are you spending your useless brain power on video games if you've managed to hack your way into my computer and phone, huh?"

    show john b_19
    show sayaka a_16

    john "Those are {i}essentials{/i} in our current day and age! If I didn't forcibly break open the locks to your devices then I'd have to buy new ones entirely!"

    show john b_17
    show sayaka a_7

    sayaka "That's not the point! You are breaching my privacy by having access to my files!"

    show sayaka a_16
    show john b_28

    john "Oh my god, can you please, for the love of god, shut up about our privacy?!"

    show john b_19
    show sayaka a_21

    john "In case you haven't noticed, right now, that computer and that phone are both {i}my{/i} property, and I-"

    show sayaka a_20:
        ease 0.25 xpos 0.7
    show john b_27

    sayaka "Don't you dare say another word about property, as if you know who it belongs to!"

    show sayaka a_16
    show john b_18

    john "You sure as hell believed that my life was your property when you tried to kill my relationship with Kat!"

    show sayaka a_7
    show john b_17

    sayaka "That bitch had it coming!"

    show john b_19
    show sayaka a_16

    john "Fuck no she didn't! She's been going through hell and you only made it worse! I can only say that it's pure luck she's even wanted to talk to me recently!"

    show sayaka a_15
    show john b_17

    sayaka "What?! You're talking with Katrina?!"

    show john a_33
    show cornelia a_14:
        alpha 0.0
        center
        faceright
        xpos 0.05

    john "As if it concerns a self-centered douchebag like you who I talk to-"

    show sayaka a_20
    show john a_27
    show cornelia:
        ease 0.75 alpha 1.0 xpos 0.15

    sayaka "You are {b}not{/b} talking to her while we are swapped! Do you fucking understand?!"

    show cornelia a_3
    show sayaka a_21

    cornelia "What the hell is going on in here?"

    show john b_19
    show cornelia a_6

    john "It's none of your business Sayaka! Absolutely, none of your business."

    show sayaka a_20
    show john b_17

    sayaka "You piece of fucking shit! I knew it, the moment I started to trust you just a little bit, you begin backstabbing me just like her!"

    show sayaka a_21
    show john a_16
    show cornelia b_6

    john "You call this a display of trust? Don't make me laugh, you'e been commanding me around like I'm your stupid puppy or something!"

    show cornelia b_3
    show john a_17 at faceleft
    show sayaka a_15

    cornelia "{size=+5}{b}{i}HEY! Both of you, stop it!{/i}{/b}{/size}"

    pause 1.5
    show sayaka a_16
    show cornelia b_17

    john "...If you want to stop anyone, then stop her! I am tired of her constant whining about how I am misusing {i}my own{/i} life."

    show sayaka a_7
    show john a_6

    sayaka "This isn't your life! It's {i}{b}my{/b}{/i} life!"

    show cornelia b_3
    show john a_0
    show sayaka a_5

    cornelia "That's it! Both of you! I've had enough of your constant fighting!"

    show john a_30

    cornelia "If you don't stop it right now, then I'm calling both of your parents until we figure something out!"

    show sayaka a_16
    show john a_32

    john "What, is that supposed to be some kind of threat?"

    show cornelia b_14
    show john a_6

    cornelia "You should know by now how Sayaka's parents work, shouldn't you?!"

    show john b_7

    "...Crap, she did have a point. I already didn't live up to their ideals of their perfect daughter who wouldn't embarrass them or their image, so I sure as hell wouldn't want to endure whatever punishment they could come up with..."

    show john b_17

    cornelia "Did you two idiots finally come to your fucking senses then?"

    show sayaka a_7

    sayaka "Corny, don't you dare call me an id-"

    show sayaka a_15
    show john b_11
    show cornelia b_3:
        ease 0.5 xpos 0.25

    cornelia "You clearly aren't in the right mindset to make any decisions right now, so I'm taking the fucking wheel here!"

    show sayaka a_16

    cornelia "You're both left alone for even a few minutes and it ends up with both of you shouting your lungs out just because you can't agree on the most minor things!"

    show cornelia a_3

    cornelia "If you're going to continue like this, then there {i}is{/i} no saving your image, Saya! We need this jerk if we want there to be any point to this party!"

    show cornelia b_3
    show john b_27
    show sayaka a_15
    with hpunch

    cornelia "{size=+5}{b}So calm the fuck down, both of you!{/b}{/size}"

    show sayaka a_27
    show john b_22
    show cornelia b_18

    sayaka "..."
    john "..."

    show sayaka a_24:
        faceright
        ease 0.5 xpos 0.75
    show john a_0

    sayaka "Tch, fine."

    show sayaka a_16 at faceleft
    show john a_5 at faceright

    sayaka "Once we swap back I'll be glad to finally cut all ties I have with this moron."

    show john a_13

    john "Oh, you wouldn't be able to imagine the pure ecstacy I would feel if I never had to talk with you again, honey."

    show cornelia b_34 at faceleft
    show john a_35 at faceleft

    cornelia "{i}Sigh...{/i}"

    show cornelia b_24

    "She turned her head away after a long scoff."

    show john a_17
    show cornelia at faceright

    "This absolute bitch was criticizing my every life choice, and I was getting sick of it."
    "This stupid party would be the very last thing I would even attempt to tolerate, and only because we had already sent out the invitations for it."
    "Cutting ties with this child should have been the solution from the beginning. At least then I wouldn't have to put up with her constant crying and could peacefully hope we might swap back one day."
    "Nothing we tried was working anyways, and no fucking wonder. After all, we barely interacted in the first place, so us performing some sort of ritual that allowed a full body swap by accident was practically impossible."

    show john at faceleft
    show cornelia b_25

    cornelia "Good. Are we fine?"

    show john a_13 at faceright
    show sayaka at faceright
    show cornelia b_24

    sayaka "Hmph."
    john "Right back at you."

    show cornelia b_6

    cornelia "..."

    scene black with dissolve
    scene bg sayaka bedroom dusk
    show john b_25:
        center
        faceright
        xpos 0.6
        ypos 1.1
    with dissolve

    "The day ended up with a very hostile feeling in the air."
    "I intentionally avoided talking to her, and she did the same."
    "We were both clearly at our limits of tolerance it seemed, and my pride only allowed for one goodbye to Cornelia."
    think "As if I'd ever talk to her again."
    "That was the only thought in my head."
    "I now cemented it into my brain. I hated her with a burning passion. I wanted out of this sickening scenario I was put into."
    "I just couldn't wait to get this party over with and get back to regular school-days, and to hopefully talk with Kiyoshi, Kyoko and Kat on a nice noon where the only real concern was coming up with new non-sense to talk about after a long class with any of our teachers."
    "I hoped that once the new week started, everything could go back to the way it was before. That Kyoko somehow figured out how to swap two people."
    "And at the end of the day, that hope was the only thing that really kept me going right now."
    "I didn't want to live my remaining life as Sayaka Sato."
    "I knew it in my very being that I did not want to."

    scene black with Dissolve(2.0)
    pause 1.5

    title "26th of August (Friday)" "Day 19 - John"

    outfit john uniform_pony_pants
    pause 1
    scene bg lunch:
        zoom 1.5 xalign 0.3 yalign 0.8
    show john a_0:
        center
        faceright
        xpos 0.4
        ypos 1.15
    show cornelia b_0 behind john:
        center
        faceright
        xpos 0.2
        ypos 1.15
    with dissolve

    "Lunch had basically become our regular meeting spot for the last few weeks, and today was supposed to be no exception."
    "For once, me and Cornelia were the first to get to the table we've managed to secure as our own now."
    "Without really talking much, we had sat down and started eating what we bought from the canteen."

    show john b_4

    "And, uh..."
    think "It's been kind of awkward today."

    show john b_5

    "The fight me and Sayaka had was still lingering in the air."

    show cornelia b_4
    show john b_13 at faceleft

    "I would have thought that Cornelia would have taken Sayaka's side more and ridiculed me for pissing her majorly off, but she had been surprisingly okay with me throughout the entire day."

    show kiyoshi a_2:
        alpha 0.0
        center
        faceleft
        xpos 0.75
    show sayaka a_5:
        alpha 0.0
        center
        faceleft
        xpos 0.95

    "She didn't talk quite as much, but she was still walking around with me from classroom to classroom as usual."

    show kiyoshi:
        ease 0.75 alpha 1.0 xpos 0.6
    show sayaka:
        pause 0.25
        ease 0.75 alpha 1.0 xpos 0.8
    show john b_11 at faceright
    show cornelia b_11

    kiyoshi "Good noon to both of you!"

    #SKIP
    show kiyoshi:
        alpha 1.0
        xpos 0.6
    show sayaka:
        alpha 1.0
        xpos 0.8

    show kiyoshi a_1
    show sayaka a_16
    show john a_14

    john "Hey man."

    show john a_0

    "Kiyoshi arrived, and just behind her was Sayaka."

    show john a_32
    show cornelia b_1

    think "Ugh, I just... Cannot stand looking at her after all..."

    show cornelia a_2
    show john a_6
    show kiyoshi:
        pause 0.5
        ease 1 ypos 1.15

    cornelia "Uhm... Hey Saya."

    show cornelia a_11
    show sayaka a_33

    sayaka "..."

    show sayaka a_16 at faceright
    show kiyoshi a_0 at faceright
    show cornelia a_8
    show john b_11

    sayaka "I'm going somewhere else."

    show sayaka:
        ease 1.5 alpha 0.0 offscreenright
    show cornelia:
        pause 0.75
        ease 0.5 ypos 1.0

    "She spun around and walked away."

    show cornelia b_8:
        ease 1.0 xpos 0.8
    show john:
        faceleft
        pause 0.5
        faceright
    show kiyoshi:
        faceleft
        pause 1
        faceright

    cornelia "Wha- Saya, wait!"

    #SKIP
    show cornelia:
        xpos 0.8
        ypos 1.0

    "She was distressed about her, quote on quote, {q}best friend{/q} just not bothering to respond, but to my surprise, Cornelia didn't follow her."

    show cornelia b_4:
        faceleft
        ease 1.5 xpos 0.2
        pause 0.25
        faceright
        pause 0.5
        ease 0.5 ypos 1.15
    show john:
        pause 1
        faceleft
    show kiyoshi a_4:
        pause 0.5
        faceleft

    "Instead, she went and sat down again, although with a really sad expression on her face."
    cornelia "..."

    show john b_4

    john "...Uhm..."

    show cornelia a_3
    show john b_11

    cornelia "{q}Uhm{/q} what?"

    show john b_4
    show cornelia a_14

    john "...Sorry if this rift between us affects you."

    show cornelia a_0

    cornelia "..."

    show cornelia a_4

    cornelia "{i}Sigh...{/i}"

    show cornelia b_4
    show john b_0

    cornelia "It's fine."

    show john b_13

    think "Now that's a response I didn't expect to hear."

    show cornelia a_22

    cornelia "She'll... Come around eventually. Sometimes she just gets really angry at something... Or someone."

    show cornelia a_4

    cornelia "What I'm worried about is tomorrow..."

    show john b_4
    show kiyoshi a_9

    john "Ah, yeah..."

    show cornelia a_0
    show john b_0

    cornelia "And I'm not just simply worried about her being happy again, it's more about-"

    show john b_25

    john "{size=-5}Is she even able to be happy?{/size}"

    show cornelia a_5
    pause 1.5
    show cornelia b_6
    show john b_13

    cornelia "Can you keep your quips to yourself for now, thanks?"

    show john b_21
    show cornelia b_24

    john "...Sorry."

    show john b_13
    show cornelia a_17

    cornelia "I'm worried about what might happen in the future between us..."

    show cornelia a_22

    cornelia "Saya is one of my only friends and my best friend. If the two of you don't swap back soon, I might never talk to her again in the future."

    show john a_4

    john "...Oh, it's like that..."

    show cornelia a_0

    think "..."
    think "I really want to swap back myself, but everything we've tried so far doesn't even work..."

    show john a_20

    "The past few days have in between school-hours been a constant adventure of Kiyoshi and Sayaka coming up with weird schemes that could trigger some sort of swap similar from a manga or light novel."
    "But it's just been complete bollocks, all of it. Some were so outlandish that I even wondered why they thought it would work in the first place."

    show john b_0 at faceright

    john "Hey, Kiyoshi, you haven't heard anything from Kyoko yet, right?"

    show kiyoshi a_0

    kiyoshi "Hm? Ah, Kyoko? I'm afraid not."

    show kiyoshi a_1

    kiyoshi "I do know that she is heavily interested in the topic. I am actually visiting her later this afternoon. Do you want me to tell her something?"

    show john b_1

    john "Oh, no, I was just curious if maybe she figured out something really quickly."

    show kiyoshi a_4

    kiyoshi "Ah, I am sorry to disappoint you then."

    show john b_6

    john "Well, to disappoint me I would have needed some sort of hope in the first place."

    show kiyoshi a_3

    kiyoshi "...That sounds rather grim."

    show kiyoshi a_0
    show john b_4

    john "Yeah, kinda does."

    scene black with Dissolve(1.0)
    pause 1.5

    title "27th of August (Saturday)" "Day 20 - John"

    scene bg sayaka house day
    show AN_asset truck:
        right
        ypos 1.25
        zoom 1.35
    show john b_11 at center, faceright
    show cornelia b_0 at centerleft, faceright
    with dissolve

    john "Huh? What's a truck doing here?!"

    show cornelia b_6

    cornelia "They are here with the alcohol and snacks, idiot."

    show john b_7 at faceleft
    show cornelia b_24

    john "Just how much do you think we're gonna be drinking?!"

    show cornelia a_6
    show john b_0

    cornelia "{i}Sigh...{/i} Just don't think too much about it."

    show john a_30 at faceright

    john "Alright then..."

    show cornelia a_0
    show john a_5 at faceleft

    cornelia "Either way, we need to start getting you ready. Saya doesn't want to fix you up, so I am going to have to do that."

    show john a_0

    "Ah yeah, Sayaka was perfectly able to do my hair and make-up and whatever else sort of ritual she performed before that mixer thing, but she refused to even talk to me right now."
    "Not that I was complaining. A bit of peace and quiet was always nice. At least when that peace and quiet was away from her."

    show cornelia b_6

    cornelia "Really, I can't believe you two are still fighting..."

    show john a_13
    show cornelia b_24

    john "It's not my fault she keeps attacking me for not living her life the way she wants."
    cornelia "Yeah, yeah, we get it, it's difficult having to get up in the morning to do your hair properly."

    show john a_32
    show cornelia b_5

    cornelia "Now get your ass inside instead of staring at a couple delivery workers."

    scene black with dissolve
    pause 1
    outfit john underwear_badhair
    accessory john set
    $ screenfilter.blur = 2
    scene bg sadie bathroom day
    show cornelia b_0:
        center
        faceright
        xpos 0.6
    show john b_0:
        center
        faceright
        xpos 0.75
        ypos 1.15
    with dissolve

    "At least she knew what she was doing."

    show john b_23

    "Cornelia was using all kinds of potentially dangerous chemicals on my face, just like Sayaka did."

    show john b_6

    think "Although I probably wouldn't know the difference between what Cornelia is doing right now and what Sayaka did..."

    show john b_1

    "I was fresh out of a nice shower and it was kind of refreshing to just sit around and have my face being operated on."

    show john b_0
    pause 1.5
    show john b_6

    john "Hey."

    show cornelia b_5

    cornelia "What?"
    john "You use this stuff often, right?"

    show cornelia b_6
    show john b_11

    cornelia "Is that a serious question?"

    show cornelia b_24

    john "Uh... Yeah."

    show john b_0
    show cornelia b_5

    cornelia "Of course I do. There aren't many girls who don't use some sort of make-up."

    show john b_11

    john "Oh."

    show john b_5
    show cornelia b_0

    john "Right."
    john "..."

    show john b_6

    john "Hey."

    show cornelia b_6
    show john b_25

    cornelia "What?"

    show cornelia b_24
    show john b_13

    john "If I'm stuck like this for longer, can you teach me this stuff?"

    show cornelia a_0

    cornelia "You haven't looked up anything yourself?"

    show john b_4

    john "Uh... No."

    show john b_13
    show cornelia b_5

    cornelia "Geez, you really aren't doing a lot to adapt yourself to being a girl, are you?"

    show cornelia b_1

    cornelia "But yeah, I can teach you."

    show cornelia b_5

    cornelia "Not right now since I need to do my own hair and face too, though. I haven't even showered myself yet."

    show john b_14

    john "Mhm."

    scene black with dissolve
    outfit john underwear
    scene bg sadie bathroom day
    show john b_1:
        center
        faceright
        xpos 0.4
    show cornelia a_1 at centerright, faceleft
    with dissolve

    "I spent another good 10 to 15 minutes shackled to this impromptu saloon chair we put into the bathroom."

    show john b_14

    "It honestly almost felt like Cornelia had a better grip of what to do compared to Sayaka."

    show john b_1

    "In the very least, she was done faster."
    cornelia "Okay, done."

    show cornelia a_3

    cornelia "And don't touch your face for the next hour or so, or else you're going to end up looking like a ghost or some shit."

    show john a_14
    show cornelia a_5

    john "'Kay."

    show cornelia b_1:
        ease 0.75 xpos 0.45
    show john b_7:
        pause 0.25
        faceleft
        ease 0.6 xpos 0.25

    cornelia "Now get out, I need to get ready too."
    cornelia "Shoo."

    show john a_0 at faceright
    show cornelia a_1

    cornelia "Find some clothes that don't suck while I'm doing my own appearance."

    show john b_2

    john "Will do."

    scene black with dissolve
    pause 0.5
    play sound sfx_door_open
    scene bg sayaka bedroom day
    show john b_0:
        center
        faceleft
        xpos 0.9
        alpha 0.0
        ease 1.25 alpha 1.0 xpos 0.35
    with dissolve
    pause 0.75

    think "Okay, so I have to find clothes that {q}don't suck{/q}."
    think "My wardrobe is absolutely massive, so it shouldn't be impossible to find something like that."
    think "..."

    show john a_6

    think "Wait, what does {q}don't suck{/q} even mean?"

    show john b_13

    "Puzzled at how I should know exactly what {q}doesn't suck{/q}, I wavered my options."

    show john b_25:
        ease 0.5 xpos 0.25

    "And I wavered my options for about 15 seconds before just settling on the thing Sayaka told me to wear during the mixer."

    show john a_13

    think "Surely this falls under the category of {q}doesn't suck{/q}."

    scene black with dissolve
    outfit john casual
    accessory john set glasses
    $ screenfilter.blur = 0
    scene bg sayaka bedroom day
    show john b_0:
        center
        faceright
        xpos 0.6
        ypos 1.1
    with dissolve

    "I got changed into this outfit once more and then turned on my EksBox."
    "Apparently, the people who were setting stuff up down below knew what they were doing, so there wasn't much for me to do anymore."
    "It was probably some party delivery thing, and I bet they've been here a couple times now."

    show john b_11

    "While playing the same old games, I checked if any new games were cropping up. I had done nothing but play the same stuff for who knows how long now, and it was starting to get rather boring not having anything new."

    show john b_23

    "And with Sayaka's credit currently in my possession, surely she wouldn't get even angrier if I spent just a little on a new title or two to pass the time."

    show john b_0

    "So there I was, browsing the shop, as I rarely do."

    show john b_13

    think "Hm... Looks crappy... Looks like pay to win... Looks like some crappy fan-made japanese visual novel..."

    show john b_11

    "Then I got my eyes on an apparently big reveal."
    think "Dank Souls... Huh, that looks cool."

    show john b_6

    think "...Releases in a week.... Great..."

    show john b_0

    "With nothing but disappointing looking titles apart from a few cool ones, I went back to trying to 100% this stupid game I played with Cornelia."

    play sound sfx_knock
    show john a_13

    "Not long after, Cornelia knocked on the door."
    cornelia "{size=-5}John? Are my clothes in there?{/size}"

    show john b_0

    think "Her clothes...?"

    show john:
        pause 0.5 faceleft

    "I looked around and remembered that she did drop her backpack of party clothes or whatever you call them off in here before we went to the bathroom together."

    show john b_12 at faceright

    john "Yeah, they're here."

    show john b_1

    cornelia "..."

    show john b_11

    cornelia "{size=-5}Well, are you going to give them to me?{/size}"

    show john b_6

    john "The door is unlocked, just come in here."

    show john b_25

    cornelia "{size=-5}I'm half naked out here!{/size}"
    john "...So what? You're going to be half naked out there too if you want to change in the hallway."
    cornelia "{size=-5}John!{/size}"

    show john b_6

    john "{i}Sigh...{/i}"

    show john a_3

    john "We told you about the entire sexuality thing that happened to us already, so chill, I'm not going to suddenly jump you or anything."

    show john a_13

    john "The game is probably more interesting anyways."

    body cornelia AN_cornelia
    outfit cornelia towel
    show cornelia a_5:
        center
        faceleft
        alpha 0.0
        xpos 1.0
    show john b_5

    cornelia "{size=-5}Urgh, fine!{/size}"

    play sound sfx_door_open
    show john b_0
    show cornelia:
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 1.5 xpos 0.3

    "With just a tad bit of hesitation, she finally came into the room."

    show john b_5

    "Sure enough, she was wearing nothing but a towel. If I was still an actual guy I might have felt a bit differently, but the game I was playing was more interesting after all and required concentration, so I barely even bothered to look."

    show cornelia a_0
    show john b_11

    john "Hey-"

    show cornelia a_7 at faceright
    show john b_13

    cornelia "D- Don't you dare turn around!"

    show john b_6
    show cornelia a_11

    john "...I was just going to ask how you managed to beat this guy last time."

    show cornelia a_0

    cornelia "{q}This guy{/q}? Oh, the Dedris King."

    show cornelia a_12
    show john b_0

    cornelia "Wait, just, let me get changed first."

    show cornelia a_1 at faceleft
    show john b_1

    john "No need to hurry."

    scene black with dissolve
    pause 0.5
    body cornelia cornelia
    outfit cornelia casual
    accessory john set
    show bg sayaka livingroom dusk:
        zoom 1.5 xalign 0.2 yalign 0.7
    show john b_0 at center, faceright
    show cornelia b_0 at centerright, faceright
    with dissolve

    "In the end, we managed to spend some 10 or 15 minutes again playing before we went downstairs to check up on how things were going."
    "I was forced to wear my eye contacts, even though I was promised I could dress however I wanted to."

    show john b_25
    show cornelia b_5

    "Guess I really didn't get anything out of that mixer thing after all..."

    show john b_11
    show cornelia b_23:
        ease 0.75 xpos 0.9 alpha 0.0

    cornelia "Hey, wait, we need the pult over in that corner!"

    show john a_6
    hide cornelia
    show marty a_9:
        alpha 0.0
        center
        faceright
        xpos 0.05
    think "And off she goes..."

    show marty:
        ease 0.5 alpha 1.0 xpos 0.25
    show john b_11 at faceleft

    marty "Ah, Ms. Sato, there you are."

    show john b_12

    john "Oh, uh... Yeah, that's me. What's up?"

    show john b_1
    show marty a_0

    marty "We are about done with the set-up. Could you make sure everything is as it should be? Just say the word and we'll make sure to rectify any mistakes."

    show john b_2

    john "Yeah, yeah, of course."

    show john b_1
    show marty a_1

    marty "Thanks."

    show john a_31
    show marty a_9:
        faceleft
        ease 0.75 alpha 0.0 xpos 0.05

    think "As if I know where everything is supposed to be, though."

    show john a_0

    think "I better let Cornelia handle this one..."

    scene black with dissolve
    pause 0.5
    scene bg sayaka house dusk
    show AN_asset truck:
        right
        ypos 1.25
        zoom 1.35
    show marty a_0 at right, faceleft
    show john b_0:
        center
        faceright
        xpos 0.55
    show cornelia b_0:
        center
        faceright
        xpos 0.35
    with dissolve

    marty "Once more, thank you for choosing our service."

    show marty a_1

    marty "I hope the party will turn out a success as always."

    show marty a_9
    show cornelia b_1
    show john b_25

    think "Man, this guy is probably only a couple years older than me and is already talking as if he's from the middle-ages."

    show john b_1

    think "Although it is kind of sweet how he addresses me-"

    show john b_27 blush
    show cornelia b_11

    extend " No no no, bad thoughts!"

    show john b_2
    show cornelia b_22

    john "Thank you for your help. Have a safe trip back."

    show marty a_0
    show john b_1

    marty "Thanks. And please give my regards to your father."

    show john a_12

    john "Heh... Uh, yeah, will do."

    show john a_13
    show cornelia b_0
    show marty:
        faceright
        ease 2 alpha 0.0 xpos 1.2

    "He got into the truck where the two other people that helped were already sitting."

    show cornelia a_1
    show john b_11 at faceleft
    hide marty

    cornelia "At least there is some hope for the party now."

    play sound AN_sfx_truck
    show AN_asset truck:
        ease 8 xpos 1.75
    show john b_6

    john "Hope? Uh... Am I supposed to know why?"

    show john b_25

    cornelia "Considering you didn't embarrass yourself at all in front of the delivery guys."

    show john b_0

    john "Oh, like that."

    show john a_14

    john "If all I have to do is just walk around for an evening then it's going to be a piece of cake."

    show john a_1
    show cornelia a_6

    cornelia "Well, you have to do a bit more than just {q}walk around{/q}, but it's a start."

    scene black with dissolve
    pause 1.0
    outfit sayaka casual
    play sound sfx_door_open
    scene bg sayaka kitchen dusk
    show john b_11:
        centerright
        faceleft
        ypos 1.1
    show cornelia a_0:
        center
        faceright
        ypos 1.1
        pause 0.5
        faceleft
    show sayaka a_5:
        offscreenleft
        faceright
        ease 1.0 left
    with dissolve

    "About thirty minutes after the delivery boys left, Sayaka finally decided to show up."

    show cornelia a_1
    show john b_25

    "Compared to what I've been put through, she sure didn't put in a lot of effort to make me look refined or whatever word she would use for herself."
    "It was just my usual clothes."

    show cornelia a_2

    cornelia "Saya, there you are! How's it going?"

    show cornelia a_1

    sayaka "Fine."

    show cornelia a_11

    cornelia "Oh... Uh, great."

    show cornelia a_1

    cornelia "There is still an hour left before the first show up, but do you... Maybe want to watch a movie while we wai-"

    show sayaka a_16
    show cornelia a_11

    sayaka "I'm checking if this idiot over there has messed something up."

    show john a_32

    cornelia "O- Oh, right, you have to do that."

    show john a_6
    show sayaka a_5

    john "Really? First thing the Dunning-Kruger bitch says to me is an insult, as usual."

    show sayaka a_16

    sayaka "Do you expect anything else than the treatment of a twerp?"

    show john a_13:
        ease 0.5 ypos 1.0
    show cornelia at faceright

    john "Yeah, screw it, I'm going to my room while you have fun licking up dust to make sure it's clean."

    show john b_3:
        faceright
        ease 1.5 offscreenright
    show cornelia a_8:
        pause 0.75
        faceleft

    sayaka "Hmph. Suit yourself, moron."

    show sayaka:
        ease 2 offscreenright
    show cornelia a_4:
        pause 0.75
        faceright

    cornelia "..."

    show cornelia a_6

    cornelia "{i}{q}Yes, one of us would love to spend time with you, Cornelia!{/q}{/i}"

    show cornelia a_19

    cornelia "Jerks."

    scene black with dissolve
    pause 1

    title "27th of August (Saturday)" "Day 20 - Sayaka"

    scene bg sayaka livingroom night
    show sayaka a_5 at centerleft, faceleft:
        pause 1
        faceright
        pause 0.75
        faceleft
    show cornelia a_19 at right, faceright
    with dissolve
    pause 1

    think "Hmph, at least he was competent enough to not screw something up."
    "I had just finished checking everything to make sure he wasn't stupid enough to leave a bowl of cereal or something around."
    "I made double sure everything was clean and having Corny check on other stuff."
    "At least she has some interest in doing this right."

    play sound sfx_bell
    show sayaka a_32 at faceleft
    show cornelia a_11:
        pause 1
        faceleft

    "And just in time, the first guest arrived."
    "I already had a good guess as to who it was."

    show sayaka a_5:
        ease 0.5 xpos 0.0 alpha 0.0

    "That couple was always way earlier than anyone else."

    scene black with dissolve
    outfit maria casual
    outfit eric casual
    accessory eric set cigarette
    scene AN_bg sayaka frontyard night
    show maria a_4 at centerleft, faceright
    show eric a_4 at left, faceright
    show sayaka a_8:
        center
        faceleft
        alpha 0.0
        xpos 1.0
        pause 1
        ease 0.75 xpos 0.6 alpha 1.0
    with dissolve

    "I was of course right. Maria and Eric always managed to be there early, due to Maria having the annoying tendency of wanting to snoop around before everyone shows up."

    #SKIP
    show sayaka:
        alpha 1.0
        xpos 0.6

    show maria a_10

    sayaka "Maria, Eric, welcome."

    show maria a_9
    show eric a_0

    maria "John! You're here already as well!"

    show sayaka a_5
    show maria a_24

    maria "Heheh, did Sayaka employ you as her new butler?"

    show sayaka a_33
    show maria a_12
    show eric a_1

    "She grinned to herself at her shitty joke, and of course Eric cracked a grin as well like the pathetic boyfriend he was."

    show maria a_0
    show eric a_0
    show sayaka a_2

    maria "Just kidding! It's good to see you."

    show maria a_9 at faceleft

    maria "Eric, show him what you brought."

    show eric a_7
    show maria a_0
    show sayaka a_32

    eric "Here."
    "He held up a rather large plastic bag which was filled with rattling bottles."

    show eric a_1
    show maria a_12

    eric "The strongest you can find around here."

    show eric a_0
    show maria a_0 at faceright
    show sayaka a_2

    sayaka "Is this what I think it is?"

    show eric a_1

    eric "If you're thinking shots, sure is."

    show sayaka a_16
    show eric a_0

    sayaka "You sure you should be bringing that?"

    show eric a_1
    show maria at faceleft

    eric "It's for the guys. The girls would go crazy after drinking this stuff, so better we get wasted instead. Heh."

    show eric a_0
    show maria a_13 at faceright
    show sayaka a_2

    maria "Can you believe it? Even I don't know where he managed to buy this stuff! I don't even think it's legal for us to have it!"

    show maria a_14

    maria "I tried that stuff and I'm lucky he didn't have the guts to completely manhandle me while I was completely wasted, haha."

    show maria a_17

    maria "Even if I would'nt have minded..."

    show sayaka a_16
    show maria a_4

    sayaka "...And you're bringing {i}that{/i} to my party?"

    show maria a_12
    show eric a_4

    maria "Are you collaborating with Sayaka on parties now too? Haha, you guys have been hanging out so much that she's even rubbing off on you."

    show maria a_0

    sayaka "I wish it were the other way around."

    show sayaka a_17

    sayaka "Anyways, get inside already."

    show maria a_24
    show eric a_0
    show sayaka a_5

    maria "Sure thing. Oh, and you still aren't going to spill anything about your romance between each other?"

    show sayaka a_7

    sayaka "For the last time, there is no romance!"

    show sayaka a_16
    show maria a_27

    maria "Mhm. If you say so."

    show maria a_0 at faceleft

    maria "Let's go get some chips, babe."

    show eric a_1

    eric "Heh, sure."

    show maria:
        faceright
        ease 1.5 xpos 1.2 alpha 0.0
    show eric a_0:
        pause 0.15
        ease 1.4 xpos 1.05 alpha 0.0
    show sayaka:
        pause 0.5
        faceright

    think "For fucks sake, can she let this go already?"
    "She'd been pestering me all the time lately, about somehow being in a loving relationship with my own body."
    "And I mean, sure, {q}John{/q} was spending an unusual amount of time with {q}Sayaka{/q} recently, but of course she had to interpret it as a freaking romance."

    show sayaka a_24

    think "It just reminds me of why I hate people who gossip about me..."

    scene black with dissolve
    outfit rita dress
    outfit irene casual_b
    outfit allison casual_b
    outfit brad casual
    outfit kiyoshi uniform_b
    show bg sayaka livingroom party:
        zoom 1.5 xalign 0.35 yalign 0.55
    show sayaka a_0:
        center
        faceright
        xpos 0.15
    show rita a_3:
        center
        faceright
        xpos 0.4
    show irene a_1:
        center
        faceleft
        xpos 0.55
    show allison b_5:
        center
        faceleft
        xpos 0.65
    show eric a_1:
        center
        faceright
        xpos 0.8
    show brad a_12:
        center
        faceleft
        xpos 0.95
    show kiyoshi a_6:
        offscreenleft
        faceright
    with dissolve

    "Eventually, most people started to arrive."
    "If I didn't know better, this was like any of my other parties."

    show bg sayaka livingroom party:
        ease 1.5 xalign 0.0
    show rita:
        ease 1.5 alpha 0.0 xpos 0.65
    show irene:
        ease 1.5 alpha 0.0 xpos 0.8
    show allison:
        ease 1.5 alpha 0.0 xpos 0.9
    show eric:
        ease 1.5 alpha 0.0 xpos 1.05
    show brad:
        ease 1.5 alpha 0.0 xpos 1.12
    show kiyoshi:
        ease 1.5 xpos 0.25
    show sayaka:
        ease 1.5 xpos 0.4
    pause 2
    show sayaka a_33

    "Well, if it weren't for this guy."
    kiyoshi "It truly is lively."
    sayaka "..."

    show sayaka a_16 at faceleft
    show kiyoshi a_10

    sayaka "Why are you even here?"

    show kiyoshi a_8

    kiyoshi "To party, of course!"

    show sayaka a_24
    show kiyoshi a_13

    sayaka "{i}Sigh...{/i}"

    show sayaka a_16

    sayaka "Fine. Just don't do weird shit."

    show kiyoshi a_14

    kiyoshi "Score!"

    show kiyoshi a_10

    kiyoshi "But I can make no promises."
    sayaka "...Seriously, don't attempt anything."

    play sound sfx_bell
    show sayaka a_5
    show kiyoshi a_0

    "Before I could shoot him more of my serious glare, I heard someone else ringing the door."
    think "Someone sure is late."

    scene black with dissolve
    pause 0.5
    outfit AN_harry casual
    scene AN_bg sayaka frontyard night
    show AN_harry a_6:
        centerleft
        faceleft
        pause 1.5
        faceright
    show sayaka a_5:
        center
        faceleft
        alpha 0.0
        xpos 1.0
        pause 1
        ease 0.75 xpos 0.6 alpha 1.0
    with dissolve

    "Who waited for me was not exactly someone I expected though."

    show sayaka:
        xpos 0.6
        alpha 1.0
    show AN_harry:
        faceright

    AN_harry "...Uhm..."

    show AN_harry a_3
    show kiyoshi a_1:
        center
        faceleft
        alpha 0.0
        xpos 1.2
        pause 1
        ease 0.75 xpos 0.8 alpha 1.0

    AN_harry "Might this be the Sato Estate?"

    show kiyoshi a_14:
        xpos 0.8 alpha 1.0

    kiyoshi "Ahh! Harry! There you are!"

    show kiyoshi a_1
    show AN_harry a_0

    AN_harry "Hello Kiyoshi. This must be the place then. Sorry, I'm a bit late."

    show AN_harry a_1

    AN_harry "And thanks for the invitation. I barely get the opportunity to go to parties like these."

    show AN_harry a_0
    show kiyoshi a_2
    show sayaka at faceright

    kiyoshi "No problemo! Anything for a friend."

    show sayaka a_16

    think "Does Kiyoshi think he is the one hosting the party when he apparently just invites people willy-nilly?"

    show sayaka at faceleft
    show AN_harry a_3
    show kiyoshi a_1

    sayaka "Who are you again?"

    show AN_harry a_7

    AN_harry "Oh yeah, I don't think we've met each other. You're John, right?"
    sayaka "And you?"

    show AN_harry a_11

    AN_harry "Harry Barlow. Nice to meet you."

    show sayaka a_5
    show AN_harry a_7

    "The name rang a bell, but I couldn't quite put my tongue on where exactly I had heard it before."
    "The guy was probably someone who had an overall low profile during school."
    sayaka "You were invited by Kiyoshi?"

    show AN_harry a_10

    AN_harry "Ah, no. Sayaka asked me if I would like to come. Kiyoshi was just kinda... There at that time, I guess?"

    show AN_harry a_7
    show sayaka a_16

    think "Seriously, what went through that guy's head when he decided to also invite this guy?"
    sayaka "Fine then, come on in. But don't cause a mess, got it?"

    show AN_harry a_9

    AN_harry "I'll try not to. Thanks."

    show AN_harry a_0:
        ease 1.5 xpos 1.2 alpha 0.0
    show sayaka:
        pause 0.5
        faceright
    show kiyoshi:
        pause 0.9
        faceright

    "He waddled his way in with a smile."

    show kiyoshi a_0 at faceleft

    sayaka "...You know this guy?"

    show kiyoshi a_10

    kiyoshi "Harry? Of course. J-man and Cornelia seem to be quite fond of him."

    show sayaka a_5

    sayaka "John is {q}fond{/q} of him?"

    show sayaka a_16

    sayaka "What does that mean?"

    show kiyoshi a_16

    kiyoshi "That they are... Uh... Friends?"
    sayaka "...That idiot."
    think "Does John not know what happens if a girl and a boy just casually become {q}friends{/q}?"
    think "The list of shit he's done keeps on piling up it seems."

    show sayaka a_5

    think "..."
    think "Isn't that the exact same that's happening between me and John...?"

    show sayaka a_20

    think "Urgh, no! No it isn't!"

    scene black with dissolve
    pause 1
    show bg sayaka livingroom party:
        zoom 1.25 xalign 0.3 yalign 0.55
    show sayaka a_5:
        center
        faceright
        xpos 0.35
    with dissolve

    "As the evening began to really roll around, no major issues had really presented themselves."
    "Music was good, everyone was chatting, some already dancing..."

    show sayaka a_0
    show kiyoshi a_11:
        center
        faceright
        xpos 0.6
        alpha 0.0
    show maria a_1:
        center
        faceleft
        xpos 0.8
        alpha 0.0
    show audrey a_0:
        center
        faceleft
        xpos 0.95
        alpha 0.0

    "The outlook towards success was starting to become visible for once during these last three weeks."

    show bg sayaka livingroom party:
        ease 0.5 xalign 0.6
    show sayaka:
        ease 0.5 xpos 0.15
    show kiyoshi:
        ease 0.5 xpos 0.4 alpha 1.0
    show maria:
        ease 0.5 xpos 0.6 alpha 1.0
    show audrey:
        ease 0.5 xpos 0.75 alpha 1.0

    "I had also spent a lot of time tutoring Kiyoshi in socializing with girls properly. He actually took it to heart, which was completely alien to me."

    show sayaka:
        xpos 0.15
    show kiyoshi:
        xpos 0.4 alpha 1.0
    show maria:
        xpos 0.6 alpha 1.0
    show audrey:
        xpos 0.75 alpha 1.0

    "Because right now, he actually felt a bit more relaxed and not up in your face."

    show kiyoshi a_6 at faceleft
    show maria a_0
    show audrey a_6

    "I frequently gave him a thumbs up when I he shot a glance my way. The girls not slapping him in the face was a constant success."

    show kiyoshi a_15 at faceright

    "I was almost proud of how he was currently talking to Maria and that Audrey girl that John apparently was in contact with without them having a look of disgust on their faces."
    think "It really was a good idea to bring him, huh?"

    show bg sayaka livingroom party:
        ease 0.5 xalign 0.45
    show sayaka a_5:
        ease 0.5 xpos 0.2
    show kiyoshi:
        ease 0.5 xpos 0.5 alpha 0.0
    show maria:
        ease 0.5 xpos 0.7 alpha 0.0
    show audrey:
        ease 0.5 xpos 0.85 alpha 0.0
    play sound AN_sfx_cell_buzz

    think "Huh? A phone call?"


    show kiyoshi:
        xpos 0.5 alpha 0.0
    show maria:
        xpos 0.7 alpha 0.0
    show audrey:
        xpos 0.85 alpha 0.0
    show sayaka a_16:
        xpos 0.2

    think "Who is it now?"
    "As I took out the phone from my pocket, I saw the person contacting me and dreaded in silence."

    show sayaka a_24
    show AN_phone a_0:
        centerright
        faceleft
        ypos 2.0

    think "Annoying Citrus. Fuck."

    show sayaka a_16 at faceright
    show AN_phone:
        ease 0.75 ypos 1.0

    "This Zoey girl had gotten a hold of my number and was calling me in the most annoying times possible. Right now was one of those times."

    show AN_phone:
        ypos 1.0

    think "Better tell her to screw off and not call me anymore today."

    play sound AN_sfx_silence
    show AN_phone a_1

    zoey "-better pick up his stupid pho-"

    show AN_phone a_2
    show sayaka a_5

    zoey "Oh! Hey John!"

    show sayaka a_16
    show AN_phone a_3

    sayaka "I can't talk right now, so stop calling me today. Got it?"

    show AN_phone a_4

    zoey "What do you mean?"

    show AN_phone a_5

    zoey "Wait, who are these people behind you-"

    show AN_phone a_6

    zoey "Are you throwing a party without inviting me, John?!"
    sayaka "See you, hopefully never."
    zoey "Hold up, answer me, Joh-!"

    show AN_phone a_7
    show sayaka a_5
    play sound AN_sfx_cell_end

    think "There."

    show AN_phone:
        ease 0.75 ypos 2.0
    show cornelia a_11 blush:
        offscreenleft
        faceright

    think "Now to put it on silent mode."

    hide AN_phone
    show bg sayaka livingroom party:
        ease 0.5 xalign 0.0
    show sayaka a_15:
        ease 0.5 xpos 0.4
    show cornelia:
        ease 0.5 xpos 0.3
    pause 0.25

    cornelia "Who was that?"

    show sayaka a_4:
        faceleft
        ease 0.25 xpos 0.45
    with hpunch

    sayaka "Oh Jesus Chris-"

    show cornelia a_19 blush
    show sayaka a_7

    sayaka "Stop scaring me like that!"

    show cornelia a_17 blush
    show sayaka a_16

    cornelia "...Sure..."

    show cornelia a_0 blush
    show sayaka a_5

    cornelia "But who was that? John's mom?"

    show sayaka a_16

    sayaka "It was that annoying sister of Brad."
    sayaka "Gosh, can she leave me freaking alone already?"

    show cornelia a_5 blush

    sayaka "Like, does she need to be hit by a car or something before she gets the hint that I don't give a damn about her?"

    show sayaka a_21

    sayaka "It's as if I'm her only fucking friend, and I can't stand having to talk to a measly little shitty runt like her!"

    show cornelia a_11 blush
    show sayaka a_16

    cornelia "..."

    show sayaka a_7

    sayaka "What?! You look at me like I'm a dog or something!"

    show cornelia a_14 blush
    show sayaka a_16

    cornelia "Are you, like, okay?"
    sayaka "Who? Me?"

    show cornelia a_3 blush

    cornelia "Who else?"

    show cornelia a_14 blush

    sayaka "What the hell do you think? I'm doing just fine, for your information. Why are you even asking?"

    show cornelia a_19 blush

    cornelia "No offense, but you've been acting really tense lately, and I don't think I've seen you talk to John today at all."

    show cornelia a_0 blush
    show sayaka a_5

    cornelia "So are you sure you're okay? You sound like you're bottling up a lot of frustration as of late."

    show sayaka a_16

    sayaka "Of course I'm okay. Have you ever seen me not being okay?"
    sayaka "Besides, as long as that dickhead doesn't screw up I'd rather not talk to him {i}at all{/i} anymore. Let alone right now."

    show cornelia b_6 blush

    cornelia "{i}Sigh...{/i} You two really... Uh... Need to fix things, you know?"

    show cornelia b_24 blush

    sayaka "And why should I listen to that idiot talking for even a second?"
    cornelia "Do I really have to explain why? You're still living his life, you two should work together, not against each other."

    show sayaka a_7
    show cornelia b_31 blush

    sayaka "Oh, lay it off already! You're starting to sound more and more like you adore him more than me!"

    show cornelia b_29 blush
    show sayaka a_16

    cornelia "...What? Who?"

    show sayaka a_7

    sayaka "John!"

    show cornelia a_11 blush

    cornelia "...Ohhh..."

    show sayaka a_15

    think "Wait, don't tell me she's already..."

    show sayaka a_16
    show cornelia a_0 blush

    sayaka "How many have you had already?"

    show cornelia b_6 blush

    cornelia "How many cans?"

    show cornelia b_24 blush

    sayaka "Yes, how many?"

    show cornelia b_34 blush

    cornelia "Uh... I think this is my ninth...?"

    show sayaka a_7
    show cornelia a_11 blush

    sayaka "What?! The clock is not even eleven yet, and you've been downing cans of alcohol like it's a fucking bachelor's party!"
    sayaka "You're supposed to help keep an eye out here!"

    show sayaka a_16
    show cornelia b_17 blush

    cornelia "Ngh... Well, it's not my fault you know! If only that asshole would finally tell me that he likes me too, then I wouldn't try to-"

    show sayaka a_7
    show cornelia b_0 blush

    sayaka "Wait, who? Kiyoshi?"

    show sayaka a_16
    show cornelia a_3 blush

    cornelia "Well, duh..."

    show cornelia a_8 blush
    show sayaka a_15

    cornelia "He isn't getting drunk at all! What's with him?"

    show cornelia b_4 blush

    cornelia "It makes, like... No sense."

    show sayaka a_25
    show cornelia b_5 blush

    sayaka "You- Ugh..."

    show sayaka a_16

    sayaka "You're a light-weight, you idiot. If you keep going you're going to be out soon."

    show sayaka a_2
    show cornelia b_3 blush

    cornelia "Then make him tell me that I look good!"

    show sayaka a_7
    show cornelia b_24 blush

    sayaka "What the hell is your obsession with this guy?!"

    show sayaka a_16
    show cornelia b_29 blush

    cornelia "He said I look ugly! I don't! Look at me!"

    show cornelia b_32 blush

    cornelia "If I just... Keep drinking with him then maybe sometime later..."

    show sayaka a_24 at faceright

    sayaka "Oh my god..."

    show sayaka a_16 at faceleft
    show cornelia b_26 blush

    sayaka "Don't tell me you're trying to get him wasted in order to make him say he likes you..."

    show cornelia b_29 blush

    cornelia "Uh..."

    show cornelia a_11 blush

    cornelia "...No...?"

    show cornelia a_0 blush
    show sayaka a_7

    sayaka "Doesn't it defeat the fucking purpose if he tells you without being at his senses? Because he'd be wasted?"

    show cornelia a_22 blush
    show sayaka a_16

    cornelia "When you're drunk, you spill the truth of what you're thinking."

    show cornelia a_17 blush

    cornelia "I think."

    show cornelia a_18 blush

    cornelia "Yeah!"

    show sayaka a_24:
        faceright
        ease 0.5 xpos 0.55
    show cornelia a_11 blush

    sayaka "Oh my god, you're a completely lost cause..."

    show cornelia a_8 blush

    cornelia "No, I'll even record it so you believe me when I say it!"

    show sayaka a_7:
        faceleft
        pause 1
        faceright

    sayaka "That wasn't what I was talking abou- Oh, fuck it."

    show sayaka a_16
    show cornelia a_11 blush

    think "At least I now know that {i}she{/i} isn't going to be of any fucking help today."

    scene black with dissolve
    pause 1.5
    show bg sayaka livingroom party
    show sayaka a_5:
        center
        faceright
        xpos 0.8
    with dissolve
    pause 0.25

    "Another half an hour passed."

    show sayaka at faceleft
    show john b_24 blush:
        center
        faceleft
        xpos 0.3
        zoom 0.75
        alpha 0.0
        ypos 1.1
    show cornelia a_19 blush:
        center
        faceleft
        xpos 0.4
        zoom 0.75
        alpha 0.0
        ypos 1.1
    show brad a_3:
        center
        faceright
        xpos 0.2
        zoom 0.75
        alpha 0.0
        ypos 1.1
    show AN_harry a_3:
        center
        faceright
        xpos 0.1
        zoom 0.75
        alpha 0.0
        ypos 1.1

    "It was perplexing not being the center of attention all the time, and John seemingly wasn't screwing things over..."

    show bg sayaka livingroom party:
        ease 0.75 zoom 1.75 xalign 0.25 yalign 0.4
    show sayaka:
        ease 0.5 zoom 1.2 xpos 0.95 alpha 0.0
    show john:
        ease 0.75 zoom 1.0 xpos 0.5 alpha 1.0
    show brad:
        ease 0.75 zoom 1.0 xpos 0.3 alpha 1.0
    show cornelia:
        ease 0.75 zoom 1.0 xpos 0.7 alpha 1.0
    show AN_harry:
        ease 0.75 zoom 1.0 xpos 0.1 alpha 1.0

    "Still, instead of talking with the people he was {i}supposed{/i} to be talking with, he kept spending time with that Harry guy, Brad, Cornelia..."

    show bg sayaka livingroom party:
        zoom 1.75 xalign 0.25 yalign 0.4
    show sayaka:
        zoom 1.2 xpos 0.95 alpha 0.0
    show cornelia:
        zoom 1.0 xpos 0.7 alpha 1.0
    show AN_harry:
        zoom 1.0 xpos 0.1 alpha 1.0
    show john b_6 blush:
        zoom 1.0 xpos 0.5 alpha 1.0
    show brad a_15:
        zoom 1.0 xpos 0.3 alpha 1.0

    "The same group of friends like fucking always."

    show AN_harry a_10
    show brad a_0
    show john b_3 blush

    "I had a lot of time to think about things right now, and I had to slowly accept that things wouldn't go back to how they were before."

    show cornelia b_24 blush at faceright
    show john a_6 blush
    show AN_harry a_7

    "I was in a terrible mood. The benefits I had from being the leader of the highest circle of people in school was evaporating in front of my eyes."

    #TODO: Make blush for this face
    show john a_32 blush:
        ease 0.5 ypos 1.0
    show brad a_1
    show AN_harry a_0

    "It had been evaporating since this semester started. And fuck, it was frustrating not being able to do anything about it."

    show bg sayaka livingroom party:
        ease 0.75 zoom 1.0
    show john:
        ease 0.75 xpos 0.3 zoom 0.75 alpha 0.0 ypos 1.0
    show cornelia:
        ease 0.75 xpos 0.4 zoom 0.75 alpha 0.0 ypos 1.1
    show brad:
        ease 0.75 xpos 0.2 zoom 0.75 alpha 0.0 ypos 1.1
    show AN_harry:
        ease 0.75 xpos 0.1 zoom 0.75 alpha 0.0 ypos 1.1
    show sayaka:
        faceright
        pause 0.25
        ease 0.5 alpha 1.0 zoom 1.0 xpos 0.8

    "Again, I kept thinking to myself, {q}Why John? What's so special about him{/q}."

    show bg sayaka livingroom party:
        zoom 1.0
    show john:
        xpos 0.3 zoom 0.75 alpha 0.0 ypos 1.0
    show cornelia:
        xpos 0.4 zoom 0.75 alpha 0.0 ypos 1.1
    show brad:
        xpos 0.2 zoom 0.75 alpha 0.0 ypos 1.1
    show AN_harry:
        xpos 0.1 zoom 0.75 alpha 0.0 ypos 1.1
    show sayaka:
        faceright
        alpha 1.0 zoom 1.0 xpos 0.8

    "I mean, sure, his family is great and he has friends, but the same was true for me too, right?"

    show john b_14 blush:
        ypos 1.01
        zoom 1.0
        xpos 0.35
        faceright

    "But really, what mistake did I do to be swapped with him..."

    show john:
        ease 0.5 alpha 1.0 xpos 0.5

    john "Heyy~~y Sayakaa~~~a- I mean, John, heh..."

    show sayaka a_33 at faceleft
    show john b_1 blush:
        alpha 1.0 xpos 0.5
    pause 1.5

    sayaka "...What?"

    show john b_12 blush

    john "You look, like... Lonely, and stuff, heh."

    show sayaka a_16
    show john b_11 blush

    sayaka "What do you care?"

    show john b_2 blush

    john "Hahah, good one!"

    show john b_13 blush

    sayaka "..."

    show john a_11 blush

    john "...Uh... So, Brad and Harry both like... Said you looked a bit lonely, you know."

    show john b_22 blush:
        ease 0.15 ypos 1.0
        ease 1.0 ypos 1.01

    john "{i}{b}Hic!{/b}{/i}"

    show sayaka a_5
    show john a_19 blush

    john "So! Do you like... Want to have a drink with us to boost the mood you're in? Heh..."

    show john a_0 blush
    show sayaka a_33

    sayaka "Are you drunk?"

    show john a_12 blush

    john "Whaat, noo..."

    show john b_2 blush
    show sayaka a_32

    john "I only had some punch and a bit of beer and some shots and you know you probably do this all the time so I bet I can take it too you know."

    show john:
        block:
            faceleft
            pause 1
            faceright
            pause 1
            repeat

    john "Whee~~"

    show sayaka a_24

    think "{i}Sigh...{/i} Add one more item to the list of issues that I have with this guy."

    show john b_12 blush at faceright
    show sayaka a_16

    john "See? My equibribrium is totally fine even after spinning~~"

    show john b_1 blush

    "I knew that my body could take a lot of alcohol before getting really wasted, so either that doesn't matter due to this swap and this guy doesn't know how to handle being drunk or he really had way too much already."

    show sayaka a_7
    show john b_11 blush

    sayaka "I am {b}not{/b} spending time with you. And stop drinking Rita's punch! It's fucking filled with alcohol!"

    show sayaka a_16
    show john b_6 blush at faceleft

    john "Alright Miss Naggy. Sorry for trying to make you happy."

    show sayaka a_7
    show john b_23 blush

    sayaka "What did you just call me?"

    show john b_25 blush:
        ease 1.5 zoom 0.9 xpos 0.35 alpha 0.0
    show sayaka a_16

    john "...Nothing..."
    think "I suddenly have a bad feeling about tonight with him on the loose."

    scene black with dissolve
    pause 1
    show bg sayaka livingroom party:
        zoom 2.0 xalign 0.3 yalign 0.7
    show sayaka a_5:
        centerright
        faceleft
    show maria a_2:
        center
        faceleft
    show kiyoshi a_0:
        centerleft
        faceright
    show cornelia a_6 blush:
        right
        faceleft
    with dissolve

    maria "So then, what do you think I see?"

    show maria a_3
    show sayaka a_32

    maria "Mallory, of all people, walking out of the dressing room!"

    show maria a_9

    maria "And where did the clothes he was allegedly {q}trying on{/q} go?"

    show maria a_20

    maria "They weren't there, at all!"

    show maria a_23

    maria "I checked all trying rooms the shop had, but none of the clothes he brought in were there!"

    show kiyoshi a_9
    show maria a_6

    kiyoshi "A robbery?"

    show maria a_1
    show kiyoshi a_4

    maria "You bet!"

    show maria a_4

    maria "But how did he do it? There were {i}way{/i} too many clothes for him to just, you know, put them on under his clothes and walk away."

    show kiyoshi a_17
    show maria a_0

    kiyoshi "Hm... Could he have an accomplice of sorts?"

    show maria a_8
    show sayaka a_33

    maria "That's the first thing I thought too. If only I had my camera with me, I could have used it as evidence."

    show kiyoshi a_0
    show maria a_13

    maria "Man, that still bums me out that I didn't have it on me. It would have been a massive story."

    show kiyoshi a_7
    show maria a_10

    kiyoshi "Perhaps you would be interested in the new Moogle watches then."

    show kiyoshi a_1
    show maria a_11

    maria "Moogle what?"

    show kiyoshi a_12

    kiyoshi "It is a watch that is currently being developed by Moogle. I believe it has an in-built camera that you can use on the fly."
    kiyoshi "I wish to acquire one for my alien hunting as well, but I am currently short on funds. I would imagine someone like you having enough cash for it however."

    show maria a_20

    sayaka "..."

    show kiyoshi a_7

    kiyoshi "Truly innovating technology."

    show kiyoshi a_8

    cornelia "..."

    show maria a_19

    maria "For real? I need to save up some money for that then!"

    show maria a_1
    show kiyoshi a_2

    think "..."

    show sayaka at faceright

    think "Oh my god this is boring..."

    show maria a_0 at faceright
    show kiyoshi a_1 at faceright
    show sayaka a_5

    cornelia "Uh..."

    show cornelia a_17 blush
    show sayaka a_32
    show kiyoshi a_0

    cornelia "Uhm... What's the word..."

    show maria a_4

    maria "Is she... Okay?"
    maria "I don't think I've ever seen Corny {i}this{/i} wasted before..."

    show cornelia b_17 blush

    cornelia "I'm not..."

    show cornelia b_21

    cornelia "..."

    show sayaka a_2 at faceleft
    show maria a_27
    show cornelia b_4 blush

    maria "..."

    show kiyoshi a_9
    show maria a_11 at faceleft
    show sayaka a_5

    kiyoshi "She likely had a few too many. I do not know why, but she really wanted to drink with me today."

    show cornelia a_4 blush
    show maria a_10 at faceright
    show sayaka at faceright
    show kiyoshi a_0

    cornelia "Just... One more, please?"

    show kiyoshi a_2
    show maria a_21

    kiyoshi "If you insist, sure."

    show maria a_3 at faceleft
    show sayaka a_2
    show kiyoshi a_1

    maria "You've been tallying with her?"

    show sayaka a_5 at faceleft
    show kiyoshi a_0
    show maria a_6

    kiyoshi "Tallying?"

    show maria at faceright

    sayaka "It means that you've been drinking the exact same as her for the entire night."

    show maria at faceleft

    maria "Yeah, that."

    show kiyoshi a_9

    kiyoshi "Hmm... I believe so? I've only had what she brought me so far."

    show maria a_5

    maria "And how much is that?"

    show kiyoshi a_4

    kiyoshi "About seventeen cups, slash, cans of beverages if I counted correctly?"

    show sayaka a_15
    show maria a_3
    show kiyoshi a_5

    maria "Seventeen?! Seventeen of what?"

    show maria a_21
    show kiyoshi a_1
    show cornelia a_17 blush

    kiyoshi "It's been a mix, but some beer, some of the small cups, some of that delicious beverage over there."

    show sayaka a_32 at faceright
    show maria a_20 at faceright

    "He pointed toward Rita's toxic Wanda surprise."

    show sayaka a_2 at faceleft
    show maria at faceleft

    sayaka "And you're not drunk at all?"

    show kiyoshi a_9

    kiyoshi "I do feel a little tingling in my head. Is that considered {q}drunk{/q}?"

    show maria a_22

    maria "...Dude, do you have some sort of black hole in your stomach?"

    show sayaka a_32 at faceright
    show maria a_17 at faceright
    show kiyoshi a_0

    cornelia "Come on..."
    maria "Girl, you really shouldn't have any more."

    show cornelia b_4 blush

    cornelia "Just one more, please..."

    show maria a_6

    maria "..."

    show sayaka a_5 at faceleft

    maria "{size=-5}Hey, what's gotten into her?{/size}"

    show maria at faceleft

    kiyoshi "Beats me."

    show maria at faceright

    "I lifted my shoulders in indifference. Telling little Ms. Gossip about touchy subjects was never a good idea, so I feigned ignorance."

    show sayaka at faceright
    show cornelia a_17:
        parallel:
            ease 0.15 xpos 0.86
            ease 0.2 xpos 0.84
        parallel:
            transform_anchor True
            ease 0.4 rotate 5 ypos 1.1

    cornelia "{i}Ugh...{/i}"

    show sayaka a_33
    show maria a_23

    think "Aa~~~and she's close to throwing up..."

    show sayaka a_6 at faceleft
    show maria a_4

    sayaka "Can you take her to the bathroom upstairs?"

    show maria a_8

    maria "Oh, it's that time of the day, huh?"
    maria "Sure."

    show maria a_9:
        ease 0.75 xpos 0.7
    show cornelia:
        pause 0.5
        faceright
    show sayaka a_5:
        pause 0.25
        faceright
        ease 0.75 xpos 0.55

    maria "Now, let's go, princess, you need to at least be able to stand on two feet."

    show maria a_8:
        ease 1 alpha 0.0 xpos 0.9
    show cornelia:
        parallel:
            ease 0.25 ypos 1.0
        parallel:
            ease 0.9 alpha 0.0 xpos 1.05

    cornelia "...But after this... Just one more... {i}{b}Hic!{/b}{/i}"
    sayaka "..."
    kiyoshi "..."
    sayaka "{size=-5}{i}Sigh... {/i}Idiot...{/size}"

    show sayaka a_32

    think "Speaking of drunk people, where is the other supposed organizer of this party?"

    show sayaka:
        faceleft
        pause 0.75
        faceright

    "I looked around the room but couldn't find my own shape amongst the people."

    show sayaka a_16

    "It kind of set an alarm of inside my head not having control over his location, but calmed down soon after since I knew I was on edge lately."

    show sayaka at faceleft

    sayaka "Do you know where John is?"

    show kiyoshi a_4

    kiyoshi "He went with Eric and Tori outside, did he not?"

    show sayaka a_7

    sayaka "Tori?!"
    sayaka "She's here again?!"

    show sayaka a_16
    show kiyoshi a_5

    kiyoshi "You didn't invite her?"

    show kiyoshi a_0

    sayaka "Of course not, but she always sneaks in and steals my drinks."

    show sayaka a_7 at faceright

    sayaka "Ugh, I'm throwing her out!"

    scene black with dissolve
    pause 0.5
    outfit tori casual
    accessory eric set
    scene bg sayaka backyard night
    show tori a_10:
        center
        faceright
        xpos 0.35
    show john b_18 blush:
        center
        faceleft
        xpos 0.575
    show eric a_0:
        center
        faceleft
        xpos 0.8
    show sayaka a_7:
        center
        faceright
        xpos 0.0
        alpha 0.0
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.1
    with dissolve

    sayaka "What is going on out he-"

    show sayaka a_5

    john "-And, if I ever! Ever! See you again! {i}{b}Hic!{/b}{/i}"

    show john a_0 blush

    john "Uh..."

    show john b_18 blush

    john "Yes! That!"

    show john a_13 blush
    show tori a_17

    tori "What the hell did you give her?"

    show eric a_4
    show tori a_19

    eric "She wanted to try it, so I let her."

    show eric a_2
    show sayaka a_15
    show john a_17 blush

    eric "Got a problem with that?"

    show eric a_0
    show tori a_1

    tori "Hah, fuck no, this is hilarious."

    show john b_17 blush
    show tori a_11
    show eric a_1

    john "It is!"

    show tori a_20
    show john b_19 blush

    john "...Not! Not!"

    show john b_22 blush
    show sayaka a_7
    show eric a_0
    show tori a_11 at faceleft

    sayaka "Wha- What's going on here?!"

    show sayaka a_16
    show tori a_1

    tori "Oh, hey twerp. So you're here too."

    show tori a_0 at faceright
    show sayaka a_5
    show john b_18 blush

    john "Sayaka, I totally got this."

    show john b_19 blush
    show sayaka a_33

    john "Hey! Get over here Vicky!"

    show john b_17 blush
    show tori a_17

    tori "...I'm right next to you."

    show john b_9 blush
    show tori a_18

    john "Stop running!"

    show john b_6 blush
    show sayaka a_7
    show tori a_19 at faceleft

    sayaka "Did you have her drink your garbage, Eric?!"

    show sayaka a_16
    show eric a_1

    eric "Exactly, hahah."

    show eric a_4
    show tori a_20

    "He flashed one of the bottles he was so proud of when he arrived."

    show sayaka a_15

    "78% alcohol. Enough to basically kill anyone who drank a full bottle."
    "What the hell are any of them thinking?!"

    show sayaka a_20

    sayaka "Fuck you Eric, you knew she was hammered already!"

    show sayaka a_16
    show tori a_0 at faceright
    show eric a_0
    show john a_3 blush

    john "Hey, hey! I'm not... A hammer!"

    show sayaka a_24
    show tori a_1
    show eric a_1
    show john a_6 blush

    think "Oh god, please stop embarrassing me like this..."

    show eric a_0
    show sayaka a_16

    eric "You want some too?"

    show sayaka a_7
    show tori a_20 at faceleft

    sayaka "No! And you! Get off my property!"

    show sayaka a_16
    show tori a_17

    tori "Your property? You married to this bitch or something?"

    show sayaka a_20
    show tori a_10
    show eric a_3
    show john a_13 blush

    sayaka "Get out!"

    show tori a_13
    show eric a_7
    show sayaka a_21

    tori "Bah, as if I'd listen to you."

    show tori a_20

    tori "I got better things to do."

    show eric a_0

    "A few others were also in the garden talking, and what John was doing was clearly the main attraction for anyone who was out here right now."

    show sayaka a_16

    think "Fucks sake, does he not know how to hold back at all?"

    show sayaka a_24

    think "This is so freaking embarrassing to watch..."

    show tori a_1 at faceright
    show john a_17 blush
    show sayaka a_16

    tori "Let's go have some of your sip."

    show eric a_1

    eric "Heh, feeling ballsy?"
    tori "Hell yeah."

    show tori:
        faceleft
        pause 0.25
        ease 0.5 alpha 0.0 xpos 0.0
    show eric a_0:
        ease 0.85 alpha 0.0 xpos 0.35
    show sayaka:
        pause 0.5
        faceleft
    show john a_3 blush

    john "Hey! Toria, you aren't supposed to be here!"

    show sayaka a_24
    show john a_17 blush

    tori "{size=-5}Yeah yeah, love you too.{/size}"

    show john b_19 blush
    show sayaka a_16 at faceright

    john "No you don't!"

    show sayaka:
        ease 0.5 xpos 0.3
    show john b_17 blush

    sayaka "{size=-5}Can you shut the fuck up already?{/size}"

    show john b_11 blush

    john "Uhuh? Me?"

    show sayaka at faceleft

    "Looking around, people started minding their own business again."
    "At least he wouldn't be able to embarrass me any further for the time being."

    show sayaka a_7 at faceright

    sayaka "{size=-5}Why the hell did you drink so much?!{/size}"

    show john a_27 blush
    show sayaka a_16

    john "Wh- Whaa...?"

    show sayaka a_7

    sayaka "{size=-5}You are so fucking useless! All I wanted was to at least give people the impression that I haven't lost my mind, but now you're just making things worse!{/size}"

    show john a_17 blush

    sayaka "{size=-5}All you had to do was talk with people!{/size}"

    show sayaka a_16
    show john a_3 blush

    john "But I- But I did that!"
    john "I tried all night to talk with those stupids- Stupid people!"

    show sayaka a_20
    show john a_27 blush

    sayaka "Those people are my friends!"

    show john b_16 blush
    show sayaka a_21

    john "Hah, they are all just- They just all suck."

    show sayaka a_20
    show john b_15 blush

    sayaka "Suck?! You absolute-"

    show john b_6 blush
    show sayaka a_15

    john "Nobody even wants to hang out with you besides Kiyoshi, hah, what a loser."

    show sayaka a_20

    sayaka "You- Wh- What?!"

    show john a_32 blush

    sayaka "Would you like to repeat what you just fucking said?!"

    show john a_3 blush
    show sayaka a_21

    john "Ohoh, you want me to repeat that? For everyone to hear how freaking {i}annoying{/i} you are with nagging- With your nagging?"

    show john b_19 blush:
        pause 0.25
        ease 1.0 xpos 0.0 alpha 0.0
    show sayaka a_15:
        pause 0.55
        faceleft

    john "{size=+7}Hey everyone, I have something totally funny to say!{/size}"

    show sayaka a_4:
        faceleft
        ease 0.5 xpos 0.0 alpha 0.0

    sayaka "No- Hey- Wait! Wha- What are you doing?!"

    scene bg sayaka livingroom party
    show bg sayaka livingroom party:
        zoom 1.5 xalign 0.7 yalign 0.5
    show tori a_18:
        center
        faceleft
        xpos 0.05
        zoom 0.8
    show brad a_8 behind tori:
        center
        faceright
        xpos 0.15
        zoom 0.8
    show AN_harry a_5:
        center
        faceleft
        xpos 0.225
        zoom 0.8
    show rita b_0:
        center
        faceright
        xpos 0.35
        zoom 0.8
    show allison a_21:
        center
        faceleft
        xpos 0.45
        zoom 0.8
    show irene a_0:
        center
        faceleft
        xpos 0.525
        zoom 0.8
    show john b_3 blush:
        center
        faceleft
        xpos 0.9
        zoom 0.95
        alpha 0.0
        pause 0.25
        ease 0.5 alpha 1.0 xpos 0.725
    show sayaka a_21:
        center
        faceleft
        xpos 1.1
        zoom 0.95
        alpha 0.0
        pause 0.75
        ease 0.5 alpha 1.0 xpos 0.975
    with dissolve

    "He went into the living room again before I could react."

    show john:
        alpha 1.0 xpos 0.725
        transform_anchor True
        faceright
        pause 0.5
        ease 0.5 rotate 5 xpos 0.775
        ease 0.25 rotate 0
        faceleft
    show bg sayaka livingroom party:
        pause 0.5
        ease 0.5 yalign 0.35
    show tori a_18:
        pause 0.5
        ease 0.5 ypos 1.15
    show brad a_8:
        pause 0.5
        ease 0.5 ypos 1.15
    show AN_harry a_5:
        pause 0.5
        ease 0.5 ypos 1.15
    show rita b_0:
        pause 0.5
        ease 0.5 ypos 1.15
    show allison a_21:
        pause 0.5
        ease 0.5 ypos 1.15
    show irene a_0 behind allison:
        pause 0.5
        ease 0.5 ypos 1.15
    show sayaka a_15:
        alpha 1.0 xpos 0.975
        pause 0.5
        ease 0.5 ypos 1.15

    "Once inside, he managed to climb onto the sofa looking all triumphant."
    "He looked at everyone, with some people seeing him pulling this stunt."
    think "Fuck, fuck fuck, what is this drunk ass doing?!"

    show john b_16 blush
    show brad a_4
    show AN_harry a_3 at faceright
    show tori at faceright
    show rita b_11
    show allison a_24 at faceright
    show irene a_5 at faceright

    john "Heheey, everyone! A friend of mine {i}really{/i} wanted me to introduce myself to everyone so that we {i}all get along just fine!{/i}"

    show sayaka a_2:
        ease 0.5 xpos 0.925
    show john b_15 blush

    sayaka "{size=-5}Get down from there, please!{/size}"

    show john b_17 blush:
        faceright
        ease 0.15 xpos 0.79
        ease 0.35 xpos 0.775
    show sayaka:
        ease 0.3 xpos 0.95

    john "As if I have to listen to you! Get off me!"

    show john b_16 blush at faceleft
    show brad a_9
    show irene a_8

    john "Hey, guys! You all know me as Sayaka Sato, I bet! But do you know what else my name is?"

    show sayaka a_15

    think "Wait. No."

    show john b_2 blush
    show allison a_26

    john "That's right, I have a {i}really cool{/i} middle name too! Anybody want to guess?"

    show john a_14 blush

    irene "What the hell is going on with her?"

    show john a_16 blush

    john "Aha, no takers, well, I have apparently {i}never{/i} told anyone about it before!"

    show john b_16 blush

    john "That's right! Sayaka {q}Sparrow{/q} Sato!"

    show sayaka a_25
    show allison a_22
    show irene a_0
    show tori a_1
    show AN_harry a_6
    show rita a_5
    show john a_15 blush

    sayaka "No no {size=+5}no no{/size}!"

    show sayaka a_21
    show tori a_20

    tori "Pfft, for real?"

    show irene b_1
    show rita a_14

    irene "Ahahahah... Seriously?! Sparrow?"
    rita "What kind of shitty parents name their daughter {q}Sparrow{/q}?"

    show rita a_19
    show brad a_14

    rita "Did they think they were going to raise a bird?"
    think "Oh god, no."
    "I never intended for anyone to know. I made sure never to use that shitty name at all. How the fuck did he figure that out?!"

    show AN_harry at faceleft
    show brad a_13

    "He must have found it by snooping around in some private stuff! That absolute...!"

    show john a_14 blush

    john "Hahah, funny, right? And I probably never even told you guys because it's such a stupid name!"

    show john b_16 blush at faceright
    show brad:
        ease 1.25 xpos 0.6 zoom 0.9
    show AN_harry:
        pause 0.25
        faceright
        pause 0.25
        ease 0.5 xpos 0.175
    show rita a_8:
        pause 0.65
        ease 0.5 xpos 0.275
    show allison:
        pause 0.7
        ease 0.5 xpos 0.35
    show irene:
        pause 0.75
        ease 0.5 xpos 0.45

    john "So. Incredibly. Stupid!"

    show john b_15 blush at faceleft

    brad "{size=-5}What exactly is going on with you?{/size}"

    "Brad had come up from the back of the crowd of people and was staring at this fucking moron having the time of his life apparently."

    show sayaka a_15

    sayaka "He- He is-"

    show john b_19 blush
    show irene a_0

    john "Oh yeah! Speaking of parents! Do you guys know {i}just how little{/i} they care about me?"

    show brad a_14
    show john b_16 blush

    john "Imagine this, right? Every day, they just don't give {i}a single shit{/i} about me! Just overall horrible people that don't even want to see me!"

    show AN_harry a_4
    show sayaka a_24
    show allison a_3

    john "My response? Cool! As long as they don't get in the way of me trying to bitch around {i}everyone around me{/i}!"

    show irene a_8

    john "They even told me that I look ugly with glasses on, can you believe that?"

    show john b_18 blush
    show sayaka:
        faceright
        ease 0.5 xpos 0.965 ypos 1.2
    show brad a_5

    sayaka "{size=-5}No- no, please stop...{/size}"

    show brad at faceleft

    john "Is it my fault they gave me some shitty nearsighted eyes? Apparently it totally is!"

    show john b_19 blush

    john "Actually, their horrible treatment is a positive! Because I get more time to practice being a terrible piece of shit myself, just like them!"

    show john a_16 blush

    john "A complete win-win situation!"

    show john a_15 blush

    irene "...She's lost it."

    show rita a_9
    show irene at faceleft

    rita "Yeah, and it's hella hilarious."

    show rita a_0
    show john b_16 blush at faceright
    show brad at faceright
    show irene at faceright
    show sayaka a_2 at faceleft

    john "Aahhh~~hahaha, take that, you stuck up bitch!"

    show john b_18 blush at faceleft

    john "And get this, they don't even give me any allowance if I don't get the grades they tell me! So this next month, I'm practically going in with almost no money to buy stuff with. Woohoo for capitalism!"

    show john b_3 blush

    irene "...Let's just get out of here."
    think "..."

    show brad a_2

    brad "Sayaka, seriously, what is this about?"

    show brad a_13
    show john b_16 blush

    john "Hey now! I'm {i}totally{/i} not forcing you annoying leeches to stay, but feel free to come back to this ghost house during halloween! Maybe we might catch a ghost of my parents!"

    show sayaka a_15
    show john a_3 blush
    show brad a_18
    show AN_harry a_6
    show rita a_12
    show irene a_3
    show allison a_26

    john "I could even increase immersion by putting on the costume of a psycho- Oh wait, I already fucking am one!"

    show john a_17 blush
    show sayaka a_2

    sayaka "{i}Sniff...{/i}"

    show rita b_12:
        faceleft
        pause 0.5
        ease 0.75 xpos 0.15 alpha 0.0
    show allison b_4:
        pause 0.75
        faceleft
        pause 0.75
        ease 0.5 xpos 0.325 alpha 0.0
    show irene a_8:
        faceleft
        pause 1
        ease 0.75 xpos 0.4 alpha 0.0

    think "..."
    "Tears were piling up now."

    show brad a_2
    show john a_13 blush

    brad "Alright, you're getting down from there, now!"

    show tori a_12:
        pause 1
        faceleft
        ease 0.75 xpos -0.05 alpha 0.0
    show brad a_14

    tori "Ahahah, that's the most hilarious thing I've seen in a while!"

    show sayaka a_15

    "He was completely humiliating me in front of everyone. Everyone who mattered was starting to leave."

    show sayaka a_2

    "And worst of all, he-"

    show brad a_3
    show AN_harry a_4:
        ease 0.75 zoom 0.9 xpos 0.25

    brad "Sayaka, what the hell are you doing?"

    show AN_harry a_6

    AN_harry "I was about to ask the same. What was that all about?"

    show john b_2 blush

    john "I am just telling everyone exactly who I am."

    show brad a_18

    brad "You- Oh, for god's sake-"

    show brad a_14

    brad "Get down from there already you lunatic."

    show john b_6 blush

    john "I- Uh- Whoah, there's far down from here."

    show brad a_14

    brad "It's 30 centimeters..."

    show brad a_3

    brad "{i}Sigh...{/i} Here, grab on."

    show bg sayaka livingroom party:
        ease 0.75 yalign 0.5
    show john b_11 blush:
        parallel:
            ease 0.5 xpos 0.7
        parallel:
            ease 0.5 ypos 1.05
            ease 0.25 ypos 1.0
    show brad:
        ease 0.75 ypos 1.0 xpos 0.45
    show sayaka:
        ease 0.75 ypos 1.05
    show AN_harry:
        ease 0.75 ypos 1.0

    john "Oh, thank you very much."

    scene black with Dissolve(1.5)
    pause 0.5

    title "27th of August (Saturday)" "Day 20 - John"

    scene bg sayaka livingroom party
    show john b_6 blush:
        center
        faceleft
        xpos 0.6
    show brad a_3:
        center
        faceright
        xpos 0.4
    show AN_harry a_3:
        center
        faceright
        xpos 0.2
    show sayaka a_2:
        center
        faceleft
        xpos 0.875
    with dissolve

    think "Oohhh, boy, I might have had a little too much after all."
    "Sayaka told me she could take an unusual amount of alcohol before she really got sick, but even so, the few drinks I had were making me very dizzy. I felt especially weird after taking in a little shot of what Eric had..."

    show john b_15 blush

    "But, finally, she got what she rightfully deserved. Hah, take that, you annoying hag."

    show john b_1 blush

    "Brad had extended his hand so I could get down from the couch without tripping."

    show john a_13 blush

    "But for some reason, everyone here looked at me in a... Uh... Weird way?"
    think "What, do they want more?"

    show john b_11 blush at faceright

    "Sayaka herself, of course, was standing there like a total crybaby."

    show john b_15 blush
    show sayaka a_21

    "One look at her was enough to make her contort her face to her typical angry self."

    show john a_13 blush
    show brad a_14

    brad "Mind explaining what went through your head in more detail?"

    show john b_2 blush at faceleft

    john "Oh, that little show? Hah, I'm glad you aske-"

    show john b_7 blush
    show brad a_2
    with hpunch

    brad "You call that a show?"

    show john b_27 blush
    show brad a_14

    john "Uh.. Well, yeah.. Wasn't it?"

    show brad a_19

    brad "Look at her for just a second and tell me she enjoyed that."

    show brad a_13
    show AN_harry a_6

    AN_harry "Why did you say all of that?"

    show john b_17 blush:
        pause 1.0
        faceright

    john "Oh, it's because John over there had it coming! Exactly."

    show AN_harry a_2

    AN_harry "...?"

    show brad a_5
    show john b_5 blush at faceleft

    brad "...Look, I know you two really... Uh... Dislike each other. But this really went too far, especially for you."

    show john a_32 blush

    john "She told me to say all of this. Not my fault."

    show brad a_13
    show AN_harry a_3
    show sayaka a_35
    show john a_6

    sayaka "Y- You-"

    show john a_24

    think "Heh, she's totally trembling. I bet she is really mad."

    show john b_11:
        pause 0.5
        faceleft
    show sayaka a_24:
        ease 0.75 xpos -0.2 alpha 0.0
    show brad:
        pause 0.65
        faceleft
    show AN_harry:
        pause 0.75
        faceleft

    "Without another word, she blazed out of the livingroom, straight to the kitchen."

    play sound sfx_door_close

    "After a bit of more time, I could hear a distant front door slamming."

    show brad a_14

    brad "{i}Sigh...{/i}"

    show brad at faceright

    brad "Weren't you two supposed to be working together on this?"

    show AN_harry at faceright

    john "Working together?"
    brad "...Does this guy know about your situation?"

    show brad at faceleft
    show john b_13 blush
    show AN_harry a_2

    "He pointed at Harry who was seemingly speechless at what happened."
    AN_harry "...What situation?"

    show AN_harry a_3
    show brad a_13 at faceright
    show john b_4 blush

    john "Uhm... No, he doesn't."

    show brad a_9

    brad "Alright. Come with me, we're going to have a talk in private."

    show brad a_7

    brad "Sorry Harry, can you wait here?"

    show AN_harry a_7

    AN_harry "Ehm... Sure, this sounds like something between friends..."

    show john b_11 blush:
        faceright
        ease 0.25 xpos 0.5
        pause 0.5
        ease 0.75 alpha 0.0 xpos 0.75
    show brad a_13:
        parallel:
            ease 1.25 xpos 0.775
        parallel:
            pause 0.5
            ease 0.75 alpha 0.0

    "Without much of a warning he grabbed my arm and dragged me along with him."

    scene black with dissolve
    pause 0.5
    scene AN_bg sayaka hallway night
    show john b_4 blush:
        center
        faceright
        xpos 0.35
        pause 0.5
        ease 0.5 alpha 1.0 xpos 0.45
    show brad a_14:
        center
        faceright
        xpos 0.45
        pause 0.25
        ease 0.75 alpha 1.0 xpos 0.65
    with dissolve

    brad "Anyone here?!"

    show brad a_9:
        alpha 1.0 xpos 0.65
    show john:
        alpha 1.0 xpos 0.45

    brad "..."

    show brad a_7

    brad "Seems not."

    show brad a_14 at faceleft
    show john b_5 blush

    brad "Alright, what's going on between you two?"

    show john b_13 blush

    john "Uhm... She told me to act like herself...?"

    show brad a_18

    brad "What part of that was acting as {q}herself{/q}?"

    show john b_18 blush

    john "She's been a pain in the ass, dude! She asked for this!"

    show brad a_9
    show john b_3 blush

    brad "{i}Sigh...{/i}"

    show brad a_14

    brad "Didn't you both want to figure out how to do that swapping thing?"

    show brad a_13
    show john b_5 blush

    john "...Well- Well yeah. But how do you even know we swapped?"

    show brad a_3

    brad "...You literally told me a few weeks ago."

    show john a_30 blush

    john "...Oh, right."

    show john a_13 blush

    brad "Queenie has also been feeling down lately, so I thought the least I could do was talk with her during school."

    show john b_11 blush

    john "Wait, who is {q}Quee-{/q} Oh, Sayaka."

    show brad a_14
    show john b_5 blush

    brad "Yes. Again, what made you think that humiliating her like that is going to be helpful to anyone?"

    show john b_6 blush
    show brad a_13

    john "Aw, come on, what I said wasn't even that bad..."
    brad "It sure looked that way."

    show brad a_9
    show john b_0 blush

    brad "Have you ever seen her act like that?"

    show john a_5 blush
    show brad a_3

    john "What, you mean angry?"

    show brad a_13

    brad "No, depressed."

    show john a_4 blush

    john "..."

    show brad a_5

    brad "...{i}Sigh{/i}..."

    show brad a_23

    brad "...Look, I don't {i}particularly{/i} like her either, but what you did there was stepping over the line."

    show john b_4 blush
    show brad a_5

    john "Well, yeah, but she has done that herself..."
    brad "So what? Two wrongs don't make a right."

    show john b_0 blush
    show brad a_8

    brad "Look at it this way; Have you ever experienced Sayaka cry?"

    show brad a_7
    show john b_4 blush

    john "..."
    john "...No."

    show john b_13 blush

    think "...Alright, maybe I did overstep my boundaries a bit."

    show john b_25 blush

    john "...So you want me to apologize to her?"

    show brad a_5

    brad "I didn't say that. But if that's what you got out of this, then that is probably what you think is the right thing to do."

    show john b_22 blush

    think "...He got me there..."

    show john b_19 blush

    john "Urgh, fine!"

    show john a_6 blush

    john "But all I'm going to do is apologize for this. She is still a bitch."

    show brad a_3

    brad "Telling me what she is won't change anything."

    show john a_13 blush

    john "Right."

    scene black with dissolve
    pause 0.75
    scene bg sadie bathroom day
    show john b_5 blush:
        alpha 0.0
        center
        faceright
        pause 0.75
        ease 0.5 alpha 1.0 centerright
    with dissolve
    play sound sfx_door_open

    "Before I'd go out looking for the crazy lady, I decided to quickly take out the contacts that had been injected into my eyes."

    #TODO: face b_5 blush with glasses
    accessory john set glasses
    show john:
        alpha 1.0 centerright
    with dissolve

    "Walking around with glasses was way more comfortable."

    scene black with dissolve
    show bg sayaka livingroom party:
        zoom 1.75 xalign 0.0 yalign 0.65
    show cornelia a_19:
        transform_anchor True
        offscreenleft
        zoom 0.8
        rotate 85
        ypos 1.025
        xpos -0.1
    show maria a_5:
        centerleft
        faceleft
        zoom 0.9
    show AN_harry a_3:
        center
        faceleft
        xpos 0.55
    show audrey a_1:
        center
        faceright
        xpos 0.975
        zoom 0.9
    #TODO: add a_0 blush with glasses
    show john a_0 blush:
        center
        faceleft
        alpha 0.0
        xpos 0.75
        pause 0.25
        ease 0.5 alpha 1.0
    with dissolve

    "People were still around downstairs, but it was obvious that a lot of people had left now."

    show john:
        alpha 1.0

    "Some were still dancing around to the music though."

    show AN_harry at faceright

    "I had hoped that Sayaka had come back after she left, but after looking around, she wasn't anywhere to be seen."

    #TODO: add b_0 blush with glasses
    show john b_0 blush:
        ease 0.5 xpos 0.7

    john "Hey Harry, have you seen John?"

    show AN_harry a_8

    AN_harry "Of course not, he left after you did... That."

    #TODO: add b_6 blush with glasses
    show john b_6 blush

    john "Right..."

    show john b_0 blush
    show AN_harry a_3

    john "..."

    show john b_6 blush

    john "Also, what's with her?"

    show AN_harry a_8 at faceleft

    AN_harry "Cornelia? Hungover already, apparently."

    show AN_harry a_3 at faceright

    john "..."
    "Cornelia looked absolutely terrible and looked like some dead girl the way she was sitting on the couch."

    show john b_0 blush

    john "I'm not gonna ask what happened. I'm going to try finding John."
    john "Can you, uh... Hold down the fort while I'm gone?"

    show AN_harry a_2

    AN_harry "Uhh... You want me to {q}hold own the fort{/q}?"

    #TODO: add b_2 blush with glasses
    show john b_2 blush

    john "Thanks, I appreciate it."

    show john b_0 blush:
        ease 0.75 alpha 0.0 xpos 0.35
    show AN_harry a_5:
        pause 0.35
        faceleft

    AN_harry "Wai- Wha-"

    scene black with dissolve
    pause 0.5
    outfit vanessa casual
    scene bg sayaka house night lights on
    show vanessa a_13:
        center
        faceright
        zoom 0.9
        xpos 0.1
    show tori a_1 behind vanessa:
        center
        faceright
        xpos 0.2
        zoom 0.9
    show eric a_1:
        center
        faceleft
        xpos 0.4
        zoom 0.9
    show john a_0:
        centerright
        faceleft
        alpha 0.0
        pause 0.25
        ease 0.5 alpha 1.0
    with dissolve

    "I couldn't find her anywhere outside her house."

    show john b_25:
        faceright
        alpha 1.0
    show eric a_0 at faceright
    show tori a_11
    show vanessa a_8

    "Some random people were sitting out here with a bottle of beer each, and the moment they looked at me, I turned my head away as if not noticing them."
    think "I can't be bothered talking to some drunkards right now..."

    scene black with dissolve
    pause 2
    show bg beach road night
    show john b_5 at centerleft, faceright
    with Dissolve(1.0)
    pause 0.75

    "I think I spent about 30 minutes just walking around the premises without being able to find her."
    "It was nice to get the dizziness out of the system, but there wasn't any trace of her in the city."

    show john b_22:
        parallel:
            ease 1.2 xpos 0.65
        parallel:
            ease 0.5 ypos 1.1
            ease 0.6 ypos 1.0
    show bg beach road night:
        ease 1.2 zoom 1.75 xalign 0.85 yalign 0.6

    "I had just about given up and was walking home now along the beach. She most likely went to my home and straight to bed or something..."
    think "Ugh, it's getting really chilly..."

    show john b_13
    pause 2

    "I couldn't help but notice how beautiful the vast sea looked right now."
    "It reflected the moonlight just right."
    think "Man, it had been a weird ride for the last 3 weeks in retrospect."
    think "If this swap never happened to me then my life would be completely different right now."

    pause 1

    think "..."
    "After admiring the view for a few seconds, I looked around at the beach. It was completely empty, which shouldn't surprise anyone considering the current time."

    show john b_25

    "But there was something quite large and out of the ordinary some few hundred meters away, which caught my interest."

    show john b_27

    think "Wait, isn't that Sayaka?!"

    show john b_5

    think "Finally, so that's where she's been hiding."

    show john b_6

    think "But, uh... Do I just walk up to her...?"
    think "..."
    think "I can already imagine how awkward this is going to be."

    scene black with dissolve
    pause 0.5
    scene bg beach rock night
    show sayaka a_2:
        center
        faceleft
        xpos 0.7
        ypos 1.15
    show john b_4:
        center
        faceright
        xpos 0.0
        alpha 0.0
        pause 2
        ease 0.75 alpha 1.0 xpos 0.2
    with dissolve
    pause 4
    show john b_1:
        alpha 1.0 xpos 0.2

    john "Uh... Hey!"

    show sayaka a_5

    sayaka "..."

    show john b_4

    think "I guess she is still angry."

    show sayaka a_2
    show john b_5

    "She was sitting on the sand and had shot me a glance, but she immediately started looking out at the sea again."
    john "..."

    show john b_4
    show sayaka a_5

    john "Uhm... I just wanted to say that I'm so-"

    show john b_0

    sayaka "Shut up."

    show john b_17

    john "..."

    show john b_18

    john "Wow. Alright."

    show john b_17
    show sayaka a_9

    sayaka "..."

    show sayaka a_27
    show john b_0

    sayaka "I'm sorry..."
    sayaka "I..."

    show john a_27

    think "Wait a minute- That's the first genuine sounding {q}sorry{/q} I've heard from her!"

    show john a_0

    john "...You're sorry about what?"

    show sayaka a_7

    sayaka "I'm saying I'm sorry, alright?!"
    sayaka "For everything!"

    show john a_28
    show sayaka a_27

    john "...Really?"

    show sayaka a_25

    sayaka "Do you think I'm lying? I didn't know that my parents got to you like that, alright?!"

    show john b_1
    show sayaka a_24

    think "..."
    "She actually feels sorry for my situation...?"

    show john b_0 at faceleft

    "I looked around to check if anyone was nearby, but nobody could be spotted."

    show john a_10:
        faceright
        ease 0.75 xpos 0.4
        pause 0.5
        ease 0.5 ypos 1.15
    show sayaka a_27

    "I took the initiative to sit down next to her. The way she was sitting, knees up to her head with her arms wrapped around them just made it look like she was really sad."

    show sayaka a_5

    john "...Thanks."
    john "I've started getting used to it by now, but... You know, it still gnaws at me."

    show john b_1

    john "Even if they aren't my actual parents."

    show sayaka a_27

    sayaka "...I know."

    show sayaka a_31
    show john b_0

    sayaka "They haven't always been so distant."

    show sayaka a_0

    sayaka "I used to go shopping with mom all the time, and it was some of the best times I ever had."
    sayaka "We used to spend evenings watching our favorite shows, and she taught me all about self-preservation back before she got promoted..."

    show sayaka a_31

    sayaka "And dad was always around when I got home from school and made us food that we used to eat together..."
    sayaka "..."

    show john b_4

    john "...They both ended up becoming really attached to their jobs, huh?"

    show sayaka a_27

    sayaka "...Yeah..."

    show sayaka a_2
    show john b_0

    sayaka "Mom got promoted and has to be available all the time in case something happens, and dad runs some corporation he says he can't talk about..."
    john "...Yikes."

    show john a_4

    "I really should have figured out that this was a painful topic for her to be mocked about..."
    "Even if I didn't care about her, it's still sensitive."

    show sayaka a_27
    show john a_0

    sayaka "{i}Sigh...{/i} It's all just gone to shit..."
    "She shook her head in slow motion and wiped her eyes with the side of her hand."

    show sayaka a_5:
        transform_anchor True
        parallel:
            ease 2 rotate 85
        parallel:
            ease 1 xpos 0.7 ypos 1.25
            ease 1.5 alpha 0.0

    "Soon after she let herself lay down in the soft beach sand."

    scene AN_bg beach night topdown
    show sayaka a_5:
        transform_anchor True
        faceleft
        rotate 10
        zoom 1.75
        center
        ypos 1.65
        xpos 0.1
    show john a_0:
        transform_anchor True
        faceright
        zoom 1.75
        center
        ypos 1.65
        xpos 0.9
        alpha 0.0
        pause 1.5
        ease 0.75 alpha 1.0 rotate -10
    with dissolve

    "I joined her since it felt like the right thing to do."
    "I came here just to say sorry, but staying with her for a while was what we both probbly needed to patch up the hole between us."

    show john a_10:
        alpha 1.0 rotate -10

    "Besides, the sky had next to no clouds and I was tired, so it was nice lying down in the sand of a beach. Kind of idyllic too."

    show sayaka at faceright
    show john a_0

    sayaka "...Were you being serious when you said you started talking to Katrina again?"

    show john a_4

    john "Uhm... Well, she talked to me, but, uhm... Said she couldn't really... Stand looking at me..."

    show john a_13

    john "I still don't really know what happened between you two, so I don't really understand what even makes her hate you so much... Besides, you know..."

    show sayaka a_2

    sayaka "Besides what?"
    john "You being a bit of a bully towards her and Kyoko, I guess..."

    show sayaka a_5 at faceleft

    sayaka "{i}Sigh{/i}... Yeah, I guess..."

    show john a_4

    john "..."

    show john a_5 at faceleft

    john "...Did something bad happen between you?"

    show sayaka a_31

    sayaka "..."

    show sayaka a_5

    sayaka "...Even if I told you what happened, you'd think I was lying to you."
    sayaka "I can't even fully remember it anymore."

    show john b_1

    john "If you swear that you're telling the truth, then I don't really have any choice but to believe you, right?"

    show sayaka a_33 at faceright

    sayaka "That is not how that works."

    show sayaka a_5
    show john b_5

    john "If there is one thing I know, it's that honor is a really important thing, you know?"
    john "Swearing on your name is something that you cannot take back."

    show sayaka a_32

    sayaka "...What, did you come from the medieval ages or something?"

    show john b_29

    john "Come on, it's just as relevant for me to know if I'm stuck as you. I'll believe you unless what you're saying is too weird."

    show john b_1
    show sayaka a_5 at faceleft

    sayaka "...Fine..."

    show john a_0

    sayaka "We actually used to be pretty good friends, if I remember right."

    show john a_13

    sayaka "Katrina's mom was close to mine since they worked together."

    show sayaka a_32

    sayaka "I think we were friends since preschool or something... I can't really remember when exactly we met."

    show sayaka a_5

    sayaka "We did homework together, invited friends over, all that stuff."

    show sayaka a_33

    sayaka "I think I even said she was my best friend or something disgusting like that once."

    show john a_6
    show sayaka a_5

    john "Hey, hey, none of the insults now, please..."

    show sayaka at faceright
    show john a_0

    sayaka "So then, what do you think happened?"

    show john a_30

    john "Uh.. You had a fight?"

    show sayaka a_7 at faceleft

    sayaka "Bah, if it were that easy."

    show sayaka a_16
    show john a_0

    think "So something serious happened?"
    sayaka "How would you react if you found out your best friends were just using you all the time?"

    show john a_5

    john "Using you? For money?"
    sayaka "Yeah."

    show john a_4

    john "Well, I would probably get really angry."

    show john b_0

    john "That's what happened?"

    show sayaka a_5

    sayaka "Partially."
    sayaka "I think I overheard them talking about how I {q}wasn't giving them enough money{/q} at some point."

    show john a_0

    sayaka "So I confronted them, and they started all kinds of rumors about me and treated me like some 3rd class citizen all of a sudden."

    show sayaka a_33

    sayaka "Realy good friends, huh?"

    show sayaka a_16
    show john b_4

    sayaka "The moment they don't see any benefit in you, they throw you to the side of the road."

    pause 1.5

    john "..."
    john "...I find it hard to believe that Kat would do something like that..."

    show john b_0
    show sayaka a_19 at faceright

    sayaka "Oh, so {i}now{/i} your entire {q}swearing on your name{/q} thing conveniently goes up in smoke."

    show john b_8

    john "Hey, I didn't say that I {i}don't{/i} believe you."

    show sayaka a_9 at faceleft
    show john b_13

    sayaka "Right..."

    show sayaka a_27

    sayaka "Sorry, I need to calm down from all of this."

    show john b_1

    john "Take your time. We've got all night."

    show sayaka a_9

    sayaka "{i}Sigh...{/i}"

    show sayaka a_5
    show john b_0

    sayaka "Anyways, those pigs made my life hell in middle-school. And then, after a few years when it's convenient for her, she suddenly starts crying for forgiveness to me, claiming {q}she wasn't a good enough friend and that she would make up for it if I let her{/q}."

    show sayaka a_16

    sayaka "In all seriousness, the fucking nerve she has to tell me how {q}{i}she's so sorry{/i}{/q} after making me go through middle-school for four years without anyone to talk to because they decided I wasn't good enough based on made-up rumors..."

    show sayaka a_25

    sayaka "Can you imagine how it feels like to be rejected by everyone else as a kid? I fucking {i}hate them all{/i} for doing that!"

    show sayaka a_16
    show john b_4

    john "...Sounds rough."

    show sayaka a_27

    sayaka "{i}Sigh...{/i} Not like that matters now anyways, I wanted to make sure people wouldn't take me as a joke in high school at least, but I guess that is going to happen now too, huh..."

    show john b_13

    think "But if she hates Kat so much, then why does she keep that photo she has with her?"

    show sayaka a_5
    show john b_11

    john "...You really don't have any attachment to Kat or anything?"

    show sayaka a_16

    sayaka "Why would I want attachment to that backstabbing bitch? Her mom was nice, and her sister was cool too if I remember right, but her? No chance."

    show john a_0

    think "Oh, Kat's mom? Well that's a convenient answer to why she has the photo."

    show sayaka a_25

    sayaka "Ugh, but it's just {i}so annoying{/i} that not even my parents give a shit anymore."

    show sayaka a_16

    sayaka "They think that I'm doing fine on my own now that people don't look down on me and that I don't need any special treatment from them anymore."

    show sayaka a_27

    sayaka "...But I do..."

    show john a_4

    sayaka "I just... Really want them to make me something good for dinner for once again..."

    show sayaka a_5

    sayaka "Or maybe just, ask me if I'm okay, or watch a movie with me, or make me something for breakfast..."

    show sayaka a_16

    sayaka "And Ms. Davis does all of that without even knowing it's me..."

    show sayaka a_7 at faceright
    show john a_27

    sayaka "For real, fuck you, John!"

    show john b_11
    show sayaka a_16

    john "Uh..."
    john "My mom did something?"

    show sayaka a_7

    sayaka "Not just your mom! I admit it, your life is so much fucking better than mine!"

    show sayaka at faceleft

    sayaka "You have her, you have friends, you have {q}hobbies{/q}, nobody cares how you look, how you act, and you've got relatives that come over regularly, fuckloads of girls that apparently want to get into your pants for god knows what reason-"

    show sayaka a_16
    show john b_27

    sayaka "Seriously, what the fuck did you do to deserve so much better?"

    show john b_28

    john "Wai- Wait, repeat that last one again?"

    show john b_27

    show sayaka a_32 at faceright

    sayaka "Huh? Oh, the girls in your pants?"

    show sayaka a_5 at faceleft

    sayaka "Yeah, I asked a handful of girls if they wanted to be your girlfriends to get payback on you and they all said yes."
    sayaka "Still fucking beats me what's going on in that department."
    sayaka "I can't even remember why I did it anymore."

    show john b_7

    john "Uhm... Alright then..."

    show sayaka a_24
    show john b_0

    sayaka "{i}Sigh...{/i} And everything you said back then is true too..."

    show sayaka a_5

    "With a wave of relief she stretched herself out, with her hands towards the sky."

    show sayaka a_9

    sayaka "I really hate my life..."

    show sayaka a_27

    sayaka "But I can't help but enjoy things in your life..."

    show sayaka a_2

    sayaka "I don't have anything that you have..."

    pause 1
    show john a_4
    pause 1.5

    john "..."

    show sayaka a_5
    show john a_30

    john "...You okay?"

    show sayaka a_27

    sayaka "..."

    show sayaka a_16
    show john a_0

    sayaka "No..."

    show sayaka a_5

    sayaka "No matter how I look at this, there is no way I'm going to win against anyone at this rate."

    show sayaka a_16

    sayaka "Whoever did this... Swapping thing, has won."
    sayaka "And you turned out to be the one who wins between us both as well. I fucking hate it."

    show john a_6
    show sayaka a_5

    john "I won? You saw this entire spectacle from the last three weeks as some kind of competition?"

    show sayaka a_16

    sayaka "Of course not. But I just really fucking hate losing to anyone..."

    show sayaka a_27
    show john a_0

    sayaka "I'm just... Really afraid of losing, I guess..."

    show sayaka a_9

    john "..."
    think "Really, this wasn't the plan..."

    show john a_4

    think "All I wanted was to give her a short sorry and then screw off again. But here she is admitting to her own faults?"

    show john a_5
    show sayaka a_5 at faceright

    john "{i}Sigh...{/i} Fine, maybe we both jumped the gun when we said we would cut off all contact last day. We both need each other if we stay like this after all."
    sayaka "..."

    show john b_5

    john "...But really, did you see me as your opponent all this time?"

    show sayaka a_16

    sayaka "...Obviously. You're friends with {i}her{/i}."

    show john a_0
    show sayaka a_5

    john "Right."

    show john a_13

    john "Then let's change it from now on. I know you're one for underhanded tricks, so-"

    show sayaka a_33

    sayaka "Rude."

    show sayaka a_5

    john "You know it's true. So why not just join the winning team if you're on the losing team?"

    show sayaka a_32

    john "We could be kind of like a team together instead of just opponents, right?"

    show sayaka a_16

    sayaka "God, you really suck at being cheesy."

    show john b_18

    john "Hey, I'm trying to motivate you!"

    show john b_17

    sayaka "Yeah yeah, what you're saying just sounds like some pickup line from an 80's love movie."

    show john b_13

    john "...Don't you like those?"

    show sayaka a_16

    sayaka "Well, yeah..."

    show john b_5

    john "...Good. So let's stop being each other's arch nemesises or something and just get along, right?"

    show sayaka a_9

    sayaka "..."

    show sayaka a_5

    sayaka "{i}Sigh...{/i} Fine. But I'm still trying to figure out how to reverse this."

    show john a_0

    john "Which is completely fine by me."

    show sayaka a_27

    sayaka "And, uh..."

    show sayaka a_5 at faceright

    sayaka "There is still that one thing we haven't tried yet."

    show john a_5

    john "...?"

    show john b_0

    john "That one thing?"

    show sayaka a_16

    sayaka "The thing Kiyoshi wanted us to do since day one?"

    show john b_13

    sayaka "Hello?"

    show john b_11

    john "...The wha- {nw}"

    show john b_27

    extend "Oh please don't tell me you mean kissing."
    sayaka "Let's just get it over with, alright? There is nobody around so it's now or never."

    show john b_28

    john "Are you- But-"

    show john b_9

    john "...Argh, fuck it, alright then, let's just get this over with."

    scene black with dissolve
    pause 3
    scene bg beach rock night
    show john b_9:
        transform_anchor True
        center
        faceright
        xpos 0.6
        pause 0.25
        ease 0.75 xpos 0.7 rotate 8 ypos 1.15
    show sayaka a_21:
        transform_anchor True
        center
        faceright
        xpos 0.45
        pause 0.5
        ease 0.5 xpos 0.4
    with dissolve

    john "{i}Cough{/i} Oh fuck-"

    show sayaka a_25 at faceleft

    sayaka "-Ew!"

    show john b_28:
        faceleft
        ease 0.5 rotate 0
    show sayaka a_21

    john "Why the hell did you suggest this?! You made me kiss myself!"

    show sayaka a_20:
        ease 0.5 xpos 0.25 rotate -10 ypos 1.2
    show john b_27

    sayaka "What the fuck do you think it feels like for me?!"

    show sayaka a_25

    "She had gone closer to the water to spit out the thought of the kiss from her head."

    show john b_19
    show sayaka a_21:
        faceright
        ease 0.5 rotate 0

    john "Don't girls like kissing other girls or something?"

    show sayaka a_20
    show john b_27

    sayaka "Who the fuck made you have that sick idea?! Do you really think a straight girl would like kissing another straight girl?!"
    sayaka "Don't tell me you watch the same sick shit as Kiyoshi does!"

    show sayaka a_21
    show john b_28

    john "Of course not!"

    show john b_9:
        ease 0.2 rotate -5
        ease 0.35 rotate 0

    john "{i}Cough!{/i} Ow- Fuck! We are {i}NEVER{/i} doing this again!"

    show john a_17
    show sayaka a_7

    sayaka "And we can both agree on that!"

    scene black with Dissolve(2.0)
    pause 1

    title "27th of August (Saturday)" "Day 20 - Cornelia and Kiyoshi"

    scene bg sayaka house night lights off
    show cornelia a_4 at right, faceleft
    show kiyoshi a_4 at centerright, faceleft
    show irene a_0:
        center
        faceright
        xpos 0.05
        zoom 0.85
    show allison a_22:
        center
        faceleft
        xpos 0.2
        zoom 0.85
    with dissolve

    kiyoshi "Hmm..."
    cornelia "..."

    show kiyoshi a_9

    kiyoshi "Say... Have you ever noticed it?"
    cornelia "..."

    show kiyoshi a_2

    kiyoshi "{q}Noticed what?{/q} you ask?"

    show kiyoshi a_1

    cornelia "..."

    show kiyoshi a_3

    kiyoshi "Good question. I believe it requires some studying, but have you ever noticed how the magnificent Allison has a purple glow on the back of her hair?"

    show kiyoshi a_0

    cornelia "..."

    show kiyoshi a_11

    kiyoshi "Perhaps she is an alien of some sorts... But I would have to think about which kind."

    show kiyoshi a_10

    cornelia "..."

    show kiyoshi a_5

    kiyoshi "I would need to consult my encyclopedia about species of aliens that have LED lights installed in their back-necks."

    show kiyoshi a_0
    show cornelia at anim_fall_over_right
    pause 0.5
    play sound sfx_whack
    with hpunch

    kiyoshi "..."

    show kiyoshi at faceright

    kiyoshi "Cornelia?"

    show kiyoshi a_4

    kiyoshi "...?"

    show kiyoshi a_3:
        ease 0.75 xpos 0.75 ypos 1.2

    kiyoshi "...You alright?"

    scene black with Dissolve(1.0)
    pause 0.5
    outfit john uniform_pony_pants
    outfit cornelia uniform
    outfit sayaka uniform_c
    outfit kiyoshi uniform
    outfit irene uniform
    outfit allison uniform
    outfit rita uniform

    title "5th of September (Monday)" "Day 29 - John"

    scene bg school hallway2 day
    show john b_0:
        center
        faceleft
        xpos 0.6
        pause 1.5
        faceright
    show cornelia a_5:
        center
        faceleft
        xpos 0.85
    show irene b_1:
        center
        faceleft
        xpos 0.25
        pause 4
        ease 0.75 alpha 0.0 xpos 0.05
    show allison a_10:
        center
        faceright
        xpos 0.05
        pause 3
        faceleft
        pause 0.5
        ease 0.75 alpha 0.0 xpos -0.15
    with dissolve

    cornelia "We're doing it now, right?"
    john "No better time than now."

    show cornelia a_1

    cornelia "Okay. Count on me."

    show john b_3:
        faceleft
        pause 0.5
        ease 1.5 xpos 0.2 alpha 0.0
    show cornelia b_15:
        pause 0.75
        ease 1.6 xpos 0.2 alpha 0.0

    "So..."
    "While the relationship with Sayaka steadily improved for the better, other things started to surface now as well."
    "When Sayaka had told me that popularity is important for girls, I really doubted her, but it did impact me after all."
    "Her so-called {q}friends{/q} were actively bullying {i}me{/i} now."
    "Irene especially."
    "Cornelia was hit as collateral as well since she stuck to me, but I was apparently too {q}lame{/q} for them now."
    "I had tried to be friendly to them, but..."

    scene bg lunch
    show sayaka a_5:
        center
        faceleft
        ypos 1.1
    show john b_5:
        centerleft
        faceright
        ypos 1.1
    show cornelia b_5:
        centerright
        faceleft
        ypos 1.1
    show AN_asset grain
    with dissolve


    sayaka "{i}You're too soft, you're not interacting with them enough, and your image is in the gutter.{/i}"

    show sayaka a_16

    sayaka "{i}Of course they would start turning on you. Irene has had her eyes on my position for a long time now.{/i}"

    show sayaka at faceright
    show cornelia b_6
    show john b_0

    cornelia "{i}The only reason we even let Irene stay with us is because she wouldn't cause trouble then.{/i}"

    show sayaka at faceleft
    show cornelia b_24
    show john b_6

    john "{i}...You guys are talking as if this is a full on conspiracy.{/i}"

    show john b_25

    sayaka "{i}It is. You've already seen it, haven't you?{/i}"

    show john b_4

    john "{i}....Well...{/i}"

    scene bg school hallway2 day
    with dissolve

    "I did."
    "At first they completely stopped interacting with me."
    "I didn't think much of it, to be honest, it didn't really bother me since I never really knew them."
    "But later, I was practically put into Kyoko's shoes."

    outfit john gym_pony
    body cornelia AN_cornelia
    outfit cornelia gym
    outfit irene athletic
    outfit rita gym
    scene bg school exterior day
    show john a_1 at centerleft, faceleft
    show cornelia a_1 at left, faceright
    show irene a_1:
        center
        faceleft
        xpos 0.7
    show rita b_2:
        center
        faceleft
        xpos 0.85
    show AN_asset grain
    with dissolve

    irene "{i}I'm really hoping little birdie over there doesn't fly away today!{/i}"

    show john a_0 at faceright
    show cornelia a_0
    show rita b_9

    rita "{i}Ahh~~~haha, that fucking name!{/i}"

    show john a_32
    show cornelia a_19
    show irene a_2

    john "{size=-3}{i}Nngh, I never should have told anyone that name.{/i}{/size}"

    show cornelia a_3

    cornelia "{i}Screw off, Irene!{/i}"

    outfit john underwear_badhair
    body cornelia cornelia
    outfit cornelia uniform
    scene bg lockerroom day
    show john b_0 at centerright, faceright
    show cornelia b_0 at centerleft, faceleft
    show AN_asset grain
    with dissolve
    play sound sfx_creak

    john "..."

    show john b_6
    show cornelia a_0 at faceright

    john "...{i}Really...?{/i}"

    show cornelia a_11

    cornelia "{i}What is it?{/i}"

    show john b_4

    john "{i}There is glitter {b}everywhere{/b} in my locker...{/i}"

    show cornelia b_5:
        ease 0.5 xpos 0.6

    cornelia "{i}Glitter?{/i}"

    show cornelia a_20

    cornelia "{i}...Oh god.{/i}"

    show cornelia b_3 at faceleft

    cornelia "{i}Those stupid-{/i}"
    john "{i}Sigh...{/i}"

    outfit john uniform_pony_pants
    outfit irene uniform
    scene bg school classroom hallway day open
    show cornelia a_1:
        center
        faceleft
        xpos 0.4
    show john b_12:
        center
        faceright
        xpos 0.175
    show irene b_0:
        center
        faceleft
        alpha 0.0
        xpos 0.7
        pause 0.5
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 0.5
    show allison a_0:
        center
        faceleft
        alpha 0.0
        xpos 0.8
        pause 0.65
        parallel:
            ease 0.5 alpha 1.0
        parallel:
            ease 0.75 xpos 0.65
    show AN_asset grain
    with dissolve
    pause 0.75
    play sound sfx_whack
    show cornelia b_29:
        transform_anchor True
        faceright
        ease 0.5 rotate -4 xpos 0.325 ypos 1.15
    pause 0.25
    show john b_7:
        ease 0.25 xpos 0.185

    cornelia "{i}Ow!{/i}"

    show irene b_1

    irene "{i}Whoops.{/i}"

    show cornelia b_17
    show john b_11
    show irene b_0

    cornelia "{i}What the hell Irene?! What was that for?!{/i}"

    show irene b_1
    show cornelia b_14:
        ease 0.75 ypos 1.0 rotate 0

    irene "{i}So sorry, didn't see you all the way down there.{/i}"

    show allison a_6
    show irene b_9 at faceright

    allison "{i}You have to remember to look down sometimes, Irene.{/i}"

    show irene b_1

    irene "{i}I'll keep that in mind, heh.{/i}"

    outfit rita uniform
    scene bg lunch
    show cornelia b_5 at centerright, faceleft
    show john b_0 at right, faceleft
    with dissolve

    "At this point, we just wanted them to stop bothering us. We decided in unison to confront Irene's group and talk this out."
    "We had managed to slip out of our previous class just very slightly earlier so that we would be able to confront them before they went to lunch, but our timing was off."

    show irene b_4:
        center
        alpha 0.0
        faceleft
        xpos 0.2
    show rita b_0:
        center
        alpha 0.0
        faceleft
        xpos 0.3
    show allison a_0:
        center
        alpha 0.0
        faceleft
        xpos 0.4

    "The bell had just rung, and people were eager to get some food inside the lunchroom."

    show irene:
        ease 0.5 alpha 1.0
        pause 0.25
        ease 0.75 alpha 0.0 xpos 0.0
    show rita:
        pause 0.25
        ease 0.5 alpha 1.0
        pause 0.25
        ease 0.75 alpha 0.0 xpos 0.1
    show allison:
        pause 0.5
        ease 0.5 alpha 1.0
        pause 0.25
        ease 0.75 alpha 0.0 xpos 0.2
    show cornelia b_11
    show john b_11

    cornelia "There! They are headed towards the lockers."
    "They used the lunchroom as a shortcut to what seemed like the lockers. An infinitely better place to talk with them than in here."
    think "Well, cripes, guess it makes more sense to talk with them alone by the lockers anyways."

    scene black with dissolve
    pause 0.25
    scene bg lockers day
    show irene b_0:
        center
        faceleft
        xpos 0.3
    show rita b_0:
        center
        faceleft
        xpos 0.45
    show allison a_10:
        center
        faceright
        xpos 0.15
    show john b_0:
        alpha 0.0
        center
        faceleft
        xpos 1.0
        ypos 1.02
        pause 2.0
        ease 0.5 alpha 1.0 xpos 0.85
    show cornelia b_5 behind john:
        alpha 0.0
        center
        faceleft
        xpos 0.9
        pause 1.75
        ease 0.5 alpha 1.0 xpos 0.7
    with dissolve

    "We followed them to the lockers."
    "Only Rita and Allison were with her."

    show allison a_3
    show irene b_4:
        pause 0.75
        faceright
    show rita a_2 behind irene:
        pause 1.0
        faceright

    "While chatting, they noticed us approaching them."

    show john b_5:
        alpha 1.0 xpos 0.85
    show cornelia:
        alpha 1.0 xpos 0.7

    john "Hey."

    show irene b_5

    irene "...What do {i}you{/i} want?"

    show irene b_4
    show john b_13

    john "Can we talk about what's going on? Like honest people?"
    irene "...?"

    show rita b_2 at faceleft
    show irene:
        pause 0.75
        faceleft
    show allison a_24

    "Irene looked at the other two, who both just slightly shrugged their shoulders."

    show irene b_0 at faceright
    show john b_5

    "With a slight smile going across her face, she turned back towards me."

    show irene b_1
    show rita at faceright

    irene "Alright. Let's talk alone, you and me."

    show cornelia b_0
    show irene b_0
    show john b_27

    john "M- Me?"
    irene "Exactly."

    show john b_13

    john "Uh... Alright. Is it alright Cornelia?"

    show cornelia a_5

    cornelia "Sure. You know what to say."

    show cornelia a_0
    show irene b_3:
        pause 0.75
        faceleft
    show rita b_14 at faceleft
    show allison a_3

    irene "I'll see both of you in a second. I just need to clear things up here."

    show allison a_1
    show rita a_0
    show irene b_9 at faceright

    allison "Sure."

    show allison a_21

    rita "Heh."

    show allison a_0:
        pause 0.75
        ease 0.5 alpha 0.0 xpos 0.6
    show cornelia b_0:
        pause 0.5
        faceright
        ease 0.5 alpha 0.0 xpos 0.95
    show rita a_1:
        faceright
        pause 1.25
        ease 0.5 alpha 0.0 xpos 0.8
    show john b_11:
        pause 1.5
        faceright

    "All three gathered their things and left for the lunchroom. Cornelia clearly didn't want to accompany them, so she took the long way around rather than the short path."

    show john b_3 at faceleft

    "With seemingly nobody around, I started to say what I wanted to say."

    show john b_4

    john "So... You know, in the last few days-"

    show irene b_4
    show john b_7

    irene "Hold up."

    show irene:
        faceleft
        ease 0.5 xpos 0.2

    john "...Uhm?"

    show irene:
        faceright
        ease 0.5 xpos 0.3 alpha 0.0
    show john b_5

    "Irene double walked around the lockerroom once more, seemingly to make sure nobody was around for some reason."

    show irene:
        ease 0.5 xpos 0.4 alpha 1.0

    "After confirming it, she went back and faced me."

    show john b_13

    john "Uhm... So as I was sayi-"

    show john b_7
    show irene b_8

    irene "Do you {i}really{/i} think someone like you should be able to come and confront {i}me{/i} about {q}bullying{/q} people?"

    show irene b_4

    irene "I assume that's what you're here for."

    show john b_4 behind irene

    john "We- Well, I've done a lot of bad things, apparently, and I realize that now, but-"

    play sound AN_sfx_crash
    show irene b_5:
        transform_anchor True
        ease 0.35 xpos 0.7
    with hpunch
    play sound AN_sfx_silence
    show john a_8:
        ease 0.2 ypos 1.0 xpos 0.87
        ease 0.4 ypos 1.02

    john "Eek!"

    show john a_27

    "With no warning and full force, she straight up {i}punched{/i} the locker right behind me, only just missing my head."
    "A massive crack of metal could be heard, which had me in complete shock."
    "She was incredibly close to me, and her height meant that she was looking down on me with extremely threatening eyes."

    show irene b_8:
        ease 0.3 rotate 3 xpos 0.69 ypos 1.02
    show john:
        transform_anchor True
        pause 0.25
        ease 0.5 ypos 1.05 rotate 4

    irene "{size=-5}Now, you listen here you sack of garbage.{/size}"

    show john a_30

    irene "{size=-5}You've made the life of many people in this school a living hell. Now you finally get a piece of the cake, and all of a sudden you have the {i}tenacity{/i} to come and beg for mercy?{/size}"

    show irene b_1

    irene "{size=-5}Don't make me laugh.{/size}"

    show irene b_4
    show john a_9

    john "{size=-8}S- So- Sorry!{/size}"

    show john a_36 at faceright

    "I was still in complete shock at the sudden show of violence and could only look at her while I was leaning myself on the lockers behind me."

    show john a_30 at faceleft
    show irene:
        ease 0.75 rotate 1 ypos 1.0 xpos 0.675

    "She finally took her fist off the lockers, and a bit of relief came over me, but I still dreaded what she'd do now."

    show john b_27

    "Irene suddenly felt like a complete wild-card, and it was terrifying looking her in the eyes."
    "My body would take heavy damage if she actually wanted to hit me, I knew that much."

    show irene b_1
    show john b_7

    irene "...Hah."
    irene "You really are pathetic. Someone finally puts you in your place, and all you can do is stand there and cower like some scared kitten."

    show john b_35
    show irene b_9

    "She put her hand around the bottom of my chin, like some pervert in a movie, and looked at me for a few seconds."

    show irene b_3

    irene "The only reason I even bothered to sit at the same table as you was to bring you down."

    show irene b_8
    show john b_7

    irene "Watching you made me sick. Seriously sick."

    show irene b_3

    irene "I thought that maybe I could influence you to not be such a massive dump of a personality, but instead you decided to go crazy all by yourself."

    show irene b_9:
        ease 0.5 xpos 0.575

    "She let go of me and laughed to herself."
    irene "So in the end, you really did me a favor by going nuts and giving me the opportunity to be the one who runs this shop."

    show john b_4

    "I was still motionless. I never thought I would be this afraid of another person, especially a girl."

    show irene b_4 at faceleft
    show john b_13

    "She looked around once more to make sure nobody was watching."

    show irene at faceright

    irene "You satisfied with your answer?"

    show irene b_8

    irene "Or do you need more convincing?"

    show irene b_9
    show john b_4

    "I simply shook my head in response to her question."
    irene "Good. Now go back and play slut with Kiyoshi."

    show irene b_8

    irene "Next time, I'll make sure that I won't miss. I'd rather hit something that isn't as hard as the lockers."

    show irene b_9:
        parallel:
            ease 1.0 xpos 1.1
        parallel:
            ease 0.5 alpha 0.0

    "With that, she up and left after picking up her things."

    show john b_22

    irene "{size=-10}Shit, that hurt.{/size}"

    show john:
        ease 0.4 ypos 1.09
        ease 0.3 ypos 1.1 rotate 6
        ease 1.2 ypos 1.2

    "I slowly slid down the locker I was leaning up on."
    "It was still a sense of shock, at how sudden everything was."
    "She just fully threatened me with violence if I bothered her again."

    show john b_28

    think "What the fuck?!"

    show john b_27

    "..."

    show john a_0:
        parallel:
            ease 0.75 ypos 1.02
        parallel:
            ease 0.5 rotate 0

    "I looked up at the spot on the locker that she punched."
    "It had a quite the bulge inwards."

    show john b_27

    think "Just how strong is Irene? I knew she was tall, but to also be able to just bend metal like that after hitting it is way too extreme!"

    show john b_4

    think "...Fuck."

    scene black with dissolve
    outfit zoey uniform
    pause 1.5
    show bg lunch:
        zoom 1.5 xalign 0.4 yalign 0.8
    show cornelia a_5:
        center
        faceright
        ypos 1.1
        xpos 0.4
    show sayaka a_5:
        center
        faceleft
        ypos 1.1
        xpos 0.6
    show kiyoshi a_1:
        center
        faceleft
        ypos 1.1
        xpos 0.8
    show john b_4:
        center
        faceright
        xpos 0.05
        alpha 0.0
        pause 1.5
        ease 1 alpha 1.0 xpos 0.2
    with dissolve

    "Regardless, I decided that I should still join the others for lunch."

    show sayaka a_32
    show cornelia a_11:
        pause 0.5
        faceleft
    show kiyoshi a_0

    "There were only a few minutes left of lunch break, but I had lost all appetite anyways."

    show cornelia a_8 at faceleft
    show john b_13:
        alpha 1.0 xpos 0.2

    cornelia "...There you are! I was worried sick that Irene arrived long ago!"

    show john b_21
    show cornelia a_0
    show sayaka a_5

    john "Oh... Uhm, hey."

    show john a_4:
        ease 0.5 ypos 1.1
    show cornelia a_14

    cornelia "What took you so long?"

    show john:
        ypos 1.1

    john "Nothing... Nothing."

    show cornelia a_5 at faceright
    show sayaka a_32

    sayaka "...?"

    show cornelia at faceleft
    show sayaka a_5
    show john a_5

    sayaka "Sounds like something you'd say when something happened."

    show john a_32

    john "No, I just, uhm... Think we just should avoid her, Irene, you know."

    show john a_6

    "Sayaka took a bite from her sandwich before answering."

    show sayaka a_33
    show john a_5

    sayaka "Wasn't the entire purpose to make her stop treating you like some 3rd world citizen?"

    show john a_4

    "Cornelia and Sayaka both eyed me curiously. Obviously they knew something was up. But it's not like it really mattered."
    "If I told them about what happened, they might just end up making matters worse."

    show sayaka a_5
    show john a_5

    sayaka "{i}Sigh...{/i} Guess you're going silent, huh. Well, your problem."
    "Sayaka didn't seem to care much, Cornelia still looked at me worried, but went back to taking her last bites out of her burger anyhow."

    show cornelia a_0 at faceright
    show sayaka a_13 at faceright
    show kiyoshi a_4
    show john a_0

    sayaka "Kiyoshi, explain to him what we're doing after school."

    show kiyoshi a_6
    show sayaka a_6

    kiyoshi "Ah, sure thing."

    show john a_6

    think "Oh right, he is here as well."

    show sayaka a_15
    show cornelia a_0
    show kiyoshi a_4
    show john a_13

    zoey "John!"

    show sayaka a_4 at faceleft

    sayaka "Oh fu-!"

    show zoey b_1 at offscreenleft, faceright

    sayaka "I'll see you later!"

    show sayaka a_15:
        faceright
        ease 0.25 ypos 1.1
        pause 0.25
        ease 0.5 offscreenright
    show john b_6
    show cornelia a_6
    show kiyoshi:
        pause 1.25
        faceright
    show zoey:
        pause 1.25
        ease 1.5 offscreenright
    pause 1

    zoey "Don't run away from me! John!"

    scene black with Dissolve(1.5)
    pause 1.5

    title "24th of December (Saturday)" "Day 139 - John"

    outfit john formal
    accessory john set glasses, xmashat
    pause 1
    scene bg sayaka kitchen night lights on
    show john b_3:
        centerright
        faceleft
        ypos 1.1
    with Dissolve(1.0)
    pause 2
    show john a_17
    pause 3
    show john b_3 at faceright

    john "..."

    show john a_17 at faceleft

    think "They promised..."
    think "They promised to at least be there today..."

    show john b_4

    think "...I can't take this anymore..."
    "Was I really being too demanding?"
    "I've been Sayaka for almost half a year now, so naturally I would want to get along with the people that mattered in her family more."
    "Christmas is a tradition that was celebrated in my real home every year with people being happy, open and all of that..."

    show john b_22

    "But this is just..."

    show john b_35

    john "{i}Sigh...{/i}"

    show john b_34

    john "{size=-5}I hate them...{/size}"

    show john b_9

    john "{size=-5}I hate them, I hate them, I hate them!{/size}"

    show john b_35

    "They promised that we would spend christmas together, those stupid parents!"

    show john b_22

    "But instead, I got two texts telling me how {q}We have {i}soooo{/i} much important stuff to do right now{/q}, as if this {b}one{/b} favor from their own daughter was just some side-thing to worry about!"

    show john b_3

    "Even if they were late, they told me they would be home by nine at the latest, but they still aren't here!"
    "I had even prepared dinner for them, all on my own without getting any help from them at all, having to look up recipes online and all of that."
    "But now even the food I had made was starting to get cold to the point where it wasn't edible any longer."

    show john a_17

    "They weren't my real parents, but I still cared enough to at least not spend christmas of all things alone!"

    show john a_27
    play sound sfx_door_close

    "And with perfect timing at the end of my angry monologue, I could finally hear the door from outside making a resemblance of sound."

    show john b_3 at faceright

    "I looked at the time, and it was twenty past ten at this point."

    show john a_17 at faceleft
    show AN_jacob a_3:
        center
        faceleft
        xpos -0.1
        alpha 0.0
        zoom 0.95

    "Oh, how I would scold them for taking so freaking long!"

    show john b_3
    show AN_jacob:
        ease 0.75 alpha 1.0 xpos 0.2

    "It was the dad. He looked tired and noticed me when I came into the kitchen."

    show AN_jacob a_9:
        alpha 1.0 xpos 0.2
        ease 0.5 xpos 0.35
    show john b_5

    AN_jacob "Hello sweetie. I'm sorry I'm home late."

    show AN_jacob a_0:
        faceright
        ease 0.5 xpos 0.3

    "..."

    show john b_3

    "That's all he had to say?"

    show AN_jacob:
        ease 0.5 xpos 0.275

    "I waited a bit longer for more of an explanation, but nothing."

    show AN_jacob a_1:
        faceleft
        ease 0.75 xpos 0.45

    "He just hung up his jacket and approached me."

    show john b_0

    AN_jacob "Here, I hope you like it."

    show john a_5

    "He handed me a small box. Not even wrapped or anything."
    "He may run a business, but where the hell did he learn to suck so badly at reading the room?"

    show john a_17

    john "A christmas gift?"

    show AN_jacob a_9

    AN_jacob "Yes."
    john "Aren't those supposed to be wrapped up? Or put under a tree or something?"

    show AN_jacob a_10

    AN_jacob "...Why would you want it wrapped? What difference does an additional coating of paper do?"

    show john b_19

    john "It's christmas! That's how you do it!"

    show john b_3
    show AN_jacob a_5

    AN_jacob "{i}Sigh...{/i} I am not in the mood for one of your breakdowns now, Sayaka."

    show john b_19
    show AN_jacob a_0

    john "One of my breakdow- {nw}"

    show john b_28

    extend "What?!"

    show john b_3
    show AN_jacob a_2

    "He rubbed his temple to display that he was tired of me."

    show AN_jacob a_3:
        parallel:
            pause 0.25
            ease 0.5 alpha 0.0
        parallel:
            ease 1.0 xpos 1.1
    show john b_27:
        pause 0.5
        faceright
    play sound sfx_door_open
    pause 0.5
    play sound sfx_door_close

    "While ignoring my question, he walked into the living room in a completely calm fashion."

    show john at faceleft

    "I had to spend a few seconds to process what just happened."
    "Did he seriously just break his promise, then call me unstable when I get angry at him?!"
    "Even ignoring the food I had spent all day making just for them?!"

    show john b_28

    "He breaks his {i}{b}one promise{/b}{/i}, and is annoyed at {i}me{/i}?!"

    show john b_27 at faceright

    "To make matters worse, I could now hear the TV going."
    "He straight up ignored his daughter to go and watch television on christmas evening!"
    think "That's it! I've fucking had it!"

    scene black with dissolve
    play sound sfx_door_open
    scene bg sayaka livingroom night
    show AN_jacob a_0:
        center
        faceleft
        xpos 0.6
        ypos 1.1
        zoom 0.95
        pause 1.25
        faceright
    show john b_28:
        center
        faceright
        alpha 0.0
        xpos 0.05
        pause 0.5
        ease 0.75 xpos 0.25 alpha 1.0
    with dissolve

    john "You are so stupid!"

    show john b_9:
        xpos 0.25 alpha 1.0
    show AN_jacob a_3 at faceright

    john "Don't you get what's going on here?!"

    show AN_jacob a_4
    show john b_27

    AN_jacob "I beg your pardon?"

    show AN_jacob a_3
    show john b_28

    john "You broke your promise! And now you're ignoring me! On christmas!"
    john "Do you have any idea how much that hurts?!"

    show AN_jacob a_4
    show john b_27

    AN_jacob "Don't you dare call me stupid, Sayaka."

    show john b_9
    show AN_jacob a_3

    john "Seriously? That's everything you got from what I just said?!"

    show AN_jacob a_10
    show john b_3

    AN_jacob "...Really, what is going on with you right now?"
    AN_jacob "You haven't had anything to drink, have you?"

    show john a_3
    show AN_jacob a_0

    john "{size=+5}Ugh! You- You terrible-!{/size}"

    show john a_17

    "My head was boiling at this point. I didn't care what was in the box he gave me."

    show john b_19
    accessory john set glasses
    with dissolve

    "I threw it on the ground as hard as I could together with my christmas hat."

    show AN_jacob a_3:
        ease 0.25 ypos 1.0
    show john a_17

    "He was shocked that I would do it, and immediately transitioned into a very serious expression."

    show AN_jacob a_4

    AN_jacob "What do you think you're doing?! Do you think I gave that to you as a joke?!"

    show john b_9:
        faceleft
        pause 2
        ease 0.75 alpha 0.0 xpos 0.05
    show AN_jacob a_3

    john "Fuck you, both of you!"

    show AN_jacob a_4
    scene black with dissolve
    play sound sfx_door_close
    scene bg sayaka kitchen night lights on
    show john b_3:
        center
        faceleft
        alpha 0.0
        xpos 0.8
        pause 0.25
        ease 0.75 xpos 0.5 alpha 1.0
    with dissolve

    AN_jacob "{size=-5}Excuse me, young lady?!{/size}"

    show john b_4

    AN_jacob "{size=-5}You are coming back into the livingroom this instant!{/size}"

    show john:
        ease 0.75 alpha 0.0 xpos 0.2
    play sound sfx_door_open
    pause 2
    scene black with dissolve
    pause 1.5
    show bg neighborhood2 night:
        zoom 2.0 xalign 0.35 yalign 0.4
        pause 0.5
        ease 10 zoom 1.0
    show john b_4:
        center
        faceright
        xpos 0.55
        parallel:
            block:
                ease 0.6 ypos 1.01
                ease 0.4 ypos 1.02
                ease 0.6 ypos 1.0
                repeat
        parallel:
            pause 0.75
            ease 8 xpos 0.65
    with dissolve

    "I left the house as fast as I could."
    "I couldn't stand it anymore. It was like mental abuse."
    "I knew he would get angry as all hell at me for saying {q}{i}Fuck you{/i}{/q} to him. And I didn't want to listen to him anymore."
    "Not today."

    show john b_13

    "It was chilly outside. Very chilly. And I only had the dress and jacket on."
    "But it still felt better than having to be next to him. It only cemented how much I hated him. And Sayaka's mom would probably not react very differently."

    show john b_4

    "Even though I felt like crying right now, I was just too angry to do so."
    "But..."

    show john b_34

    john "{i}Achoo-!{/i}"

    show john b_6

    think "...God, it's cold outside..."

    show john b_4

    "..."
    think "I don't want this anymore... I just want to go home...To mom, and Holly, and Natsumi who visits some days..."

    scene black with dissolve
    scene bg main house dark
    show john b_5 at centerright, faceleft
    with dissolve
    pause 2
    show john b_4

    "It felt wrong to actually visit my real home."
    "It was still... Christmas, after all..."
    "We hadn't told anyone about the swap besides our small friend group."

    show john b_5

    "Kat, Kyoko, Kiyoshi, Cornelia and Brad were still the only ones who really knew about it. But recently, it started becoming extremely lonely, despite those five knowing my actual identity."
    "So I took the courage to perhaps do this today. To perhaps convince my mom of who I really was."

    show john b_3

    john "{i}Sigh...{/i} Here we go..."

    scene black with dissolve
    outfit leona casual
    outfit sayaka winter_tshirt
    outfit yui casual
    scene bg main entrance night
    show john a_15:
        centerleft
        faceright
        alpha 0.0
    with dissolve
    play sound sfx_knock

    "I knocked on the door."

    play sound sfx_knock
    show sandra b_3:
        centerright
        faceleft
        alpha 0.0

    "It took a while before I noticed someone approaching it through the window, maybe a minute of knocking here and there was required."

    show sandra:
        ease 0.5 alpha 1.0 center

    "The door was locked, and so someone from the inside opened it."

    play sound sfx_door_open
    show john:
        ease 0.5 alpha 1.0 xpos 0.3
    pause 1.5
    show sandra b_7:
        alpha 1.0 center

    sandra "Uh- Sayaka?!"

    show john a_14:
        alpha 1.0 xpos 0.3

    john "He- Hey..."

    show john a_5
    show sandra b_8

    sandra "Goodness, what are you doing out here so late- And in those clothes?!"

    show john b_4

    john "Uhm... No, I just had to hurry, because... Uh-"

    show john b_5
    show sandra b_4:
        pause 0.5
        faceright
    show leona a_5:
        right
        faceleft
        alpha 0.0

    sayaka "{size=-10}Who is it mom?!{/size}"

    show sandra b_8
    show leona:
        ease 0.75 alpha 1.0

    sandra "It's Sayaka from school! Did you invite her?!"

    show leona:
        alpha 1.0
    show john b_35
    show sayaka a_2:
        center
        faceleft
        alpha 0.0
        xpos 0.8
    show yui a_12:
        center
        faceleft
        alpha 0.0
        xpos 0.9
    show sandra b_3 at faceleft

    john "No, no, I'm here out of my own will, uhm-"

    show sayaka:
        ease 0.5 xpos 0.6 alpha 1.0
    show yui:
        pause 0.25
        ease 0.5 xpos 0.725 alpha 1.0
    show sandra

    sayaka "Oh. Hey. Uh... What are you doing here?"

    show sayaka:
        xpos 0.6 alpha 1.0
    show yui:
        xpos 0.725 alpha 1.0

    yui "{size=-3}Sayaka?{/size}?"

    show john b_12

    john "Uhm, hey guys..."

    show sayaka a_5
    show john b_3

    sayaka "No really, what are you doing here?"

    show john a_4
    show yui a_13

    john "..."

    show sayaka a_32
    show john b_4

    john "{i}Sob....{/i}"

    show sandra b_7:
        pause 0.25
        ease 0.25 xpos 0.525
        ease 0.25 xpos 0.5 ypos 1.05
    show john b_9:
        transform_anchor True
        ease 0.5 rotate 4 xpos 0.4 ypos 1.15
    show sayaka a_15
    show yui b_9
    show leona a_8

    john "I- I'm- I'm sorry, I can't do this anymore...!"

    scene black with dissolve
    pause 1

    "I ended up crying my heart out in front of them that night."
    "Even if something like that is hard to admit as a guy."
    "It was one of the most memorable nights of my life, by far."
    "The feeling of neglect was instantly gone when they welcomed me in and even heated up the leftovers from the many ducks they had that evening."

    outfit sayaka casual
    scene bg main livingroom day
    show sandra a_3 at centerright, faceleft
    show john b_4:
        center
        faceright
        xpos 0.45
    show sayaka a_5:
        center
        faceright
        xpos 0.3
    with dissolve

    "Me and Sayaka both agreed that we would tell my mom about the situation the day after, and we did."

    show john b_5
    show sandra a_6

    "She had noticed that something was off long ago, and hesitated a bit when we told her."

    show john b_1
    show sandra a_1
    show sayaka a_6

    "But she really believed us at the end."
    "It turned out to be a good christmas night after all, and I never looked back on those excuses of parents that were now my biological one."

    scene black with Dissolve(2.0)
    pause 2
    body john AN_sayakaAP
    body sayaka AN_johnAP
    body cornelia AN_corneliaAP
    body kiyoshi maurice

    title "11th of April - 9 years later (Friday)" "Day 3170 - John"

    outfit john casual_2
    accessory john set glasses
    pause 2
    play sound sfx_door_open
    show AN_bg AP entrance:
        zoom 1.5 xalign 0.65 yalign 0.3
    show john b_0 at centerright, faceleft
    with Dissolve(1.0)
    pause 1.5
    show john b_8
    pause 1

    john "{i}Sigh...{/i} Finally home..."

    show john b_5

    think "Man, work is totally killing me right now."
    think "..."

    show john a_7

    "Oh, right."

    show john a_6

    "So, we didn't really end up anywhere with the... Uh, well, {q}experiments{/q}."

    show john b_1:
        parallel:
            ease 0.5 ypos 1.02
            ease 0.6 ypos 1.0
            ease 0.5 ypos 1.03
            ease 0.7 ypos 1.0
        parallel:
            ease 1.5 xpos 0.4
    show AN_bg AP entrance:
        ease 2 zoom 1.0

    "Despite the lack of results, Kiyoshi had actually impressed me at the stuff he could come up with."
    "Like really, I think at some point we ended up catching a fly, cooking it, splitting it in two, and had both me and John eat one half."

    show john b_5

    "I believe the theory would then be that flies carried around some genetic mutation that would enable two people to swap personalities and holy hell does it sound stupid when I think back on it."

    show john b_4

    "Honestly I have no idea what went through our minds back then..."

    scene AN_bg AP livingroom
    show john b_9:
        left
        faceright
        pause 0.75
        ease 1.0 center
    with dissolve

    "Oh, and me and John now refer to each other by our body name, even while alone. It just makes more sense that way."

    show john b_8

    "I can't even count how many times someone managed to eavesdrop us and thought we were crazy or something."

    show john a_4

    "...But yeah, life's been surprisingly normal since then."

    show john a_5

    "I would have planned to just doze off on the sofa for the rest of the rest of the day, were it not for the fact that I had to get ready for the evening at some point."

    show john a_0

    "I knew that Cornelia would appear because I promised her to take home her package-"

    show john b_0 at faceleft
    play sound sfx_bell
    pause 1.5

    "...And speak of the devil, she's probably already here. She is unusually early."

    scene black with dissolve
    outfit cornelia uniform
    show AN_bg AP entrance:
        zoom 1.5 xalign 0.65 yalign 0.3
    show john b_9 at center, faceright
    with dissolve
    pause 0.25
    play sound sfx_door_open
    pause 0.25
    show cornelia b_1 at Position(pos=(0.7, 1.05), anchor=(0.5, 1.0)), faceleft with dissolve


    john "Why, hello there."

    show cornelia b_2:
        ease 0.5 xpos 0.6
    show john a_4

    cornelia "Saya! Hey!"
    "She went straight in for an unexpected hug-attack."

    show john a_2

    "Naturally I countered with my own hug."
    john "Good to see you too."

    show john a_8
    show cornelia b_1:
        ease 0.5 xpos 0.7

    cornelia "Sorry for having me come on a short notice."

    show john a_9

    john "Got nothing better to do."

    show john a_8
    show cornelia a_2

    cornelia "Heheh, I suppose not."

    show cornelia a_1

    cornelia "Did my parcel arrive?"

    show john b_2

    john "Yeah yeah. Come on in."

    scene black with dissolve
    pause 0.5
    scene AN_bg AP livingroom
    show cornelia b_11:
        center
        faceleft
        xpos 0.7
        ypos 1.05
    show john b_9:
        center
        faceright
        xpos 0.45
    with dissolve

    cornelia "There it is. About time it arrived."

    show cornelia b_10
    show john b_2

    john "I was about to head home before I suddenly saw it lying in front of the office. Talk about luck that I had a longer day than expected."

    show cornelia b_8
    show john b_9

    cornelia "Figures."

    show cornelia b_1
    show john b_0

    "She began slowly unpacking it. I already knew the contents, new clothes she wanted to wear for today."
    "But that specific set was always out of stock until she managed to get lucky."

    show john a_6:
        faceleft
        ease 0.5 xpos 0.4
        pause 0.5
        faceright
        pause 0.25
        ease 0.5 ypos 1.1

    "I was beat from all the work I had to do today, so I went straight to the sofa and sat myself down."

    show cornelia b_7
    show john a_5

    cornelia "Everything fine at work?"
    cornelia "Since you mentioned overtime."

    show cornelia b_1
    show john b_9

    john "Oh, yeah, we just have a few deadlines we need to crunch through."

    show john a_9

    john "They want me to do a few extra things because I'm the only woman in programming. You know, with voice-overs and support and stuff."

    show john a_8
    show cornelia b_12

    cornelia "You mentioned that before. You sure it doesn't get a bit lonely as the only girl in your department?"

    show john a_10

    john "Nah, it's alright. The guys are pretty cool to hang out with. And I get to talk with some interesting people most of the time."

    show john a_8

    cornelia "If you say so."

    show cornelia a_0
    show john a_0

    "As if on queue, she managed to finally tear open the box."

    show cornelia b_11
    show john a_8

    "She lifted up a sweet looking dress, and her eyes glimmered with excitement."

    show cornelia b_2

    cornelia "Finally, I've been waiting to get my hands on this."

    show john b_9

    "She was practically hugging the set of clothes at this point. I kind of felt happy for her that she finally got what she wanted."

    show cornelia b_1

    cornelia "You don't mind if I change here, right? I can give you a lift since you did me this favor."
    john "Feel free to."

    show cornelia b_2

    cornelia "Thanks."

    show john b_0
    show cornelia b_6

    cornelia "But, uh... Are you not going to be under stress if you still want to dress and all that? I already took a shower at uni, but if we want to make it in time, we need to be on the road in thirty minutes."

    show cornelia b_13
    show john a_2:
        pause 1
        faceleft

    john "Thirty minutes? Isn't that a bit too soon-"

    show john b_7

    john "Oh shoot, it's already a quarter to six!"

    show john b_10

    "I got a bit of a shock when I saw the clock. I thought I still had an hour left!"

    show cornelia a_2
    show john at faceright

    cornelia "Haha, you really didn't notice?"

    show john b_3:
        ease 0.5 ypos 1.0
    show cornelia a_1

    john "They must have fixed the clock at work, it's been on winter time since the start of March!"

    show cornelia b_1:
        pause 0.75
        faceright
    show john b_7:
        ease 1.25 xpos 0.9 alpha 0.0

    john "Crap, crap! I'll skip the shower! I'll be sure to be ready by six!"

    show cornelia b_2

    "With that, I frantically ran into my bedroom to find the clothes I had laid out for tonight."

    scene black with dissolve
    pause 2
    outfit john formal
    outfit cornelia casual
    scene AN_bg extravagant entrance night
    show john b_0:
        center
        faceleft
        xpos 0.85
        alpha 0.0
        pause 0.5
        ease 0.75 alpha 1.0 xpos 0.65
    show cornelia b_1:
        center
        faceleft
        xpos 1.0
        alpha 0.0
        ypos 1.05
        pause 0.5
        ease 0.75 alpha 1.0 xpos 0.8
    with dissolve

    "We still managed to be there a bit too late despite my hurrying."
    think "Not like we are the only ones anyways. I saw some couples arriving late as well."

    show john b_9:
        alpha 1.0 xpos 0.65
    show cornelia:
        alpha 1.0 xpos 0.8

    "They weren't really people I recognized. Most people I know would probably already be here since they were helping with organization and stuff."

    show john a_5 at faceright
    show cornelia b_11

    cornelia "I hope he likes the look."

    show john a_9

    john "You're still addicted to having him tell you that?"

    show cornelia a_6

    cornelia "I'm not addicted! I just like it."

    show john b_1 at faceleft

    john "Right."

    scene black with dissolve
    outfit sandra formal
    accessory sandra set glasses
    outfit leona dress
    scene AN_bg extravagant foyer
    show leona a_4:
        left
        faceleft
        xpos 0.15
    show sandra a_1:
        left
        faceleft
        xpos 0.35
    show john b_9:
        center
        faceleft
        xpos 0.7
        alpha 0.0
        pause 1.0
        ease 0.75 xpos 0.6 alpha 1.0
    show cornelia b_12:
        center
        faceleft
        xpos 0.95
        ypos 1.05
        alpha 0.0
        pause 1.25
        ease 0.75 xpos 0.75 alpha 1.0
    with dissolve

    "As we went in, mom and Leona were naturally receiving the guests in the lobby area."

    show sandra a_0 at faceright

    "Mom saw me and waved us over."

    show sandra a_1
    show john b_0:
        xpos 0.6 alpha 1.0
        ease 0.75 xpos 0.55
    show cornelia b_1:
        xpos 0.75 alpha 1.0
        pause 0.25
        ease 0.75 xpos 0.7

    sandra "There you guys are! You almost made me worry you'd be missing out on the welcome speech."

    show leona a_1 at faceright
    show sandra a_0
    show john a_10

    john "Hey mom. And hello Leona. Congratulations on the 50 years!"

    show john a_8
    show cornelia a_2

    cornelia "Likewise, and thanks for inviting us."

    show cornelia a_1
    show leona a_7

    "We both gave Leona the presents we brought her."
    "Most people I know from family and friends were invited for Leona's 50 year birthday today, and Leona was one of the few who knew about our swap, together with my mom."

    show leona a_4

    "So in a sense, they were both really close people."
    leona "Thanks, and thank you for coming, you two."

    show leona a_1

    leona "It makes me happy that both of you want to spend time with your good old english teacher."

    show john a_9

    think "Although, she probably isn't happy to turn 50, is she? Would any woman be?"

    show leona a_4
    show john a_8
    show cornelia a_5

    leona "John and Kiyoshi are already in the dining room, in case you're looking for them."

    show sandra a_1
    show john b_2:
        pause 0.5
        ease 0.5 alpha 0.0
    show cornelia b_2:
        pause 0.75
        ease 0.5 alpha 0.0

    "We nodded, both with a smile on our faces as a thanks, and headed further into the building as more people came to greet both of them."

    scene black with dissolve
    pause 0.5
    outfit sayaka suit
    show AN_bg extravagant restaurant:
        zoom 1.25 yalign 0.7 xalign 0.0
    show john a_0:
        center
        faceright
        alpha 0.0
        xpos 0.3
        pause 0.5
        ease 0.5 alpha 1.0
    show cornelia a_0:
        center
        faceright
        alpha 0.0
        xpos 0.1
        ypos 1.05
        pause 0.6
        ease 0.5 alpha 1.0
    with dissolve

    "There were loads of people to greet here, so we made a quick round to introduce ourselves to everyone."

    show john:
        alpha 1.0
    show cornelia:
        alpha 1.0

    think "I didn't even know Leona had this many acquaintances..."

    show AN_bg extravagant restaurant:
        ease 1.0 xalign 1.0
    show john:
        ease 0.5 xpos 0.15 alpha 0.0
    show cornelia:
        ease 0.5 xpos -0.05 alpha 0.0
    show sayaka a_14:
        center
        faceleft
        alpha 0.0
        xpos 1.0
        pause 0.5
        ease 0.5 xpos 0.9 alpha 1.0
    show kiyoshi a_1:
        center
        faceright
        alpha 0.0
        xpos 0.8
        pause 0.5
        ease 0.5 xpos 0.65 alpha 1.0

    "Eventually, I spotted John and Kiyoshi talking to each other."

    show AN_bg extravagant restaurant:
        xalign 1.0
    show kiyoshi a_4:
        xpos 0.65 alpha 1.0
    show sayaka a_2:
        xpos 0.9 alpha 1.0
    show john:
        xpos 0.15 alpha 0.0
    show cornelia:
        xpos -0.05 alpha 0.0

    sayaka "-No, look, I'm not going to raise it."

    show sayaka a_14
    show john a_8:
        ease 0.75 alpha 1.0 xpos 0.45
    show cornelia b_12:
        pause 0.5
        ease 0.75 alpha 1.0 xpos 0.3

    sayaka "Why do you even want one to begin with?"

    show john:
        alpha 1.0 xpos 0.45
    show cornelia:
        alpha 1.0 xpos 0.3
    show sayaka a_3

    sayaka "Oh, hey girls."

    show sayaka a_0
    show kiyoshi a_0 at faceleft

    kiyoshi "Oh?"

    show cornelia a_1
    show kiyoshi a_1

    cornelia "Hey."

    show john a_2

    john "Whazzup."

    show john a_0
    show sayaka a_2

    sayaka "Drop the attempt at being hip with the times already. Seriously."

    show john a_9
    show cornelia a_0
    show sayaka a_14

    "And here he goes bickering again."

    show john a_8

    john "It's not like I would say that to people I barely know."
    john "You guys talking about anything particularly interesting?"

    show sayaka a_10

    sayaka "It sounds more insane if he explains it."

    show sayaka a_3
    show kiyoshi at faceright
    show john a_4

    sayaka "So go right ahead, what were we talking about?"

    show kiyoshi a_3
    show sayaka a_0

    kiyoshi "I cannot really see the {q}insane{/q} in it."

    show kiyoshi a_2 at faceleft
    show cornelia a_5

    kiyoshi "I just wanted John to raise a guard dog for us."

    show kiyoshi a_5
    show john a_6

    kiyoshi "I believed it was well within his power to do so since he works with animals on a daily basis."

    show sayaka a_7
    show kiyoshi a_0 at faceright

    sayaka "The entire point of a guard dog is for the guard dog to actually {i}guard{/i} you, you moron."

    show sayaka a_15
    show john a_6

    sayaka "If I were to raise it then it wouldn't see you as it's master, which totally defeats the entire point of a guard dog."

    show sayaka a_0
    show kiyoshi at faceleft
    show cornelia a_6
    show john a_4

    cornelia "Uh, honey, a dog?"

    show kiyoshi a_5

    kiyoshi "Of course. I thought, on days where you were off, you might feel less lonely with a companion around when I am not home."

    show cornelia b_2

    cornelia "Aw. That's kind of sweet, isn't it?"

    show john a_9
    show cornelia b_1
    show kiyoshi a_1

    john "I guess it's the thought that counts?"

    show sayaka a_14

    sayaka "It's a stupid thought."

    show john a_6
    show cornelia b_11

    john "Well aren't you the romantic?"

    show cornelia b_12
    show kiyoshi a_3
    show john a_5

    kiyoshi "Is that a new outfit you're wearing?"

    show cornelia a_7

    cornelia "Oh? Y- Yeah, I hope you like it..."

    show kiyoshi a_4
    show cornelia a_4
    show john a_4

    kiyoshi "You look stunning."

    show sayaka a_10

    "His praise was apparently something that got Cornelia completely addicted."

    show cornelia a_10
    show sayaka a_18

    "As he smiled while praising her, she swooned just a little and didn't really mask her red face."

    show john:
        pause 0.5
        faceleft
        ease 0.5 xpos 0.65
    show kiyoshi a_1:
        ease 0.75 xpos 0.4
    show cornelia b_2

    "He grabbed her around the waist and gave her a little kiss on her forehead."

    show cornelia b_11
    show kiyoshi a_2
    show john b_8 at faceright
    show sayaka a_10

    "While he was mumbling something to her which I didn't quite catch, me and John both just sighed."
    "It was a pretty common occurrence for Cornelia to seek praise from this guy, enough to make us both think she has a bit of a problem."

    scene black with dissolve
    pause 1
    show AN_bg extravagant restaurant:
        zoom 1.5 xalign 0.45 yalign 0.7
    show john a_8:
        center
        faceright
        xpos 0.4
        ypos 1.1
    show sayaka a_0 behind john:
        center
        faceright
        xpos 0.6
        ypos 1.1
    with dissolve

    "Before long, we were all seated with Leona briefly saying thanks to everyone for coming and telling us what food she was treating us with."
    "We all knew it was going to be her favorite dish, pulled pork burgers with all kinds of cheese, vegetables and fillings and dressing."
    "Having been invited over for dinner at her home a good few times now really goes to show that you can easily figure out what kind of food they like."

    show sayaka at faceleft

    "It was admittedly a bit weird to consider that I was rather good friends with my high-school English teacher, but I wouldn't complain about it."
    "Having personally aged a bit now, I knew a bit more about the issues adults normally face, and having my mom and Leona as back-up advisors was nice in that regard."

    show sayaka a_1

    "Also, they were both cool to hang out with on occasion."

    show john a_4
    show sayaka a_14:
        ease 0.25 xpos 0.575
        ease 0.5 xpos 0.6

    "My inner thoughts were swiftly interrupted though when John nudged me, demanding my attention."

    show john b_5

    john "{size=-5}What is it?{/size}"

    show sayaka a_0

    sayaka "{size=-5}See that woman over there?{/size}"

    show john at faceleft

    "I followed her eyesight towards a woman I had only seen on a few occasions before, and let out a low grunt to signal a yes."
    sayaka "{size=-5}Her dress.{/size}"

    show john a_4 at faceright

    john "{size=-5}...What about it?{/size}"

    show sayaka a_14

    "I already knew the answer though."

    sayaka "{size=-5}If you get the chance, you should ask her where she got it from.{/size}"

    show john a_6

    john "{size=-5}{i}Sigh...{/i} I already have enough {q}party-wear{/q}. I'm not rich, you know.{/size}"

    show john a_0

    sayaka "{size=-5}At least ask her for reference then.{/size}"

    show sayaka a_15

    sayaka "{size=-5}You're still in your glory days, you should make the best of it before you turn way too old.{/size}"

    show john b_4

    john "{size=-5}Yeah yeah, I know...{/size}"

    scene black with wipeclock
    pause 0.5
    outfit AN_circel maid
    show AN_bg extravagant restaurant:
        zoom 1.5 xalign 0.45 yalign 0.7
    show john a_2:
        center
        faceright
        xpos 0.4
        ypos 1.1
    show sayaka a_15 behind john:
        center
        faceleft
        xpos 0.6
        ypos 1.1
    with wipeclock

    "Everyone was chatting at this point."

    show sayaka a_0
    show john a_8:
        pause 0.75
        faceleft
    show AN_circel b_1:
        center
        faceright
        xpos 0.25
        alpha 0.0
        pause 0.5
        ease 0.75 alpha 1.0
    $ AN_circel.name = "Waitress"

    "The waiters and waitresses were going around and pouring red- and white wine to anyone who wanted some."

    show AN_circel:
        alpha 1.0

    "Since Cornelia was driving, I thought I might as well have some."

    show AN_circel b_0

    AN_circel "Would you like a glass?"

    show AN_circel b_1
    show sayaka a_15

    sayaka "Yes. Red wine."

    show sayaka a_0
    show john a_10

    john "I'd like some white wine myself, please."

    show john a_8
    show AN_circel b_3

    AN_circel "Sure."

    show AN_circel b_1:
        pause 0.5
        ease 0.5 xpos 0.325

    "She gave a short smile before pouring it for us to drink."

    show john b_0

    "Meanwhile, the food was starting to be served at a separate table for everyone to take from, kind of like a buffet."

    show sayaka a_15
    show john:
        pause 0.5
        faceright

    sayaka "One of the best things about becoming a guy is that I'm able to actually eat a good fill of those things."

    show john b_5
    show sayaka a_3
    show AN_circel b_4

    sayaka "I kind of pity you for not even being able to stomach just one burger, heh."

    show john a_4

    "I just rolled my eyes at her usual flaunting."

    show john a_0 at faceleft

    "The waitress looked a bit confused at what John said though."

    show sayaka a_0

    "Which would be natural with him just openly saying something like that."

    show AN_circel a_6

    AN_circel "Ah, pardon!"

    show AN_circel b_4:
        ease 0.75 alpha 0.0 xpos 0.7
    show john a_4:
        pause 0.25
        faceright
    show sayaka a_13:
        pause 0.6
        faceright

    "She swiftly moved on to the next guests to offer them wine."

    show sayaka a_1:
        pause 0.5
        faceleft
    show john a_6

    john "At least be a {i}bit{/i} subtle about it."

    show sayaka a_14
    show john a_4

    sayaka "About that girl? Who cares, not like I'm ever going to meet her again."
    john "Well, your problem."

    scene black with dissolve
    pause 0.5
    show AN_bg extravagant restaurant2:
        zoom 1.25 xalign 1.0 yalign 0.6
    show john b_2:
        center
        faceright
        xpos 0.5
        parallel:
            block:
                ease 0.75 xpos 0.525
                ease 1.5 xpos 0.475
                ease 0.75 xpos 0.5
                pause 0.25
                faceleft
                pause 0.5
                faceright
                pause 0.5
                faceleft
                pause 0.5
                faceright
                pause 0.75
                repeat
        parallel:
            block:
                ease 0.5 ypos 1.02
                ease 0.75 ypos 1.0
                ease 0.75 ypos 1.03
                ease 0.5 ypos 1.0
                repeat
    show sayaka a_0:
        center
        faceleft
        xpos 0.75
        parallel:
            block:
                ease 0.75 xpos 0.775
                ease 1.5 xpos 0.725
                ease 0.75 xpos 0.75
                pause 0.25
                ease 0.75 xpos 0.775
                ease 0.5 xpos 0.75
                ease 0.5 xpos 0.775
                ease 0.5 xpos 0.75
                repeat
        parallel:
            block:
                ease 0.75 ypos 1.02
                ease 0.5 ypos 1.0
                ease 0.5 ypos 1.03
                ease 0.75 ypos 1.0
                repeat
    with dissolve

    "Right now, we were pretty relaxed with nothing really going on between us."
    "He wasn't very tensed up and I wasn't angry at him, so we decided to join the people that were dancing to the music on the dancefloor."

    show john b_9

    "Despite how we both got angry at each other way too often, we still enjoyed each other's company at this point. Being angry at each other was just a thing we had."
    "So of course, having a bit of drunken fun was enjoyable every now and then."

    show john b_2
    show sayaka a_3
    show cornelia a_7:
        center
        faceleft
        alpha 0.0
        xpos 0.45
        ypos 1.05
    show kiyoshi a_1:
        center
        faceleft
        xpos 0.6
        alpha 0.0

    "And it's not like I can't break a smile out of him every now and then."

    show AN_bg extravagant restaurant2:
        ease 1.75 zoom 1.35 xalign 0.0 yalign 0.7
    show john:
        ease 0.75 xpos 0.75 alpha 0.0
    show sayaka:
        ease 0.75 xpos 1.05 alpha 0.0
    show cornelia:
        pause 1.0
        ease 0.75 xpos 0.35 alpha 1.0
    show kiyoshi:
        pause 1.25
        ease 0.75 xpos 0.525 alpha 1.0
    pause 1.25

    cornelia "Phew... I didn't know you were this athletic. I thought you would be exhausted faster than me."

    show AN_bg extravagant restaurant2:
        zoom 1.35 xalign 0.0 yalign 0.7
    show cornelia a_5:
        xpos 0.35 alpha 1.0
    show kiyoshi a_2:
        xpos 0.525 alpha 1.0

    kiyoshi "I have the stamina of... A gorilla."

    show kiyoshi a_0
    show cornelia a_6

    kiyoshi "They have a lot of stamina, right?"

    show cornelia a_2

    cornelia "Heh, beats me."

    show cornelia a_1
    show kiyoshi at faceright behind cornelia
    pause 0.75
    show cornelia at faceright

    kiyoshi "...Say, have you ever seen them dance together before?"

    show cornelia a_0

    cornelia "Huh? Saya and John?"

    outfit AN_circel maid
    show cornelia a_10
    show AN_circel a_4:
        center
        faceright
        xpos 0.15
        alpha 0.0

    cornelia "It's not often that we go to parties like this where they both attend, so I guess not."

    show AN_circel:
        ease 0.5 alpha 1.0
    show kiyoshi:
        pause 0.5
        faceleft
    show cornelia a_5 behind kiyoshi:
        pause 0.25
        faceleft

    AN_circel "Uhm... Excuse me?"

    show kiyoshi a_4
    show AN_circel a_5:
        alpha 1.0

    kiyoshi "Hm? What is it?"

    show AN_circel a_7

    AN_circel "Could I ask about the two you were talking about? Saya and John are their names? The gray haired man and the pink haired woman."

    show cornelia a_6

    cornelia "Uh, yeah. What about them?"

    show AN_circel b_5

    AN_circel "Are... Uh... This is difficult to really explain properly..."

    show AN_circel b_0
    show cornelia a_0
    show kiyoshi a_0

    AN_circel "Are they perhaps married or something?"

    show AN_circel b_4
    show cornelia b_2
    show kiyoshi a_3

    cornelia "Pffahaha, those two?"

    show cornelia b_1
    show kiyoshi a_1

    cornelia "Hell no. They barely even get along most of the time."

    show kiyoshi a_2

    kiyoshi "Yup."

    show cornelia b_12:
        pause 1.0
        faceright

    kiyoshi "But they do share a special bond that goes beyond what most people share."

    show cornelia a_2 at faceright
    show AN_circel b_2

    cornelia "A special bond? That's a really poetic way of explaining it."

    show kiyoshi a_1
    show cornelia b_11 at faceleft

    cornelia "But yeah, can't say much more than that they are a special case."

    show cornelia b_12

    AN_circel "Mhm. Interesting."
    cornelia "Why are you asking?"

    show AN_circel a_13

    AN_circel "Oh! Uh...! Nothing! No, really, I was just curious!"

    show kiyoshi a_3
    show cornelia b_6

    cornelia "Uh, alright."

    show kiyoshi:
        ease 0.25 xpos 0.5
    show AN_circel a_12

    kiyoshi "{size=-5}Hey Corny. She sounds suspicious.{/size}"

    show cornelia a_3 at faceright

    cornelia "{size=-5}Of course she does you dum-dum.{/size}"

    show cornelia a_0 at faceleft
    show AN_circel a_6

    AN_circel "I'm terribly sorry for bothering you! I have to get back to the bar now, thank you for talking to me."

    show kiyoshi a_5
    show cornelia a_10

    kiyoshi "Our pleasure."

    scene black with dissolve
    pause 1.5
    scene AN_bg extravagant entrance night
    show john b_9:
        center
        faceright
        xpos 0.6
    show sayaka a_0 at centerleft, faceright
    with dissolve

    "It had become late now. 2 o'clock, to be more precise."
    "Most people were getting ready to leave for their beds. And I especially welcomed the thought of getting a good night's sleep."
    "Me and John were waiting outside for Cornelia and Kiyoshi."
    "Both of them were still inside saying their goodbyes, and since they were driving tonight, we were forced to wait for them."

    show sayaka a_15
    show john b_0

    sayaka "I love nights like these."

    show sayaka a_0
    show john a_8 at faceleft

    john "Where you get something to eat for free?"

    show john a_0

    sayaka "No, the atmosphere."

    show sayaka a_3

    sayaka "You know, chilly, late night with no skies together with friends."

    show john a_10
    show sayaka a_0

    john "Oh, yeah. That's nice."

    show sayaka a_13
    show john a_0

    sayaka "Hey, mom lives right down the road, I'm sure she has Holly's bed available if you don't want to drive another hour."

    show sayaka a_19
    show john a_8

    john "Nah, it's fine. I'd like to visit her but I'm just not really in the mood for it right now."

    show sayaka a_0

    sayaka "Fair enough. Just thought I'd mention it."

    show john a_5

    "Right after concluding that talk, I saw someone watching us from behind."

    show john b_5:
        ease 0.5 xpos 0.55
    show sayaka a_19

    "Sure enough, someone was looking at us from behind the wall for the establishment."
    "The onlooker shrieked as they realized I knew they were there and retreated."

    show john b_0
    show sayaka a_13

    sayaka "Something the matter?"

    show john b_1:
        ease 0.75 xpos 0.6
    show sayaka a_19

    john "Oh, nothing."

    show john b_5

    john "There was just someone looking at us from behind there."

    show sayaka a_1:
        pause 0.75
        faceleft

    sayaka "...Huh?"

    show john b_0

    "He turned his head in curiosity."

    show sayaka a_14

    "Of course, he didn't find anything since the person was likely long gone by now."

    show sayaka at faceright

    sayaka "Anyone you know?"
    john "No idea who it was."

    show sayaka a_18

    sayaka "Hm..."

    show sayaka a_14

    sayaka "Come."

    show john b_10:
        pause 1.5
        ease 0.5 xpos 0.5
    show sayaka:
        ease 0.5 xpos 0.375
        pause 0.25
        faceleft
        pause 0.5
        ease 0.5 xpos 0.275

    "He grabbed my hand and dragged me along with him, and then headed straight for where the person might be hiding."

    show john b_7
    show sayaka at faceright

    john "Hey, no! It's going to be extremely awkward if someone was actually watching us and we meet them!"

    show sayaka a_19
    show john b_10

    sayaka "We're going to be stuck waiting anyways. Let's just make sure it's not some psycho."

    show john a_4:
        transform_anchor True
        pause 0.4
        faceright
        parallel:
            ease 0.25 rotate -8 ypos 1.05
        parallel:
            pause 0.25
            ease 0.75 xpos 0.3 alpha 0.0
    show sayaka a_14:
        faceleft
        pause 0.4
        ease 0.85 xpos 0.0 alpha 0.0

    "It was a norm now that he dragged me with him if he felt like it, so I just accepted my fate."

    scene black with dissolve
    pause 0.5
    scene AN_bg extravagant alley
    show AN_circel b_5 at centerright, faceleft
    show sayaka a_14:
        center
        faceright
        xpos 0.25
        alpha 0.0
        pause 1.25
        ease 0.5 xpos 0.4 alpha 1.0
    show john b_5:
        center
        faceright
        xpos 0.0
        alpha 0.0
        pause 1.35
        ease 0.5 xpos 0.15 alpha 1.0
    with dissolve
    pause 0.5
    show AN_circel a_13
    pause 1.0
    show john a_4

    "Sure enough, that waitress girl that I recognized from the party was just straight up glaring at us in terror as we came into view."

    show john:
        xpos 0.15 alpha 1.0
    show sayaka:
        xpos 0.4 alpha 1.0
    show AN_circel a_6

    AN_circel "Ah! I'm sorry! I shouldn't have spied on you!"

    show sayaka a_19 at faceleft
    show john a_0
    show AN_circel a_13

    "John just looked at me as if expecting me to know what to do in this situation."

    show john a_5

    "I just shrugged while telling him {q}You dragged me into this, handle it yourself!{/q} in body language."

    show sayaka at faceright

    sayaka "You were spying on us?"

    show sayaka a_14
    show AN_circel a_8

    sayaka "Are we really that interesting? Who are you even?"

    show sayaka a_19
    show AN_circel b_0
    show john

    AN_circel "Of course you're interesting. I thought that maybe you were the ones I've been looking forever for and since I really hate this job it would have been nice to-"

    show john a_4
    show AN_circel a_13

    AN_circel "Ah! No more words!"
    "We both raised a brow at this weirdo."

    show AN_circel b_5

    AN_circel "Sigh... I might as well ask to be sure."

    show sayaka a_14
    show john b_5

    sayaka "If you're going to ask us something then do it now. Do you want to know how the food was or something?"

    show AN_circel a_8

    AN_circel "Ah, no! Nothing of that sort."

    show AN_circel a_7

    AN_circel "This is a really weird question to ask so just ignore me if it sounds... Really weird."

    show sayaka a_5
    show john b_0

    sayaka "Just spit it out."

    show sayaka a_14
    show AN_circel a_6

    AN_circel "Of course!"

    show AN_circel b_0

    AN_circel "Did anything really... Uh... Anything special happen in your life?"
    AN_circel "Kind of like... You suddenly are someone else or something?"

    show john b_10
    show sayaka a_20:
        pause 0.75
        faceleft
    show AN_circel b_4

    "Again, we both looked at each other, this time with wide open eyes."
    "This was the first stranger to ever ask a question like this to us, so there was no way she wasn't involved in our swap in some way."

    show john b_7
    show sayaka a_14

    john "How did you-"

    show john b_10
    show sayaka at faceright

    sayaka "That is a question that could mean a lot of things, so specify."

    show john b_3

    john "What? John, she is asking us if-"

    show sayaka a_18

    sayaka "Shut it."

    show john b_10

    "His serious glare meant that I was screwing up."

    show sayaka a_14
    show john b_5

    "I realized soon after that trusting someone like this probably wouldn't be the best idea."
    "Just because she knew about the swap, wouldn't mean that she wants to help us or anything."

    show AN_circel b_2

    AN_circel "Um... Well, you see, I work at a... Special place, where we do work to help people like that, without revealing too much that I can't tell."

    show AN_circel a_0

    AN_circel "I've been looking for people like that here, since we know for certain that three people like that exist here, but I could never find these people."

    show john b_0
    show AN_circel b_1

    think "Three people?"

    show sayaka a_19

    think "But with me and John, it's only two who were swapped."
    "It was clear that he was confused too, but he still had a more relaxed expression now."

    show sayaka a_13
    show AN_circel b_4

    sayaka "And by help, you mean...?"

    show sayaka a_19
    show AN_circel b_5

    AN_circel "{i}Sigh...{/i} We give people the opportunity to undo it. I don't know how else to be less specific."

    show AN_circel b_4

    sayaka "...In that case, yes, we are likely to be part of that group of people you're looking for."

    show AN_circel a_0

    AN_circel "Really?!"

    show AN_circel a_4
    show sayaka a_13
    show john b_5

    AN_circel "Yes!"

    show sayaka a_14
    show AN_circel a_1

    sayaka "You're talking about people that had their personalities switched, correct?"

    show AN_circel a_5

    AN_circel "Oh god, yes! That's exactly what it is!"

    show sayaka a_19

    "Her face was gleaming with joy. I wondered just how long she had been looking for us."

    show AN_circel a_0

    AN_circel "If it's really true then I can report back!"

    show sayaka a_13
    show john b_0
    show AN_circel a_4

    AN_circel "Which also means, I can finally do this!"

    outfit AN_circel angel
    show AN_circel a_1
    with dissolve
    pause 0.5
    show john b_10
    show sayaka a_20

    "As if in an instant, her clothes changed, and out of her back sprouted an incredibly large pair of wings."

    show sayaka:
        ease 0.25 xpos 0.35
    show john:
        ease 0.2 xpos 0.1

    "John and I both took a step back at how sudden that change was, eyes and mouth wide open once more."

    show sayaka a_17
    show AN_circel a_8

    sayaka "Wha- What the hell kind of magic trick was that?!"

    show john b_7

    john "Don't tell me you're actually-"

    show sayaka a_20
    show john b_10
    show AN_circel a_4

    AN_circel "An angel? Yup!"

    show AN_circel b_1

    AN_circel "Hee-hee."
    "She smirked as if she had been anticipating to reveal her true self."

    show AN_circel b_4
    show sayaka a_5

    sayaka "What the hell is this? Do you seriously think we'd believe that?"

    show sayaka a_7

    AN_circel "Oh! Right, most humans don't really believe angels exist anymore."

    show john b_5
    show AN_circel b_5

    AN_circel "That kind of ruins the reveal..."

    show john a_0
    show AN_circel b_4
    show sayaka a_13:
        pause 0.75
        faceleft

    john "Wait, so can you for real fly with those things?"

    show sayaka a_5

    sayaka "The hell do you mean {q}fly{/q}? It's a trick! Don't tell me you actually think this is real."

    show john a_4

    john "Dude, why are you so riled up if you think she isn't the real deal..."

    show sayaka a_14

    sayaka "I'm not at all riled up- I mean, obviously angels aren't real, and you're an idiot for thinking so!"

    show sayaka:
        pause 0.75
        faceright
    show john a_5
    $ AN_circel.name = "Circel, 9th generation messenger angel of the high heavens"

    john "Sorry, what's your name again?"

    show AN_circel b_0

    AN_circel "Circel, 9th generation messenger angel of the high heavens."

    $ AN_circel.name = "Circel"
    show john a_4
    show AN_circel b_1

    john "Alright, can I call your Circel?"
    AN_circel "Of course."

    show john a_8

    john "Alright, Circel. I think he might be doubting whether you're real or not, so can you just levitate a bit or something? At least it would be confirmation for me as well."

    show sayaka a_5 at faceleft

    sayaka "I'm not doubting anything! I'm sure!"

    show john a_4

    john "Right."

    show sayaka a_14 at faceright
    show john a_5
    show AN_circel b_0

    AN_circel "Sure."

    show sayaka a_20
    show john a_11
    show AN_circel a_1:
        ease 0.25 ypos 0.98
        ease 0.25 ypos 0.95
        block:
            ease 0.5 ypos 0.91
            ease 0.25 ypos 0.9
            ease 0.75 ypos 0.94
            ease 0.25 ypos 0.95
            repeat

    "Without much effort, she started flapping the wings a tiny bit, resulting in large windcurrents being released with each flap."
    "Sure enough, she started hovering over the ground."

    show AN_circel a_4
    show john a_0

    AN_circel "See?"

    show sayaka a_7
    show AN_circel a_8

    sayaka "As if that proves anythi-"

    show john a_4

    john "John, we both had our bodies swapped. Angels being real is a very minor side-dish to that fact."
    sayaka "..."

    show sayaka a_10

    sayaka "Urgh, fine. You're an angel, whatever."

    show AN_circel a_5
    show john b_0
    show sayaka a_19

    AN_circel "Hee-hee."

    show sayaka a_5
    show AN_circel a_9

    sayaka "Now wipe that smirk of your face and stop making it so freaking chilly around here with all that wind."

    show AN_circel a_6:
        ease 0.75 ypos 0.98
        ease 1.0 ypos 1.0
    show sayaka a_14

    AN_circel "Oh! I'm sorry!"

    show john b_1
    show AN_circel a_13

    "She landed and bowed to signify her apology."

    show john b_5
    show AN_circel a_8

    john "You said you can swap us back?"

    show AN_circel b_0
    show sayaka a_19

    AN_circel "Yes, yes. It takes a bit of time since it's new technology, even for us, but we've helped a lot of people already!"

    show sayaka a_14
    show AN_circel b_1

    sayaka "So we just go back to their normal lives and pretend as if nothing had happened?"

    show AN_circel b_0
    show john b_0

    AN_circel "Exactly! We have the power to make it a seamless process. You won't even know you swapped if you would like that."

    show sayaka a_18

    sayaka "...Hm, I don't know..."

    show AN_circel b_4
    show john b_8

    john "I'm in the same boat, this sounds a little... You know..."

    show john b_0
    show AN_circel b_0
    show sayaka a_19

    AN_circel "Fishy? We can let you talk with people who we've helped before if you don't trust us, so you don't have to worry about user reviews!"

    show sayaka a_14
    show AN_circel b_1

    sayaka "User reviews? Wha- No, that's not what I meant."

    show sayaka a_2

    sayaka "I'm happy with my life right now. Another swap would be extremely unnecessary and just complicate things."

    show sayaka a_19
    show AN_circel b_4
    show john b_4

    john "Yeah."

    show AN_circel a_8

    AN_circel "Huh? You don't want to go back?"

    show AN_circel a_7
    show john b_5

    AN_circel "How did you guys even meet in the first place?"
    john "...School?"

    show AN_circel a_10

    sayaka "High school."
    AN_circel "Oh, wow. You both went to school together and were swapped?"

    show AN_circel a_0

    AN_circel "You guys are lucky."

    show john b_0

    AN_circel "I guess that's why you're okay with it then."

    show sayaka a_14
    show AN_circel a_8

    sayaka "How is this lucky? We worked hard towards the outcome together."
    sayaka "If anything we were lucky to turn this mess of ours into something positive."

    show john b_8

    john "Agreed."

    show john b_0
    show AN_circel a_1

    AN_circel "Uh... To each their own I suppose."

    show AN_circel a_9

    AN_circel "But you are certain you don't want to go back to your original bodies then?"

    show sayaka a_0

    sayaka "Of course. We've already talked about this."

    show sayaka at faceleft

    sayaka "We both agreed that if we ever were to be put into a situation where we could choose to undo everything, we'd both say no."

    show john b_2

    john "Yep."

    show john b_9
    show sayaka a_19 at faceright

    sayaka "We did that a long time ago. To just go back and act as if everything was normal would be terrible."

    show AN_circel a_4
    show sayaka a_0

    AN_circel "Ah. I see. Then this has also managed to make some people happy. That is a relief."

    show AN_circel a_8
    show sayaka a_19
    show john b_0

    cornelia "{size=-5}Saya?! John?! Are you guys out here?!{/size}"
    think "Ah, they must be long done saying their farewells inside by now."

    show AN_circel b_3

    AN_circel "Oh, and uh, don't tell anyone else I exist, please. I think my boss doesn't want everyone to know that I'm an angel and everything... You know."

    show AN_circel b_1
    show sayaka a_0

    sayaka "We've been keeping a bigger secret like that throughout half our lives. Our lips are sealed."

    show john b_9
    show AN_circel b_0

    AN_circel "Thank you so much."

    show sayaka a_19

    AN_circel "In the name of Andarius the Holy, I wish you both farewell and the best."
    AN_circel "And if you ever meet a being called Circe, please make sure to greet her for me."

    show AN_circel a_1:
        ease 0.5 ypos 0.9 alpha 0.0
    show john b_0

    "With that, she was gone."
    sayaka "She dead-ass just flew away. Wow."

    show sayaka at faceleft

    sayaka "Someone like her probably waited for an opportunity to take a leave like that."

    show john b_1

    john "Heh."

    show john b_5

    "Still, we just met an actual angel. What the hell? Did that mean religion was real?"

    show sayaka at faceright
    show john b_0
    show cornelia b_7:
        center
        faceleft
        xpos 0.9
        ypos 1.05
        alpha 0.0
        pause 0.5
        ease 0.75 alpha 1.0 xpos 0.7

    cornelia "Hello~~o?"

    show cornelia b_13

    cornelia "There you are! What on earth are you doing back here?"

    show john b_9

    john "Hey."

    show john b_4

    john "Sorry, we got sidetracked."

    show cornelia b_2

    cornelia "I was almost worried you both decided to walk home from here."

    show sayaka a_14
    show john b_0

    sayaka "We're not {b}that{/b} drunk."

    scene black with Dissolve(1.5)
    pause 1
    outfit john casual
    outfit cornelia casual_b

    title "24th of May (Saturday)" "Day 3213‬ - John"

    pause 0.5
    show AN_bg AP livingroom:
        zoom 1.5 xalign 0.45 yalign 0.8
    show john b_0:
        center
        faceright
        xpos 0.35
        ypos 1.1
    show cornelia b_12:
        center
        faceleft
        xpos 0.65
        ypos 1.15
    with dissolve

    john "Name five dog breeds."

    show cornelia b_6

    cornelia "Hmm... That could be anything."

    show john a_4
    show cornelia b_12

    john "I know you, this one is easy for you."

    show cornelia b_5
    show john a_0

    cornelia "There's husky, border co-"

    show john a_6
    show cornelia b_12

    john "You already got it."

    show cornelia b_2

    cornelia "Hah, really? Was it husky?"

    show cornelia b_1
    show john a_9

    john "Yeah..."

    show john a_8

    "We were playing a new game Cornelia had bought right now."
    "She usually comes to visit on days where we both have nothing to do."
    "It's nice to hang out with her. We are really close friends after all."
    "The game was pretty simple. Draw a card with a word on it, and the other player needs to guess that word through some task."
    "Cornelia and Kiyoshi had a husky at home, so obviously this one was way easy for her to guess in this case."

    show cornelia a_2
    show john a_0

    cornelia "It's like the game was made for me."

    show john b_5
    show cornelia a_1

    john "Yeah yeah, you get the easy ones."

    show cornelia b_11

    cornelia "Hehe, someone's a sore loser."

    show cornelia b_1
    show john b_0

    cornelia "Has life been treating you well recently?"

    show john b_8

    john "Well, the usual. We just started a new project and they already want to crunch it."

    show cornelia b_12
    show john b_0

    cornelia "Yikes."

    show john b_9

    john "Your turn."
    cornelia "Right."

    show cornelia b_4
    show john b_0

    cornelia "But you managed to avoid being part of that crunching thing again?"

    show john b_5

    john "There are {i}a lot{/i} of voiceovers to be made this time. You wouldn't even believe it. So I don't think I can weasel myself out of this one."

    show cornelia b_12
    show john b_0

    cornelia "That sucks. Alright, name three oceans."

    show john b_8

    john "God, I suck at geography."

    show john b_5

    john "There's the Pacific ocean..."

    play sound sfx_bell
    show john b_0:
        pause 1.0
        faceleft
    show cornelia b_5

    "The front-bell rang at that moment."

    show cornelia b_12
    show john at faceright

    "We both looked at each other, but neither of us seemed to expect anyone to visit."

    show cornelia b_4

    cornelia "Kids selling cookies or something maybe?"

    show john b_1

    john "Sounds like you're hoping for some sweets to eat."

    show john b_9:
        ease 0.5 ypos 1.0
    show cornelia b_2

    cornelia "I wouldn't mind spending a dollar or twenty on it."

    show john b_0 at faceleft
    show cornelia b_12
    play sound sfx_door_open

    "I got off the couch to see who it was, but right as I started walking towards the door, it opened."

    show john a_4

    "At that point, I knew who it was."

    show john b_3

    john "John?!"

    show john b_0

    sayaka "{size=-5}It's me!{/size}"
    think "What business does he have now?"
    sayaka "{size=-5}You won't believe what the newspapers just publi- Argh, fucking shoelaces!{/size}"

    show john b_5

    think "Newspapers? He isn't usually someone to be very hyped about those."

    scene black with dissolve
    outfit sayaka casual_j
    pause 0.25
    scene AN_bg AP entrance
    show john b_0:
        left
        faceright
        alpha 0.0
        pause 0.75
        ease 0.5 alpha 1.0 centerleft
    show sayaka a_21:
        center
        faceright
        xpos 0.8
    with dissolve
    pause 1.0
    show sayaka a_19

    john "Need help?"

    show john:
        alpha 1.0 centerleft
    show sayaka a_14 at faceleft

    sayaka "Argh, no, I just managed to get them tangled around my leg."

    show sayaka a_0

    sayaka "Oh, and, hey."

    show john b_5
    show sayaka a_19

    john "Anything exciting happened? Since you took the trip here without announcing it."

    show sayaka:
        faceright
        ease 0.5 right

    sayaka "Corny is here too?"

    show john b_0

    think "Right, he noticed her shoes."

    outfit sayaka casual
    with dissolve
    show john b_9

    john "We were playing in the living room. Want to join?"

    show sayaka a_13 at faceleft

    cornelia "{size=-5}What's up, John?!{/size}"

    show sayaka a_4

    sayaka "Hey! Sorry for interrupting what you were doing!"

    show sayaka a_0

    cornelia "{size=-5}No problemo!{/size}"

    show sayaka a_19:
        ease 0.75 xpos 0.6
    show john b_0

    sayaka "Here."
    "He handed me a crumpled newspaper he brought with her."

    show john b_5

    sayaka "Kiyoshi phoned me about it. He tried texting you too but you hadn't responded yet."
    john "My phone is charging in my bedroom, so that's why."

    show sayaka a_14

    sayaka "It's the headline today."

    show sayaka a_13
    show john b_0

    sayaka "No, wait, let's go into the living room before you read it."

    show sayaka a_19:
        parallel:
            ease 1.25 xpos 0.1
        parallel:
            pause 0.5
            ease 0.5 alpha 0.0
    show john:
        pause 0.75
        faceleft

    "This had me genuinely curious now."
    "He was way too hyped for this to be some ordinary stuff. Did he get an article about himself or something?"

    scene black with dissolve
    scene AN_bg AP livingroom
    show sayaka a_3 at center, faceright
    show cornelia b_2:
        center
        faceleft
        xpos 0.75
        ypos 1.05
    show john b_0:
        center
        faceright
        xpos 0.1
        alpha 0.0
        pause 0.75
        ease 0.75 xpos 0.25 alpha 1.0
    with dissolve

    "We went back into the livingroom, where John and Cornelia did their usual meeting ritual of a handclap."

    show john:
        xpos 0.25 alpha 1.0
    show cornelia b_1
    show sayaka a_0

    sayaka "I can move it a bit, right?"

    show cornelia b_12

    "He pointed towards the game we were playing."

    show sayaka a_19 at faceleft
    show john b_9

    john "Yeah, go ahead."

    show cornelia b_4
    show john b_0
    show sayaka a_0 at faceright

    "While John was making room, seemingly to give space for the newspaper, Cornelia had a curious look."

    show cornelia b_12
    show sayaka a_19

    cornelia "Something happened?"

    show sayaka:
        pause 0.5
        faceleft
        ease 0.5 xpos 0.45

    sayaka "Here."

    show john a_4
    show sayaka:
        faceright
        ease 0.75 xpos 0.5

    "He snatched the paper out of my hand and placed it on the table."

    show john b_0

    sayaka "Just read the headline."

    $ gui.textbox_yalign = 0.03
    scene AN_bg newspaper with dissolve

    "It had an image of a woman."
    think "{q}I became someone else{/q}."
    "That was the headline for the article."
    "I continued reading the synopsis right below."
    think "{q}Michelle Bloom (28) describes her recent years of panic and anxiety, as she believes herself to be born as someone else entirely. In her past, she claims to have been Zendaya Uduike, and despite never having shown interest in African culture, manages to speak fluent Swahli and knows many other customs and locations. Her story is chilling, to the point where one could wonder if there is a grain of truth in it.{/q}"

    $ gui.textbox_yalign = 1.0
    scene AN_bg AP livingroom
    show sayaka a_19 at center, faceright
    show cornelia b_9:
        center
        faceleft
        xpos 0.75
        ypos 1.05
    show john b_0:
        center
        faceright
        xpos 0.25
    with dissolve

    "Cornelia was done reading before I was, so when I looked up, she had already recoiled."
    cornelia "{b}{i}That{/i}{/b} Michelle?! From our high-school?!"

    show sayaka a_14

    sayaka "It's her, I double-checked."

    show cornelia a_7

    cornelia "People thought that girl had freaking died!"

    show john b_10
    show cornelia a_8

    "I was bad at remembering people, but after thinking about it, I remembered everything here."
    "She was one of Kat's best friends."
    "She suddenly stopped coming to school because of some incident."

    show john a_11
    show sayaka a_19:
        pause 1.5
        faceleft

    "I remembered how Kat explained the situation back then."

    show cornelia a_5

    "It made too much sense now. The newspaper might doubt it, but reading it with context of our swap and her sudden insanity, it had to be true."

    show sayaka a_14
    show john b_10

    sayaka "Sayaka, calm down."
    sayaka "The girl says she is living a good life at the end if that worries you."

    show john b_4

    john "Wha-"

    show john b_5

    "I noticed now that I was sweating a bit after reading it."

    show sayaka a_19
    show john b_8

    john "I- Uh..."

    show cornelia a_0

    think "I should tell them about what Kat told me, shouldn't I..."
    think "Even if I promised her not to tell anyone about it..."

    show john b_4

    john "{i}Sigh...{/i} About this..."

    scene black with dissolve
    pause 1.5
    scene AN_bg AP livingroom
    show sayaka a_18:
        center
        faceleft
        ypos 1.1
    show cornelia b_4:
        center
        faceleft
        xpos 0.75
        ypos 1.15
    show john b_8:
        center
        faceright
        xpos 0.25
        ypos 1.1
    with dissolve

    sayaka "Jesus... I feel kinda bad for making fun of her now..."

    show john b_5

    cornelia "You took the words right out of my mouth."
    "Luckily they didn't get mad at me for not sharing it with them."
    "After telling them the story, it helped them understand just how fucked up this girl's situation must have been after having been swapped."

    show sayaka a_10

    sayaka "Even if it was you, I can't imagine how screwed my life would be if I swapped with someone across the globe, assuming what happened to her was the exact same as what happened to us..."

    show sayaka a_1

    sayaka "Especially from a dump like Africa."

    show john b_0
    show sayaka a_19 at faceright
    show cornelia b_12

    cornelia "But what happened to the real Michelle then?"

    show sayaka at faceleft

    john "I was wondering that too."

    show sayaka a_18

    sayaka "Right... About that."

    show sayaka a_14

    sayaka "I really suck at being empathetic, so I don't really know how to say it in a way that isn't going to freak you out, but..."
    sayaka "She is probably dead."

    show cornelia b_9
    show john b_10

    "Cornelia gasped and put her hands around her mouth."
    john "It... It says in the article?"

    show sayaka a_19

    sayaka "At the end, yeah."
    sayaka "In short she told them that in her previous life, or body, whatever, she was about to starve to death and probably would have died with another few days..."

    show cornelia b_8

    john "..."

    show john b_4

    john "I think I get why we were lucky then..."

    show sayaka a_14
    show john b_5

    sayaka "I thought back to those words too. That girl we met must have known about Michelle."

    show cornelia b_12

    sayaka "But doesn't this just confirm the most fucked up thing? The thing we hadn't even thought about?"

    show john b_0

    john "That we weren't the only ones?"
    sayaka "Exactly. In just our little city, three people had this happen to them. Imagine how many people this has happened to worldwide!"

    show sayaka a_18

    sayaka "We weren't targeted at all. We just... Happened to be in the crossfire or were collateral or something..."

    show john b_4

    sayaka "I don't know... I don't really want to dig deeper either..."
    sayaka "Without that girl's help, we probably would never have been able to swap back anyways."
    john "...This really is kind of fucked up. So there are probably many others like us out there then."

    show john b_0
    show sayaka a_19 at faceright

    cornelia "Wh- Who is {q}that girl{/q}?"

    show sayaka a_13

    sayaka "Uh... Can't say, sorry."

    show sayaka a_19
    show cornelia b_13

    "Cornelia raised a brow, but didn't look further into it."

    show sayaka a_18
    show cornelia b_12
    show john b_5

    sayaka "But really, it does make me curious. What on earth really happened back then to cause all of this..."

    scene black with Dissolve(2.5)
    pause 2

    title "10th of august (Wednesday)" "Day 2 - ???"

    define unknownA = Character("????", color="#ccd4be", what_color='#8e8fff', window_background=Frame("AN_asset db_scanner", gui.textbox_borders, tile=True))
    define unknownB = Character("?????", color="#ffd4be", what_color='#ff8e8e', window_background=Frame("AN_asset db_scanner", gui.textbox_borders, tile=True))

    pause 3
    scene AN_bg mindscape
    show AN_asset grain:
        block:
            ease 3 alpha 0.2
            ease 1 alpha 0.1
            ease 1 alpha 0.2
            ease 3 alpha 0.7
            repeat
    with Dissolve(3.0)
    pause 3
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "S- Sister...?"

    hide minunknown at centerleft with wiperight
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "What is it?"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "We might be in... Slight trouble."

    hide minunknown at centerleft with wiperight
    pause 1.5
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "The way you worded {q}slight{/q} makes me believe there is more trouble than the word implies."

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "..."
    unknownA "The modifications we did a while back. Do you remember them?"

    hide minunknown at centerleft with wiperight
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "Is this related to that?"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "...Not directly."

    hide minunknown at centerleft with wiperight
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "Then what is it?"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "The modifications were a success, but might have had... Issues."

    hide minunknown at centerleft with wiperight
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "Just spit it out! What is the issue?"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "Dimension A-N-12 was affected by it and has caused several errors."
    unknownA "And these errors have affected a comparatively large amount of it's population compared to what the modification was supposed to fix."

    hide minunknown at centerleft with wiperight
    pause 2
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "...What errors?"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "The mixing of souls."

    hide minunknown at centerleft with wiperight
    play sound AN_sfx_psyred
    show philunknown at centerright, faceleft with wiperight

    unknownB "How did that happen?"
    unknownB "That dimension isn't even connected to O-S-8!"

    hide philunknown at centerright with wipeleft
    play sound AN_sfx_psyblue
    show minunknown at centerleft with wipeleft

    unknownA "...The boss is going to be very upset if he finds out about this..."

    hide minunknown at centerleft with wiperight
    pause 1.5
    scene black with Dissolve(2.0)
    pause 1

    gameover "The end. Thanks for playing!"

    pause 2

    "Before you go, I would just like to say a huge thanks to GarySavage and Finn Underwood who have helped a lot with assets for this scenario."
    "Some assets were created from scratch or modified from other assets, but without their help, this scenario would never have been possible."
    "And thank you to everyone else who helped me out visualizing this story!"
    "I very much hope you enjoyed playing this scenario. See you on the next one!"

    pause 2
    return
