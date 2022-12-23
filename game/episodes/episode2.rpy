label episode2:
    $ renpy.block_rollback()

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    scene episode2 
    with fade
    
    $ renpy.pause(4.0, hard='True')

    stop sound fadeout 1.0

    if(company_with_E_ep1):
        if(company_chosen_ep1 == 1):
            jump vrhere_with_E_ep2
        else:
            jump nltech_with_E_ep2
    else:
        if(company_chosen_ep1 == 1):
            jump vrhere_alone_ep2
        else:
            jump nltech_alone_ep2
    return

#Линия с Эллитом
label vrhere_with_E_ep2:
    $ renpy.block_rollback()
    scene bg job hallway day
    with fade 

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    teo "Ну что, я вроде готов…"
    elliot "Ни пуха, ни пера! Я уверен, все пройдет отлично!"
    teo "Я должен произвести хорошее впечатление, но упоминать о своей идее пока не буду"
    elliot "Все идеи мы можем обсудить потом с дядей, я же обещал познакомить вас"
    teo "Волнительный день… В общем, я пошел"

    jump vrhere_with_E_jobint_ep2
    return

label vrhere_with_E_jobint_ep2:
    $jobint_answers_ep2 = 0

    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show hr normal at outofmap2

    "Чувствую, что обстановка немного напряженная. Наверное, я слишком волнуюсь"
    hr "По вашему резюме заметно, что у вас довольно большой опыт в сфере нейроразработки. Скажите, вы в курсе, кем вам предстоит работать в нашей компании?"
    teo "Да, у меня действительно есть опыт различных стажировок со времен университета, а также участия в проектах."

    menu :

        "В компанию я устраиваюсь как разработчик нейроинтерфейсов, поэтому предполагаю, что им я и буду работать?":
            $jobint_answers_ep2 -=1

        "Так как я устраиваюсь по вакансии разработчик нейроинтерфейсов, я предполагаю, что сначала у меня будет период ознакомления с системой того, как происходит разработка тех или иных продуктов, так как в этом задействованы множество специалистов. Я бы хотел подробно узнать, как устроена вся работа и выяснить, какую именно нишу я смогу занять здесь.":
            $jobint_answers_ep2 +=1

    hr "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

    menu :
        "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

        "Прежде всего упорство и желание идти к цели. Это трудоемкая, серьезная работа, требующая готовности работать с большим количеством информации, аналитическое мышление и сочетающая в себе множество сфер: от биологии до математики.":
            $jobint_answers_ep2 +=1

        "Думаю, что помимо знания своего дела, конечно же коммуникативные навыки. Потребуется работать в большой команде, а процесс должен быть слаженным и эффективным.":
            $jobint_answers_ep2 +=1

        "Наверное, талант? Проектировать интерфейсы не так уж легко.":
            $jobint_answers_ep2 -=1
    
    hr "Каких целей вы хотите для себя достичь в нашей компании?"

    menu :
        "Каких целей вы хотите для себя достичь в нашей компании?"
        
        "Я не уверен, есть ли у меня конкретные цели…Точнее, кое-что есть, но я не могу так сразу говорить об этом…":
            $jobint_answers_ep2 -=1
        "Я планирую разработать свой продукт, идея для которого у меня уже есть. Я верю в его уникальность и реальную возможность создать это.":
            $jobint_answers_ep2 +=1

    jump vrhere_with_E_hallway_ep2
    return 

