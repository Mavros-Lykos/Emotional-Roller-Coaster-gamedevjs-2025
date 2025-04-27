$ renpy.reload_script()




define narrator = Character(None)
define mc = Character("[player_name]", color="#c8ffc8", image="player")


default player_name = "Jack"

default kindness = 0
default confidence = 0
default patience = 0
default frugality = 0
default honesty = 0
default game_progress = 0
default history = []


define flash = Fade(.25, 0, .75, color="#fff")
define dissolve_long = Dissolve(1.0)
define slide_up = MoveTransition(0.5, enter=slides.slideup, leave=slides.slideup)


init python:

    config.keymap['dismiss'].append('mouseup_1')  
    config.keymap['dismiss'].append('K_RETURN')   
    config.keymap['dismiss'].append('K_SPACE')    

    def create_blurred_bg(img_name):
        return (img_name, 3.0)


    def add_to_history(event, choice, outcome, k=0, c=0, p=0, f=0, h=0):
        history.append({
            "event": event,
            "choice": choice,
            "outcome": outcome,
            "kindness_change": k,
            "confidence_change": c,
            "patience_change": p,
            "frugality_change": f,
            "honesty_change": h
        })


    def check_win():
        if (0 <= kindness <= 1 and 
            0 <= confidence <= 1 and 
            0 <= patience <= 1 and 
            0 <= frugality <= 1 and 
            0 <= honesty <= 1):
            return True
        else:
            return False


    def auto_save():
        renpy.save("auto-save")


    def force_refresh_saves():
        renpy.renpy.loader.cleardirfiles()
        renpy.restart_interaction()




    def advance_text():
        if renpy.get_screen("top_text"):
            renpy.hide_screen("top_text")
            return True
        return False




image main = "images/main_menu_bg.webp"
image main_large = im.Scale("images/main_menu_bg.webp",1920,1080)

image dorm = "images/dorm.webp"
image dorm_blur = im.Scale("images/blur/dorm.png", 1920, 1080)
image campus = "images/campus.jpg"
image campus_blur = im.Scale("images/blur/campus.png", 1920, 1080)
image cafeteria = "images/cafeteria.jpg"
image cafeteria_blur = im.Scale("images/blur/cafeteria.png", 1920, 1080)
image study_room = "images/study_room.png"
image study_room_blur = im.Scale("images/blur/study_room_blur.png", 1920, 1080)
image campus_path = "images/study_room.jpg"
image campus_path_blur = im.Scale("images/blur/campus_path_blur.png", 1920, 1080)
image dorm_evening = "images/dorm_evening.jpg"
image dorm_evening_blur = im.Scale("images/blur/dorm_evening_blur.png", 1920, 1080)
image garden = "images/garden.jpg"
image garden_blur = im.Scale("images/blur/garden.png", 1920, 1080)
image emotional_balance = im.Scale("images/emotional_balance.png", 1920, 1080)



image player normal = "images/player_normal.png"
image player happy = "images/player_happy.png"
image player sad = "images/player_sad.png"
image player angry = "images/player_angry.png"
image roommate normal = "images/roommate_normal.png"
image classmate normal = "images/classmate_normal.png"


define audio.main_theme = "audio/main_theme.mp3"
define audio.tension = "audio/tension.mp3"
define audio.success = "audio/success1.wav"
define audio.failure = "audio/failure1.wav"
define audio.ui_click = "audio/click.wav"
define audio.ui_hover = "audio/hover.wav"
define audio.calm = "audio/calm.mp3"

screen blurred_background(bg="dorm_blur"):
    add bg


screen event_title(title):
    frame:
        background None
        xalign 0.5
        yalign 0.5
        text title style "event_title_style"



screen top_text(t):
    frame:
        background Frame(Solid("#0000007c"), 20, 20)
        xalign 0.5
        yalign 0.05
        xsize 1600
        padding (20, 20)
        has vbox
        xalign 0.5

        text "{cps=30}[t]{/cps}" style "top_text_style"


screen mid_text(t):
    frame:
        background None
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        text t style "mid_text_style"

screen bottom_choices(question, choices):
    modal True

    frame:
        xalign 0.5
        yalign 0.82
        xsize 800
        padding (30, 30)
        background Frame(Solid("#00000070"), 20, 20)

        has vbox
        xalign 0.5
        spacing 20

        text question style "top_text_style" xalign 0.5

        for caption, action in choices:
            textbutton caption:
                action action
                xsize 700
                xalign 0.8
                text_align 0.5
                text_size 24
                background Solid("#1a1a1a")
                hover_background Solid("#333388")
                insensitive_background Solid("#555555")
                padding (15, 10)



screen emotion_tracker():
    frame:
        xalign 0.96
        yalign 0.9
        background "images/ui/pointBox.png"
        xsize 250
        ysize 300
        padding (80, 70)

        has fixed
        xysize (250, 300)

        vbox:
            pos (10, 10)
            spacing 10

            text "Traits:" style "text_style"
            text "Kindness: [kindness]" style "text_style"
            text "Confidence: [confidence]" style "text_style"
            text "Patience: [patience]" style "text_style"
            text "Frugality: [frugality]" style "text_style"
            text "Honesty: [honesty]" style "text_style"




