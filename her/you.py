import time
import os
def print_all_letters_side_by_side():
    os.system("cls" if os.name == "nt" else "clear")
    # Define the ASCII art for each letter
    s_art = [
        " ####  ",
        "#      ",
        " ####  ",
        "    #  ",
        " ####  "

    ]
    o_art = [
        " ####  ",
        "#    # ",
        "#    # ",
        "#    # ",
        " ####  "
    ]
    
    r_art = [
        " ####  ",
        "#    # ",
        "#####  ",
        "#  #   ",
        "#   #  "
    ]
    
    r_art = [
        " ####  ",
        "#    # ",
        "#####  ",
        "#  #   ",
        "#   #  "
    ]
    y_art = [
        "#   #  ",
        " # #   ",
        "  #    ",
        "  #    ",
        "  #    "
    ]
    
    spce = [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]

    c_art = [
        " ####  ",
        "#      ",
        "#      ",
        "#      ",
        " ####  "
    ] 
    o_art = [
        " ####  ",
        "#    # ",
        "#    # ",
        "#    # ",
        " ####  "
    ]
  
    c_art = [
        " ####  ",
        "#      ",
        "#      ",
        "#      ",
        " ####  "
    ]
    o_art = [
        " ####  ",
        "#    # ",
        "#    # ",
        "#    # ",
        " ####  "
    ]

    fstop_art = [
        "   ",
        "   ",
        "   ",
        "## ",
        "## "
    ]
    
    spce = [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]
    a_art = [
        "  ###  ",
        " #   # ",
        " ##### ",
        " #   # ",
        " #   # "
    ]


    l_art = [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ]
    
    s_art = [
        " ####  ",
        "#      ",
        " ####  ",
        "    #  ",
        " ####  "

    ]

    o_art = [
        " ####  ",
        "#    # ",
        "#    # ",
        "#    # ",
        " ####  "
    ]
    
    comm_art = [
        "     ",
        "     ",
        "     ",
        "  #  ",
        " ##  "

    ]
    spce = [
        "     ",
        "     ",
        "     ",
        "     ",
        "     "
    ]

    s_art = [
        " ####  ",
        "#      ",
        " ####  ",
        "    #  ",
        " ####  "

    ]
    l_art = [
        "#    ",
        "#    ",
        "#    ",
        "#    ",
        "#####"
    ]
    a_art = [
        "  ###  ",
        " #   # ",
        " ##### ",
        " #   # ",
        " #   # "
    ]

    y_art = [
        "#   #  ",
        " # #   ",
        "  #    ",
        "  #    ",
        "  #    "
    ]
    exc_art = [
        "  ##   ",
        "  ##   ",
        "  ##   ",
        "       ",
        "  ##   "
    ]
    

    
    # Print the letters side by side
    for i in range(5):
        time.sleep(0.8)  # Loop through each row of the letters
        print(s_art[i],o_art[i],r_art[i],r_art[i],y_art[i],spce[i],c_art[i],o_art[i],c_art[i],o_art[i],fstop_art[i],spce[i],a_art[i],l_art[i],s_art[i],o_art[i],comm_art[i],s_art[i],l_art[i],a_art[i],y_art[i],exc_art[i])

# Call the function to print all letters side by side
print_all_letters_side_by_side()
