import easygui

flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                          default='Vanilla')
# flavor = easygui.enterbox("What is your favorite ice cream flavor?")
easygui.msgbox("You entered " + flavor)

# flavor = easygui.buttonbox("What is your favorite ice cream flavor?",
#                            choices=['Vanilla', 'Chocolate', 'Strawberry'])
# flavor = easygui.choicebox("What is your favorite ice cream flavor?",
#                            choices=['Vanilla', 'Chocolate', 'Strawberry'])
# easygui.msgbox("You picked " + flavor)

# easygui.msgbox("Hello There!")