label vrhere_with_E_hallway_ep2:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    ""
    elliot confused "И как? Чего такой хмурый?"
    teo "Хмурый? Нет, все, кажется, прошло довольно неплохо!"
    elliot normal "По тебе и не поймешь! Ну, расскажи хоть что-нибудь?"
    teo "Не знаю, что именно ты хочешь узнать, но я удивился тому, что они меня помнят: вроде видели на одном из проектов"
    elliot @ smile "Ого, да ты популярен, ты точно у них в приоритете"

    show elliot normal at leftpos
    with move
    
    show arthur_vrhere_hidden normal at rightpos
    with moveinright

    if(jobint_answers_ep2>0):
        arthur_vrhere_hidden @ smile "Друзья, приветствую! Тэо, восхищен твоим потенциалом, отличное собеседование."
        
        elliot @ smile "Вот видишь, я не сомневался, что все пройдет отлично!"
    else:
        arthur_vrhere_hidden @ tricky "Друзья, приветствую! Тэо, довольно интересное было сегодня интервью!"
        arthur_vrhere_hidden "Возможно, тебе многое еще предстоит узнать, хотя твои навыки несомненно впечатляющие, судя по твоему резюме"
        elliot @ confused "Тэо, что ты там наговорить успел?"
        teo "Просто немного переволновался…"
    
    elliot "Ладно, знакомься, это мой двоюродный дядя – Артур"

    show arthur_vrhere normal at rightpos
    
    hide arthur_vrhere_hidden

    teo "Приятно познакомиться лично, даже не знал, что у Эллиота в роду есть кто-то, помимо врачей"
    arthur_vrhere @ big_smile "А вот, именно поэтому он со мной и общается – для остальной части семьи мы изгои, ха-ха!"
    arthur_vrhere "К слову, Эллиот упоминал о какой-то интересной идее, предлагаю прямо сейчас пойти и обсудить ее"
    elliot @ confused "Да, но прямо сейчас? Тебе разве не нужно работать?"
    arthur_vrhere @ tricky "Может и надо, но не суть, я хочу послушать идеи, идеи и еще раз идеи! "

    jump vrhere_with_E_cafe_ep2
    return

label vrhere_with_E_cafe_ep2:
    scene bg cafe day 
    with fade 

    show teo normal at outofmap

    show elliot normal at leftpos
    with dissolve

    show arthur_vrhere normal at rightpos
    with dissolve 

    arthur_vrhere "Тэо, готов тебя выслушать"
    teo "Не уверен, с чего стоит начать…"
    elliot "Просто расскажи все как есть!"

    menu :

        "Эта идея пришла мне в голову, потому что я хочу помочь своей подруге детства. Если не вдаваться в подробности, то я собираюсь создать уникальный нейроинтерфейс в своем роде…":
            teo "Он позволит сосчитать разум и воспоминания в виртуальную реальность и погрузиться в нее. Она сможет воссоздать эти воспоминания, прожить их заново и, возможно, нейроинтерфейс даст ей шанс на начало жизни с чистого листа."
            arthur_vrhere "Вижу ты серьезно настроен, идея довольно занимательная, но ты понимаешь, что здесь должно быть определенное применение, все же наша компания по большей степени опирается на сферу развлечений"
            arthur_vrhere "Творить и разрабатывать что-то в такой компании возможно лишь при том, что у продукта есть назначение. Руководство не даст добро даже на гениальную идею, если у нее не будет перспектив"
        "С некоторого времени я загорелся идеей создать кое-что…В общем, это такой нейроинтерфейс, что позволит сосчитать разум и воспоминания людей в виртуальную реальность и погрузиться в нее.":
            teo "Совсем как наш мир, но для некоторых там не будет ограничений, что преследуют их в реальной жизни, можно будет воссоздавать места из памяти и многое другое…например, проживать воспоминания заново!"
            arthur_vrhere "Заманчивая идея, мальчишка, но в чем же ты видишь ее применение?"
            arthur_vrhere "Творить и разрабатывать что-то в такой компании возможно лишь при том, что у продукта есть назначение. Руководство не даст добро даже на гениальную идею, если у нее не будет перспектив"

    teo "Безусловно, это все-таки прежде всего может быть ориентировано на индустрию игр и развлечений, но я считаю, что подобное должно иметь больший смысл."
    teo "Что насчет людей, у которых нет привычных нам возможностей: видеть, чувствовать, передвигаться? Если хоть раз в жизни они смогут испытать это…"
    arthur_vrhere @ smile "Такие вещи противоречивы, это не простая тема, хоть я понимаю к чему ты клонишь."
    arthur_vrhere @ tricky "Мне нравится твоя идея, еще немного и я достаточно заинтересуюсь этим, и тогда ты не отвертишься, если тебя примут в компанию! А уж я думаю, что ты точно влип!"
    elliot "Я же говорил! Дядя – тот самый человек, что нам нужен"
    arthur_vrhere "Тем не менее, мой дорогой племянник до сих пор не собирается даже работать. Ты что, собираешься помогать своему другу советами?"
    arthur_vrhere "Не уверен, что ты так сможешь, когда у нас начнется разработка официально"
    elliot "Я же говорил, что пока не хочу куда-то устраиваться, мне нужен отдых. Я готов помочь Тэо, но насчет остального – пока ничего не знаю"
    teo "Он очень упертый, и я не понимаю, почему он так отрекается от своей судьбы! Только не говори, что вдруг решил стать хирургом или кем-то еще? Твои родители будут невероятно рады конечно, но поверь – это не твое!"
    elliot "Очень смешно, Тэо!"
    elliot "Если на меня будут давить с двух сторон, то я точно получу второе образование, так что осторожнее со словами!"

    jump room_ending_ep2
 
