label episode_1:
    $ renpy.block_rollback()
    scene black 
    with fade
    $ renpy.pause(0.5, hard='True')

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    scene episode1 
    with fade
    
    $ renpy.pause(4.0, hard='True')

    stop sound fadeout 1.0

    jump conference_ep1
    return

label conference_ep1:
    $ quick_menu = True
    $ renpy.block_rollback()

    scene bg conference day 
    with fade 

    play music "/audio/music/base1.ogg" fadein 1.0 volume 1.4 loop

    play sound "/audio/sfx/conference.ogg" fadein 3.0 volume 0.05 loop

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve
    
    
    teo "Мы хорошо справились, не думаешь? Нам повезло, что мы попали на эту конференцию"
    elliot "Да, но, если бы ты сразу же не запнулся в названии нашего исследования, было бы немного лучше…"
    teo "Не будь занудой. Нельзя всем понравиться! Не думаю, что это кого-то волновало, ведь дальше я вполне неплохо продолжил"
    teo "Точно неплохо же, да?"
    elliot @ smile "Для человека, которому в итоге аплодировали доктора наук, сойдет. Ну что, идем обедать?"

    menu:

        "Идем, только в темпе, у меня есть важные дела":
            stop sound fadeout 1.0
            jump cafe_ep1

        "Как нибудь в другой раз. Сегодня у Ирмы день рождение, так что сейчас я поеду в больницу":

            elliot "Как знаешь, передавай ей мои поздравления"
            stop sound fadeout 1.0
            jump street_ep1
    return
 
label cafe_ep1:
    scene bg cafe day
    with fade

    queue sound "audio/sfx/cafe.ogg" fadein 1.0 loop volume 0.2

    show teo normal at outofmap
    
    show elliot normal at middlepos
    with dissolve

    $renpy.pause(0.2)
    elliot "Чего ты так торопишься? Ешь спокойнее, дела могут и подождать, пока ты не закончишь."
    teo "Не то чтобы я тороплюсь, я же рассказывал тебе об Ирме? Она моя подруга детства и лежит в больнице уже долгое время…"
    elliot "Да, рассказывал. В чем дело, с ней что-то случилось?"
    teo "Нет, все в порядке, точнее – это явно не порядок для нее. В общем, сегодня ее день рождения, хочу навестить и поздравить"
    teo "Ты знаешь, я вижу и знаю, что каждый день для нее в больнице – пытка. Она не может больше нормально ходить, но не сдается и все остается там, пытается вылечиться, ей то ставят аппараты, то убирают."
    teo "Я бы хотел поддержать ее, помочь ей вернуться хоть на мгновение к настоящей жизни, к той, к которой она привыкла и которую потеряла"
    elliot "Ей действительно тяжело. Когда мы встретились с тобой на первом курсе, она уже лежала в стационаре..."
    elliot "Все это звучит довольно грустно. Эй, как тебе такой вариант: может я схожу с тобой поздравить ее? Я думаю, ей наскучило видеть твое унылое лицо каждый раз. Ее явно развеселит компания в моем лице!"
    teo "Кхм…не уверен"

    menu:
        "[[Согласиться](Сомневаюсь, что это хорошо отразится на его психике, но попробовать стоит. Общение с новыми людьми вряд ли ей повредит! День обещает быть веселым)":

            teo "Отлично, давай сходим вместе. Только перед этим зайдем в магазин, я, кажется, не купил подарок"

            elliot "Если ты так переживал о ее состоянии, как ты мог забыть его купить? Вечно ты со своими исследованиями зависаешь, мог бы и подумать о подруге"

            teo "Я не задумывался об этом, разве это настолько важно по сравнению с тем…"

            elliot "Как она с тобой до сих пор общается вообще?"
            stop sound fadeout 1.0
            jump shop_together_ep1

        "[[Отказаться](Ну уж нет, Ирма такая вредная, мне точно влетит за то, что я привел незнакомого ей человека, и сомневаюсь, что это хорошо отразится на его психике)":

            teo "Знаешь, я лучше один съезжу, все-таки вы незнакомы, странно будет в ее же день рождения приводить тебя, познакомлю вас в другой раз. "
            teo "Надо еще забежать в магазин, купить ей подарок"
            elliot "Как хочешь, тогда в следующий раз"
            stop sound fadeout 1.0
            jump shop_alone_ep1

    return

