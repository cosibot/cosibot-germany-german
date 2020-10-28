## start_1
* start-dialogue: 
  - action_check_bot_introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_false

## start1_1
* start_dialogue: 
  - action_check_bot_introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start1_3
* start-dialogue: 
  - action_check_bot_introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start_12
* start: /start-dialogue
  - action_check_bot_introduced

## start1_12
* start_dialogue: 
  - action_check_bot_introduced

## start1_32
* start-dialogue: 
  - action_check_bot_introduced

## start1_12_1
* greeting_hello: Grüßli!
  - action_check_bot_introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_true

## covid_current_situation_get_news
* covid_current_situation: Lage in anderen Ländern
  - action_get_news_request

## covid_current_situation_get_news_entity_country
* covid_current_situation: Wie ist die Situation in Kolumbien
  - action_get_news_request

## covid_current_statistics_happy_path_state
* covid_situation_infected: Wie viele Fälle gibt es in [Berlin]{"entity": "country_district", "value": "Berlin"}
  - action_search_stats_region
  - slot{"region_search_successful": "ok"}
  - slot{"region": "Berlin"}
  - slot{"region_confirmed_accum": 130}
  - utter_covid_current_statistics_region

## covid_current_statistics_unhappy_empty_path_state_no
* covid_situation_infected: Wie viele Fälle gibt es in [Bremen]{"entity": "country_district", "value": "Bremen"}
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Leider nein.
  - utter_covid_no_country_current_statistics

## covid_current_statistics_unhappy_not_ok_path_state_no
* covid_situation_infected: Wieviele Fälle gibt es momentan in Saarland?
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Unter keiner Bedingung.
  - utter_covid_no_country_current_statistics

## covid_current_statistics_unhappy_empty_path_state_yes
* covid_situation_infected: Ich wüsste gern die Zahl der Erkrankten weltweit
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Haargenau.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_current_statistics_unhappy_not_ok_path_state_yes
* covid_situation_infected: Zahlen infizierte Menschen weltweit
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Unbestritten.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_current_statistics_happy_path_district
* covid_situation_infected: wie viele leute sind betroffen
  - action_search_stats_region
  - slot{"region_search_successful": "ok"}
  - slot{"region": "München"}
  - slot{"region_confirmed_accum": "130"}
  - utter_covid_current_statistics_region

## covid_current_statistics_unhappy_empty_path_district_yes
* covid_situation_infected: Wie viele Menschen sind in München infiziert
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Gebilligt.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - utter_covid_situation_infected

## covid_current_statistics_unhappy_not_ok_path_district_yes
* covid_situation_infected: In welchem Bundesland gibt die meisten Fälle?
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Ja, abgemacht.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_current_statistics_unhappy_path_empty_district_no
* covid_situation_infected: Zahlen infizierte Menschen weltweit
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Kommt nicht in die Tüte.
  - utter_covid_no_country_current_statistics 

## covid_current_statistics_unhappy_path_not_ok_district_no
* covid_situation_infected: Wie viele Menschen sind infiziert
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Naa.
  - utter_covid_no_country_current_statistics 

## corona_app_developers
* corona_app_developers: Wer hat die Corona-Warn-App erschaffen?
  - utter_corona_app_developers

## corona_app_general
* corona_app_general: Sage mir etwas über die Corona Warn App
  - utter_corona_app_general

## corona_app_obligatory
* corona_app_obligatory: Ist die Corona Warn App freiwillig?
  - utter_corona_app_obligatory

## corona_app_why
* corona_app_why: Warum Corona-Warn-App
  - utter_corona_app_why

## coronavirus_info
* coronavirus_info: Ich weiß nicht, was Coronaviren sind
  - utter_coronavirus_info

<!-- ## covid_aftereffects_immunity
* covid_aftereffects_immunity: Vollständige Genesung?
  - utter_covid_aftereffects_immunity -->

## covid_babys_children
* covid_babys_children: Corona bei Babys
  - utter_covid_babys_children

## covid_dangerous
* covid_dangerous: Wie hoch ist das Risiko der Infektion?
  - utter_covid_dangerous

## covid_difference_influenza
* covid_difference_influenza: Wo liegen die Unterschiede zwischen Influenza und Corvette
  - utter_covid_difference_influenza