label nltech_with_E_ep2:
    $ renpy.block_rollback()
    scene bg job hallway day
    with fade 

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    teo "Ну что, я вроде готов…"
    elliot "Ни пуха, ни пера! Я уверен, все пройдет отлично"
    teo "Я должен произвести хорошее впечатление, но упоминать о своей идее пока не буду"
    elliot "Все идеи мы можем обсудить потом с дядей, я же обещал познакомить вас"
    teo "Волнительный день… В общем, я пошел"

    jump nltech_with_E_jobint_ep2
    return

label nltech_with_E_jobint_ep2:
    $jobint_answers_ep2 = 0

    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show hr normal at outofmap2

    "Чувствую, что обстановка немного напряженная. Наверное, я слишком волнуюсь"
    
    hr "По вашему резюме заметно, что у вас довольно большой опыт в сфере нейроразработки. Скажите, вы в курсе, кем вам предстоит работать в нашей компании?"
    teo "Да, у меня действительно есть опыт различных стажировок со времен университета, а также участия в проектах."

    menu:

        "В компанию я устраиваюсь как разработчик нейроинтерфейсов, поэтому предполагаю, что им я и буду работать?":
            $jobint_answers_ep2 -=1
        "Так как я устраиваюсь по вакансии разработчик нейроинтерфейсов, я предполагаю, что сначала у меня будет период ознакомления с системой того, как происходит разработка тех или иных продуктов, так как в этом задействованы множество специалистов. Я бы хотел подробно узнать, как устроена вся работа и выяснить, какую именно нишу я смогу занять здесь.":
            $jobint_answers_ep2 +=1

    hr "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

    menu: 
        "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

        "Прежде всего упорство и желание идти к цели. Это трудоемкая, серьезная работа, требующая готовности работать с большим количеством информации, аналитическое мышление и сочетающая в себе множество сфер: от биологии до математики.":
            $jobint_answers_ep2 +=1
        "Думаю, что помимо знания своего дела, конечно же коммуникативные навыки. Потребуется работать в большой команде, а процесс должен быть слаженным и эффективным.":
            $jobint_answers_ep2 +=1
        "Наверное, талант? Проектировать интерфейсы не так уж легко.":
            $jobint_answers_ep2 -=1
    
    hr "Каких целей вы хотите для себя достичь в нашей компании?"

    menu :
        "Каких целей вы хотите для себя достичь в нашей компании?"

        "Я не уверен, есть ли у меня конкретные цели…Точнее, кое-что есть, но я не могу так сразу говорить об этом…":
            $jobint_answers_ep2 -=1
        "Я планирую разработать свой продукт, идея для которого у меня уже есть. Я верю в его уникальность и реальную возможность создать это.":
            $jobint_answers_ep2 +=1
    
    jump nltech_with_E_hallway_ep2
    return

label nltech_with_E_hallway_ep2:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    ""
    elliot @ confused "И как? Чего такой хмурый?"
    teo "Хмурый? Нет, все, кажется, прошло довольно неплохо!"
    elliot "По тебе и не поймешь! Ну, расскажи хоть что-нибудь?"
    teo "Не знаю, что именно ты хочешь узнать, но я удивился тому, что они меня знают: вроде помнят с одного из проектов"
    elliot @ smile "Ого, да ты популярен, ты точно у них в приоритете"

    show elliot normal at leftpos
    with move
    
    show arthur_nltech_hidden normal at rightpos
    with moveinright

    if(jobint_answers_ep2>0):
        arthur_nltech_hidden @ smile "Друзья, приветствую! Тэо, восхищен твоим потенциалом, отличное собеседование."
        
        elliot @ smile "Вот видишь, я не сомневался, что все пройдет отлично!"
    else:
        arthur_nltech_hidden @ tricky "Друзья, приветствую! Тэо, довольно интересное было сегодня интервью!"
        arthur_nltech_hidden "Возможно, тебе многое еще предстоит узнать, хотя твои навыки несомненно впечатляющие, судя по твоему резюме"
        elliot @ confused "Тэо, что ты там наговорить успел?"
        teo "Просто немного переволновался…"
    
    elliot "Ладно, знакомься, это мой двоюродный дядя – Артур"

    show arthur_nltech normal at rightpos
    
    hide arthur_nltech_hidden

    teo "Приятно познакомиться лично, даже не знал, что у Эллиота в роду есть кто-то, помимо врачей"
    arthur_nltech @ big_smile "А вот, именно поэтому он со мной и общается – для остальной части семьи мы изгои, ха-ха!"
    arthur_nltech "К слову, Эллиот упоминал о какой-то интересной идее, предлагаю прямо сейчас пойти и обсудить ее"
    elliot @ confused "Да, но прямо сейчас? Тебе разве не нужно работать?"
    arthur_nltech @ tricky "Может и надо, но не суть, я хочу послушать идеи, идеи и еще раз идеи! "

    jump nltech_with_E_cafe_ep2
    return

