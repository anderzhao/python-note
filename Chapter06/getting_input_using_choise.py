import easygui
flavor = easygui.choicebox("What is your favorite ice cream flavor?",
                           choices=['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " + flavor)