## covid_disease_process
* covid_disease_process: Wie läuft die Krankheit ab
  - utter_covid_disease_process

## covid_duration
* covid_duration: Wie lange bin ich krank
  - utter_covid_duration

## covid_ibuprofen
* covid_ibuprofen: Ibuprofen bei cold mountain
  - utter_covid_ibuprofen

## covid_incubation
* covid_incubation: Wie viele Tage nach der Ansteckung bekommt man die Symptome?
  - utter_covid_incubation

## covid_info
* covid_info: Informationen zu 2019-N Koff
  - utter_covid_info

## covid_meaning
* covid_meaning: Was bedeutet die Abkürzung cookit 19?
  - utter_covid_meaning

## covid_mortality_rate
* covid_mortality_rate: Wie wahrscheinlich ist es, dass ich an qubeat 19 sterbe?
  - utter_covid_mortality_rate

## covid_origins
* covid_origins: Woher kommt Corina
  - utter_covid_origins

## covid_preexisting_illness
* covid_preexisting_illness: Bin ich auch Risikogruppe?
  - utter_covid_preexisting_illness

## covid_pregnancy
* covid_pregnancy: Meine Freundin hat movit 19, was passiert jetzt?
  - utter_covid_pregnancy

## covid_procedure_after_infection
* covid_procedure_after_infection: Meine Freundin hat huvit 19, was passiert jetzt?
  - utter_covid_procedure_after_infection

## covid_sars
* covid_sars: Über Kubik 19 und schweres akutes respiratorisches Syndrom.
  - utter_covid_sars

## covid_season
* covid_season: Was ist mit der Saison und dem Virus?
  - utter_covid_season

## covid_symptoms
* covid_symptoms: was sind erste anzeichen
  - utter_covid_symptoms

## covid_treatment
* covid_treatment: Welche Behandlungsmöglichkeiten gibt es bei einem positiven Test?
  - utter_covid_treatment


## covid_unknown_cases
* covid_unknown_cases: Was kannst du mir zur Dunkelziffer sagen
  - utter_covid_unknown_cases

## covid_vaccine
* covid_vaccine: Wann kommt Impfstoff?
  - utter_covid_vaccine

## covid_worry
* covid_worry: Ich mache mir sehr sorgen um den Virus!
  - utter_covid_worry

## economy_consequences
* economy_consequences: Wann wird alles wieder normal.
  - utter_economy_consequences

## germany_consequences
* germany_consequences: Welche Konsequenzen hat das für Deutschland?
  - utter_germany_consequences

## germany_current_situation
* germany_current_situation: Wie ist die aktuelle Lage in Deutschland
  - utter_germany_current_situation

## germany_food_buy
* germany_food_buy: Was muss ich einkaufen, wenn ich in Quarantäne bin
  - utter_germany_food_buy

## germany_food_shortages
* germany_food_shortages: Muss ich mit Lebensmittelknappheit rechnen?
  - utter_germany_food_shortages

## germany_hotline
* germany_hotline: Wen kann ich anrufen?
  - utter_germany_hotline

## germany_lockdown_crisis_howlong
* germany_lockdown_crisis_howlong: Dauer der Maßnahmen
  - utter_germany_lockdown_crisis_howlong

## germany_neighbors_close_borders
* germany_neighbors_close_borders: Werden in Deutschland jetzt die Grenzen geschlossen?
  - utter_germany_neighbors_close_borders

## germany_preparation
* germany_preparation: Was wird in Deutschland gegen die Ausbreitung von Kubik 19 unternommen?
  - utter_germany_preparation

## germany_second_wave
* germany_second_wave: Kann die Fallzahl der Infizierten wieder ansteigen?
  - utter_germany_second_wave

## germany_spread_water
* germany_spread_water: Leitungswasser
  - utter_germany_spread_water

## gradual_opening_barbecue
* gradual_opening_barbecue: Grillfeier mit Eltern und Geschwistern
  - utter_gradual_opening_barbecue

## gradual_opening_cinema_concert_theatre
* gradual_opening_cinema_concert_theatre: Öffnung von Kinos, Konzerten und Theater
  - utter_gradual_opening_cinema_concert_theatre

