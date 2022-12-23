label splashscreen:

    scene black
    
    play sound "/audio/splashscreen/splashcreen.ogg" fadein 1.0

    show splashscreen with dissolve
    #$ renpy.pause(5.0, hard='True')
    pause 5

    stop sound fadeout 1.0

    scene black with dissolve
    #$ renpy.pause(0.2, hard='True')
    pause 2
    
    return