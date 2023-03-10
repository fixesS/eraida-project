label episode3:
    $ renpy.block_rollback()

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    scene episode3 
    with fade
    
    $ renpy.pause(4.0, hard='True')

    stop sound fadeout 1.0
    $quick_menu = True
    play music "/audio/music/company_base.ogg" fadein 1.0 volume 0.6 loop
    if(company_chosen_ep1 == 1):
        jump vrhere_1_ep3
    else:
        jump nltech_1_ep3

    return  

label vrhere_1_ep3:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show arthur_vrhere normal at middlepos
    with dissolve

    "Сегодня мой первый день работы, надеюсь все пройдет успешно"
    arthur_vrhere @ smile "Тэо! Добро пожаловать уже в качестве сотрудника! Ну что, готов знакомиться со злыми коллегами, которые будут перемывать тебе косточки?"
    teo "Что? В смысле…"
    arthur_vrhere @ tricky "Ха-ха! Я просто пошутил, не бойся, малец"
    arthur_vrhere "Держи бейджик, и пошли на небольшую экскурсию"
    teo "Хорошо..."
    "Его шуточки каждый раз меня очень напрягают!"

    jump vrhere_2_ep3

    return

label vrhere_2_ep3:
    scene bg job office day
    with fade

    show teo normal at outofmap

    show arthur_vrhere normal at middlepos
    with dissolve

    arthur_vrhere "Как ты знаешь, а я надеюсь что знаешь, разработка нейроинтерфейсов – это всегда командная работа. Здесь задействованы биологи, психологи, математики, инженеры и программисты."
    arthur_vrhere "У каждого здесь свои задачи, но мы трудимся над одной целью, поэтому важно, чтобы все понимали это для нашей слаженной работы"
    arthur_vrhere "Сейчас я познакомлю тебя со своей мини-командой, так скажем – основным составом!"

    jump vrhere_3_ep3
    return

label vrhere_3_ep3:
    scene bg job office diana day
    with fade

    show teo normal at outofmap

    show diana tired at leftpos
    with dissolve

    show arthur_vrhere normal at rightpos
    with dissolve

    arthur_vrhere "Проходи, это кабинет нашего дорогого нейробиолога"
    diana tired "Боже, кто здесь? (зевает)"
    arthur_vrhere @ smile "Диана, ты как всегда… свежа"
    arthur_vrhere "Знакомься, это наш новый сотрудник – Тэо, будущий гениальный проектировщик интерфейсов!"
    teo "Приятно познакомиться, я Тэо, наслышан о вас – вы писали множество интересных диссертаций!"
    diana @ surprise "Ой, точно! У нас же новый работничек!"
    diana @ tricky "Да-да, мне тоже очень приятно. Множество – это легко сказано, хотя по моему внешнему виду наверняка заметно…"
    diana "Артур, ты можешь принести мне кофе? Мне кажется, я не смогу дойти до кухни…умоляю!"
    arthur_vrhere @ tricky "У нас сейчас небольшая экскурсия, так что давай-ка ты сама и сбегаешь потом или…можешь взять в рабы Тэо!"
    teo "Вы все очень дружелюбны, я так ценю это! Артур, может нам следует отправиться дальше?"
    diana @ tired "Ой все, идите тогда. Вот когда я приду в себя после ночных бдений, а это произойдет, когда я наконец выпью парочку кружек кофе, то жду тебя на обсуждение твоих рабских обязанностей!"

    jump vrhere_4_ep3
    return

label vrhere_4_ep3:
    scene bg job lab1
    with fade

    show teo normal at outofmap

    show arthur_vrhere normal at middlepos
    with dissolve

    arthur_vrhere "Ну, как тебе Диана? Очень веселая, не так ли?"
    teo "Вы чем-то похожи, не уверен, хорошо ли это… Но в любом случае, я думаю, что мы отлично сработаемся."
    arthur_vrhere "Я не сомневаюсь! Хоть Диана постоянно как зомби, но она один из самых талантливых нейробиологов в нашей области – работать с ней в команде – это большая удача"
    arthur_vrhere "Это одна из наших лабораторий. Кажется, здесь никого нет. Идем дальше!"

    jump vrhere_5_ep3
    return