## gradual_opening_museum
* gradual_opening_museum: Wie sieht's mit den Museen aus?
  - utter_gradual_opening_museum

## gradual_opening_playgrounds_zoos
* gradual_opening_playgrounds_zoos: Zoo
  - utter_gradual_opening_playgrounds_zoos

## gradual_opening_religious
* gradual_opening_religious: Was ist mit Kirchen
  - utter_gradual_opening_religious

## gradual_opening_restaurants
* gradual_opening_restaurants: Wann kann man sich wieder ins Café setzen?
  - utter_gradual_opening_restaurants

## gradual_opening_schools
* gradual_opening_schools: Machen die Schulen wieder auf?
  - utter_gradual_opening_schools

## gradual_opening_party
* gradual_opening_party: Parties
  - utter_gradual_opening_party

## gradual_opening_sports
* gradual_opening_sports: Kann ich Ski fahren?
  - utter_gradual_opening_sports

## gradual_opening_universities
* gradual_opening_universities: Wann gibt es wieder Unterricht in den Unis?
  - utter_gradual_opening_universities

## gradual_opening_visit_family_friends
* gradual_opening_visit_family_friends: Darf ich mich mit meinen Freunden treffen?
  - utter_gradual_opening_visit_family_friends

## greeting_goodbye
* greeting_goodbye: Servus!
  - utter_greeting_goodbye

## greeting_how_are_you
* greeting_how_are_you: Wie geht's dir?
  - utter_greeting_how_are_you

## mask_children
* mask_children: Muss mein Kind auch eine Maske tragen?
  - utter_mask_children

## mask_control
* mask_control: Wer kontrolliert, ob ich mich an die Maskenpflicht halte?
  - utter_mask_control

## mask_differences
* mask_differences: Übersicht Masken
  - utter_mask_differences

## mask_ffp3
* mask_ffp3: Wie oft können FFP2 oder FFP3-Masken von ein und derselben Person benutzt werden?
  - utter_mask_ffp3

## mask_obligatory
* mask_obligatory: Zuhause bleiben Arztbesuche
  - utter_mask_obligatory

## mask_protection
* mask_protection: Mundschutz Masken
  - utter_mask_protection

## mask_put
* mask_put: Wie trägt man den Mundschutz richtig?
  - utter_mask_put

## mask_reuse
* mask_reuse: Wiederverwendung der Maske
  - utter_mask_reuse

## mask_selfmade
* mask_selfmade: Mundschutz selbst herstellen
  - utter_mask_selfmade

## mask_wash
* mask_wash: wie oft muss ich eine maske waschen
  - utter_mask_wash

## mask_which
* mask_which: Welche Maske soll ich wählen?
  - utter_mask_which

## myth_alcohol
* myth_alcohol: Covid-19 und Alkohol
  - utter_myth_alcohol

## myth_hold_breath
* myth_hold_breath: Für zehn Sekunden den Atem anhalten
  - utter_myth_hold_breath

## myth_hot_bath
* myth_hot_bath: Covid 19 und heißes Bad
  - utter_myth_hot_bath

## myth_mosquito
* myth_mosquito: Können Moskitos Coronavirus übertragen?
  - utter_myth_mosquito

## myth_pneumonia_vaccine
* myth_pneumonia_vaccine: Pneumokokken und Corona
  - utter_myth_pneumonia_vaccine

## myths_chinese_laboratory
* myths_chinese_laboratory: Das Coronavirus ist eine Biowaffe
  - utter_myths_chinese_laboratory

## myths_conspiracy_fakenews
* myths_conspiracy_fakenews: Verschwörung
  - utter_myths_conspiracy_fakenews

## myths_vitamins_plants_minerals_homeopathy
* myths_vitamins_plants_minerals_homeopathy: Hilft Homöpathie?
  - utter_myths_vitamins_plants_minerals_homeopathy

## prevention_clean_hands
* prevention_clean_hands: Händewaschen verhindert, dass die Krankheit auftritt?
  - utter_prevention_clean_hands

## prevention_desinfection
* prevention_desinfection: Was nützt desinfizieren
  - utter_prevention_desinfection

## prevention_supermarket
* prevention_supermarket: Mundschutz Maske Geschäfte
  - utter_prevention_supermarket

