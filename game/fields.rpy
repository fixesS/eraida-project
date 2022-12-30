init offset = -1

transform presayzoom:
    linear 0.2 zoom 1.03

transform postsayzoom:
    linear 0.1 zoom 1

init :
    python :
        #class allows zoom in-out character when it speaks
        class ZoomCharacter(object):
            def __init__(self, *args, **kwargs):
                self.chr = renpy.character.Character(*args, **kwargs)
                if not self.chr.image_tag:
                    raise Exception('A ZoomCharacter must have an image')

            def __call__(self, *args, **kwargs):
                renpy.show(self.chr.image_tag, at_list=[presayzoom])
                self.chr(*args, **kwargs)
                renpy.show(self.chr.image_tag, at_list=[postsayzoom])    

    #Positions of charcters
    $leftpos = Position(xalign = -0.1, yalign = 1)
    $middlepos = Position(xalign = 0.5, yalign = 1)
    $rightpos = Position(xalign = 1.1, yalign = 1) 
    $outofmap = Position(xalign = 80, yalign = 1) 
    $outofmap2 = Position(xalign = 100, yalign = 1)

    $pos2left2 = Position(xalign = -0.5,yalign = 1)
    $pos2left1 = Position(xalign = -0.1,yalign = 1)
    $pos2middle = Position(xalign = 0.5,yalign = 1)
    $pos2right1 = Position(xalign = 1.1,yalign = 1)
    $pos2right2 = Position(xalign = -1.5,yalign = 1) 
     

#Characters
define elliot = Character('Эллиот', color="#0066ff", image = "elliot")
define teo = Character('Тэо', color="#f2f2f2", image = "teo")
define arthur_vrhere = Character('Артур', color="#09ff00",image = "arthur_vrhere")
define arthur_vrhere_hidden = Character('{sc=1}?????{/sc}',image = "arthur_vrhere_hidden")
define arthur_nltech = Character('Артур', color="#09ff00",image = "arthur_nltech")# Оставил два варианат артура чтобы можно было легко заменить спрайты
define arthur_nltech_hidden = Character('{sc=1}?????{/sc}',image = "arthur_nltech_hidden")
define irma = Character('Ирма', color ="#ff751a",image = "irma")
define hr = Character('Рекрутер', color ="#b6f2ff",image = "hr")
define diana = Character('Диана',color = "#9b0bee",image = "diana")
define nana = Character('Нана',color = "#ffd480",image = "nana")
define nana_hidden = Character('{sc=1}????{/sc}',color = "#ffd480",image = "nana_hidden")
define mark = Character("Марк", color = "#e69900",image = "mark")
define aeby = Character('Эби',color = "#ffd480",image = "aeby")
define aeby_hidden = Character('{sc=1}???{/sc}',color = "#ffd480",image = "aeby_hidden")
define harry = Character("Гарри", color = "#e69900",image = "harry")
define boss = Character('Руководитель', color ="#ff8f8f",image = "boss")


#Plot variables
define gift_to_irma_ep1 = 0 # 1-Любимый торт Ирмы  2-Букет цветов с открыткой 3-Футболка с забавной зверюшкой
define company_chosen_ep1 = 0 # 1-VRHere 2-NL Technology
define company_with_E_ep1 = False #todo АККУРАТНО возможно я пропущу обработку пременной в будущем
define company_feedback_ep1 = False #todo АККУРАТНО
define elliot_and_irma_met = False

define jobint_answers_ep2 = 0 # >0-green <0-blue

define number_of_steps_ep3 = 0
define nana_visited_ep3 = False
define mark_visited_ep3 = False
define diana_visited_ep3 = False
define aeby_visited_ep3 = False
define harry_visited_ep3 = False

define presenters_ep4 = 0 # 1-pro 2-noob
define prsentation_ep4 = 0 # 1-good 2-bad

define quick_menu = True

#Main menu animation
image main_menu_animated:
    At("bg hospital building day",chromatic_offset)
    pause 5
    At("bg hospital building morning",chromatic_offset)
    pause 5
    At("bg hospital building evening",chromatic_offset)
    pause 5
    At("bg irma room day",chromatic_offset)
    pause 5
    At("bg irma room evening",chromatic_offset)
    pause 5
    At("bg irma room night",chromatic_offset)
    pause 5
    At("bg hospital out day",chromatic_offset)
    pause 5 
    At("bg hospital out morning",chromatic_offset)
    pause 5
    At("bg hospital out evening",chromatic_offset)
    pause 5
    At("bg hospital out night",chromatic_offset)
    pause 5
    At("bg street country day",chromatic_offset)
    pause 5
    At("bg street country morning",chromatic_offset)
    pause 5
    At("bg street country night",chromatic_offset)
    pause 5
    repeat

image locker_room_chroma:
    At("bg irma locker_room day",chromatic_offset)

image football3_chroma:
    At("bg football3",chromatic_offset)