label vrhere_5_ep3:
    scene bg job lab2
    with fade

    show teo normal at outofmap

    show arthur_vrhere normal at rightpos
    with dissolve

    show nana_hidden little_angry at leftpos
    with dissolve

    arthur_vrhere "О, а вот и наша коротышка-инженер!"
    nana_hidden @ little_angry "Артур, я сделаю вид, что не слышала этого."
    nana_hidden "Кого вы мне привели? Подопытного?"
    arthur_vrhere @ displeasure "Ты не достойна оценить мои невероятные шутки…Подопытные прибудут позже, а это наш новый сотрудник – Тэо, знакомьтесь!"
    teo "Привет, я Тэо, надеюсь мы сработаемся!"

    show nana little_angry at leftpos

    hide nana_hidden 

    nana "Аа, точно, это о тебе Артур мне все уши прожужжал! Привет-привет, я Нана."
    arthur_vrhere @ smile "Как видишь, мы с Наной – лучшие друзья"
    arthur_vrhere "Познакомились, бежим дальше."
    "Какие все здесь интересные…надеюсь, про промывать косточки – это точно была шутка"

    jump vrhere_6_ep3
    return

label vrhere_6_ep3:
    $number_of_steps_ep3 = 0
    $nana_visited_ep3 = False
    $mark_visited_ep3_ep3 = False
    $diana_visited_ep3 = False

    scene bg job office mark day 
    with fade

    show teo normal at outofmap

    show mark normal at leftpos
    with dissolve

    show arthur_vrhere normal at rightpos
    with dissolve

    arthur_vrhere "Марк, к вам можно?"
    mark "Ну, вы же уже зашли."
    arthur_vrhere "Знакомьтесь, это Тэо – наш новый сотрудник, к тому же очень перспективный разработчик нейроинтерфейсов! Надеюсь, вы подружитесь, детишки!"
    mark @ arrogant "Одного сдружиться будет мало, Артур! Главное – качественно и вовремя выполнять свои задачи. "
    mark @ smile "Приятно познакомиться, я Марк – грубо говоря, математик."
    teo "Мне тоже, поверь, свою работу я буду выполнять именно так, как ты сказал! Можно ведь обращаться на «ты?»"
    mark "Вполне."
    arthur_vrhere "Итак, Тэо, ты со всеми знаком."
    arthur_vrhere "Перед назначением твоих прямых обязанностей, в качестве первого дня предлагаю тебе подробнее разузнать о задачах каждого из твоих коллег, влиться в рабочую среду."
    arthur_vrhere "К кому хочешь пойти?"

    menu: 
        "К кому хочешь пойти?"

        "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
            $number_of_steps_ep3+=1
            jump vrhere_7_diana_ep3
        "Я бы хотел поговорить с Наной. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
            $number_of_steps_ep3+=1
            jump vrhere_7_nana_ep3
        "Я бы хотел поговорить с Марком. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
            $number_of_steps_ep3+=1
            jump vrhere_7_mark_ep3

    return 

label vrhere_7_diana_ep3:
    $diana_visited_ep3 = True

    scene bg job office diana day
    with fade

    show teo normal at outofmap

    show diana normal at middlepos
    with dissolve

    teo "Добрый день еще раз! Артур отправил меня на исследования, решил заглянуть к вам. Расскажете подробнее, чем вы занимаетесь сейчас?"
    diana "Ого, ты выбрал меня, я тронута до глубины души! Как видишь, кофе я выпила, теперь в состоянии все тебе выложить"
    diana "Помимо изучения процессов, происходящих в мозге человека, я занимаюсь измерением электрической активности мозга. Например, провожу ЭЭГ – электроэнцефалографию – она, кстати, и может быть использована прямо в нейроинтерфейсах. "
    diana "Мы фиксируем то, что происходит на электроэнцефалограмме, учим алгоритм различать результаты и затем угадываем с его помощью, о чем думает испытуемый: например, о правой руке или о левой."
    teo "Над чем вы сейчас работаете?"
    diana "Мы хотим уйти в сторону разработки неинвазивных интерфейсов. Неинвазивные располагают на голове, а инвазивные вживляют в мозг."
    diana "Хоть с помощью них можно получить наиболее детальную информацию, но все же для нашей компании найти применение инвазивным интерфейсам довольно тяжело, так как у нас в приоритете именно VR."
    teo "Да! Я рад, что именно такие интерфейсы сейчас в приоритете у вас, я бы хотел поучаствовать в разработке настолько много, насколько это возможно при моем опыте"
    diana "Может быть, все может быть!"
    teo "Кстати, крутой халат, выглядите прямо-таки серьезно!"
    diana "Спасибо-спасибо! Я-то вот ношу халат, потому что я биолог, а Артур, потому что хочет выглядеть загадочно."
    diana @ laugh "Ты не задумывался, зачем он ему вообще нужен?"
    teo "И правда, ха-ха!"
    teo "В общем, спасибо за разговор, было правда интересно узнать о вашей деятельности"

    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Наной. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
                $number_of_steps_ep3+=1
                jump vrhere_7_nana_ep3
            "Я бы хотел поговорить с Марком. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
                $number_of_steps_ep3+=1
                jump vrhere_7_mark_ep3
    
    jump vrhere_8_ep3
    return