label start:

    $ player_name = persistent.player_name if hasattr(persistent, "player_name") and persistent.player_name else "Jack"
    $ kindness = 0
    $ confidence = 0
    $ patience = 0
    $ frugality = 0
    $ honesty = 0
    $ game_progress = 0
    $ history = []

    call name_selection

    play music audio.main_theme fadein 1.0


    show campus_blur
    show campus at truecenter with dissolve_long


    show screen top_text(f"Welcome to 'Balance: The Game', {player_name}.")
    pause 
    hide screen top_text

    show screen top_text("Your journey through a day at university begins now. Remember, every choice affects your emotional balance.")
    pause 
    hide screen top_text

    show screen top_text("The key to success is finding the right balance - extremes in any direction can lead to unexpected consequences.")
    pause 
    hide screen top_text



    $ game_progress = 1
    $ auto_save()
    jump event1


label name_selection:
    scene main_large with dissolve
    show main_large
    show screen top_text("Before we begin, what is your name?")

    $ player_name = renpy.input("Enter your name:", default=player_name)
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name = "Jack"

    $ persistent.player_name = player_name

    "Welcome, [player_name]!"
    return


label event1:

    scene black with dissolve_long
    show screen blurred_background("dorm_blur")


    show screen event_title("Event 1: Morning Rush")
    pause 2.0
    hide screen event_title


    scene dorm with dissolve_long
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker

    play music audio.tension fadein 1.0


    show screen top_text("Your alarm failed to go off and now you're running late for Professor Stevens' important exam preparation class.")
    pause  
    hide screen top_text


    show roommate normal at left with dissolve
    show screen top_text("The professor is known for locking the door exactly at start time.")

    show roommate normal at left with dissolve

    show screen top_text(f"Roommate: Hey {player_name}, I can't find my project file anywhere! Can you help me look? My presentation is in an hour!")
    pause  
    hide screen top_text

    show screen top_text("You check your watch. The class starts in 15 minutes, and it's a 10-minute sprint across campus.")
    pause  
    hide screen top_text

    hide roommate with dissolve


    $ event1_choices = [
    ("Ignore them completely and rush out", Jump("event1_outcome1")),
    ("Tell them you can't help now but will look when you return", Jump("event1_outcome2")),
    ("Take 5 minutes to help look, then leave", Jump("event1_outcome3")),
    ("Skip class entirely to help them find it", Jump("event1_outcome4")),
    ("Blame them for being disorganized and rush out", Jump("event1_outcome5"))
    ]
    show screen bottom_choices("What will you do?", event1_choices)
    pause  


label event1_outcome1:

    hide screen bottom_choices

    scene dorm with flash
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker
    play sound "audio/door_slash.wav"

    show screen top_text("You grab your bag and rush out without a word, leaving your roommate looking surprised and hurt.")
    pause
    hide screen top_text

    scene campus with dissolve
    show screen blurred_background("campus_blur")

    show screen top_text("You make it to class with a minute to spare, sliding into your seat just as Professor Stevens closes the door.")
    pause
    hide screen top_text

    show screen top_text("Later that day, when you're struggling with a difficult problem set, you notice your roommate deliberately avoiding eye contact when you try to ask for help.")
    pause
    hide screen top_text


    $ kindness -= 1
    $ confidence += 1
    $ add_to_history("Morning Rush", "Ignored roommate", "Damaged relationship", -1, 1, 0, 0, 0)

    $ game_progress = 2
    $ auto_save()
    jump event2


label event1_outcome2:

    hide screen bottom_choices

    scene dorm with flash
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker

    show screen top_text("You quickly explain the situation and promise to help as soon as you return.")
    pause
    hide screen top_text

    show screen top_text("Your roommate nods, disappointed but understanding.")
    pause
    hide screen top_text

    scene campus with dissolve
    show screen blurred_background("campus_blur")

    show screen top_text("You make it to class just in time, your mind racing with the material Professor Stevens begins covering immediately.")
    pause
    hide screen top_text

    show screen top_text("Later, your roommate thanks you for being honest and still asks if you can help when you get back.")
    pause
    hide screen top_text


    $ kindness += 0
    $ confidence += 1
    $ add_to_history("Morning Rush", "Promised to help later", "Maintained relationship", 0, 1, 0, 0, 0)

    $ game_progress = 2
    $ auto_save()
    jump event2


label event1_outcome3:

    hide screen bottom_choices

    scene dorm with flash
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker

    show screen top_text("You spare five minutes to help look under piles of paper and laundry.")
    pause
    hide screen top_text

    show screen top_text("Eventually, your roommate finds it in their folder — right where it should’ve been all along.")
    pause
    hide screen top_text

    scene campus with dissolve
    show screen blurred_background("campus_blur")

    show screen top_text("You jog to class and arrive two minutes late.")
    pause
    hide screen top_text

    show screen top_text("Professor Stevens raises an eyebrow but lets you in with a stern look.")
    pause
    hide screen top_text

    show screen top_text("Your roommate seems extra grateful later and offers to help you study that evening.")
    pause
    hide screen top_text

    $ kindness += 1
    $ confidence += 0
    $ add_to_history("Morning Rush", "Helped briefly", "Gained appreciation", 1, 0, 0, 0, 0)

    $ game_progress = 2
    $ auto_save()
    jump event2