label street_ep1:

    scene bg street city day
    with fade

    queue sound "audio/sfx/street.ogg" fadein 1.0 loop volume 0.05

    show teo normal at outofmap

    "Всегда так морально тяжело идти к Ирме. Сегодня ведь праздник, я должен взбодрить ее, но этого все равно недостаточно."
    "Она лежит в больнице так долго, что я уже еле вспоминаю те времена, когда она жила обычной жизнью. "
    "Ее мечты стать футболисткой вдребезги разбились из-за травмы ног, и кажется, что надежды уже нет: ей то ставят аппараты, то убирают, но ничего не меняется."
    "Она прекрасно держится, вполне себе жизнерадостна, но я ведь ее знаю – эта жизнь сейчас для нее невыносима"
    "Возможно ли помочь ей вернуться к прежней жизни хоть ненадолго?"
    stop sound fadeout 1.0
    jump shop_alone_ep1

    return 

label shop_together_ep1:
    scene bg shop day 
    with fade 

    queue sound "audio/sfx/shop.ogg" fadein 1.0 loop volume 0.05

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    teo "Tаак… понятия не имею, что выбрать. Наверное, над идеальным подарком мне стоило задуматься намного раньше"
    elliot "Здравая мысль в твоей умной голове возникла поздновато! Надеюсь, что в твою гениальную дырявенькую голову придет какая-то стоящая идея, иначе она обидится. "
    elliot "Ну, я бы на ее месте точно обиделся"
    teo "Логично, что ж, давай посмотрим, что тут есть"

    menu:
        "[[Любимый торт Ирмы](Вкусное воспоминание из прошлого. Раньше Ирма часто ела его. Она до сих пор обожает этот десерт)":
            $gift_to_irma_ep1 = 1

            elliot "Торт? Ты уверен?"

        "[[Букет цветов с открыткой](Хороший же подарок? Кажется, флорист составила композицию на языке цветов. Какой смысл в букете? Жаль, что я в этом не разбираюсь…)":
            $gift_to_irma_ep1 = 2

            elliot @ smile "Симпатичный веник!"
            teo "В тебе никакого чувства эстетики!"

        "[[Футболка с забавной зверюшкой](Ей либо понравится, либо она швырнет в меня этим, в любом случае это лучше, чем просто принести свою одинокую тушку…)":
            $gift_to_irma_ep1 = 3

            elliot "Зря ты это взял…"
            teo "Почему? Забавно же"
            elliot "Поговорим об этом, когда она это увидит… Будь я на ее месте - убил бы тебя."
    stop sound fadeout 1.0
    jump hospital_hallway_together_ep1

    return


label shop_alone_ep1:
    scene bg shop day 
    with fade 

    queue sound "audio/sfx/shop.ogg" fadein 1.0 loop volume 0.05

    show teo normal at outofmap

    "Какой подарок купить человеку, который потерял интерес к жизни? "
    "Хороший вопрос…"

    menu:
        "[[Любимый торт Ирмы](Вкусное воспоминание из прошлого. Раньше Ирма часто ела его. Она до сих пор обожает этот десерт)":
            $gift_to_irma_ep1 = 1
        "[[Букет цветов с открыткой](Хороший же подарок? Кажется, флорист составила композицию на языке цветов. Какой смысл в букете? Жаль, что я в этом не разбираюсь…)":
            $gift_to_irma_ep1 = 2
        "[[Футболка с забавной зверюшкой](Ей либо понравится, либо она швырнет в меня этим, в любом случае это лучше, чем просто принести свою одинокую тушку…)":
            $gift_to_irma_ep1 = 3
    stop sound fadeout 1.0
    jump hospital_hallway_alone_ep1

    return   

