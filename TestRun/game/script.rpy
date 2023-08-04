# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Iida")
define b = Character("Bakugo")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    i "Encyclopedia of Manta Rays, Encyclopedia of Gamma Rays, Encyclopedia of X-Rays,... Just where is that book?"

    b "..."

    #scene change here

    b "...!!" 
    

    i "Oh, this lovely gentleman cannot reach the book he is looking for. I would say, “Allow me,” but the library requires us to remain silent."
    
    #scene change here 

    i "??"

    b "..."

    i "They seem kind of familiar"
    # This ends the game.

    return