label nltech_with_E_cafe_ep2:
    scene bg cafe day 
    with fade 

    show teo normal at outofmap

    show elliot normal at leftpos
    with dissolve

    show arthur_nltech normal at rightpos
    with dissolve 

    arthur_nltech "Тэо, готов тебя выслушать"
    teo "Не уверен, с чего стоит начать…"
    elliot "Просто расскажи все как есть!"

    menu:

        "Эта идея пришла мне в голову, потому что я хочу помочь своей подруге детства. Если не вдаваться в подробности, то я собираюсь создать уникальный нейроинтерфейс в своем роде…":
            teo "Люди, у которых нет привычной нам возможности передвигаться – они смогут снова испытать это и вернуть себе полноценную жизнь за счет расшифровки сигнала человека и передачи его в экзоскелет с большой точностью, и моя подруга так сможет, спустя долгое время…"
        "С некоторого времени я загорелся идеей создать кое-что…В общем, это такой нейроинтерфейс, что позволит полностью восстановить движение – расшифровать намерение человека и передать этот сигнал на экзоскелет":
            teo "Люди, у которых нет привычной нам возможности передвигаться – они смогут снова испытать это и вернуть себе полноценную жизнь! Я уверен, что возможно создать такой интерфейс, обладающий большой точностью"
    
    arthur_nltech "Вижу ты серьезно настроен, твоя идея очень интересная, но сложная. Если ты считаешь это осуществимым, значит понимаешь, каким образом воплотить это."
    arthur_nltech @ tricky "Мне нравится твоя идея, еще немного и я достаточно заинтересуюсь этим, и тогда ты не отвертишься, если тебя примут в компанию! А уж я думаю, что ты точно влип!"
    elliot "Я же говорил! Дядя – тот самый человек, что нам нужен"
    arthur_nltech "Тем не менее, мой дорогой племянник до сих пор не собирается даже работать. Ты что, собираешься помогать своему другу советами? Не уверен, что ты так сможешь, когда у нас начнется разработка официально"
    elliot "Я же говорил, что пока не хочу куда-то устраиваться, мне нужен отдых. Я готов помочь Тэо, но насчет остального – пока ничего не знаю"
    teo "Он очень упертый, и я не понимаю, почему он так отрекается от своей судьбы! Только не говори, что вдруг решил стать хирургом или кем-то еще? Твои родители будут невероятно рады конечно, но поверь – это не твое!"
    elliot "Очень смешно, Тэо! Если на меня будут давить с двух сторон, то я точно получу второе образование, так что осторожнее со словами!"

    jump room_ending_ep2
    return 

#Линия ОДИН 
label vrhere_alone_ep2:
    $ renpy.block_rollback()
    scene bg job hallway day
    with fade 

    show teo normal at outofmap
    
    teo "Надеюсь, я не слишком рано"

    show arthur_vrhere_hidden normal at rightpos
    with dissolve

    teo "Хм, тот человек выглядит знакомо, я его видел где-то раньше?"
    teo "Ладно, неважно, пора на собеседование"

    jump vrhere_alone_jobint_ep2
    return

