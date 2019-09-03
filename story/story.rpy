label AN_initited:

    $ renpy.movie_cutscene(AN_movie_intro)

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

    title "8th of August" "The first day - John"

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
    show school entrance day:
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

    show school entrance day:
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
    show school entrance day:
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

    title "8th of August" "The first day - Sayaka"

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
    show school hallway day:
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

    title "8th of August" "The first day - John"

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

    title "9th of August" "Day 2 - Sayaka"

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
    body carrie AN_carrie
    scene bg main house day
    show sayaka a_5:
        centerright
        faceright
        block:
            ease 0.6 yanchor 0.99
            ease 0.8 yanchor 1.00
            repeat
    show carrie a_9 at center, faceright:
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

    show carrie a_33 at faceleft

    carrie "{size=-8}Is this my chance...?{/size}"

    show sayaka behind carrie
    show carrie a_36:
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
    show carrie a_34

    sayaka "Uh, yes. Do I have to repeat myself or some shit?"

    show carrie a_9

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
    show carrie a_9:
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
    title "9th of August" "Day 2 - John"

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

    scene classroom 1
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

    title "9th of August" "Day 2 - Night"

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

    title "11th of August" "Day 4 - John"

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

    title "11th of August" "Day 4 - Sayaka"

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

    title "12th of August" "Day 5 - John"

    show school entrance day:
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
    show sayaka a_5 at left, faceright:
        alpha 0.0

    think "...{size=+10}What?!{/size}"

    #TODO: Add john with pink hair

    show school entrance day:
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

    show sayaka a_15 at faceright

    john "What the hell do you think you're doing?!"
    "She finally noticed me waltzing her way and was shocked at first."

    show sayaka a_17

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

    show sayaka a_7
    show john
    show cornelia b_0

    sayaka "He fucked up my hair! That's wha-"

    show sayaka a_4

    sayaka "I- I mean..."
    "The charade of keeping this secret was out by now anyways, thanks to Kiyoshi, but obviously I hadn't told Sayaka about that."

    show sayaka a_16

    "She was still concerned about keeping up appearances even though our lives were taking a freaking skydive for the worst."

    show sayaka a_7

    sayaka "{b}She{/b} messed up her hair! Can you believe it?!"

    show cornelia b_6
    show sayaka a_16

    cornelia "...Saya has been walking around like that for four days now, so what do you care?"

    show sayaka a_7
    show cornelia a_7

    sayaka "But it's terrible! The hair is terrible! Fuck you for messing up my hair!"

    show john a_3
    show sayaka a_16
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

    AN_harry "Ah, well, not really gawking or anything. I thought we would all go get the equipment."

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

    title "12th of August" "Day 5 - Sayaka"

    pause 1
    scene bg classroom 1
    show jack a_0 at centerright, faceleft
    with dissolve

    jack "Now, is there {i}anyone{/i} in here who is able to tell me anything about Charles Philippe?"

    show jack a_8
    show sayaka a_5 at Position(pos=(0.2, 1.1), anchor=(0.5, 1.0)):
        faceright
        alpha 0.0

    jack "...Nobody?"

    show jack a_9
    show sayaka:
        ease 0.5 alpha 1.0

    jack "...How about you, John? Got anything {q}wise{/q} to share with us about this topic since you so seemingly believe you do not need to pay attention?"

    show sayaka a_2:
        alpha 1.0

    sayaka "Huh? Wh-What?"

    show sayaka a_16

    "What actually is his deal here?"
    "I looked away for ten seconds and already he starts fucking singling me out again!"
    sayaka "Don't know."

    show jack a_0

    jack "I believe I made it perfectly clear that this was homework assignment for today, didn't I?"
    sayaka "No it wasn't. We had to read a text from some documentalist."

    show jack a_1

    jack "That was the assignment for the class. But of course your inferior head wouldn't be able to keep track of me telling you to research this topic last class."

    show sayaka a_7

    sayaka "You never told me anything like that!"

    show sayaka a_16
    show jack a_0

    "To add fucking insult to injury, the entire class was humoring themselves as if this was some kind of circus. Nobody was defending me, at all!"
    "Why is any of this happening? What did I ever do to that fuckface?"
    jack "I made it very clear. So I am expecting a report on Charles Philippe's rule this tuesday. Just to make sure you actually do something for once."

    show jack a_9

    jack "Oh, and be sure to add in a section that retrospects on why it is important to listen to your teacher. Maybe you could make advancements by yourself where even the best would fail to teach you."

    show sayaka a_20

    sayaka "I already have two reports for tuesday that you gave me two days ago!"

    show jack a_3
    show sayaka a_16

    jack "Am I to assume you would like one more, this time about proper behavior in class?"

    show sayaka a_24

    sayaka "I- N- No."

    show jack a_0
    show sayaka a_16

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
    show sayaka a_24:
        center
        faceleft
        ypos 1.1
    with dissolve

    think "Sigh... Okay, just keep it cool. No more flipping out."

    show sayaka a_16

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

    show sayaka a_2 at faceright

    think "Huh?"

    show sayaka a_5

    think "Oh, it's Brad."
    think "What does he want from a twerp like John?"
    sayaka "Yeah, sure."

    show brad a_7:
        ease 0.5 ypos 1.1

    brad "Thanks. I saw what you're reading. That's some weird stuff you're gonna talk about in front of Jack."

    show sayaka a_16

    sayaka "Oh, this? I'm just trying to read some books to figure out something completely unrelated. I couldn't give less of a shit about that jerk."

    show brad a_4

    brad "Uhuh. {q}Spiritual Bond{/q}... Didn't know you were into the... Metaphysical stuff and books like that, or what do you call it?"

    show brad a_1
    show sayaka a_2

    brad "What are you trying to figure out? I'm not into spirits and such, but you know I'm a great advisor, heh."

    show sayaka a_5
    show brad a_0

    sayaka "I really doubt you would be interested. Or even know anything about this."
    brad "That just piques my interest even more. Come on, you starting a new religion or something?"

    show sayaka a_27 at faceleft

    sayaka "{i}Sigh{/i}... Alright, because it's you... How do I even explain this so you get it..."

    show sayaka a_5 at faceright

    sayaka "Something that isn't possible happened. And I don't know how it happened or who or what did it."

    show brad a_3

    sayaka "So I've been trying to read any book about some sci-fi bullshit I could find but I'm getting nowhere with this."

    show brad a_4

    brad "Something impossible? Doesn't that just mean it is possible?"

    show sayaka a_16

    sayaka "Obviously. But I want to know how it happened, hence why I am reading this. But even after reading the first few pages I know this one's a dud as well."

    show brad a_5

    brad "But you don't want to share what happened?"
    sayaka "Fuck no. Only me and someone else can know about this."

    show brad a_1

    brad "Ah well, too bad."

    show brad a_0
    show sayaka a_2

    brad "But it sounds interesting. More interesting than whatever Mallory has planned for us."
    brad "Honestly I don't really know what else to tell you. Sounds to me like you're into something weird."

    show sayaka a_16

    sayaka "It totally is."

    show sayaka a_5
    show brad a_1

    brad "You know, when I was in middle school, Zoey did some weird-ass stuff too."

    show brad a_4

    brad "Oh, you know Zoey, my sister, right? She started here as a freshman this year."

    show sayaka a_2

    sayaka "I think I saw some yellow runt telling everyone she was your sibling or something yesterday."

    show brad a_7

    brad "She did?"

    show brad a_1

    brad "Hah, that's sweet of her."

    show brad a_0

    brad "Anyways, her shenanigans are really annoying sometimes, I wouldn't say that her pranks were out of this world or anything impossible like you claim your problem to be, but I grew to like it when she did something stupid."

    show sayaka a_24

    sayaka "God, it's so cliche to say that I can turn this into something positive."

    show sayaka a_16
    show brad a_7

    brad "I know, but cliche stuff is cliche because it's normal, right?"

    show sayaka a_5

    sayaka "And man, you really swoon over your sister, don't you?"

    show brad a_1

    brad "Can't help it."

    show brad a_4

    brad "Oh, and uh... Nice hair you got there...?"

    show sayaka a_16

    sayaka "Drop it, I know it's stupid."
    brad "Did you lose a bet?"
    sayaka "I tried to get back at someone but now I'm stuck with this ridiculous color."

    show sayaka a_27

    sayaka "{size=-5}It doesn't fit me at all right now...{/size}"

    show brad a_1
    show sayaka a_2

    brad "Was it Kat?"

    show sayaka a_7
    show brad a_4

    sayaka "Katrina? Fuck no. Why would you think that?"

    show sayaka a_16
    show brad a_6

    brad "Ah, you know, with the rumors going around and all..."

    show sayaka a_2

    think "The rumors?"

    show sayaka a_5

    sayaka "What rumors?"

    show brad a_5

    brad "About you and Kat."

    show sayaka a_16

    sayaka "I don't give a shit about her."

    show brad a_3

    brad "Man, you guys got into that bad of a fight?"
    sayaka "Let's not make this about her. What is the rumor?"

    show brad a_5

    brad "You know, you and Kat are seen as the {q}nerdy{/q} couple of the school, so you guys causing such a big fallout in the lunchroom has sparked all kinds of people to speculate."

    show sayaka a_5

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

    show sayaka a_0
    show brad a_0

    sayaka "It's okay. I needed someone to talk to."

    show brad a_1

    brad "Stressed week?"

    show brad a_0
    show sayaka a_10

    sayaka "Oh, you wouldn't know."

    show sayaka a_0
    show brad a_7

    brad "Hey, if you want, you can come along with me to our table during lunch. In case you're still not getting along with your friends."

    show sayaka a_5

    "Brad had never been this nice to any of the girls I knew, yet he was being a complete bro to freaking John of all people?"

    show sayaka a_15

    think "He isn't actually, like, secretly popular amongst the cool guy group, is he?"

    show sayaka a_6

    sayaka "Uhh... Sure, I think I'll take you up on the offer."

    show sayaka a_2

    sayaka "Better than sitting around doing nothing."

    show brad a_0

    brad "Cool. Let's jet."

    scene black with dissolve
    show bg lunch:
        zoom 1.5 xalign 0.8 yalign 0.95
    show sayaka a_0 at centerright, faceleft
    show brad a_0 at center, faceleft
    with dissolve

    "The last two days during lunch had been excessively boring."

    show sayaka a_5

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

    show sayaka a_2:
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

    title "12th of August" "Day 5 - John"

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
    show sayaka a_16 at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0)) behind john:
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

    show sayaka a_7

    sayaka "Uh, hello?! Yes?! Anyone but him! Did you tell them about us?"

    show sayaka a_16

    john "Of course I did. They both know we swapped."

    show sayaka a_20
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

    show sayaka a_21
    show brad a_4

    "Sayaka's half-way shouting was now garnering a bit of attention."

    show sayaka a_15:
        faceright
        pause 0.5
        faceleft
        pause 0.5
        faceright
    show john b_13

    "Attention that she noticed."

    show sayaka at faceleft

    "Even though the attention on us three was aplenty already because the number one girl in school was sitting with the most despised guy among the girls."

    show sayaka a_21

    sayaka "{size=-5}Why can you not do ONE thing properly?{/size}"

    show john b_17
    show cornelia b_5

    brad "Uh, John?"

    show john b_18
    show brad a_5

    john "You're not exactly keeping it a secret yourself in this public space either."

    show sayaka a_15
    show john b_17

    sayaka "...!"

    show john a_17

    john "You know he is actually willing to help try to reverse the swap."

    show sayaka a_16

    sayaka "Oh spare me the formalities, I know you're probably just as much of a sick perv as him and want to take advantage of this."

    show cornelia b_29
    show john b_0

    cornelia "Hold on."

    show sayaka at faceright

    "The girl that was pretty much sinking into her chair out of confusion finally spoke up."

    show cornelia b_31

    cornelia "Is... Is this entire swap thing actually a real thing?"

    show sayaka a_7

    sayaka "No! No swaps, no nothing! I'm Dumbass Davis and he is Sayaka Sato!"

    show sayaka a_16 at faceleft
    show john b_6

    john "You know that you can trust her, right?"

    show sayaka a_21

    sayaka "N-"

    show cornelia b_11
    show john b_23

    think "Heh, if you answer no here it would make you look bad, wouldn't it?"

    show john b_31

    john "As I tried telling you this morning, yes, me and Sayaka swapped bodies for some reason."

    show brad a_4

    cornelia "..."

    show cornelia a_22
    show sayaka a_16 at faceright

    cornelia "But that shouldn't be possible..."

    show john b_27
    show sayaka a_15

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

    show sayaka a_16

    show john a_13 at faceleft

    john "{i}Sigh{/i}... She, or he, whatever, is Sayaka, not John."

    show brad a_4

    brad "Whoah. So I was talking to Queenie all the time?"
    brad "That's trippy."

    show john a_6

    think "He is... unusually accepting as well."

    show sayaka a_20
    show john b_0 at faceright
    show cornelia b_31

    sayaka "Fine! Anyone else want to know?!"

    show john b_3
    show sayaka a_16

    john "Dude, chill. Let's just put all the stuff we've done behind us and actually get help on this, alright?"

    show sayaka a_7

    sayaka "Alright?! You probably still haven't lifted a finger trying to figure out how to swap back!"

    show john b_19
    show sayaka a_16

    john "I got Kiyoshi to help us!"

    show sayaka a_7
    show john b_3

    sayaka "Bullshit! I bet you've been oggling all over me ever since you told him!"

    show sayaka a_16
    show cornelia a_22

    cornelia "Uhm... I think he {i}is{/i} trying to help..."

    show sayaka a_21 at faceright
    show john b_6
    show cornelia a_8

    "Sayaka turned her absolute fury towards Cornelia now."
    think "Boy, this girl is a living volcano..."

    show sayaka a_20
    show brad a_3

    sayaka "You're siding with them now, Corny?!"

    show sayaka a_16
    show cornelia b_32

    cornelia "Wha- N- No! Im not siding with anybody! Everything they've talked about for lunch was how they want to figure out how to swap back or something!"

    show john b_0
    show kiyoshi a_1
    show cornelia b_31
    show sayaka a_5

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

    show sayaka a_2

    sayaka "...Are you actually willing to help us then? Without being your usual shitty self?"

    show kiyoshi a_2

    kiyoshi "I very much plan to, oh maiden in need of ai-"

    show kiyoshi a_1
    show sayaka a_16
    show john at faceright

    sayaka "Yeah yeah, whatever. Fine then."

    show john b_1

    "For the first time, I was able to calm her down, if even a little. Be it with the help of two other people, but still, we've tamed the dragon."

    show brad a_7
    show kiyoshi at faceleft
    show cornelia b_0
    show sayaka a_5
    show john b_0 at faceleft

    brad "Uh, so yeah, good luck to you guys."

    show sayaka a_16

    sayaka "Ugh, you heard everything, didn't you?"

    show brad a_1

    brad "Sorry, it was just a bit too interesting to listen for me to just bail out of the conversation."

    show brad a_5

    brad "But you and Sayaka have switched places then?"

    show cornelia b_17
    show john at faceright
    show sayaka a_2 at faceright
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
    show sayaka a_16
    show john a_32

    sayaka "I am not attracted to you, you fucking perv."

    show kiyoshi a_2

    kiyoshi "Denial is the sweetest way of showing love."

    show cornelia a_0
    show brad a_0
    show john a_0
    show sayaka a_5

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
    show sayaka a_5 at Position(pos=(0.4, 1.1), anchor=(0.5, 1.0)), faceleft
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

    show sayaka a_16

    sayaka "Are you kidding me? Of course they help! Would you not categorize what {i}really happened{/i} to us as fiction under normal circumstances?"

    show john a_0

    john "Well, if you put it like that..."
    sayaka "If anything, we might get ideas on what to do in order to swap back."

    show sayaka a_5 at faceleft

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

    show sayaka a_16
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
    show sayaka a_5
    pause 1.5

    cornelia "...Uhm..."

    show cornelia a_11
    show sayaka a_16
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

    show sayaka a_7
    show john b_17

    sayaka "Fuck you. I didn't ask for any of this to happen!"

    show sayaka a_16

    sayaka "Also, why have you been rubbing your eyes all this time?"

    show john a_13

    john "Huh?"
    "Ah. I was doing it subconsciously at this point, but my eyes had become {i}really{/i} itchy now."

    show john b_4

    john "I don't know, it hurts like hell and I was going to ask you anyways."

    show sayaka a_5
    show cornelia b_0

    john "Sometime yesterday it suddenly started itching, and whenever I touch my eyes it hurts like hell."
    sayaka "When you touch your eyes...?"

    show sayaka a_16
    show john b_5

    sayaka "Did you not clean my co-"

    show sayaka a_15
    show john b_6

    "She just stopped herself midway during her sentence, as if not wanting to be heard."

    show sayaka a_5:
        ease 0.5 xpos 0.45

    sayaka "{size=-5}Did you not clean my contact lenses properly?{/size}"

    show john a_13

    john "Contact lenses?"

    show sayaka a_16

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
    show sayaka a_7

    sayaka "Seriously?! I even gave you  list of things to do!"

    show john b_28
    show sayaka a_16

    john "You gave me seven pages to read through!"

    show john b_27
    show sayaka a_7
    show cornelia b_24

    sayaka "Did I not make it clear to read through all seven pages?!"

    show sayaka a_16

    john "..."

    show john b_17

    john "Maybe..."

    show sayaka a_25

    sayaka "Oh my fu-"

    show sayaka a_7:
        ease 0.5 ypos 1.0

    sayaka "Come with me you fucking noodle brain."

    show sayaka a_16:
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
    show sayaka a_16:
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

    show sayaka a_7
    show john b_27

    sayaka "Are you fucking stupid?! What if someone caught me being in there? Rumors would spread like wildfire!"

    show john a_6
    show sayaka a_16

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
    show sayaka a_5 at faceleft

    sayaka "Good. Now put a finger on your lower eye-lid and look up."

    show john a_6

    john "I do what?"

    show sayaka a_16 at faceright

    sayaka "Those instructions were, like, the {i}simplest{/i} instructions ever."

    show john a_32

    john "Well excusez moi, Ms. Perfect, but I've never done this before."

    show sayaka a_24 at faceleft
    show john a_0

    sayaka "{i}Sigh{/i}..."

    show sayaka a_16 at faceright

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

    show sayaka a_5

    sayaka "Now look up."
    sayaka "The lens should slide down. Then you can grab it."

    show john b_28

    john "I what?! Grab it with these nails?!"

    show sayaka at faceright

    john "Oh god this feels weird as fuck!"

    show sayaka a_7
    show john b_27

    sayaka "Stop crying you baby! Just pick it and take it out!"

    show john b_11

    "Easier said than done. Her nails were a thing, and I honestly have absolutely no idea of how not to mutilate my eyes like this."

    show sayaka a_5 at faceleft

    sayaka "Just use the... What's the word for it..."

    show john b_26
    show sayaka at faceright

    john "Oh god I can feel it slowly sliding down under my eyelid!"

    show john b_27
    show sayaka a_7

    sayaka "Pinch it out already! Use your... fingerprint-place of the finger!"

    show sayaka a_16
    show john b_28

    john "What the fuck is the fingerprint-place of the finger?!"

    show sayaka a_20

    sayaka "Pinch it between your fingers! How hard can it be?!"

    scene black with dissolve
    pause 1

    title "12th of August" "Day 5 - Zoey...?"

    scene bg school hallway2 day
    show zoey a_0 at centerleft, faceleft
    show mel a_7 at center, faceleft
    with dissolve

    zoey "Oooh! And a burger place too! My great bro told me ll about it!"

    show zoey b_2

    zoey "You're gonna be amazed at that place especially!"

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

















    placeholder