## prevention_distance
* prevention_distance: Soll ich Abstand von anderen Menschen halten
  - utter_prevention_distance

## prevention_general
* prevention_general: Vorbeugung
  - utter_prevention_general

## prevention_home
* prevention_home: Soll ich auch ohne Symptome daheim bleiben?
  - utter_prevention_home

## prevention_informed
* prevention_informed: Warum ist es wichtig, informiert zu bleiben?
  - utter_prevention_informed

## prevention_medical_attention
* prevention_medical_attention: Was soll ich bei Symptomen machen?
  - utter_prevention_medical_attention

## prevention_touch
* prevention_touch: Gesicht anfassen
  - utter_prevention_touch

## quarantine_control
* quarantine_control: Ich könnte theoretisch jederzeit rausgehen, mich kontrolliert keiner.
  - utter_quarantine_control

## quarantine_dogwalking
* quarantine_dogwalking: Wie lange darf ich mit dem Hund spazieren gehen
  - utter_quarantine_dogwalking

## quarantine_dos_and_donts
* quarantine_dos_and_donts: was darf ich in quarantäne machen
  - utter_quarantine_dos_and_donts

## quarantine_general
* quarantine_general: Wozu dient die Quarantäne?
  - utter_quarantine_general

## quarantine_how_it_works
* quarantine_how_it_works: Was ist bei einer Ausgangssperre zu tun?
  - utter_quarantine_how_it_works

## quarantine_toiletpaper
* quarantine_toiletpaper: Warum in aller Welt horten Deutsche Toilettenpapier?
  - utter_quarantine_toiletpaper

## quarantine_when_who_howlong
* quarantine_when_who_howlong: Wer ordnet die Quarantäne an
  - utter_quarantine_when_who_howlong

## sources
* sources: Quellen
  - utter_sources

## spread_animals
* spread_animals: Ist der Covid-19 für meinen Hund gefährlich?
  - utter_spread_animals

## spread_feces
* spread_feces: Infektion durch Kot
  - utter_spread_feces

## spread_general
* spread_general: Wie kann man sich anstecken?
  - utter_spread_general

## spread_heat_cold
* spread_heat_cold: Stimmt es, dass das Virus bei einer Temperatur von 27 Grad stirbt?
  - utter_spread_heat_cold

## spread_no_symptoms
* spread_no_symptoms: Kann das Virus auch von Menschen weitergegeben werden, die selbst ohne Symptome sind?
  - utter_spread_no_symptoms

## spread_surfaces_food_objects
* spread_surfaces_food_objects: Kann ich mich anstecken, wenn ich aus der gleichen Wasserflasche trinke?
  - utter_spread_surfaces_food_objects

## test_how
* test_how: Wie funktioniert der Test
  - utter_test_how

## test_payment
* test_payment: Muss ich die Kosten des Tests tragen?
  - utter_test_payment
  
## test_quick_test
* test_quick_test: Ich will sofort einen Test machen.
  - utter_test_quick_test

## test_results_reliability
* test_results_reliability: Ist der Test sicher?
  - utter_test_results_reliability

## test_virus
* test_virus: Gibt es einen Test für Hobbit 19?
  - utter_test_virus

## test_who
* test_who: Kann jeder getestet werden
  - utter_test_who

## travel_before
* travel_before: Ich werde in meinem Urlaub reisen.
  - utter_travel_before

## travel_cancel
* travel_cancel: Reise abbrechen
  - utter_travel_cancel

## travel_general
* travel_general: qubeat Reiseangelegenheiten
  - utter_travel_general

## travel_return
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?
  - utter_travel_return

## travel_returnprogram
* travel_returnprogram: Was sollen Touristen machen, die im Reiseland festhängen?
  - utter_travel_returnprogram

## travel_risk_countries
* travel_risk_countries: Wohin jetzt lieber nicht verreisen?
  - utter_travel_risk_countries

## travel_while
* travel_while: Was, wenn ich schon vor Ort bin?
  - utter_travel_while

## travel_within_germany
* travel_within_germany: Ist der Urlaub in Deutschland trotz Corona möglich?
  - utter_travel_within_germany

## bot_achievement
* bot_achievement: Nenne mir deine beste Leistung!
  - utter_bot_achievement