label vrhere_alone_jobint_ep2:
    $jobint_answers_ep2 = 0
    scene bg job hallway day
    with fade 

    show teo normal at outofmap

    show hr normal at outofmap2

    "Чувствую, что обстановка немного напряженная. Наверное, я слишком волнуюсь"

    hr "По вашему резюме заметно, что у вас довольно большой опыт в сфере нейроразработки. Скажите, вы в курсе, кем вам предстоит работать в нашей компании?"
    teo "Да, у меня действительно есть опыт различных стажировок со времен университета, а также участия в проектах."

    menu:

        "В компанию я устраиваюсь как разработчик нейроинтерфейсов, поэтому предполагаю, что им я и буду работать?":
            $jobint_answers_ep2 -=1;
        "Так как я устраиваюсь по вакансии разработчик нейроинтерфейсов, я предполагаю, что сначала у меня будет период ознакомления с системой того, как происходит разработка тех или иных продуктов, так как в этом задействованы множество специалистов. Я бы хотел подробно узнать, как устроена вся работа и выяснить, какую именно нишу я смогу занять здесь.":
            $jobint_answers_ep2 +=1;

    hr "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

    menu:
        "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

        "Прежде всего упорство и желание идти к цели. Это трудоемкая, серьезная работа, требующая готовности работать с большим количеством информации, аналитическое мышление и сочетающая в себе множество сфер: от биологии до математики.":
            $jobint_answers_ep2 +=1
        "Думаю, что помимо знания своего дела, конечно же коммуникативные навыки. Потребуется работать в большой команде, а процесс должен быть слаженным и эффективным.":
            $jobint_answers_ep2 +=1
        "Наверное, талант? Проектировать интерфейсы не так уж легко.":
            $jobint_answers_ep2 -=1

    hr "Каких целей вы хотите для себя достичь в нашей компании?"

    menu:
        
        "Я не уверен, есть ли у меня конкретные цели…Точнее, кое-что есть, но я не могу так сразу говорить об этом…":
            $jobint_answers_ep2 -=1
        "Я планирую разработать свой продукт, идея для которого у меня уже есть. Я верю в его уникальность и реальную возможность создать это.":
            $jobint_answers_ep2 +=1
        
    jump vrhere_alone_hallway_ep2
    return 

label vrhere_alone_hallway_ep2:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show arthur_vrhere_hidden normal at middlepos
    with dissolve

    teo "Да, я определенно видел того человека раньше. Это тот самый, по моему мнению, «сумасшедший», которого я встретил около компании некоторое время назад. Мне стыдно, что я так о нем думал…Все-таки это один из главных разработчиков компании!"
    teo "Что если он запомнил меня, а я ведь тогда проигнорировал его…"

    
    
    arthur_vrhere_hidden "Молодой человек! Хотя, я уже знаю ваше имя – Тэо, верно? Молодой ум, да и еще и такой перспективный. Очень приятно познакомиться с вами, я Артур"
    teo "Аа…Да, добрый день!"

    show arthur_vrhere normal at middlepos
    
    hide arthur_vrhere_hidden
    
    ""
    if(jobint_answers_ep2 > 0):
        arthur_vrhere @ smile "Мне очень понравилось наше собеседование. К слову, вы упомянули одну наверняка интересную идею…Не желаете ли обсудить подробнее?"
    else:
        arthur_vrhere @ smile "Мне очень понравилось наше собеседование, довольно странные ответы, но это даже к лучшему, ха-ха!"
        teo "Немного переволновался…"
        arthur_vrhere "К слову, вы упомянули одну наверняка интересную идею…Не желаете ли обсудить подробнее?"

    teo "Обсудить?"
    arthur_vrhere "Скажу прямо, меня заинтриговали ваши слова. Предлагаю поговорить об этом прямо сейчас!"

    jump vrhere_alone_cafe_ep2
    return