label vrhere_7_nana_ep3:
    $nana_visited_ep3 = True
    scene bg job lab2
    with fade
    
    show teo normal at outofmap

    show nana little_angry at leftpos
    with easeinright

    pause(0.2)

    show nana little_angry at rightpos
    with ease

    pause(0.2)

    show nana little_angry at middlepos
    with ease

    teo "Ээ, Нана? Чего ты так носишься? Что-то случилось? Чем-то помочь?"
    nana @ confused "Я очень-очень тороплюсь!!!"
    nana "Помощь мне может и понадобилась бы, но ты пока всего лишь стажер, который не в курсе всех дел…"
    teo "Я, собственно, поэтому и пришел. Можешь рассказать подробнее о том, чем ты занимаешься сейчас?"
    nana "Так, ну я занимаюсь технической частью, в основном созданием аппаратной части устройств."
    nana "Сейчас я пытаюсь довести до совершенства наш VR-шлем, но в перспективах у нас новый проект, подробностей не знаю, но компания хочет что-то уникальное"
    teo "Здорово, спасибо"

    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
                $number_of_steps_ep3+=1
                jump vrhere_7_diana_ep3
            "Я бы хотел поговорить с Марком. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
                $number_of_steps_ep3+=1
                jump vrhere_7_mark_ep3
    
    jump vrhere_8_ep3
    return

label vrhere_7_mark_ep3:
    $mark_visited_ep3 = True
    scene bg job office mark day
    with fade

    show teo normal at outofmap

    show mark normal at middlepos
    with dissolve

    teo "Марк, ты не сильно занят? Можно поинтересоваться, в чем заключается твоя деятельность поподробнее?"
    mark "Разве так можно, чтобы стажер в первый день просто разгуливал и спрашивал всех, кто чем занимается?"
    mark "Ладно, я постараюсь быстро ввести тебя в курс дела"
    mark "В мои задачи входит анализ сигналов в интерфейсе мозг-компьютер, декодирование сигналов активности мозга с помощью физиологически интеретируемых нейронных сетей и прочее"
    mark "Я и остальные ученые пытаемся смоделировать сложную систему работы мозга посредством простых математических моделей, хоть это и звучит странно или парадоксально "
    mark "С каждым разом мы приближаемся все больше к пониманию мозга человека, так что нам остается лишь работать и работать, пока не придем к настоящему результату"
    teo "У тебя и правда сложная работа!"
    teo "Пока в студенчестве я работал над различными проектами, иногда приходилось совмещать все сферы деятельности, так что понимаю, как это нелегко"
    mark @ smile "Действительно? Ну, я рад, обращайся если что-то нужно"
    
    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
                $number_of_steps_ep3+=1
                jump vrhere_7_diana_ep3
            "Я бы хотел поговорить с Наной. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
                $number_of_steps_ep3+=1
                jump vrhere_7_nana_ep3
    
    jump vrhere_8_ep3
    return