label event1_outcome4:

    hide screen bottom_choices

    scene dorm with flash
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker

    show screen top_text("You sigh and decide to stay and help. You tear through the dorm together until you finally find the file wedged under a stack of books.")
    pause
    hide screen top_text

    show screen top_text("Your roommate nearly cries with relief.")
    pause
    hide screen top_text

    scene campus with dissolve
    show screen blurred_background("campus_blur")

    show screen top_text("You arrive at the lecture hall just as the door clicks shut. You knock, but Professor Stevens doesn’t open.")
    pause
    hide screen top_text

    show screen top_text("Later that day, your roommate apologizes and promises to repay the favor. But the exam prep you missed puts you behind.")
    pause
    hide screen top_text

    $ kindness += 2
    $ confidence -= 1
    $ add_to_history("Morning Rush", "Skipped class to help", "Missed crucial information", 2, -1, 0, 0, 0)

    $ game_progress = 2
    $ auto_save()
    jump event2


label event1_outcome5:

    hide screen bottom_choices

    scene dorm with flash
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker
    play sound "audio/door_slash.wav"

    show screen top_text("You blame your roommate for being disorganized, muttering something about 'personal responsibility' before storming out.")
    pause
    hide screen top_text

    scene campus with dissolve
    show screen blurred_background("campus_blur")

    show screen top_text("You make it to class on time, confident in your priorities.")
    pause
    hide screen top_text

    show screen top_text("But word gets around quickly — your roommate tells mutual friends, and by evening, a few people are giving you cold looks.")
    pause
    hide screen top_text

    $ kindness += 0
    $ confidence += 2
    $ add_to_history("Morning Rush", "Blamed roommate", "Created tension", 0, 2, 0, 0, 0)

    $ game_progress = 2
    $ auto_save()
    jump event2




label event2:

    scene black with dissolve_long
    show screen blurred_background("cafeteria_blur")


    show screen event_title("Event 2: Lunch Dilemma")
    pause 2.0
    hide screen event_title


    scene cafeteria with dissolve_long
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    play music audio.calm fadein 1.0


    show screen top_text("You're in the cafeteria with only $15 to last until your allowance arrives tomorrow.")
    pause
    hide screen top_text

    show screen top_text("A classmate you want to befriend sits down and mentions they forgot their wallet.")
    pause
    hide screen top_text


    show classmate normal at left with dissolve
    show screen top_text(f"Classmate: Hey {player_name}, I’m really sorry to ask, but... I forgot my wallet. Could you spot me today?")
    pause
    hide screen top_text
    hide classmate with dissolve


    $ event2_choices = [
    ("Pretend you don't have money either", Jump("event2_outcome1")),
    ("Buy them a small snack and have a modest meal yourself", Jump("event2_outcome2")),
    ("Buy them a full meal and skip lunch yourself", Jump("event2_outcome3")),
    ("Explain your situation honestly and suggest sharing your meal", Jump("event2_outcome4")),
    ("Buy both full meals and put it on your nearly maxed-out credit card", Jump("event2_outcome5"))
    ]
    show screen bottom_choices("What will you do?", event2_choices)
    pause  


label event2_outcome1:

    hide screen bottom_choices

    scene cafeteria with flash
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    show screen top_text("You pretend you’re broke too, despite the tray of food in front of you.")
    pause
    hide screen top_text

    show screen top_text("Your classmate eyes your plate, nods slowly, and the conversation grows awkward.")
    pause
    hide screen top_text

    $ honesty -= 1
    $ frugality += 1
    $ add_to_history("Lunch Dilemma", "Pretended to be broke", "Missed chance to connect", -1, 0, 0, 1, 0)

    $ game_progress = 3
    $ auto_save()
    jump event3


label event2_outcome2:

    hide screen bottom_choices

    scene cafeteria with flash
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    show screen top_text("You hand them a granola bar and smile. They light up in appreciation.")
    pause
    hide screen top_text

    show screen top_text("You both enjoy a light meal and talk about shared classes.")
    pause
    hide screen top_text

    $ kindness += 1
    $ frugality += 1
    $ add_to_history("Lunch Dilemma", "Shared snack", "Gained appreciation", 1, 0, 0, 1, 0)

    $ game_progress = 3
    $ auto_save()
    jump event3


label event2_outcome3:

    hide screen bottom_choices

    scene cafeteria with flash
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    show screen top_text("You buy them a full meal and eat nothing yourself.")
    pause
    hide screen top_text

    show screen top_text("By the afternoon, your stomach is rumbling, making it hard to concentrate.")
    pause
    hide screen top_text

    $ kindness += 2
    $ frugality += 0
    $ add_to_history("Lunch Dilemma", "Bought them full meal", "Left hungry", 2, 0, 0, 0, 0)

    $ game_progress = 3
    $ auto_save()
    jump event3


label event2_outcome4:

    hide screen bottom_choices

    scene cafeteria with flash
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    show screen top_text("You explain your tight budget and offer to split your food.")
    pause
    hide screen top_text

    show screen top_text("They laugh and accept, promising to treat you tomorrow.")
    pause
    hide screen top_text

    $ honesty += 1
    $ kindness += 1
    $ add_to_history("Lunch Dilemma", "Offered to share meal", "Built mutual respect", 1, 1, 0, 0, 0)

    $ game_progress = 3
    $ auto_save()
    jump event3


label event2_outcome5:

    hide screen bottom_choices

    scene cafeteria with flash
    show screen blurred_background("cafeteria_blur")
    show screen emotion_tracker

    show screen top_text("You swipe your card and both of you enjoy full meals.")
    pause
    hide screen top_text

    show screen top_text("Later, you check your account and feel a wave of financial anxiety.")
    pause
    hide screen top_text

    $ frugality -= 1
    $ kindness += 1
    $ add_to_history("Lunch Dilemma", "Charged both meals", "Financial stress", 1, 0, 0, -1, 0)

    $ game_progress = 3
    $ auto_save()
    jump event3