label hospital_hallway_together_ep1:
    scene bg hospital hallway day
    with fade

    stop music fadeout 2.0

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    teo "Мы пришли, вот ее палата. В общем, если она вдруг скажет что-то странное, не волнуйся – она всегда так себя ведет, она очень… доброжелательная на самом-то деле"
    elliot "Звучит пугающе…"

    jump hospital_ward_with_E_ep1

    return


label hospital_hallway_alone_ep1:
    scene bg hospital hallway day
    with fade

    stop music fadeout 2.0

    show teo normal at outofmap

    teo "Так, так, так… Надо собраться! Сейчас бодренько захожу и дарю ей подарок…"

    jump hospital_ward_ep1

    return 

label hospital_ward_with_E_ep1:
    $elliot_and_irma_met = True

    scene bg hospital ward
    with fade

    play music "/audio/music/base1.ogg" fadein 1.0 volume 1.0 loop
    
    show teo normal at outofmap

    show elliot normal at rightpos
    with dissolve

    show irma normal at leftpos
    with dissolve

    teo "Ирма, поздравляю тебя с твоим днем рождения!"
    irma @ smile "Ого! Неужели ты пришел…и не один? " 
    teo "Да, я подумал так будет веселее. Знакомься, это Эллиот – мой друг и бывший однокурсник, все важные проекты мы делаем вместе"
    elliot @ smile "Приятно познакомиться, я Эллиот. Поздравляю тебя с днем рождения!"
    irma "Спасибо, спасибо…Тэо, да ты меня прямо удивляешь, привел мне компанию, как будто мне тебя недостаточно!! "
    irma @ smile"Ахах, не знала, что у тебя прямо друзья есть"
    teo "Представляешь, есть!"
    elliot "Я, кажется, понял, о чем ты говорил ранее"
    irma "М? О чем вы?"
    teo "Неважно, я, между прочим, купил тебе подарок. Давай открывай"

    if gift_to_irma_ep1 == 1:
        irma @ smile"Мой любимый торт!! "
        irma "Хоть какая-то польза от тебя! Неужели в кои-то веки не придется есть больничную отраву. "
        irma "Я прощаю тебе твое нелепое поздравление и, так уж и быть, поделюсь кусочком"
        teo "Ты же не собираешься питаться несколько дней одним тортом? Я пробовал здесь еду пару раз, не такая уж и отрава"
        irma "А ты попробуй есть это каждый день своей жизни, так что да – пока есть возможность, буду питаться тортом!! "
        irma "Кстати, готова поделиться с твоим другом, он хотя бы не ведет себя как ты."

    elif gift_to_irma_ep1 == 2:
        irma @ sad "Букет подснежников?"
        irma "Тот, кто собирал его, кажется знал, какой смысл нужно вложить… "
        irma "О, тут еще открытка? Продолжаешь меня удивлять сегодня, надеюсь там не признание в любви?"
        "Смысл?...Кажется, я сделал что-то не так"
        teo "Если так переживаешь, то проверь открытку прямо сейчас"
        irma "Нет, ты что! Твои сокровенные мысли я прочитаю после твоего ухода, не будем смущать людей вокруг"
        elliot @ smile "Тэо, не знал, что ты успел написать в открытке мемуары, пока был в магазине! Да ты у нас талант!!"
        teo "Кажется, это коллективное издевательство надо мной"
    
    elif gift_to_irma_ep1 == 3:
        irma @ confused "Так, давай откроем. У меня нет слов… Это… что?!"
        teo "О, я рад, что тебе понравился мой подарок!"
        irma "То есть, с прошлого года, когда ты подарил мне носки, ты ничего не усвоил? "
        irma @ tricky "Ладно, поговорим об этом после, я тебе все выскажу о том, как сильно мне нравится эта чудо-футболка"
        elliot "А я же говорил…Зря ты купил это."
        irma "Ну, в этот раз хотя бы не носки!"

    elliot "Так, давайте вы прекратите ваши жужжания, и мы, например, поговорим"
    irma @ tricky "Отличная идея! Я обожаю разговаривать с людьми, у меня здорово получается, не так ли?"
    teo "Да-да…"
    elliot "Как вы вообще познакомились? Долго дружите?"
    teo "Лет с пяти-шести? О, а история знакомства что ни на есть показательная"
    irma "Обожаю вспоминать это!! Я пнула футбольный мяч на поле, и он совершенно случайно прилетел какому-то ребенку в лицо, угадайте кто же это оказался?"
    elliot @ smile "Ахах, верно сказано, что история показательная!"
    teo "Тебе, Ирма, доставляет удовольствие рассказывать это, но я не сломаюсь, так и знай!"
    
    jump street2_together_ep1

    return