label vrhere_alone_cafe_ep2:
    scene bg cafe day 
    with fade 

    show teo normal at outofmap

    show arthur_vrhere normal at middlepos
    with dissolve 

    arthur_vrhere "Расскажите же о вашей будущей разработке."
    teo "Надеюсь, что действительно будущей…"
    teo "С некоторого времени я загорелся идеей создать кое-что…В общем, это такой нейроинтерфейс, что позволит сосчитать разум и воспоминания людей в виртуальную реальность и погрузиться в нее."
    teo "Совсем как наш мир, но для некоторых там не будет ограничений, что преследуют их в реальной жизни, можно будет воссоздавать места из памяти и многое другое…"
    arthur_vrhere "Заманчивая идея, Тэо, но в чем же вы видите ее применение? Творить и разрабатывать что-то в такой компании возможно лишь при том, что у продукта есть назначение. Руководство не даст добро даже на гениальную идею, если у нее не будет перспектив"
    teo "Безусловно, это все-таки прежде всего может быть ориентировано на индустрию игр и развлечений, но я считаю, что подобное должно иметь больший смысл. "
    teo "Что насчет людей, у которых нет привычных нам возможностей: видеть, чувствовать, передвигаться? Если хоть раз в жизни они смогут испытать это…"
    arthur_vrhere @ smile "Такие вещи противоречивы, это не простая тема, хоть я понимаю к чему вы клоните."
    arthur_vrhere @ tricky "Мне определенно нравится ваша идея, еще немного и я достаточно заинтересуюсь этим, и тогда вы не отвертитесь, если вас примут в компанию! "
    teo "Даже не знаю, что вам ответить. Я бы очень хотел попасть в VRHere! Видя ваш интерес, я думаю, мы могли бы неплохо сработаться в дальнейшем…"
    "(Мне очень стыдно за то, что я думал об этом человеке ранее)"
    arthur_vrhere "Вот и я с нетерпением жду начала нашей с вами работы! Вот моя визитка, можете в любой момент присылать мне ваши разработки."
    teo "Спасибо, я ценю ваше желание помочь, хоть меня еще и не приняли "
    "Артур Ловатия? Ого, они с Эллиотом однофамильцы, здорово, это ведь такая редкая фамилия…"

    jump vrhere_alone_callE_ep2
    return 

label vrhere_alone_callE_ep2:
    scene bg street country day
    with fade

    show teo normal at outofmap

    "Нужно позвонить Эллиоту и рассказать, что вообще произошло за это время"

    show elliot normal at outofmap2
    with dissolve

    teo "Эллиот, не представляешь, но я сегодня сходил на собеседование в VRHere! Думаю, все прошло успешно. Это мой единственный шанс на сегодняшний день"
    elliot "Неужели? Здорово, я рад. Почему же единственный?"
    teo "Оба собеседования поставили в один день, вот я и выбрал свой окончательный вариант"
    teo "Кстати, это очень забавная ситуация, но после дня рождения Ирмы я шел домой, и около здания компании встретил одного странного мужчину, и он действительно странно себя вел! "
    teo "Возможно он уже знал меня, хотя я точно ни в чем не уверен, но оказалось, что он главный разработчик компании! И он был на этом собеседовании, а после него мы даже обсуждали мою идею проекта, который я решил воплотить ради Ирмы"
    elliot "Кажется, я понимаю, о ком ты, ахах…"
    teo "М? Кроме этого, представь себе – у него твоя редкая фамилия! Разве не смешно?"
    elliot "Тэо, это мой двоюродный дядя."
    teo "Что? Ты имеешь ввиду, что он…?"
    elliot "Да, именно так!"
    teo "Разве у тебя в семье не все врачи? Откуда вдруг такое? Ты меня удивляешь, даже не рассказывал о нем!"
    elliot "Хотел оставаться немного загадочным…Зато как смешно сейчас было слушать тебя!"
    teo "Вау, ну спасибо тебе, дружище…В любом случае, кажется он заинтересован в моей идее"
    elliot "Дядя Артур – именно тот человек, что нужен для подобного. Он не может сидеть без дела! Это отличная новость, к тому же, я уверен, что тебя примут с твоим то опытом и достижениями"
    teo "Сейчас остается лишь ждать две недели…"

    jump room_ending_ep2
    return

label nltech_alone_ep2:
    $ renpy.block_rollback()
    scene bg job hallway day
    with fade 

    show teo normal at outofmap
    
    teo "Надеюсь, я не слишком рано"

    show arthur_nltech_hidden normal at rightpos
    with dissolve

    teo "Хм, тот человек выглядит знакомо, я его видел где-то раньше?"
    teo "Ладно, неважно, пора на собеседование"

    jump nltech_alone_jobint_ep2
    return

