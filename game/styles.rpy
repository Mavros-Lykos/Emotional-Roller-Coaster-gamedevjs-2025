# Custom styles for the game
style game_button:
    background "#4b7bec"
    hover_background "#3867d6"
    padding (20, 10)
    xsize 250
    
style game_button_text:
    color "#ffffff"
    hover_color "#f1f2f6"
    size 22
    font "fonts/Roboto-Bold.ttf"
    align (0.5, 0.5)
    
style hint_text:
    color "#f5f6fa"
    size 20
    font "fonts/PlusJakartaSans-Medium.ttf"
    
style emotion_text:
    color "#2f3542"
    size 18
    font "fonts/Roboto-Medium.ttf"
    
style heading_text:
    color "#2f3542"
    size 40
    font "fonts/Tagesschrift-Regular.ttf"
    text_align 0.5
    
style normal_text:
    color "#2f3542"
    size 22
    font "fonts/PlusJakartaSans-Medium.ttf"

# Custom animations for UI elements
transform pulse_animation:
    ease 0.5 alpha 0.7
    ease 0.5 alpha 1.0
    repeat

transform bounce:
    ease 0.1 yoffset -5
    ease 0.1 yoffset 0

style toptext_frame:
    background None
    padding (20, 10)

style toptext_text:
    size 32
    color "#ffffff"
    outlines [ (2, "#000000") ]
    text_align 0.5
    xalign 0.5

# Define proper styles for our text display
style top_text_style:
    align (0.5, 0.0)
    text_align 0.5
    size 28
    color "#ffffff"
    outlines [(2, "#000000", 0, 0)]  

style mid_text_style:
    align (0.5, 0.5)
    text_align 0.5
    size 40
    color "#ffffff"
    outlines [(3, "#000000", 0, 0)]
    

style event_title_style:
    align (0.5, 0.5)
    text_align 0.5
    size 50
    color "#ffffff"
    outlines [(3, "#000000", 0, 0)]
    
    
style menu_button:
    size 24
    padding (10, 10)
    background "#333"
    foreground "#fff"
    hover_background "#555"
    xalign 0.5

style choice_button is default:
    xalign 0.5
    background "#2c2c2c"
    hover_background "#3a3a3a"
    padding (20, 10)
    xminimum 300

style choice_button_text is default:
    xalign 0.5
    color "#ffffff"
    hover_color "#50a1ff"
    size 28
 