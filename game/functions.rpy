# functions.rpy - Helper functions for the game

init python:
    # Function to get color for emotion display based on value
    def get_emotion_color(value):
        if value < 0:
            return "#e74c3c"  # Red for negative
        elif value == 0:
            return "#f1c40f"  # Yellow for neutral
        elif value == 1:
            return "#2ecc71"  # Green for balanced
        else:  # value >= 2
            return "#9b59b6"  # Purple for extreme
    
    # Function to get hints for each event
    def get_hint_for_event(event_num):
        hints = {
            1: "This morning situation tests your balance between personal responsibilities and helping others. Consider both immediate needs and relationship consequences.",
            
            2: "Financial decisions often reveal our values. Being generous is good, but not at the expense of your basic needs. Find a middle ground between selfishness and excessive generosity.",
            
            3: "Group dynamics require balanced honesty and patience. Speaking your mind is important, but how you deliver criticism matters just as much as the criticism itself.",
            
            4: "Rules exist for reasons, but situations are rarely black and white. Consider both principles and practicality when making decisions.",
            
            5: "Money management requires balancing immediate desires, social connections, and future planning. The wisest choice often involves compromise across all areas."
        }
        
        if event_num in hints:
            return hints[event_num]
        else:
            return "Remember that balance is key. Extreme emotions in any direction can lead to unexpected consequences."
    
    # Define a slideshow transition for images
    class Slideshow(object):
        def __init__(self):
            self.slideup = MoveTransition(0.5, enter_factory=MoveIn(0.5, direction="up"), 
                                                leave_factory=MoveOut(0.5, direction="up"))
            self.slidedown = MoveTransition(0.5, enter_factory=MoveIn(0.5, direction="down"), 
                                                leave_factory=MoveOut(0.5, direction="down"))
            self.slideleft = MoveTransition(0.5, enter_factory=MoveIn(0.5, direction="left"), 
                                                leave_factory=MoveOut(0.5, direction="left"))
            self.slideright = MoveTransition(0.5, enter_factory=MoveIn(0.5, direction="right"), 
                                                leave_factory=MoveOut(0.5, direction="right"))
    
    # Create slideshow instance
    slides = Slideshow()
    
    # Particle effect for special transitions
    def create_particles(count):
        renpy.show_screen("particle_effect", count=count)
        renpy.pause(2.5)
        renpy.hide_screen("particle_effect")

# Simple snow particle animation using ATL
image snow_particle:
    "images/particles/snowflke.svg"
    zoom 0.1
    linear 3.0 yoffset 800 alpha 0.0

screen particle_effect(count=50):
    for i in range(count):
        add "snow_particle" xpos renpy.random.randint(0, config.screen_width) ypos renpy.random.randint(-200, -50)

# Custom transitions for emotional moments
define happy_transition = MultipleTransition([
    False, dissolve,
    "white", 0.1,
    False, Function(create_particles, 50),
    True, dissolve
])

define sad_transition = MultipleTransition([
    False, dissolve,
    "#113a69", 0.2,
    True, dissolve
])

define angry_transition = MultipleTransition([
    False, dissolve,
    "#690000", 0.15,
    True, dissolve
])