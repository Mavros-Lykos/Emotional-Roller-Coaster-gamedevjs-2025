# screens.rpy - UI screen definitions

# Main menu screen
screen main_menu():
    tag menu
    add "images/main_menu_bg.webp" at Transform(xysize=(1920, 1080))


    frame:
        style_prefix "main_menu"
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "#00000077"
        
        vbox:
            spacing 20
            
            text "EMOTIONAL ROLLERCOASTER" style "heading_text" xalign 0.5 color "ffffff"
            text "THE GAME" style "heading_text" xalign 0.5 color "ffffff"

            
            null height 30
            
            textbutton "New Game" action Start() style "game_button"
            
            #textbutton "Continue" action If(len(renpy.list_saved_games()) > 0,
            #                                    Continue(),
            #                                   Notify("No save file found."))            
            textbutton "About Game" action ShowMenu("about_game") style "game_button"
            
            textbutton "How to Play" action ShowMenu("tutorial") style "game_button"
            
            textbutton "Developer Note" action ShowMenu("dev_note") style "game_button"
            
            textbutton "Quit" action Quit(confirm=True) style "game_button"

# Modify your screen definitions:
screen top_text(t):
    frame:
        xalign 0.5
        yalign 0.05
        padding (20, 20)
        background "#0008"  # semi-transparent background
        has vbox:
            xalign 0.5
        add TypewriterText(Text(t, style="top_text_style"))

screen mid_text(t):
    frame:
        xalign 0.5
        yalign 0.5
        padding (20, 20)
        background "#0008"  # semi-transparent background
        has vbox:
            xalign 0.5
        add TypewriterText(Text(t, style="mid_text_style"))

screen choice_menu(items):
    modal True
    
    frame:
        style_prefix "choice"
        xalign 0.5
        yalign 0.9
        xpadding 50
        ypadding 30
        background "#0008"
        
        vbox:
            spacing 15
            for i in items:
                textbutton i.caption action i.action


# Notification for no save game
screen save_load_notify():
    zorder 100
    frame:
        xalign 0.5
        yalign 0.3
        padding (30, 20)
        background "#00000099"
        
        vbox:
            text "No saved game found!" style "hint_text"
            null height 10
            textbutton "OK" action Hide("save_load_notify") style "game_button" xalign 0.5

# Emotion tracker display
screen emotion_tracker():
    zorder 90
    frame:
        xalign 0.98
        yalign 0.92
        padding (15, 15)
        background "images/ui/pointBox.png"
        
        vbox:
            spacing 5
            text "EMOTIONAL BALANCE" style "emotion_text" xalign 0.5
            null height 5
            
            hbox:
                spacing 10
                text "Kindness:" style "emotion_text"
                text "[kindness]" style "emotion_text" color get_emotion_color(kindness)
                
            hbox:
                spacing 10
                text "Confidence:" style "emotion_text"
                text "[confidence]" style "emotion_text" color get_emotion_color(confidence)
                
            hbox:
                spacing 10
                text "Patience:" style "emotion_text"
                text "[patience]" style "emotion_text" color get_emotion_color(patience)
                
            hbox:
                spacing 10
                text "Frugality:" style "emotion_text"
                text "[frugality]" style "emotion_text" color get_emotion_color(frugality)
                
            hbox:
                spacing 10
                text "Honesty:" style "emotion_text"
                text "[honesty]" style "emotion_text" color get_emotion_color(honesty)

# Hint button
screen hint_button():
    zorder 80
    frame:
        xalign 0.02
        yalign 0.98
        background "#ffffff"
        
        textbutton "HINT" action Show("hint_display", 
                                    hint_text=get_hint_for_event(game_progress)) at pulse_animation style "game_button"

# Hint display
screen hint_display(hint_text):
    zorder 100
    modal True
    
    add "#00000080"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 30)
        background "images/ui/pointBox.png"
        xmaximum 800
        
        vbox:
            spacing 15
            text "HINT" style "heading_text" xalign 0.5
            null height 10
            text hint_text style "hint_text"
            null height 20
            textbutton "Close" action Hide("hint_display") style "game_button" xalign 0.5

# Navigation menu
screen quick_menu():
    zorder 100
    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 0.98
            spacing 20
            
            textbutton "History" action ShowMenu("history_screen") style "game_button"
            textbutton "Save" action ShowMenu("save") style "game_button"
            textbutton "Main Menu" action MainMenu() style "game_button"