label hospital_ward_ep1: 
    $elliot_and_irma_met = False

    scene bg hospital ward
    with fade
    
    play music "/audio/music/base1.ogg" fadein 1.0 volume 1.0 loop

    show teo normal at outofmap

    show irma normal at middlepos
    with dissolve

    teo "Привет-привет !! Ирма, поздравляю тебя с твоим днем рождения!"
    irma "Вау, наконец-то пришел мой единственный и неповторимый!"
    irma "Неужели помнишь? Поставил себе напоминание, а не как в прошлом году?"
    teo "Я желаю тебе, чтобы с этого момента, с этого дня рождения, твоя жизнь начала двигаться вперед, и ты стала счастливой Ирмой"
    irma "Спасибо…мне приятно, но ты же знаешь, что это невозможно. Моя язвительность, как и мои проблемы никуда не денутся, умник."
    teo "Хватит нудеть. В наших силах все изменить. Кстати, я принес тебе небольшой подарок"

    if gift_to_irma_ep1 == 1:
        irma @ smile"Мой любимый торт!! "
        irma "Хоть какая-то польза от тебя! Неужели в кои-то веки не придется есть больничную отраву. "
        irma "Я прощаю тебе твое нелепое поздравление и, так уж и быть, поделюсь кусочком"
        teo "Сама щедрость! Не жадничай, в конце концов ты же не собираешься питаться несколько дней одним тортом? "
        teo "Я пробовал здесь еду пару раз, не такая уж и отрава. "
        teo "(шепотом) По крайней мере всяко лучше, чем когда готовишь ты "
        irma "Чего, чего? А ты попробуй есть это каждый день своей жизни, так что да – пока есть возможность, буду питаться тортом!!"
        irma @ angry "И не так уж плохо я готовлю…"

    elif gift_to_irma_ep1 == 2:
        irma @ sad "Букет подснежников?"
        irma "Тот, кто собирал его, кажется знал, какой смысл нужно вложить… "
        irma "О, тут еще открытка? Продолжаешь меня удивлять сегодня, надеюсь там не признание в любви?"
        "Смысл?...Кажется, я сделал что-то не так"
        teo "Если так переживаешь, то проверь открытку прямо сейчас"
        irma "Нет, ты что! Твои сокровенные мысли я прочитаю после твоего ухода, вдруг ты расплачешься…"
    
    elif gift_to_irma_ep1 == 3:
        irma @ confused "Так, давай откроем. У меня нет слов… Это… что?!"
        teo "О, я рад, что тебе понравился мой подарок!"
        irma "Ты издеваешься надо мной? Я не понимаю, откуда у тебя берутся подобные идеи. "
        irma @ angry"Это же полный абсурд! В прошлом году ты вообще подарил мне стремные носки!!!"
        teo "Ахах, ну Ирма, не злись ты так – я всего лишь хотел купить забавный подарок"
        irma @ smile "Посмотрим, как тебе будет забавно, когда ты откроешь подарок от меня на свой день рождения"
    
    stop music fadeout 5.0
    teo "Мы давно не общались, ты не звонишь… Занимаешься чем-нибудь последнее время?"
    irma "Эм, нет…Вот бы было легко найти себе новые интересы, кажется для меня это сложновато – у меня ни к чему не лежит душа"
    queue music "/audio/music/irma_sad.ogg" fadein 1.0 volume 0.6 loop
    irma sad "В смысле, я не просто лежу целыми днями, я пытаюсь чем-то заниматься, но все не то, понимаешь?"
    irma "Я даже начинала осваивать новую профессию. Возможно ты считаешь, что я просто не хочу, но это не так! Я люблю учиться, ты же знаешь… "
    irma "Но это все мне не подходит."
    irma "И…я хочу сказать, что несмотря на мое поведение, я правда ценю, что ты пришел… Ты же знаешь, да?"
    irma "Даже мои родители не рядом со мной в этот день, как всегда заняты. "
    irma "Раньше меня это не так смущало, ведь я не была здесь и не была в таком состоянии, но сейчас это ощущается совсем по-другому."
    irma "Думаю, им самим надоело видеть меня такую каждый день. Именно поэтому они ушли."
    teo "Я в любой момент могу прийти к тебе на помощь, но…"
    irma "Я знаю, я прекрасно знаю, что не могу отпустить прошлое! "
    irma "Но как я должна отпустить его, ни разу ни имея шанса хоть на секунду вернуться в то время, когда я могла мечтать, могла заниматься футболом? "
    irma crying2 "Всего лишь на мгновение…"
    teo "Если бы была возможность «хоть на секунду» вернуться в прошлое, сделала бы это?"
    irma crying2 "Конечно, я бы рискнула всем! Но о чем ты? Это же невозможно, я не хочу тешить себя глупыми мечтами."

    jump street2_alone_ep1

    return 