label event3:

    scene black with dissolve_long
    show screen blurred_background("study_room_blur")


    show screen event_title("Event 3: Group Project Tension")
    pause 2.0
    hide screen event_title


    scene studyroom with dissolve_long
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    play music audio.tension fadein 1.0


    show screen top_text("In your afternoon study group, one member hasn't contributed anything.")
    pause
    hide screen top_text

    show screen top_text("The project is due tomorrow, and everyone is growing frustrated.")
    pause
    hide screen top_text


    show group_member normal at left with dissolve
    show screen top_text(f"Group Member: Hey {player_name}, I’ve just been... really swamped. I’ll get to it tonight, I swear.")
    pause
    hide screen top_text
    hide group_member with dissolve


    $ event3_choices = [
    ("Confront them aggressively in front of everyone", Jump("event3_outcome1")),
    ("Say nothing and do their work yourself", Jump("event3_outcome2")),
    ("Take them aside and discuss the issue calmly", Jump("event3_outcome3")),
    ("Report them to the professor immediately", Jump("event3_outcome4")),
    ("Passive-aggressively hint at their lack of contribution", Jump("event3_outcome5"))
    ]
    show screen bottom_choices("What will you do?", event3_choices)
    pause  


label event3_outcome1:

    hide screen bottom_choices

    scene study_room with flash
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    show screen top_text("You call them out in front of everyone. The room falls silent.")
    pause
    hide screen top_text

    show screen top_text("They look stunned and defensive. The rest of the group grows tense.")
    pause
    hide screen top_text

    $ patience -= 1
    $ honesty += 2
    $ add_to_history("Group Project Tension", "Confronted publicly", "Created tension", 0, 0, 2, 0, -1)

    $ game_progress = 4
    $ auto_save()
    jump event4


label event3_outcome2:

    hide screen bottom_choices

    scene study_room with flash
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    show screen top_text("You say nothing and take on the extra work.")
    pause
    hide screen top_text

    show screen top_text("The project gets done, but you’re exhausted and frustrated by the end.")
    pause
    hide screen top_text

    $ patience += 1
    $ honesty -= 1
    $ add_to_history("Group Project Tension", "Stayed silent", "Burned out", 0, 0, -1, 0, 1)

    $ game_progress = 4
    $ auto_save()
    jump event4


label event3_outcome3:

    hide screen bottom_choices

    scene study_room with flash
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    show screen top_text("You pull them aside and talk calmly.")
    pause
    hide screen top_text

    show screen top_text("They open up about some personal issues and promise to finish their part tonight.")
    pause
    hide screen top_text

    $ patience += 1
    $ honesty += 1
    $ add_to_history("Group Project Tension", "Private discussion", "Improved cooperation", 0, 0, 1, 0, 1)

    $ game_progress = 4
    $ auto_save()
    jump event4


label event3_outcome4:

    hide screen bottom_choices

    scene study_room with flash
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    show screen top_text("You report the situation to the professor.")
    pause
    hide screen top_text

    show screen top_text("Later, the professor follows up with your group. The dynamics shift awkwardly, but the project gets done.")
    pause
    hide screen top_text

    $ patience -= 1
    $ honesty += 1
    $ add_to_history("Group Project Tension", "Reported to professor", "Fair but strained", 0, 0, 1, 0, -1)

    $ game_progress = 4
    $ auto_save()
    jump event4


label event3_outcome5:

    hide screen bottom_choices

    scene study_room with flash
    show screen blurred_background("study_room_blur")
    show screen emotion_tracker

    show screen top_text("You make sarcastic comments about people not pulling their weight.")
    pause
    hide screen top_text

    show screen top_text("Everyone picks up on the tension. The group becomes quiet and awkward.")
    pause
    hide screen top_text

    $ honesty += 1
    $ kindness -= 1
    $ add_to_history("Group Project Tension", "Hinted passive-aggressively", "Uncomfortable vibes", -1, 0, 1, 0, 0)

    $ game_progress = 4
    $ auto_save()
    jump event4


label event4:

    scene black with dissolve_long
    show screen blurred_background("campus_path_blur")


    show screen event_title("Event 4: Campus Shortcut")
    pause 2.0
    hide screen event_title


    scene campus_path with dissolve_long
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    play music audio.calm fadein 1.0


    show screen top_text("You're walking back to your dorm, rushing for an online meeting.")
    pause
    hide screen top_text

    show screen top_text("You notice a shortcut through a landscaped garden marked with a 'Keep Off' sign.")
    pause
    hide screen top_text

    show screen top_text("It's tempting. The detour would save precious minutes.")
    pause
    hide screen top_text


    $ event4_choices = [
    ("Take the shortcut without hesitation", Jump("event4_outcome1")),
    ("Follow the proper path and explain you'll be late", Jump("event4_outcome2")),
    ("Run frantically along the proper path", Jump("event4_outcome3")),
    ("Take shortcut and lecture others if caught", Jump("event4_outcome4")),
    ("Debate with yourself loudly while standing there", Jump("event4_outcome5"))
    ]
    show screen bottom_choices("What will you do?", event4_choices)
    pause  