label nltech_alone_jobint_ep2:
    $jobint_answers_ep2 = 0
    scene bg job hallway day
    with fade 

    show teo normal at outofmap

    show hr normal at outofmap2

    "Чувствую, что обстановка немного напряженная. Наверное, я слишком волнуюсь"

    hr "По вашему резюме заметно, что у вас довольно большой опыт в сфере нейроразработки. Скажите, вы в курсе, кем вам предстоит работать в нашей компании?"
    teo "Да, у меня действительно есть опыт различных стажировок со времен университета, а также участия в проектах."

    menu:

        "В компанию я устраиваюсь как разработчик нейроинтерфейсов, поэтому предполагаю, что им я и буду работать?":
            $jobint_answers_ep2 -=1;
        "Так как я устраиваюсь по вакансии разработчик нейроинтерфейсов, я предполагаю, что сначала у меня будет период ознакомления с системой того, как происходит разработка тех или иных продуктов, так как в этом задействованы множество специалистов. Я бы хотел подробно узнать, как устроена вся работа и выяснить, какую именно нишу я смогу занять здесь.":
            $jobint_answers_ep2 +=1;

    hr "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

    menu:
        "Какими качествами, по вашему мнению, должен обладать сотрудник на этой должности?"

        "Прежде всего упорство и желание идти к цели. Это трудоемкая, серьезная работа, требующая готовности работать с большим количеством информации, аналитическое мышление и сочетающая в себе множество сфер: от биологии до математики.":
            $jobint_answers_ep2 +=1
        "Думаю, что помимо знания своего дела, конечно же коммуникативные навыки. Потребуется работать в большой команде, а процесс должен быть слаженным и эффективным.":
            $jobint_answers_ep2 +=1
        "Наверное, талант? Проектировать интерфейсы не так уж легко.":
            $jobint_answers_ep2 -=1

    hr "Каких целей вы хотите для себя достичь в нашей компании?"

    menu:
        
        "Я не уверен, есть ли у меня конкретные цели…Точнее, кое-что есть, но я не могу так сразу говорить об этом…":
            $jobint_answers_ep2 -=1
        "Я планирую разработать свой продукт, идея для которого у меня уже есть. Я верю в его уникальность и реальную возможность создать это.":
            $jobint_answers_ep2 +=1
        
    jump nltech_alone_hallway_ep2
    return 

label nltech_alone_hallway_ep2:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show arthur_nltech_hidden normal at middlepos
    with dissolve

    teo "Да, я определенно видел того человека раньше. Это тот самый, по моему мнению, «сумасшедший», которого я встретил около компании некоторое время назад. Мне стыдно, что я так о нем думал…Все-таки это один из главных разработчиков компании!"
    teo "Что если он запомнил меня, а я ведь тогда проигнорировал его…"

    
    
    arthur_nltech_hidden "Молодой человек! Хотя, я уже знаю ваше имя – Тэо, верно? Молодой ум, да и еще и такой перспективный. Очень приятно познакомиться с вами, я Артур"
    teo "Аа…Да, добрый день!"

    show arthur_nltech at middlepos
    
    hide arthur_nltech_hidden

    if(jobint_answers_ep2 > 0):
        arthur_nltech @ smile "Мне очень понравилось наше собеседование. К слову, вы упомянули одну наверняка интересную идею…Не желаете ли обсудить подробнее?"
    else:
        arthur_nltech @ smile "Мне очень понравилось наше собеседование, довольно странные ответы, но это даже к лучшему, ха-ха!"
        teo "Немного переволновался…"
        arthur_nltech "К слову, вы упомянули одну наверняка интересную идею…Не желаете ли обсудить подробнее?"

    teo "Обсудить?"
    arthur_nltech "Скажу прямо, меня заинтриговали ваши слова. Предлагаю поговорить об этом прямо сейчас!"

    jump nltech_alone_cafe_ep2
    return

label nltech_alone_cafe_ep2:
    scene bg cafe day 
    with fade 

    show teo normal at outofmap

    show arthur_nltech normal at middlepos
    with dissolve 

    arthur_nltech "Расскажите же о вашей будущей разработке."
    teo "Надеюсь, что действительно будущей…"
    teo "С некоторого времени я загорелся идеей создать кое-что…В общем, это такой нейроинтерфейс, что позволит сосчитать разум и воспоминания людей в виртуальную реальность и погрузиться в нее."
    teo "Совсем как наш мир, но для некоторых там не будет ограничений, что преследуют их в реальной жизни, можно будет воссоздавать места из памяти и многое другое…"
    arthur_nltech "Заманчивая идея, Тэо, но в чем же вы видите ее применение? Творить и разрабатывать что-то в такой компании возможно лишь при том, что у продукта есть назначение. Руководство не даст добро даже на гениальную идею, если у нее не будет перспектив"
    teo "Безусловно, это все-таки прежде всего может быть ориентировано на индустрию игр и развлечений, но я считаю, что подобное должно иметь больший смысл. "
    teo "Что насчет людей, у которых нет привычных нам возможностей: видеть, чувствовать, передвигаться? Если хоть раз в жизни они смогут испытать это…"
    arthur_nltech @ smile "Такие вещи противоречивы, это не простая тема, хоть я понимаю к чему вы клоните."
    arthur_nltech @ tricky "Мне определенно нравится ваша идея, еще немного и я достаточно заинтересуюсь этим, и тогда вы не отвертитесь, если вас примут в компанию! "
    teo "Даже не знаю, что вам ответить. Я бы очень хотел попасть в NL Technology! Видя ваш интерес, я думаю, мы могли бы неплохо сработаться в дальнейшем…"
    "(Мне очень стыдно за то, что я думал об этом человеке ранее)"
    arthur_nltech "Вот и я с нетерпением жду начала нашей с вами работы! Вот моя визитка, можете в любой момент присылать мне ваши разработки."
    teo "Спасибо, я ценю ваше желание помочь, хоть меня еще и не приняли "
    "Артур Ловатия? Ого, они с Эллиотом однофамильцы, здорово, это ведь такая редкая фамилия…"

    jump nltech_alone_callE_ep2
    return

