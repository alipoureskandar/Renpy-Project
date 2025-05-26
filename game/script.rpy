define e = Character("Heide")

image bg room = "images/musicalBg.jpeg"

label start:
    scene bg room
    e "Let's play a rhythm game!"

    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()
    
    call screen rhythm_game(
        'audio/my-music.ogg', 
        'audio/my-music.beatmap.txt'
        )
    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return

    # Determine the message based on performance
    if num_hits >= 20 and num_notes >= 27:
        $ performance_message = "Great job!"
    elif 10 < num_hits < 20:
        $ performance_message = "Better luck next time."
    else:
        $ performance_message = "Ouch!"

    e "You hit [num_hits] notes out of [num_notes]. [performance_message]"

    return