label event4_outcome1:

    hide screen bottom_choices

    scene garden_path with flash
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    show screen top_text("You dart through the shortcut, saving time... but a security officer catches you mid-run.")
    pause
    hide screen top_text

    show screen top_text("They give you a warning and jot down your student ID.")
    pause
    hide screen top_text

    $ honesty -= 1
    $ confidence += 1
    $ add_to_history("Campus Shortcut", "Took shortcut", "Caught by campus security", 0, 0, 0, 0, 1)

    $ game_progress = 5
    $ auto_save()
    jump event5


label event4_outcome2:

    hide screen bottom_choices

    scene campus_path with flash
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    show screen top_text("You sigh and stick to the path. You’re late, but your group appreciates your honesty.")
    pause
    hide screen top_text

    show screen top_text("They even offer to catch you up on what you missed.")
    pause
    hide screen top_text

    $ honesty += 1
    $ patience += 1
    $ add_to_history("Campus Shortcut", "Followed rules", "Gained respect", 0, 0, 0, 0, 1)

    $ game_progress = 5
    $ auto_save()
    jump event5


label event4_outcome3:

    hide screen bottom_choices

    scene campus_path with flash
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    show screen top_text("You sprint like your life depends on it.")
    pause
    hide screen top_text

    show screen top_text("You arrive, panting and disheveled, just in time to catch most of the meeting.")
    pause
    hide screen top_text

    $ honesty += 1
    $ patience -= 1
    $ add_to_history("Campus Shortcut", "Ran proper path", "Made it barely", 0, 0, 0, 0, 0)

    $ game_progress = 5
    $ auto_save()
    jump event5


label event4_outcome4:

    hide screen bottom_choices

    scene garden_path with flash
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    show screen top_text("You take the shortcut. When a security guard confronts you, you start a moral rant about student priorities.")
    pause
    hide screen top_text

    show screen top_text("They’re not amused, and your peers hear about it.")
    pause
    hide screen top_text

    $ confidence += 2
    $ honesty -= 2
    $ add_to_history("Campus Shortcut", "Hypocritical shortcut", "Damaged reputation", 0, 0, 0, 0, 2)

    $ game_progress = 5
    $ auto_save()
    jump event5


label event4_outcome5:

    hide screen bottom_choices

    scene campus_path with flash
    show screen blurred_background("campus_path_blur")
    show screen emotion_tracker

    show screen top_text("You freeze, loudly arguing with yourself about the ethics of rule-breaking.")
    pause
    hide screen top_text

    show screen top_text("By the time you make a decision, it’s too late to matter.")
    pause
    hide screen top_text

    $ confidence -= 2
    $ add_to_history("Campus Shortcut", "Indecisive moment", "Wasted time", 0, 0, 0, 0, -1)

    $ game_progress = 5
    $ auto_save()
    jump event5


label event5:

    scene black with dissolve_long
    show screen blurred_background("dorm_blur")


    show screen event_title("Event 5: Evening Financial Decision")
    pause 2.0
    hide screen event_title


    scene dorm with dissolve_long
    show screen blurred_background("dorm_blur")
    show screen emotion_tracker

    play music audio.main_theme fadein 1.0


    show screen top_text("You receive a surprise $100 from a relative.")
    pause
    hide screen top_text

    show screen top_text("Your laptop has been acting up, you need new clothes, and your friend is throwing a big birthday party.")
    pause
    hide screen top_text

    show screen top_text("You sit down on your bed, thinking how to spend it wisely.")
    pause
    hide screen top_text


    $ event5_choices = [
    ("Spend it all on the birthday party", Jump("event5_outcome1")),
    ("Save it all for laptop repairs", Jump("event5_outcome2")),
    ("Split it: laptop $60, gift $20, savings $20", Jump("event5_outcome3")),
    ("Buy trendy clothes to impress classmates", Jump("event5_outcome4")),
    ("Loan the entire amount to a friend", Jump("event5_outcome5"))
    ]
    show screen bottom_choices("What will you do?", event5_choices)
    pause  



label event5_outcome1:

    hide screen bottom_choices

    scene party_night with flash
    show screen blurred_background("dorm_evening_blur")
    show screen emotion_tracker

    show screen top_text("The party is wild and fun. Your friend is thrilled.")
    pause
    hide screen top_text

    show screen top_text("But the next day, your laptop freezes mid-assignment.")
    pause
    hide screen top_text

    $ kindness += 2
    $ frugality -= 2
    $ add_to_history("Evening Financial Decision", "Spent on party", "Fun night, tech troubles", 2, 0, 0, -2, 0)

    $ game_progress = 6
    $ auto_save()
    jump end_of_chapter


label event5_outcome2:

    hide screen bottom_choices

    scene dorm_evening with flash
    show screen blurred_background("dorm_evening_blur")
    show screen emotion_tracker

    show screen top_text("You head to the repair shop the next day. The laptop runs much better.")
    pause
    hide screen top_text

    show screen top_text("You skip the party and see the photos online later.")
    pause
    hide screen top_text

    $ frugality += 1
    $ add_to_history("Evening Financial Decision", "Saved for repairs", "Functional laptop, no social memory", 0, 0, 0, 2, 0)

    $ game_progress = 6
    $ auto_save()
    jump end_of_chapter