label vrhere_8_ep3:
    scene bg job talkroom day
    with fade

    show teo normal at outofmap

    show arthur_vrhere normal at middlepos

    teo "Долго ждете? Что-то я забегался"
    arthur_vrhere @ big_smile "Надеюсь команда не держала тебя в заложниках? Ха-ха! Даже если бы долго ждал, дел всегда невпроворот и всегда есть чем заняться"
    arthur_vrhere "Итак, давай обсудим твои наработки и конкретные идеи"

    if(diana_visited_ep3):
        teo "Я слышал, что у компании как раз курс на неинвазивные нейроинтерфейсы, к тому же более продвинутые, поэтому есть следующая идея"
    else:
        teo "Я слышал, что у компании как раз курс на что-то новое и уникальное, поэтому есть следующая идея"

    teo "Как насчет того, чтобы создать нейроинтерфейс, позволяющий уходить в свое «сознание», воссоздавать там свои воспоминания и прочее? В дальнейшем это можно превратить в экзокортекс, который сможет объединить сознание нескольких человек, а то и больше"
    teo "Интерфейс будет прикрепляться на голову, а при его включении человек будет погружаться в виртуальную реальность"
    teo "Будет возможно применять это во многих играх, но важно правильно реализовать технологию. Вот все мои наработки, но нам нужна помощь команды в дальнейшем"
    arthur_vrhere @ smile "Понял. Знаешь, отличнейшая идея! Не зря я сразу заинтересовался "
    arthur_vrhere "У меня нет сомнения, что руководству это также приглянется, но все же перед презентацией мы должны максимально составить план и показать им смысл и перспективы этой разработки"
    arthur_vrhere "Я посмотрю внимательно все твои записи и схемы, и затем можем приступать к работе!"
    teo "Хорошо, спасибо за доверие! Тогда, встретимся на следующей неделе?"
    arthur_vrhere "Хоть каждый день! А вообще да, потому что я ничего не успеваю"
    arthur_vrhere @ sad "Даже такой гениальный человек как я может быть завален кучей дел и не иметь возможности выбраться…"

    jump save_scene_ep3
    return

label nltech_1_ep3:
    scene bg job hallway day
    with fade

    show teo normal at outofmap

    show arthur_nltech normal at middlepos
    with dissolve

    "Сегодня мой первый день работы, надеюсь все пройдет успешно"
    arthur_nltech @ smile "Тэо! Добро пожаловать уже в качестве сотрудника! Ну что, готов знакомиться со злыми коллегами, которые будут перемывать тебе косточки?"
    teo "Что? В смысле…"
    arthur_nltech @ tricky "Ха-ха! Я просто пошутил, не бойся, малец"
    arthur_nltech "Держи бейджик, и пошли на небольшую экскурсию"
    teo "Хорошо..."
    "Его шуточки каждый раз меня очень напрягают!"

    jump nltech_2_ep3

    return

label nltech_2_ep3:
    scene bg job office day
    with fade

    show teo normal at outofmap

    show arthur_nltech normal at middlepos
    with dissolve

    arthur_nltech "Как ты знаешь, а я надеюсь что знаешь, разработка нейроинтерфейсов – это всегда командная работа. Здесь задействованы биологи, психологи, математики, инженеры и программисты."
    arthur_nltech "У каждого здесь свои задачи, но мы трудимся над одной целью, поэтому важно, чтобы все понимали это для нашей слаженной работы"
    arthur_nltech "Сейчас я познакомлю тебя со своей мини-командой, так скажем – основным составом!"

    jump nltech_3_ep3
    return

label nltech_3_ep3:
    scene bg job office diana day
    with fade

    show teo normal at outofmap

    show diana tired at leftpos
    with dissolve

    show arthur_nltech normal at rightpos
    with dissolve

    arthur_nltech "Проходи, это кабинет нашего дорогого нейробиолога"
    diana tired "Боже, кто здесь? (зевает)"
    arthur_nltech @ smile "Диана, ты как всегда… свежа"
    arthur_nltech "Знакомься, это наш новый сотрудник – Тэо, будущий гениальный проектировщик интерфейсов!"
    teo "Приятно познакомиться, я Тэо, наслышан о вас – вы писали множество интересных диссертаций!"
    diana @ surprise "Ой, точно! У нас же новый работничек!"
    diana @ tricky "Да-да, мне тоже очень приятно. Множество – это легко сказано, хотя по моему внешнему виду наверняка заметно…"
    diana "Артур, ты можешь принести мне кофе? Мне кажется, я не смогу дойти до кухни…умоляю!"
    arthur_nltech @ tricky "У нас сейчас небольшая экскурсия, так что давай-ка ты сама и сбегаешь потом или…можешь взять в рабы Тэо!"
    teo "Вы все очень дружелюбны, я так ценю это! Артур, может нам следует отправиться дальше?"
    diana @ tired "Ой все, идите тогда. Вот когда я приду в себя после ночных бдений, а это произойдет, когда я наконец выпью парочку кружек кофе, то жду тебя на обсуждение твоих рабских обязанностей!"

    jump nltech_4_ep3
    return