label street2_together_ep1:
    scene bg street city evening
    with fade

    play sound "audio/sfx/street.ogg" fadein 2.0 loop volume 0.15

    show teo normal at outofmap

    show elliot normal at middlepos
    with dissolve

    teo "Не знаю, что делать…"
    elliot "О чем ты? Ирма кажется очень даже веселой"
    teo "Это не так. Да, ее характер сам по себе такой, но сейчас она совсем не в духе"
    teo "Я бы хотел, чтобы у нее появилась возможность хоть на мгновение вернуться к тому, что ее когда-то радовало, перед тем, как отпустить это навсегда…"
    teo "Она должна двигаться вперед, и я знаю это, но так больно осознавать, что для нее это буквально разрушение ее привычного мира"
    elliot "Слушай, это ведь исполнимо. Вспомни свою цель и кем ты хочешь быть, разве это не в твоих возможностях?"
    elliot "Ты можешь разработать то, что хоть на немного вернет ее в ту реальность, в которой она жила раньше."
    teo "Ты имеешь ввиду…"
    elliot "Да, именно это. Все это время ты учился на разработчика нейроинтерфейсов, развивался в этой сфере, и я был с тобой во всех проектах, поэтому знаю, на что ты способен"
    teo "Я не думал об этом в таком ключе, но, кажется, понял мысль. Мне нужно все обдумать, у меня есть идея, но все нужно просчитать"
    elliot "Тебя все еще не пригласили на собеседование в компанию?"
    teo "Отправил резюме в две компании, но пока ни одна не ответила. Хотелось бы сходить на собеседование в каждую"
    elliot "Интересно, столкнешься ли ты там с моим двоюродным дядей…"
    teo "Что? Почему я должен с ним столкнуться?"
    elliot "Он главный разработчик компании, немного чудаковатый, хотя я уверен, что именно такой человек нужен, чтобы создать что-то новое"
    teo "Ты никогда не рассказывал мне об этом?! И в какой именно компании?"
    elliot "Оставлю это в секрете, пока не определишься, в какую именно захочешь пойти! Могу попросить его быстрее принять тебя"
    teo "Честно, я немного шокирован тем, что у тебя столько тайн…Я ценю твою помощь, но я бы не хотел опираться на знакомства при устройстве в компанию, в которую действительно желаю попасть"
    elliot @ smile "Я лишь попрошу его поскорее принять тебя на собеседование, не волнуйся. К тому же, я уверен, что ты идеальный кандидат, да ты и сам это знаешь "
    teo "Ладно, спасибо, друг, посмотрим, во что все это выльется…"

    stop sound fadeout 2.0

    jump room_ending2_ep1

    return