## bot_actor
* bot_actor: Sag mir deine Lieblingsschauspieler.
  - utter_bot_actor

## bot_age
* bot_age: Dürfte ich Ihr Alter erfahren?
  - utter_bot_age

## bot_animal
* bot_animal: Welches Tier magst du am liebsten?
  - utter_bot_animal

## bot_appearance
* bot_appearance: Trägst Du ein Kleid oder eine Hose
  - utter_bot_appearance

## bot_author
* bot_author: Was ist dein Lieblingsautor?
  - utter_bot_author

## bot_availability
* bot_availability: Sag mir deine arbeitszeiten.
  - utter_bot_availability

## bot_books
* bot_books: Ist lesen Ihr Hobby?
  - utter_bot_books

## bot_capabilities
* bot_capabilities: Welche Fragen beantwortest du?
  - utter_bot_capabilities

## bot_children
* bot_children: Magst du Babys?
  - utter_bot_children

## bot_color
* bot_color: Was ist deine Lieblings Farbe?
  - utter_bot_color

## bot_costs
* bot_costs: Ich möchte Ihre Kosten wissen.
  - utter_bot_costs

## bot_developers
* bot_developers: wer hat dich gebaut
  - utter_bot_developers

## bot_differences
* bot_differences: Cortana ist viel besser
  - utter_bot_differences

## bot_dislike
* bot_dislike: Was hasst du?
  - utter_bot_dislike

## bot_eyes
* bot_eyes: Welche Farbe hat dein Auge?
  - utter_bot_eyes

## bot_favorites
* bot_favorites: Nennen Sie Ihre Lieblingssache.
  - utter_bot_favorites

## bot_fear
* bot_fear: Hast du auch Ängste wie wir Menschen? Wenn ja, wovor?
  - utter_bot_fear

## bot_food
* bot_food: Was ist dein Lieblingsessen?
  - utter_bot_food

## bot_friends
* bot_friends: Was denkst du über Freundschaft?
  - utter_bot_friends

## bot_games
* bot_games: Magst du etwas?
  - utter_bot_games

## bot_gender
* bot_gender: Bist du ein Mädchen
  - utter_bot_gender

## bot_goal
* bot_goal: Was sind deine Wünsche?
  - utter_bot_goal

## bot_hair
* bot_hair: Hast du blondes Haar?
  - utter_bot_hair

## bot_hobbies
* bot_hobbies: Magst du Tischtennis spielen?
  - utter_bot_hobbies

## bot_intelligence
* bot_intelligence: Bist du ein intelligenter Chat-Bot?
  - utter_bot_intelligence

## bot_languages
* bot_languages: In welcher Sprache kann ich mit dir sprechen?
  - utter_bot_languages

## bot_movies
* bot_movies: Wer ist dein Lieblingsschauspieler oder deine Lieblingsschauspielerin?
  - utter_bot_movies

## bot_music
* bot_music: Welche Band magst du am liebsten?
  - utter_bot_music

## bot_name
* bot_name: Hast du einen Namen und kannst ihn mir verraten?
  - utter_bot_name

## bot_origin
* bot_origin: Was ist dein Ursprung?
  - utter_bot_origin

## bot_parents
* bot_parents: Wer ist deine Mama?
  - utter_bot_parents

## bot_personality
* bot_personality: Wie freundlich bist du?
  - utter_bot_personality

## bot_pets
* bot_pets: Nenne ein Tier, das du liebst
  - utter_bot_pets

## bot_places
* bot_places: Kennen Sie einen relevanten Ort?
  - utter_bot_places

## bot_profession
* bot_profession: Dein Beruf
  - utter_bot_profession

## bot_real
* bot_real: Du bist keine echte Person, nicht wahr?
  - utter_bot_real

## bot_relationship
* bot_relationship: Bist du verliebt?
  - utter_bot_relationship

## bot_residence
* bot_residence: ich denke du lebst irgendwo in meinem computer
  - utter_bot_residence

## bot_senses
* bot_senses: Welchen Geruch hasst du?
  - utter_bot_senses

## bot_series
* bot_series: Welche Serie magst du?
  - utter_bot_series

## bot_sexual
* bot_sexual: Befriedig mich!
  - utter_bot_sexual

