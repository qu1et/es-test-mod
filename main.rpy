init:

    $ mods["prlg"]=u"Миша исследует лагерь"

    $ mhp = Character(u"Миша", color="5A9FE7", ctc="ctc_animation", ctc_position="fixed", what_color="ffdd7d", drop_shadow = [(2, 2)], drop_shadow_color = "#000", what_drop_shadow = [(2, 2)], what_drop_shadow_color = "#000")

    image josh = "mods/es-test-mod/resources/images/josh.jpg"

label prlg:
    play sound sfx_ikarus_arrive
    play sound sfx_ikarus_open_doors
    scene bg ext_bus with dissolve
    play music music_list["went_fishing_caught_a_girl"] fadein 2
    "Автобус по маршруту Щукино - Сол Волга приехал в конечный пункт"
    th "Как же я устал ехать, это было тяжелее, чем ходить по коридорам мтуси"
    mhp "Так, надо обойти всю территорию, вдруг тут спрятались партизаны с кафедры ит, ненавижу их"
    window show
    "Миша начал хаотично передвигаться между домиков"
    window hide
    scene bg ext_camp_entrance_day with dissolve
    scene bg ext_clubs_day with dissolve
    scene bg ext_dining_hall_away_day with dissolve
    scene bg ext_dining_hall_near_day  with dissolve
    scene bg ext_house_of_dv_day with dissolve
    scene josh with dspr
    scene bg ext_musclub_day with dspr
    window show
    "Прошло два часа"
    window hide
    scene bg ext_musclub_day with dissolve
    play sound sfx_dinner_jingle_speaker_tape
    "Неожиданно раздается речь и динамиков"
    mt "Мишаил ебаный рот Посохов, пройди к ебучему домику вожатой и заселись уже, заебал ходить везде"
    mhp "АААААА Я ПОНЯЛ! Здесь же надо заселяться"
    th "Но я знаю, где находится домик вожатой. Надеюсь, это не Сачивко"
    th "Пойду в обратную сторону"
    scene bg ext_clubs_day with dissolve
    mhp "О, дом! Наверное она там сидит, в клубе тусит"
    "Миша решил зайти в клубы"
    stop music fadeout 2
    play sound sfx_open_door_1
    scene black with dissolve
    th "Хм, почему-то тут пусто, может попробовать позвать"
    mhp "Извините, а я ходил, меня позвали с неба матом"
    "Послышались шаги за дверью в подсобку"
    jump gas_opening

label gas_opening:
    $ renpy.movie_cutscene("mods/es-test-mod/resources/video/vlad.ogv")