label street2_alone_ep1:
    scene bg street city evening
    with fade

    play sound "audio/sfx/street.ogg" fadein 3.0 loop volume 0.15 

    show teo normal at outofmap
    
    "Перед тем, как начать новую жизнь, она просто хочет еще раз испытать счастливые моменты прошлого. Это не дает ей покоя все это время…"
    "Она важна для меня. У меня сердце разрывается, когда я вижу ее в таком состоянии, я должен придумать, как ей помочь. Так больше не может продолжаться."
    "О, кажется, мне пришли письма с приглашением на собеседование"

    stop music fadeout 3.0

    "Что…Почему собеседование в VRHere и NL Technology в один день? Да еще и с промежутком в час… Я смогу успеть только в одно место!"
    "Видимо, это момент выбрать, к какой сфере моя душа лежит больше… По крайней мере, если меня точно примут, то именно там я буду работать еще долгое время"

    menu:
        "Пойду на собеседование в VRHere. Все-таки, тема виртуальной реальности наиболее интересна для меня. Здесь я смогу дать волю своей фантазии и создать что-то действительно стоящее.":
            $company_chosen_ep1 = 1

            jump vrhere_ep1

        "Пойду на собеседование в NL Technology. Я хочу помогать людям с ограниченными возможностями, возвращать их к полноценной жизни. Это действительно моя стезя.":
            $company_chosen_ep1 = 2  

            jump nl_tech_ep1
    
    return
    
label vrhere_ep1:

    stop sound fadeout 2.0
    stop music fadeout 2.0

    queue music "/audio/music/company_base.ogg" fadein 2.0 volume 0.6 loop
    
    scene bg job big evening
    with fade

    show teo normal at outofmap

    "Моя самая большая цель теперь – попасть сюда."
    "Я уверен, возможности человека можно расширить в обеих реальностях. "
    "И именно благодаря технологии нейроинтерфейсов сфера VR продвинется далеко вперед, ведь управление силой мысли обеспечит людям полный спектр погружения: чувства, запахи, вкусы, тактильные ощущения"
    "О, и еще мне кажется отличной идеей возможность создать реальность под себя, связанную со своими воспоминаниями, местами, атмосферой…"
    "Свое окружение? Своя реальность? Это…это то, что нужно…Так, мне срочно надо записать это!"

    show arthur_vrhere_hidden normal at middlepos
    with dissolve

    arthur_vrhere_hidden "Молодой человек?"

    jump near_job_ep1

    return

label nl_tech_ep1:

    stop sound fadeout 2.0
    stop music fadeout 2.0

    play music "/audio/music/company_base.ogg" fadein 1.0 volume 0.6 loop

    scene bg job small evening
    with fade

    show teo normal at outofmap

    "Моя самая большая цель теперь – попасть сюда."
    "Я уверен, люди с ограниченными возможностями имеют шанс на полноценную жизнь. И именно благодаря технологии нейроинтерфейсов"
    "Нейропротезы смогут восстановить передачу сигналов в разных участках организма. Таким образом можно будет восстановить и слух, и зрение, и память, и осязание…"
    "И… Ирма смогла бы снова играть в футбол? Точно…Она бы точно смогла! Так, мне срочно нужно записать это!"
    
    show arthur_nltech_hidden normal at middlepos
    with dissolve

    arthur_nltech_hidden "Молодой человек?"

    jump near_job_ep1

    return