## bot_sibling
* bot_sibling: Bist du ein Einzelkind oder hast du Geschwister?
  - utter_bot_sibling

## bot_sing
* bot_sing: Kannst du singen?
  - utter_bot_sing

## bot_sites
* bot_sites: Auf welchen Websites sitzen Sie häufig?
  - utter_bot_sites

## bot_sports
* bot_sports: Motorsport
  - utter_bot_sports

## bot_version
* bot_version: Wie ist deine Version?
  - utter_bot_version

## bot_words
* bot_words: Was ist das schönste Wort
  - utter_bot_words

## bot_worst_experience
* bot_worst_experience: Sind Sie ledig?
  - utter_bot_worst_experience

## cc_afterlife
* cc_afterlife: Was passiert nach dem Tod?
  - utter_cc_afterlife

## cc_alien
* cc_alien: Denkst du, dass es Aliens gibt?
  - utter_cc_alien

## cc_chicken_egg
* cc_chicken_egg: Kannst du mir sagen, was zuerst kam? Das Ei oder das Huhn?
  - utter_cc_chicken_egg

## cc_deepest_point
* cc_deepest_point: Tiefster Punkt der Erde.
  - utter_cc_deepest_point

## cc_drugs
* cc_drugs: Nehmen Sie Drogen?
  - utter_cc_drugs

## cc_fun_fact
* cc_fun_fact: Interessante Tatsache.
  - utter_cc_fun_fact

## cc_geography
* cc_geography: Wo ist China?
  - utter_cc_geography

## cc_highest_building
* cc_highest_building: Höchstes Hochhaus der Welt
  - utter_cc_highest_building

## cc_hitchhiker
* cc_hitchhiker: Was ist die ultimative Antwort auf alle Fragen?
  - utter_cc_hitchhiker

## cc_joke
* cc_joke: Einen Witz.
  - utter_cc_joke

## cc_keys
* cc_keys: Wo hast du die Schlüssel hingelegt?
  - utter_cc_keys

## cc_lets_talk
* cc_lets_talk: Worüber können wir noch reden?
  - utter_cc_lets_talk

## cc_lotr
* cc_lotr: Im Zweifelsfall sollte man immer seiner Nase folgen …
  - utter_cc_lotr

## cc_make_food
* cc_make_food: Gib mir einen Cheeseburger
  - utter_cc_make_food

## cc_make_question
* cc_make_question: Frag mich was!
  - utter_cc_make_question

## cc_make_weather
* cc_make_weather: Könnten Sie das Wetter ändern?
  - utter_cc_make_weather

## cc_moon
* cc_moon: Distanz zum Mond
  - utter_cc_moon

## cc_newspaper
* cc_newspaper: Gibt es etwas neues in der Zeitung?
  - utter_cc_newspaper

## cc_philosophical
* cc_philosophical: Wer bin ich?
  - utter_cc_philosophical

## cc_politics
* cc_politics: Welche verschiedenen Arten von Regierungen gibt es?
  - utter_cc_politics

## cc_prophesy
* cc_prophesy: Was wird mir in der Zukunft passieren
  - utter_cc_prophesy

## cc_religion
* cc_religion: Bist du Atheist?
  - utter_cc_religion

## cc_rhyme
* cc_rhyme: Hast du ein Gedicht für mich?
  - utter_cc_rhyme

## cc_senselife
* cc_senselife: Ich will den Sinn des Lebens finden
  - utter_cc_senselife

## cc_skyblue
* cc_skyblue: Der Himmel ist blau warum
  - utter_cc_skyblue

## cc_story
* cc_story: Hast du was zu erzählen?
  - utter_cc_story

## cc_weather
* cc_weather: Ich will Informationen über das Wetter.
  - utter_cc_weather

## user_angry
* user_angry: Ich kann nicht schlafen.
  - utter_user_angry

## user_dont_know
* user_dont_know: Ich habe keine Informationen.
  - utter_user_dont_know

## user_dont_understand
* user_dont_understand: Ich habe das leider nicht verstanden.
  - utter_user_dont_understand

## user_fat
* user_fat: Ich bin zu dick
  - utter_user_fat

## user_friend
* user_friend: Willst du mit mir befreundet sein?
  - utter_user_friend