label nltech_alone_callE_ep2:
    scene bg street country day
    with fade

    show teo normal at outofmap

    "Нужно позвонить Эллиоту и рассказать, что вообще произошло за это время"

    show elliot normal at outofmap2
    with dissolve

    teo "Эллиот, не представляешь, но я сегодня сходил на собеседование в VRHere! Думаю, все прошло успешно. Это мой единственный шанс на сегодняшний день"
    elliot "Неужели? Здорово, я рад. Почему же единственный?"
    teo "Оба собеседования поставили в один день, вот я и выбрал свой окончательный вариант"
    teo "Кстати, это очень забавная ситуация, но после дня рождения Ирмы я шел домой, и около здания компании встретил одного странного мужчину, и он действительно странно себя вел! "
    teo "Возможно он уже знал меня, хотя я точно ни в чем не уверен, но оказалось, что он главный разработчик компании! И он был на этом собеседовании, а после него мы даже обсуждали мою идею проекта, который я решил воплотить ради Ирмы"
    elliot "Кажется, я понимаю, о ком ты, ахах…"
    teo "М? Кроме этого, представь себе – у него твоя редкая фамилия! Разве не смешно?"
    elliot "Тэо, это мой двоюродный дядя."
    teo "Что? Ты имеешь ввиду, что он…?"
    elliot "Да, именно так!"
    teo "Разве у тебя в семье не все врачи? Откуда вдруг такое? Ты меня удивляешь, даже не рассказывал о нем!"
    elliot "Хотел оставаться немного загадочным…Зато как смешно сейчас было слушать тебя!"
    teo "Вау, ну спасибо тебе, дружище…В любом случае, кажется он заинтересован в моей идее"
    elliot "Дядя Артур – именно тот человек, что нужен для подобного. Он не может сидеть без дела! Это отличная новость, к тому же, я уверен, что тебя примут с твоим то опытом и достижениями"
    teo "Сейчас остается лишь ждать две недели…"

    jump room_ending_ep2
    return

label room_ending_ep2:
    scene bg room evening 
    with fade

    show teo normal at outofmap

    teo "Собеседование пройдено…Еще один шаг, и я смогу начать воплощать в жизнь то, что задумал. Но смогу ли?"
    teo "Артур воодушевлен идеей, но вдруг я слишком много надумываю… В любом случае, я еще даже не приступил к работе"
    teo "Через две недели я узнаю, приняли ли меня, а пока остается лишь ждать и продумывать разработку"

    scene black 
    with fade

    show screen notify("Спустя какое-то время ...")
    pause(3)

    show bg room day
    with fade

    show teo normal at outofmap
    teo "Пришло письмо! Кажется, это один из самых волнительных моментов в моей жизни…"
    teo "Ну что, пора открывать…"
    teo "Уважаемый Тэо…так, так, так…Собеседование прошло успешно, можете приступать к работе!!!"
    teo "Да! Я действительно теперь работаю в компании своей мечты! С нетерпением жду первый день, каким же он будет?"

    jump save_scene_ep2
    return

label save_scene_ep2:
    $ renpy.block_rollback()
    scene black 
    with fade

    $ renpy.pause(0.5, hard='True')

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    show screen notify("Решения записаны...")

    $ renpy.pause(4, hard='True')

    stop sound fadeout 1.0

    $ renpy.pause(2, hard='True')

    jump episode3

    return 