label near_job_ep1:

    menu:
        "[[Уйти](Боже, это, вероятно, странно, что я уже час стою напротив компании. Нужно уходить.)":
            $company_feedback_ep1 = False

            if( company_chosen_ep1 == 1):
                arthur_vrhere_hidden @ smile "Кажется, испугался…"
            else:
                arthur_nltech_hidden @ smile "Кажется, испугался…"
            
        "[[Откликнуться](Кто это? Какой-то мужчина в халате…Он работает там? Надеюсь, меня сейчас не прогонят за то, что я стою около входа)":
            $company_feedback_ep1 = True

            teo "Да, что такое?"
            if( company_chosen_ep1 == 1):
                arthur_vrhere_hidden "Я вас знаю, случайно ли не хотите пройти со мной? Мы могли бы обсудить нынешнее положение дел"
            else:
                arthur_nltech_hidden "Я вас знаю, случайно ли не хотите пройти со мной? Мы могли бы обсудить нынешнее положение дел"

            "Что за ненормальные тут шатаются… Какой-то странный дед. Он уж точно не сможет мне помочь"
            teo "Аа… извините, я пойду"

    stop music fadeout 2.0
    jump room_ending1_ep1 

    return 

label room_ending1_ep1:
    scene bg room evening
    with fade

    show teo normal at outofmap

    "Я понял, что должен сделать. "
    "Пока меня не пригласили на собеседование, разработаю концепцию проекта, а после я добьюсь того, что начну работать над ним. "
    "Ради Ирмы."

    jump save_scene_ep1
    
    return 
label room_ending2_ep1:
    scene bg room evening
    with fade

    show teo normal at outofmap

    "О, кажется, мне пришли письма с приглашением на собеседование"
    "Что…Почему собеседование в VRHere и NL Technology в один день?"
    "Да еще и с промежутком в час…Я смогу успеть только в одно место!" 
    "Видимо, это момент выбрать, к какой сфере моя душа лежит больше…по крайней мере, если меня точно примут, то именно там я буду работать еще долгое время"

    menu:

        "(Пойду на собеседование в VRHere. Все-таки, тема виртуальной реальности наиболее интересна для меня. Здесь я смогу дать волю своей фантазии и создать что-то действительно стоящее.)":
            $company_chosen_ep1 = 1
        "(Пойду на собеседование в NL Technology. Я хочу помогать людям с ограниченными возможностями, возвращать их к полноценной жизни. Это действительно моя стезя.)":
            $company_chosen_ep1 = 2  

    "Что ж, раз я определился, то стоит позвонить Эллиоту" 

    scene bg room evening
    with fade

    show teo normal at outofmap

    elliot "Неужели? Тебе очень повезло, ведь ты встретишься с моим дорогим дядей! Ну что, мне стоит позвонить ему?"
    teo "Нет, не нужно, все равно это уже скоро. Буду смиренно ждать и готовиться!"
    elliot "Тогда я думаю, что мы могли бы после твоего собеседования обсудить с ним некоторые идеи?"
    teo "Да, было бы неплохо!"

    $company_with_E_ep1 = True
    jump save_scene_ep1
    return


label save_scene_ep1:
    $ quick_menu = False
    $ renpy.block_rollback()
    scene black 
    with fade
    
    stop sound fadeout 0.2
    stop music fadeout 0.2

    $ renpy.pause(0.5, hard='True')

    play sound "/audio/episode/episode_sound.ogg" fadein 1.0

    show screen notify("Решения записаны...")

    $ renpy.pause(4, hard='True')

    stop sound fadeout 1.0

    $ renpy.pause(2, hard='True')

    jump episode2

    return 