# Player choice history screen
screen history_screen():
    tag menu
    
    add "#000000cc"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "gui/overlay/history_bg.png"
        xmaximum 900
        ymaximum 700
        
        vbox:
            spacing 20
            text "YOUR CHOICES" style "heading_text" xalign 0.5
            
            viewport:
                scrollbars "vertical"
                mousewheel True
                draggable True
                
                vbox:
                    spacing 30
                    
                    if not history:
                        text "No choices made yet." style "normal_text"
                    else:
                        for entry in history:
                            frame:
                                padding (20, 15)
                                background "#f1f2f655"
                                
                                vbox:
                                    spacing 10
                                    text "Event: " + entry["event"] style "emotion_text" size 24
                                    text "Choice: " + entry["choice"] style "normal_text"
                                    text "Outcome: " + entry["outcome"] style "normal_text"
                                    
                                    hbox:
                                        spacing 15
                                        text "K: [entry[kindness_change]]" style "emotion_text" color get_emotion_color(entry["kindness_change"])
                                        text "C: [entry[confidence_change]]" style "emotion_text" color get_emotion_color(entry["confidence_change"])
                                        text "P: [entry[patience_change]]" style "emotion_text" color get_emotion_color(entry["patience_change"]) 
                                        text "F: [entry[frugality_change]]" style "emotion_text" color get_emotion_color(entry["frugality_change"])
                                        text "H: [entry[honesty_change]]" style "emotion_text" color get_emotion_color(entry["honesty_change"])
            
            null height 20
            textbutton "Return" action Return() style "game_button" xalign 0.5

# About game screen
screen about_game():
    tag menu
    
    add "#ffffffff"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "gui/overlay/about_bg.png"
        xmaximum 900
        
        vbox:
            spacing 20
            text "ABOUT BALANCE: THE GAME" style "heading_text" xalign 0.5
            
            text "In this game, you navigate through a day in the life of a university student. Every decision affects your emotional balance." style "normal_text"
            
            text "The game tracks five key emotions:" style "normal_text"
            
            vbox:
                spacing 10
                text "• Kindness: From selfishness (-) to extreme generosity (+2)" style "normal_text"
                text "• Confidence: From insecurity (-) to arrogance (+2)" style "normal_text"
                text "• Patience: From impulsiveness (-) to extreme passivity (+2)" style "normal_text"
                text "• Frugality: From wastefulness (-) to extreme penny-pinching (+2)" style "normal_text"
                text "• Honesty: From dishonesty (-) to brutal candor (+2)" style "normal_text"
            
            text "To win, aim for balanced emotions (score between 0 and +1). Avoid extremes in either direction!" style "normal_text"
            
            text "This game simulates real life where balance is key to success and happiness. Even positive traits in extreme can lead to negative outcomes." style "normal_text"
            
            null height 20
            textbutton "Return" action Return() style "game_button" xalign 0.5
screen tutorial():
    tag menu

    # White transparent overlay for fade-style background
    add "#ffffffff"

    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "gui/overlay/about_bg.png"
        xmaximum 900

        vbox:
            spacing 20

            text "HOW TO PLAY" style "heading_text" xalign 0.5

            text "This tutorial will help you understand how to navigate Balance: The Game." style "normal_text"

            text "Follow these steps to succeed:" style "normal_text"

            vbox:
                spacing 10
                text "1. Navigate through 5 events in a university student's day" style "normal_text"
                text "2. For each event, select one of 5 options from the menu" style "normal_text"
                text "3. Each choice affects your emotional scores" style "normal_text"
                text "4. After each choice, you'll see the immediate consequence" style "normal_text"
                text "5. At the end, your emotional balance determines your life outcome" style "normal_text"
                text "6. To win, keep all emotions between 0 and +1" style "normal_text"
                text "7. Click on the HINT button for guidance during gameplay" style "normal_text"
                text "8. You can't change past choices, just like in real life!" style "normal_text"
                text "9. Use the History button to review your previous choices" style "normal_text"
                text "10. The game autosaves after each major decision" style "normal_text"

            null height 20

            textbutton "Return" action Return() style "game_button" xalign 0.5


# Developer note screen
screen dev_note():
    tag menu
    
    add "#ffffffff"
    
    frame:
        xalign 0.5
        yalign 0.5
        padding (40, 40)
        background "gui/overlay/dev_note_bg.png"
        xmaximum 900
        
        vbox:
            spacing 20
            text "DEVELOPER'S NOTE" style "heading_text" xalign 0.5
            
            text "Dear Player," style "normal_text"
            
            text "Balance: The Game was created to explore how our daily choices, especially emotional responses, shape our lives. The concept came from observing how even positive traits, when taken to extremes, can lead to negative outcomes." style "normal_text"
            
            text "In designing this game, I wanted to create an experience that would make players reflect on their own decision-making processes and the importance of emotional balance." style "normal_text"
            
            text "Life rarely rewards extremes - even extremely 'good' traits like kindness or honesty can become harmful when not balanced with practicality and self-care. Similarly, traits often viewed negatively can have their place in a balanced life." style "normal_text"
            
            text "I hope this game provides both entertainment and a moment of reflection on how we navigate our own emotional responses in daily life." style "normal_text"
            
            text "Thank you for playing!" style "normal_text"
            
            null height 20
            textbutton "Return" action Return() style "game_button" xalign 0.5
style menu_choice_button:
    xalign 0.5  # centers each button

style menu_choice:
    xalign 0.5

# Top-centered text display
screen top_center_text(text_string):
    frame:
        style_prefix "toptext"
        xalign 0.5
        yalign 0.05
        text text_string

# Custom menu with top-centered question and bottom-centered choices
screen custom_menu(title, items):
    frame:
        style_prefix "toptext"
        xalign 0.5
        yalign 0.05
        text title

    vbox:
        style_prefix "menu"
        xalign 0.5
        yalign 0.8
        spacing 20

        for caption, action in items:
            textbutton caption action action