label event5_outcome3:

    hide screen bottom_choices

    scene dorm_evening with flash
    show screen blurred_background("dorm_evening_blur")
    show screen emotion_tracker

    show screen top_text("You budget smartly—laptop works fine, you show up with a thoughtful gift, and still save a bit.")
    pause
    hide screen top_text

    show screen top_text("Feels like a small personal win.")
    pause
    hide screen top_text

    $ frugality += 1
    $ kindness += 1
    $ add_to_history("Evening Financial Decision", "Balanced spending", "Everything works out", 1, 0, 0, 1, 0)

    $ game_progress = 6
    $ auto_save()
    jump end_of_chapter


label event5_outcome4:

    hide screen bottom_choices

    scene dorm_evening with flash
    show screen blurred_background("dorm_evening_blur")
    show screen emotion_tracker

    show screen top_text("You rock the new clothes, and classmates compliment you.")
    pause
    hide screen top_text

    show screen top_text("But your laptop gives up completely two days later.")
    pause
    hide screen top_text

    $ confidence += 1
    $ frugality -= 1
    $ add_to_history("Evening Financial Decision", "Bought clothes", "Compliments now, regret later", 0, 0, 1, -1, 0)

    $ game_progress = 6
    $ auto_save()
    jump end_of_chapter


label event5_outcome5:

    hide screen bottom_choices

    scene dorm_evening with flash
    show screen blurred_background("dorm_evening_blur")
    show screen emotion_tracker

    show screen top_text("Your friend is relieved and promises to repay you soon.")
    pause
    hide screen top_text

    show screen top_text("Days pass... you're still waiting.")
    pause
    hide screen top_text

    $ kindness += 2
    $ frugality -= 1
    $ add_to_history("Evening Financial Decision", "Loaned money", "Friend grateful, uncertain return", 2, 0, 0, -1, 0)

    $ game_progress = 6
    $ auto_save()
    jump end_of_chapter



# Now let's define a proper ending screen
label end_of_chapter:
    scene black with dissolve_long
    hide screen emotion_tracker
    hide screen blurred_background
    show screen blurred_background("emotional_balance")
    
    show screen top_text("Your journey through the day has shaped your emotional balance.")
    pause
    hide screen top_text
    
    show screen top_text("Let's see what future lies ahead for you based on your choices...")
    pause 
    hide screen top_text

    show screen emotion_tracker

    if kindness == 1 and confidence == 1 and patience == 1 and frugality == 1 and honesty == 1:
        jump balanced_ending
    elif kindness >= 2:
        jump extreme_kindness_ending
    elif kindness < 0:
        jump negative_kindness_ending
    elif confidence >= 2:
        jump extreme_confidence_ending
    elif confidence < 0:
        jump negative_confidence_ending
    elif patience >= 2:
        jump extreme_patience_ending
    elif patience < 0:
        jump negative_patience_ending
    elif frugality >= 2:
        jump extreme_frugality_ending
    elif frugality < 0:
        jump negative_frugality_ending
    elif honesty >= 2:
        jump extreme_honesty_ending
    elif honesty < 0:
        jump negative_honesty_ending
    # Combo endings — using same "≥ 2 and < 2" logic
    elif kindness >= 2 and frugality < 2:
        jump kind_not_frugal_ending
    elif patience >= 2 and honesty < 2:
        jump patient_not_honest_ending
    elif confidence >= 2 and kindness < 2:
        jump confident_not_kind_ending
    elif honesty >= 2 and patience < 2:
        jump honest_not_patient_ending
    elif frugality >= 2 and confidence < 2:
        jump frugal_not_confident_ending

    # Continue with other ending conditions
    
    else :# Default fallback
        jump complex_imbalance_ending
# All possible endings for Balance: The Game

label balanced_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.success fadein 2.0
    
    show player happy at center with dissolve
    
    # Create an ending screen with all text in one place
    screen ending_summary():
        frame:
            background "gui/ending_box.png"  # Create this image or use Frame()
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Balanced Path" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "You complete your university years with strong relationships, good academic standing, and healthy financial habits." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your balanced approach to life's challenges has prepared you well for the future. You find yourself with job offers, genuine friendships, and the emotional stability to handle life's ups and downs." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your professors respect your work ethic, your friends value your reliable nature, and potential employers see you as someone who can navigate complex situations with maturity." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "While your life isn't perfect, you have the tools to navigate whatever comes your way. You've learned that the middle path is often the wisest one." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Balance Master - You've found the elusive middle path!" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5
    
    # Show the ending summary screen
    show screen ending_summary
    
    # Wait for player input (click or key press)
    pause
    
    # Hide the screen and proceed to scores
    hide screen ending_summary
    return

# Kindness Imbalances
# Kindness Imbalances

label extreme_kindness_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Selfless Martyr" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your extreme generosity left you emotionally and financially drained. You graduated with significant debt from constantly helping others at your own expense." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Friends and classmates grew accustomed to your sacrifices, often taking advantage of your good nature without reciprocating." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "By age 40, you're working extra jobs to support others' emergencies while neglecting your own needs. Your health suffers as you consistently put yourself last." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You realize too late that helping others requires first maintaining your own stability. True kindness must be balanced with self-care." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Heart of Gold - Sometimes too precious for your own good" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label negative_kindness_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player angry at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Isolated Success" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your focus on self-preservation alienated potential allies and friends. While you achieved academic success, you built a reputation as someone not to be trusted or relied upon." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Years later, you find professional advancement difficult despite your competence, as networking opportunities evaporate when colleagues discover your history of self-centered behavior." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your achievements feel hollow without anyone to share them with. The corner office has a great view, but no one ever stops by to chat." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Lone Wolf - Success at the cost of connection" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