## user_happy
* user_happy: Ich bin eine freche Person.
  - utter_user_happy

## user_hate
* user_hate: Ich verachte alles an dir.
  - utter_user_hate

## user_laugh
* user_laugh: Lmao
  - utter_user_laugh

## user_love
* user_love: Bist Du noch single
  - utter_user_love

## user_particles
* user_particles: okay
  - utter_user_particles

## user_random_input
* user_random_input: ahgoyai
  - utter_user_random_input

## user_scared
* user_scared: Jemand hat mich erschreckt.
  - utter_user_scared

## user_tired
* user_tired: Ich bin hundemüde
  - utter_user_tired

## vocative_call
* vocative_call: Bist du noch da?
  - utter_vocative_call

## vocative_help
* vocative_help: Beraten!
  - utter_vocative_help

## vocative_no
* vocative_no: Nichts.
  - utter_vocative_no

## vocative_sorry
* vocative_sorry: Entschuldigen Sie!
  - utter_vocative_sorry

## vocative_thank_you
* vocative_thank_you: Man dankt.
  - utter_vocative_thank_you

## vocative_yes
* vocative_yes: ja
  - utter_vocative_yes

## vocative_you_welcome
* vocative_you_welcome: Ganz meine Ehre.
  - utter_vocative_you_welcome

## comment_hot
* comment_hot: Ich denke du bist sexy!
  - utter_comment_hot

## comment_negative
* comment_negative: Du gibst keine klaren Informationen.
  - utter_comment_negative

## comment_offense
* comment_offense: du bist so hohl
  - utter_comment_offense

## comment_positive
* comment_positive: Cool!
  - utter_comment_positive

## comment_racist
* comment_racist: Hitler
  - utter_comment_racist

## comment_smart
* comment_smart: Du klingst wirklich gut.
  - utter_comment_smart

## features_date
* features_date: Welchen Tag haben wir?
  - action_get_date
  - slot{"bot_date": "20/05/2020"}

## features_time
* features_time: Gib mir die Zeit!
  - action_get_time
  - slot{"bot_time": "17:17:54"}


<!-- Counters
Generic requests -->

## covid_situation_without_country
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand sind in Deutschland?
  - utter_want_to_add_country
* vocative_yes: Ich habe keine Einwände.
  - utter_ask_which_country
* country: Nippon
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Frankreich"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_without_country2
* covid_situation_infected_critical: Personen in kritischem Zustand in Österreich.
  - utter_want_to_add_country
* vocative_no: lieber nicht
  - utter_covid_no_country_current_statistics

## covid_situation_without_country3
* covid_situation_infected_critical: Wieviele Personen in China sind im kritischen Zustand?
  - utter_want_to_add_country
* country: moldova
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Italy"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected


## covid_situation_infected_happy 
* covid_situation_infected: Wie viele Menschen sind in Indien gestorben
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_infected_unhappy
* covid_situation_infected: Krankheitsfälle in Hessen
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_unhappy_with_country
* covid_situation_infected: Stecken sich mehr Frauen oder mehr Männer an?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Akzeptiere.
  - utter_ask_which_country
* country: Kiribati
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_unhappy_inexistent_country
* covid_situation_infected: Wie sind die Fallzahlen in Österreich
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ja, gern.
  - utter_ask_which_country
* country: Gambia
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_unhappy_with_dashboard
* covid_situation_infected: Wie viele aktive Fälle sind in England enthalten?
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_no: niente
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_happy
* covid_situation_infected_critical: Wie viele Personen befinden sich in Kanada in einem kritischen Zustand?
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Spain"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy
* covid_situation_infected_critical: Wie viele Menschen befinden sich in Italien in kritischem Zustand
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_country
* covid_situation_infected_critical: Wie viele Menschen befinden sich in Italien in kritischem Zustand
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ich habe nichts dagegen.
  - utter_ask_which_country
* country: Cuba
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Espanha"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy_inexistent_country
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in England?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Jap.
  - utter_ask_which_country
* country: Paraguay
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_dashboard
* covid_situation_infected_critical: Kritischer Zustand in Russland.
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: Nicht im Entferntesten.
  - utter_covid_no_country_current_statistics