label nltech_4_ep3:
    scene bg job lab1
    with fade

    show teo normal at outofmap

    show arthur_nltech normal at middlepos
    with dissolve

    arthur_nltech "Ну, как тебе Диана? Очень веселая, не так ли?"
    teo "Вы чем-то похожи, не уверен, хорошо ли это… Но в любом случае, я думаю, что мы отлично сработаемся."
    arthur_nltech "Я не сомневаюсь! Хоть Диана постоянно как зомби, но она один из самых талантливых нейробиологов в нашей области – работать с ней в команде – это большая удача"
    arthur_nltech "Это одна из наших лабораторий. Кажется, здесь никого нет. Идем дальше!"

    jump nltech_5_ep3
    return

label nltech_5_ep3:
    scene bg job lab2
    with fade

    show teo normal at outofmap

    show arthur_nltech normal at rightpos
    with dissolve

    show aeby_hidden normal at leftpos
    with dissolve

    arthur_nltech "О, а вот и наша коротышка-инженер!"
    aeby_hidden @ smile "Артур, вы и ваши шутки как всегда поднимают настроение!"
    aeby_hidden @ smile "Кого вы мне привели? Подопытного?"
    arthur_nltech @ smile "Только ты и достойна оценить мои невероятные шутки…Подопытные прибудут позже, а это наш новый сотрудник – Тэо, знакомьтесь!"
    teo "Привет, я Тэо, надеюсь мы сработаемся!"

    show aeby normal at leftpos

    hide aeby_hidden

    aeby "Аа, точно, это о тебе Артур мне все уши прожужжал! Ты его новый любимчик? Привет-привет, я Эби."
    arthur_nltech @ smile "Как видишь, мы с Эби – лучшие друзья. Познакомились, бежим дальше"
    "Какие все здесь интересные…надеюсь, про промывать косточки – это точно была шутка"


    jump nltech_6_ep3
    return

label nltech_6_ep3:
    $number_of_steps_ep3 = 0
    $aeby_visited_ep3 = False
    $harry_visited_ep3 = False
    $diana_visited_ep3 = False

    scene bg job office mark day 
    with fade

    show teo normal at outofmap

    show harry normal at leftpos
    with dissolve

    show arthur_nltech normal at rightpos
    with dissolve

    arthur_nltech @ smile "Гарри, к вам можно?"
    harry "Ну, вы же уже зашли."
    arthur_nltech "Знакомьтесь, это Тэо – наш новый сотрудник, к тому же очень перспективный разработчик нейроинтерфейсов! Надеюсь, вы подружитесь, детишки!"
    harry @ arrogant "Одного сдружиться будет мало, Артур! Главное – качественно и вовремя выполнять свои задачи. "
    harry "Приятно познакомиться, я Гарри – грубо говоря, математик."
    teo "Мне тоже, поверь, свою работу я буду выполнять именно так, как ты сказал! Можно ведь обращаться на «ты?»"
    harry "Вполне."
    arthur_nltech "Итак, Тэо, ты со всеми знаком. Перед назначением твоих прямых обязанностей, в качестве первого дня предлагаю тебе подробнее разузнать о задачах каждого из твоих коллег, влиться в рабочую среду."
    arthur_nltech "К кому хочешь пойти?"

    menu:
        "К кому хочешь пойти?"

        "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
            $number_of_steps_ep3 +=1
            jump nltech_7_diana_ep3
        "Я бы хотел поговорить с Эби. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
            $number_of_steps_ep3 +=1
            jump nltech_7_aeby_ep3
        "Я бы хотел поговорить с Гарри. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
            $number_of_steps_ep3 +=1
            jump nltech_7_harry_ep3            

    return