# Confidence Imbalances

label extreme_confidence_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player smug at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Arrogant Leader" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your unwavering belief in your own abilities propelled you into leadership roles early. However, your refusal to acknowledge mistakes and dismissive attitude toward others led to frequent conflicts." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Despite your successes, former classmates and coworkers often recall your arrogance and difficulty working as part of a team." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "In your 30s, you lead a startup that burns brightly but quickly collapses due to poor collaboration and unchecked ego." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Shooting Star - Bright, bold, and short-lived" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label negative_confidence_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player nervous at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Hidden Talent" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Despite having great potential, your lack of confidence prevented you from seizing opportunities. You often doubted your worth and let chances slip away to those less capable but more assertive." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Over time, your career stalled in entry-level roles. Friends and family knew you were capable of more, but you couldn't bring yourself to believe it." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "By your mid-30s, you're stuck in positions far below your abilities, quietly resenting the world — and yourself — for playing small." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Hidden Gem - Brilliant, but buried too deep" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

# Patience Imbalances

label extreme_patience_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player calm at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Eternal Doormat" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your excessive patience meant you never established boundaries. People regularly took advantage of your time and energy, knowing you wouldn't object." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You became the person always waiting for recognition that never came, the one who would tolerate any behavior without complaint." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "By mid-life, you harbor deep resentment toward friends and colleagues who advanced while you patiently waited your turn, a turn that never arrived. You realize too late that patience without assertion is simply surrender." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Saint's Patience - Martyrdom by a thousand inconveniences" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label negative_patience_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player angry at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Burning Bridge" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your impulsive reactions and quick temper created a trail of damaged relationships. You developed a reputation for being brilliant but impossible to work with." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Job opportunities disappeared after reference checks, and your social circle narrowed to those with similarly short fuses. Each outburst seemed justified in the moment, but the cumulative cost was enormous." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You frequently wonder how different life might be if you'd counted to ten before responding. So many doors closed because of words spoken in haste." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Powder Keg - Quick to ignite, difficult to extinguish" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

# Frugality Imbalances
# Frugality Imbalances

label extreme_frugality_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Wealth Without Joy" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your obsession with saving every penny meant missing formative experiences and connections during university. You graduated debt-free but with few memories or friends." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "By middle age, you've accumulated impressive wealth but struggle to enjoy it, feeling anxiety about any purchase. Your spacious home feels empty, your time filled with counting and recounting your savings." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your health suffers from years of choosing the cheapest rather than the healthiest options. You've gained financial security but lost the ability to find pleasure in simple indulgences." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Dragon's Hoard - Wealth accumulated but never enjoyed" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label negative_frugality_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Golden Handcuffs" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your pattern of impulsive spending snowballed into crippling debt. The stress of financial insecurity follows you decades after graduation, limiting your career choices to those that pay the most rather than fulfill you." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Relationships strain under money arguments, and retirement seems like an impossible dream. Every paycheck is spent before it arrives, leaving you perpetually anxious about unexpected expenses." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You wonder if those designer clothes and lavish parties were worth the decades of financial anxiety that followed. The momentary pleasures have long faded, but the debt remains." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Champagne Tastes, Water Budget - The high cost of living for the moment" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

# Honesty Imbalances

label extreme_honesty_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player normal at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Truth at All Costs" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your commitment to brutal honesty regardless of context earned you a reputation for cruelty disguised as principle. Job interviews ended abruptly after unnecessarily frank assessments of potential employers." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Relationships withered under your unfiltered observations. You prided yourself on never telling a lie, but failed to recognize how truth without compassion becomes a weapon." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "In middle age, you find yourself respected for integrity but rarely invited anywhere twice, your honesty untempered by kindness. The truth you value so highly has become a barrier between you and others." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Brutal Truth - Honesty without mercy is merely cruelty" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label negative_honesty_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The House of Cards" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your pattern of convenient lies and misrepresentations created a precarious existence. You advanced quickly through charm and fabrication, but lived in constant fear of discovery." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Eventually, inconsistencies in your stories caught up with you, resulting in professional disgrace and personal rejection. Your carefully constructed persona collapsed under scrutiny." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Years later, you struggle to rebuild trust with those who wonder if anything you say is true. You've learned that shortcuts built on deception lead to longer, harder paths in the end." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Web Weaver - Tangled in your own creation" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return


# Mixed Extreme Imbalances

label kind_not_frugal_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Bankrupt Saint" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your generosity without financial boundaries led to financial ruin. You're loved by many but unable to help anyone effectively anymore, including yourself." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You live in a small apartment surrounded by thank-you cards but struggling to pay bills. The people you helped rarely return when you're the one in need." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Looking back, you realize that sustainable giving requires sustainable resources. Your heart was in the right place, but your finances weren't structured to support your generosity." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Generous to a Fault - Literally gave until it hurt" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label patient_not_honest_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Silent Sufferer" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your combination of infinite patience and dishonesty created a life where you never express your true feelings. You've become a mystery even to yourself, going through the motions while suppressing your authentic voice." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your relationships feel hollow, built on a foundation of what you thought others wanted rather than truth. Decades pass as you smile and nod through discomfort, never expressing your real needs or desires." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Eventually, you realize you've become so good at hiding your truth that you can no longer find it yourself." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Mask Collector - Lost behind the faces you show others" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return

