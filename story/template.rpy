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

    show john b_17
    show AN_sayaka b_17

    think "Okay, assess the situation."
    think "I'm John Davis. Not Sayaka. For some reason I must have become her and am now in her room."
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

    play sound AN_sfx_silence
    $ renpy.sound.set_volume(1)
    scene black with dissolve
    scene AN_bg road 1 day
    show john b_0 at Position(pos=(0.40, 1.02), anchor=(0.5, 1.0)), faceleft
    with dissolve
    pause 1

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

    show school entrance day:
        ease 0.5 zoom 2.0 xalign 0.6
    show sandra b_8 at offscreenleft:
        ease 0.5 alpha 0.0
    show sayaka a_7 at Position(pos=(0.65, 1.0), anchor=(0.5, 1.0))
    show john a_27 at right
    with ease

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

    show sandra a_6

    sandra "{i}Sigh...{/i} I wonder what happened..."

    scene black with dissolve
    scene bg school garden day
    show sayaka a_5 at left, faceleft
    show john a_0 at centerright, faceleft
    with dissolve

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

    john "What do you think?! I was in a hurry to get to school to figure out what's going on myself!"

    show sayaka a_16

    john "Are you just constantly angry or something? Jesus H. fucking Christ, can we stop screaming at each other and fix this?!"

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

    scene black with dissolve

    "With that, we silently rushed to the ceremony together."

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

    "Other teachers who knew us well were on the other hand surprised to see us entering together too."

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

    "I heard her last comment and decided to keep my comeback for later. One of the teachers me to seat myself already."

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

    abby "If you don't know what class you are in, check in with me here afterwards. I have a list of all classes here."

    show abby a_5 at faceright

    abby "Anything else?"

    title "8th of August" "The first day - Sayaka"

    scene black
    show AN_bg auditorium:
        zoom 2.5 xalign 0.2 yalign 0.9
    show sayaka a_2 at centerleft, faceright
    with dissolve

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
    sayaka "{size=-5} Ugh, I can only shudder at having to live like a guy.{/size}"
    think "But I can fix this. Everything is going to work my way eventually. If it can happen once, it can happen twice."

    scene black
    show school hallway day:
        zoom 1.25 xalign 0.9
    show sayaka a_16 at centerright, faceleft
    with dissolve

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

    scene black with dissolve
    play sound sfx_bell
    scene bg school garden day
    show sayaka a_16 at centerleft, faceleft
    with dissolve

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
    sayaka "{i}Sigh... {/i} That bitch does everything I tell her except fuck off when I tell her to."

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
    sayaka "I'm not trusting anyone in this school. As soon as they know a weakness, they will backstab you and take your position at the top."

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
    sayaka "I am {i}not{/} going to act as your pathetic girlfriend and go buy lunch with you if that is what you're asking."

    show john a_3

    john "I just bought two sandwiches before coming here, so can you calm the fuck down with your assumptions?"

    show john b_17

    "He took out the food he purchased {i}with MY{/i} money and handed me one."
    think "What guy isn't going to take advantage of me like this anyways? He might be lying to himself, but he isn't going to lie to me."
    think "I bet he is thinking to himself that this is bringing us closer like some shitty 90's movie."

    title "8th of August" "The first day - John"

    scene bg school garden day
    show sayaka a_16 at center, faceright
    show john a_31 at Position(pos=(0.8, 1.0), anchor=(0.5, 1.0)), faceleft
    with dissolve

    think "Phew, if she found out I was checking her out in the mirror before going here..."

    show john a_6

    "Yeah, the Cornelia story was fake, so what? At least she bought it and calmed down after being handed something to eat."
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
    "I didn't know why, but she broke out of laughter all of sudden. Not the good kind of {q}yeah that's pretty funny{/q} kind of laugh, but the mocking kind of."
    sayaka "{i}I'm not even surprised at how boring your life has to be if you're playing effing video games on a saturday night, {b}pfhaaahahaha{/b}~{/i}"

    show AN_john a_16

    john "{i}Yeah, real funny. I thought you wanted to know what I did yesterday, but here you are interrupting the short time we have to talk.{/i}"
    sayaka "{i}~ahaah, yeah. I think you may be right for once.{/i}"
    "I intentionally waited until she was completely silent. I hoped it would send her a message."






































































    placeholder