label nltech_7_diana_ep3:
    $diana_visited_ep3 = True

    scene bg job office diana day
    with fade

    show teo normal at outofmap

    show diana normal at middlepos
    with dissolve

    teo "Добрый день еще раз! Артур отправил меня на исследования, решил заглянуть к вам. Расскажете подробнее, чем вы занимаетесь сейчас?"
    diana "Ого, ты выбрал меня, я тронута до глубины души! Как видишь, кофе я выпила, теперь в состоянии все тебе выложить"
    diana "Помимо изучения процессов, происходящих в мозге человека, я занимаюсь измерением электрической активности мозга. Например, провожу ЭЭГ – электроэнцефалографию – она, кстати, и может быть использована прямо в нейроинтерфейсах. "
    diana "Мы фиксируем то, что происходит на электроэнцефалограмме, учим алгоритм различать результаты и затем угадываем с его помощью, о чем думает испытуемый: например, о правой руке или о левой."
    teo "Над чем вы сейчас работаете?"
    diana "У нас очень много разработок, а также видов деятельности: управление нейропротезами, нейромускульная стимуляция, постинсультная реабилитация, восстановление функций мозга и сенсорных органов, общение парализованных людей без помощи голоса и рук"
    diana "Конкретно сейчас компания хочет углубиться в разработку внутренних нейроинтерфейсов, которые могли бы сыграть роль, например, в восстановлении движения людей. Не просто протезы, а именно инвазивные интерфейсы, чтобы изнутри можно было восстановить связь между нейронами!"
    teo "Да! Я рад, что именно такие интерфейсы сейчас в приоритете у вас, я бы хотел поучаствовать в разработке настолько много, насколько это возможно при моем опыте"
    diana "Может быть, все может быть!"
    teo "Кстати, крутой халат, выглядите прямо-таки серьезно!"
    diana "Спасибо-спасибо! Я-то вот ношу халат, потому что я биолог, а Артур, потому что хочет выглядеть загадочно."
    diana @ laugh "Ты не задумывался, зачем он ему вообще нужен?"
    teo "И правда, ха-ха!"
    teo "В общем, спасибо за разговор, было правда интересно узнать о вашей деятельности"

    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Эби. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
                $number_of_steps_ep3 +=1
                jump nltech_7_aeby_ep3
            "Я бы хотел поговорить с Гарри. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
                $number_of_steps_ep3 +=1
                jump nltech_7_harry_ep3 
    
    jump nltech_8_ep3
    return


label nltech_7_aeby_ep3:
    $aeby_visited_ep3 = True
    scene bg job lab2
    with fade
    
    show teo normal at outofmap

    show aeby normal at leftpos
    with easeinright

    pause(0.2)

    show aeby normal at rightpos
    with ease

    pause(0.2)

    show aeby normal at middlepos
    with ease

    teo "Ээ, Эби? Чего ты так носишься? Что-то случилось? Чем-то помочь?"
    aeby @ sad "Я очень-очень тороплюсь!!!"
    aeby "Помощь мне бы очень понадобилась, но, к сожалению, это дело я смогу завершить только сама"
    teo "А я пришел поинтересоваться, чем ты занимаешься… Может ты сможешь уделить мне минутку?"
    aeby "Так, ну я занимаюсь технической частью, в основном созданием аппаратной части устройств."
    aeby "Сейчас я пытаюсь довести до совершенства наш VR-шлем, но в перспективах у нас новый проект, подробностей не знаю, но компания хочет что-то уникальное"
    teo "Здорово, спасибо"

    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
                $number_of_steps_ep3 +=1
                jump nltech_7_diana_ep3
            "Я бы хотел поговорить с Гарри. Он отвечает за внутреннюю часть проектов, наверняка это очень сложно и интересно. Будет интересно разузнать о его деятельности.":
                $number_of_steps_ep3 +=1
                jump nltech_7_harry_ep3 
    
    jump nltech_8_ep3
    return