label confident_not_kind_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player normal at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Lonely Achiever" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your supreme self-assurance unchecked by compassion propelled you to professional heights while leaving a wake of wounded colleagues." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Your office has an impressive view but no personal photos. Awards fill your shelves, but no one attends your celebration dinners. Former classmates avoid industry events when they know you'll be present." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "You achieved everything you aimed for, only to discover it meant nothing without someone to share it with. Success without connection has a hollow ring to it." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: Summit Solitude - It's cold and lonely at the top" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return


label honest_not_patient_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player normal at center with dissolve

    screen ending_summary():
        frame:
            background "gui/ending_box.png"
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Unheard Truth" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your honesty came without the patience to see things through. You told the truth, but without consideration for timing or gentleness." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "While others appreciated your directness, many felt hurt or misunderstood. Relationships were quick to start, but quicker to end, as your bluntness never allowed space for others to process their feelings." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Ultimately, your unwavering truth left you isolated, with few people left who could handle the harsh light you shone on everything." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: The Sharpshooter - Pierced through people's defenses, but lost the target" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    show screen ending_summary
    pause
    hide screen ending_summary

    return


label frugal_not_confident_ending:
    scene campus with dissolve_long
    show screen blurred_background("campus_blur")
    play music audio.tension fadein 2.0

    show player sad at center with dissolve

    screen ending_summary():
        frame:
            background Solid("#1a1a1a")  # Dark gray button
            hover_background Solid("#333388")  # Deep blue on hover
            insensitive_background Solid("#555555")
            xalign 0.5
            yalign 0.2
            xsize 1000
            padding (30, 30)
            has vbox:
                spacing 20
                xalign 0.5
            text "The Miserable Saver" size 50 xalign 0.5 color "#ffdc7a" outlines [(2, "#000000", 0, 0)]
            null height 10
            text "Your fear of spending and lack of confidence led to a life of constant hesitation. You saved every penny, but rarely took any chances, living in the shadows of what could have been." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "Opportunities passed you by because you couldn't bring yourself to take the first step. Even small purchases became monumental decisions." size 24 xalign 0.5 text_align 0.5
            null height 5
            text "As years went on, you found yourself with plenty of savings but no experiences to spend it on, realizing that the richest moments in life are the ones you risk for." size 24 xalign 0.5 text_align 0.5
            null height 20
            text "ACHIEVEMENT: The Hoarder - You saved everything, except your happiness" size 28 xalign 0.5 color "#ffd700" outlines [(2, "#000000", 0, 0)] text_align 0.5

    # Show the ending summary screen
    show screen ending_summary
    
    # Wait for player input (click or key press)
    pause
    
    # Hide the screen and proceed to scores
    hide screen ending_summary
    
    # This is the critical line - explicitly jump to show_scores
    return

# Complex Mixed Endings

label complex_imbalance_ending:
    scene campus with dissolve_long
    show campus_blur behind campus
    play music audio.tension fadein 2.0
    
    with dissolve
    show player normal at truecenter
    "The Complex Consequence"
    
    "Your pattern of emotional responses created a complex tapestry of strengths and weaknesses. Some areas of your life flourished while others withered under neglect or excess."
    
    if kindness > 1 and confidence > 1:
        "Your generosity and confidence made you a natural leader, but your tendency to overcommit and overestimate your capabilities led to spectacular failures that damaged your reputation."
    elif kindness < 0 and honesty < 0:
        "Your self-focused approach and flexible relationship with the truth helped you advance quickly, but left you surrounded by people who neither trust nor genuinely care for you."
    elif patience > 1 and frugality > 1:
        "Your patient, frugal approach built a stable foundation, but your life lacks spontaneity and joy. You've confused security with fulfillment."
    elif confidence < 0 and patience < 0:
        "Your combination of self-doubt and impulsiveness created a chaotic life pattern. You react hastily to compensate for insecurity, often making situations worse."
    else:
        "Your particular combination of emotional extremes created unique challenges that affected your relationships, career, and personal fulfillment."
    
    "Looking back on your university days, you recognize how those early patterns shaped your life's trajectory. Balance, you realize, isn't just about moderation—it's about appropriate responses to each unique situation."
    
    "ACHIEVEMENT: Human Complexity - A reminder that we're all works in progress"
    pause
    
    return

# Final score display and options
label show_scores:
    scene black with dissolve
    "Your Final Emotional Balance:"
    
    $ score_text = ""
    $ score_color = ""
    
    # Format each score with appropriate color and indicator
    python:
        emotions = [
            ("Kindness", kindness),
            ("Confidence", confidence),
            ("Patience", patience),
            ("Frugality", frugality),
            ("Honesty", honesty)
        ]
        
        for emotion, value in emotions:
            if value < 0:
                indicator = "NEGATIVE"
                color = "#e74c3c"
            elif value == 0:
                indicator = "NEUTRAL"
                color = "#f1c40f"
            elif value == 1:
                indicator = "BALANCED"
                color = "#2ecc71"
            else:
                indicator = "EXTREME"
                color = "#9b59b6"
                
            score_text += "{0}: {1} ({2})\n".format(emotion, value, indicator)
    
    show text score_text at truecenter
    pause 1.0
    
    "Remember: In life as in this game, balance is key to long-term happiness and success."
    
    menu:
        "What would you like to do now?"
        
        "View Choice History":
            jump history_screen
            
        "Play Again":
            jump start
            
        "Return to Main Menu":
            return