label nltech_7_harry_ep3:
    $mark_visited_ep3 = True
    scene bg job office mark day
    with fade

    show teo normal at outofmap

    show harry normal at middlepos
    with dissolve

    teo "Гарри, ты не сильно занят? Можно поинтересоваться, в чем заключается твоя деятельность поподробнее?"
    harry "Разве так можно, чтобы стажер в первый день просто разгуливал и спрашивал всех, кто чем занимается?"
    harry "Ладно, я постараюсь быстро ввести тебя в курс дела"
    harry "В мои задачи входит анализ сигналов в интерфейсе мозг-компьютер, декодирование сигналов активности мозга с помощью физиологически интеретируемых нейронных сетей и прочее"
    harry "Я и остальные ученые пытаемся смоделировать сложную систему работы мозга посредством простых математических моделей, хоть это и звучит странно или парадоксально"
    harry "С каждым разом мы приближаемся все больше к пониманию мозга человека, так что нам остается лишь работать и работать, пока не придем к настоящему результату"
    teo "У тебя и правда сложная работа! "
    teo "Пока в студенчестве я работал над различными проектами, иногда приходилось совмещать все сферы деятельности, так что понимаю, как это нелегко"
    harry @ smile "Действительно? Ну, я рад, обращайся если что-то нужно"
    
    if(number_of_steps_ep3<2):
        menu:
            "Куда мне сходить еще?"

            "Я бы хотел поговорить с Дианой. Будет интересно узнать о том, чем конкретно она сейчас занимается, что изучает":
                $number_of_steps_ep3+=1
                jump nltech_7_diana_ep3
            "Я бы хотел поговорить с Эби. Будет интересно узнать о технической части работы, какую разработку она сейчас ведет":
                $number_of_steps_ep3 +=1
                jump nltech_7_aeby_ep3
    
    jump nltech_8_ep3
    return

label nltech_8_ep3:
    scene bg job talkroom day
    with fade

    show teo normal at outofmap

    show arthur_nltech normal at middlepos

    teo "Долго ждете? Что-то я забегался"
    arthur_nltech @ big_smile "Надеюсь команда не держала тебя в заложниках? Ха-ха! Даже если бы долго ждал, дел всегда невпроворот и всегда есть чем заняться"
    arthur_nltech "Итак, давай обсудим твои наработки и конкретные идеи"

    if(diana_visited_ep3):
        teo "Я слышал, что у компании как раз курс на неинвазивные нейроинтерфейсы, к тому же более продвинутые, поэтому есть следующая идея"
    else:
        teo "Я слышал, что у компании как раз курс на что-то новое и уникальное, поэтому есть следующая идея"

    teo "Как насчет того, чтобы создать нейроинтерфейс, позволяющий уходить в свое «сознание», воссоздавать там свои воспоминания и прочее? В дальнейшем это можно превратить в экзокортекс, который сможет объединить сознание нескольких человек, а то и больше"
    teo "Людям, не имеющим возможности передвигаться, не обязательно будут нужны протезы или экзоскелеты"
    teo "Это будет огромный шаг в медицине, но важно правильно реализовать технологию. Вот все мои наработки, но нам нужна помощь команды в дальнейшем"
    arthur_nltech @ smile "Понял. Знаешь, отличнейшая идея! Не зря я сразу заинтересовался "
    arthur_nltech "У меня нет сомнения, что руководству это также приглянется, но все же перед презентацией мы должны максимально составить план и показать им смысл и перспективы этой разработки"
    arthur_nltech "Я посмотрю внимательно все твои записи и схемы, и затем можем приступать к работе!"
    teo "Хорошо, спасибо за доверие! Тогда, встретимся на следующей неделе?"
    arthur_nltech "Хоть каждый день! А вообще да, потому что я ничего не успеваю"
    arthur_nltech @ sad "Даже такой гениальный человек как я может быть завален кучей дел и не иметь возможности выбраться…"

    jump save_scene_ep3
    return

label save_scene_ep3:
    stop music fadeout 1.0
    $quick_menu = False
    $ renpy.block_rollback()
    scene black 
    with fade

    $ renpy.pause(0.5, hard='True')

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    show screen notify("Решения записаны...")

    $ renpy.pause(4, hard='True')

    stop sound fadeout 1.0

    $ renpy.pause(2, hard='True')

    jump episode4

    return 