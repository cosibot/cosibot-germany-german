## start_1
* start-dialogue: /start-dialogue
  - action_check_bot_introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_false

## start1_1
* start_dialogue: /start-dialogue
  - action_check_bot_introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start1_3
* start-dialogue: /start-dialogue
  - action_check_bot_introduced
  - slot{"bot_introduced": "True"}
  - utter_greeting_hello_introduced_false

## start_12
* start: /start-dialogue
  - action_check_bot_introduced

## start1_12
* start_dialogue: /start-dialogue
  - action_check_bot_introduced

## start1_32
* start-dialogue: /start-dialogue
  - action_check_bot_introduced

## start1_12_1
* greeting_hello: Huhu?
  - action_check_bot_introduced
  - slot{"bot_introduced": true}
  - utter_greeting_hello_introduced_true

## covid_current_situation_get_news
* covid_current_situation: Lage in - Wie ist die Situation in Kolumbien
  - action_get_news_request

## covid_current_situation_get_news_entity_country
* covid_current_situation: Was ist mit Bolivien?
  - action_get_news_request

## covid_current_statistics_happy_path_state
* covid_situation_infected: Wie viele Menschen weltweit sind mit dem Virus infiziert
  - action_search_stats_region
  - slot{"region_search_successful": "ok"}
  - slot{"region": "Berlin"}
  - slot{"region_confirmed_accum": 130}
  - utter_covid_current_statistics_region

## covid_current_statistics_unhappy_empty_path_state_no
* covid_situation_infected: COVID-19 Fälle nach Altersgruppe und Geschlecht
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Eigentlich nicht
  - utter_covid_no_country_current_statistics

## covid_current_statistics_unhappy_not_ok_path_state_no
* covid_situation_infected: wie viele Menschen sind in Deutschland betroffen
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Keinesfalls.
  - utter_covid_no_country_current_statistics

## covid_current_statistics_unhappy_empty_path_state_yes
* covid_situation_infected: Wie viele Infizierte gibt es in Baden-Württemberg
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Machen Sie das.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_current_statistics_unhappy_not_ok_path_state_yes
* covid_situation_infected: Wo finde ich aktuelle Zahlen?
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Bremen"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Wie Sie wollen.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_current_statistics_happy_path_district
* covid_situation_infected: Wie viele Menschen sind am Virus gestorben
  - action_search_stats_region
  - slot{"region_search_successful": "ok"}
  - slot{"region": "München"}
  - slot{"region_confirmed_accum": "130"}
  - utter_covid_current_statistics_region

## covid_current_statistics_unhappy_empty_path_district_yes
* covid_situation_infected: Anzahl der Toten in Brasilien
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_yes: Alle Mal.
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Deutschland"}
  - slot{"total_infected_critical": "176"}
  - utter_covid_situation_infected

## covid_current_statistics_unhappy_not_ok_path_district_yes
* covid_situation_infected: wie schauen die zahlen in Frankreich aus
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Frankfurt"}
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

## covid_current_statistics_unhappy_path_empty_district_no
* covid_situation_infected: Weißt du wie viele Erkrankte es weltweit gibt?
  - action_search_stats_region
  - slot{"region_search_successful": "empty"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Nicht wirklich
  - utter_covid_no_country_current_statistics 

## covid_current_statistics_unhappy_path_not_ok_district_no
* covid_situation_infected: Wie viele Menschen sind in Indien gestorben
  - action_search_stats_region
  - slot{"region_search_successful": "not-ok"}
  - slot{"region": "Frankfurt"}
  - slot{"country_code": "DE"}
  - utter_region_nodata
* vocative_no: Nee.
  - utter_covid_no_country_current_statistics 

## corona_app_developers
* corona_app_developers: Wer steht hinter der Corona Warn App?
  - utter_corona_app_developers

## gradual_opening_party
* gradual_opening_party: Kann ich mit meinen Freunden Party feiern?
  - utter_gradual_opening_party

## prevention_supermarket
* prevention_supermarket: Welche Maßnahmen muss ich beim Einkaufen beachten?
  - utter_prevention_supermarket

## bot_developers
* bot_developers: Wer hat euch entwickelt?
  - utter_bot_developers

## corona_app_general
* corona_app_general: Corona-Warn-App
  - utter_corona_app_general

## corona_app_obligatory
* corona_app_obligatory: Muss ich jetzt die Corona Warn App nutzen?
  - utter_corona_app_obligatory

## corona_app_why
* corona_app_why: Corona-Warn-App - warum?
  - utter_corona_app_why

## coronavirus_info
* coronavirus_info: Ich weiß nicht, was Coronavirus ist
  - utter_coronavirus_info

<!-- ## covid_aftereffects_immunity
* covid_aftereffects_immunity: Kann ich mich nach Genesung erneut anstecken?
  - utter_covid_aftereffects_immunity -->

## covid_babys_children
* covid_babys_children: Kinder Coronavirus
  - utter_covid_babys_children

## covid_dangerous
* covid_dangerous: Eine Infizierung mit Q19 ist gefährlich.
  - utter_covid_dangerous

## covid_difference_influenza
* covid_difference_influenza: Wo liegen die Unterschiede zwischen einer Erkältung und COVID
  - utter_covid_difference_influenza

## covid_disease_process
* covid_disease_process: Wie verläuft die neuartige Lungenkrankheit
  - utter_covid_disease_process

## covid_duration
* covid_duration: Wie lange ist man krank
  - utter_covid_duration

## covid_ibuprofen
* covid_ibuprofen: Kann das frei verkäufliche Schmerzmittel Ibuprofen bei einer Infektion mit Sars-CoV-2 zu einem schlimmeren Krankheitsverlauf führen?
  - utter_covid_ibuprofen

## covid_incubation
* covid_incubation: Wie lange dauert es, bis die Symptome nach der Ansteckung eintreten?
  - utter_covid_incubation

## covid_info
* covid_info: Informationen zum huvit 19
  - utter_covid_info

## covid_meaning
* covid_meaning: Was heißt cookit 19
  - utter_covid_meaning

## covid_mortality_rate
* covid_mortality_rate: Wie hoch ist die Sterblichkeitsrate?
  - utter_covid_mortality_rate

## covid_origins
* covid_origins: Ursprung Coronavirus
  - utter_covid_origins

## covid_preexisting_illness
* covid_preexisting_illness: Welche Vorerkrankungen führen zu schwereren Verläufen?
  - utter_covid_preexisting_illness

## covid_pregnancy
* covid_pregnancy: Schwangerschaft
  - utter_covid_pregnancy

## covid_procedure_after_infection
* covid_procedure_after_infection: 
  - utter_covid_procedure_after_infection

## covid_sars
* covid_sars: SARS und COVID 19.
  - utter_covid_sars

## covid_season
* covid_season: Hat die Saison Einfluss auf Covid?
  - utter_covid_season

## covid_situation_infected
* covid_situation_infected: Wie viele Menschen infizieren sich täglich in Deutschland?
  - utter_covid_situation_infected

## covid_situation_infected_critical
* covid_situation_infected_critical: Wie viele Personen befinden sich in einem kritischen Zustand in England?
  - utter_covid_situation_infected_critical

## covid_symptoms
* covid_symptoms: Ich habe ein leichtes kratzen im Halsbereich
  - utter_covid_symptoms

## covid_treatment
* covid_treatment: Behandlungsmöglichkeiten cookit 19
  - utter_covid_treatment

## covid_unknown_cases
* covid_unknown_cases: 
  - utter_covid_unknown_cases

## covid_vaccine
* covid_vaccine: Impfung?
  - utter_covid_vaccine

## covid_worry
* covid_worry: Ich mache mir sehr sorgen um den Virus!
  - utter_covid_worry

## economy_consequences
* economy_consequences: Was sind die wirtschaftlichen Folgen
  - utter_economy_consequences

## germany_consequences
* germany_consequences: Wie viele Kranke wird es in Deutschland geben
  - utter_germany_consequences

## germany_current_situation
* germany_current_situation: Covid 19 in Deutschland
  - utter_germany_current_situation

## germany_food_buy
* germany_food_buy: Welche Lebensmittel sollte ich für die Quarantäne vorrätig zu Hause haben
  - utter_germany_food_buy

## germany_food_shortages
* germany_food_shortages: Sind Lebensmittel Engpässe zu befürchten
  - utter_germany_food_shortages

## germany_hotline
* germany_hotline: Telefonnummer bitte
  - utter_germany_hotline

## germany_lockdown_crisis_howlong
* germany_lockdown_crisis_howlong: Wie lange dauert der Lockdown
  - utter_germany_lockdown_crisis_howlong

## germany_neighbors_close_borders
* germany_neighbors_close_borders: Grenzen schließen im Corona Kampf
  - utter_germany_neighbors_close_borders

## germany_nomoney
* germany_nomoney: Was bietet mir das Hilfspaket, wenn ich meinen Kredit oder meine Versicherung nicht mehr bezahlen kann?
  - utter_germany_nomoney

## germany_pandemic
* germany_pandemic: Pandemie in Deutschland
  - utter_germany_pandemic

## germany_preparation
* germany_preparation: Welche Maßnahmen gibt es jetzt in Sachsen Anhalt
  - utter_germany_preparation

## germany_risk
* germany_risk: Risiko Ressourcenbelastung des Gesundheitssystems
  - utter_germany_risk

## germany_second_wave
* germany_second_wave: Ist die Pandemie jetzt überstanden?
  - utter_germany_second_wave

## germany_spread_water
* germany_spread_water: Coronavirus und Reisen per Bahn
  - utter_germany_spread_water

## gradual_opening_barbecue
* gradual_opening_barbecue: Grill Parties
  - utter_gradual_opening_barbecue

## gradual_opening_cinema_concert_theatre
* gradual_opening_cinema_concert_theatre: Was ist mit Friseuren
  - utter_gradual_opening_cinema_concert_theatre

## gradual_opening_museum
* gradual_opening_museum: Wann kan man wieder in ein Museum?
  - utter_gradual_opening_museum

## gradual_opening_playgrounds_zoos
* gradual_opening_playgrounds_zoos: Was ist mit Spielplätzen?
  - utter_gradual_opening_playgrounds_zoos

## gradual_opening_religious
* gradual_opening_religious: Was ist mit der Kommunion?
  - utter_gradual_opening_religious

## gradual_opening_restaurants
* gradual_opening_restaurants: Kann ich ein Restaurant besuchen?
  - utter_gradual_opening_restaurants

## gradual_opening_schools
* gradual_opening_schools: Wann muss ich wieder in die Schule?
  - utter_gradual_opening_schools

## gradual_opening_sports
* gradual_opening_sports: Darf ich wieder trainieren?
  - utter_gradual_opening_sports

## gradual_opening_universities
* gradual_opening_universities: Universitäten machen auf
  - utter_gradual_opening_universities

## gradual_opening_visit_family_friends
* gradual_opening_visit_family_friends: Darf ich noch meine Freundin besuchen?
  - utter_gradual_opening_visit_family_friends

## greeting_goodbye
* greeting_goodbye: Freundliche Grüße!
  - utter_greeting_goodbye

## greeting_how_are_you
* greeting_how_are_you: Wie läuft's bei dir so?
  - utter_greeting_how_are_you

## mask_children
* mask_children: Maskenpflicht und Kinder
  - utter_mask_children

## mask_control
* mask_control: Kontrolle der Maskenpflicht
  - utter_mask_control

## mask_differences
* mask_differences: Schutzmasken Übersicht
  - utter_mask_differences

## mask_ffp3
* mask_ffp3: FFP3-Schutzmasken mit Filter
  - utter_mask_ffp3

## mask_obligatory
* mask_obligatory: Helfen Atemschutzmasken gegen Kubik 19?
  - utter_mask_obligatory

## mask_protection
* mask_protection: 
  - utter_mask_protection

## mask_put
* mask_put: Was gilt es zu beachten wenn man eine Maske trägt
  - utter_mask_put

## mask_reuse
* mask_reuse: Kann ich den Mund Nasen Schutz noch einmal verwenden?
  - utter_mask_reuse

## mask_selfmade
* mask_selfmade: Masken selber herstellen
  - utter_mask_selfmade

## mask_wash
* mask_wash: Kann man den Mundschutz zur Reinigung in die Mikrowelle geben?
  - utter_mask_wash

## mask_which
* mask_which: Welche Maske schützt am besten vor einer Infektion
  - utter_mask_which

## myth_alcohol
* myth_alcohol: Tötet das Einreiben Viren ab?
  - utter_myth_alcohol

## myth_hold_breath
* myth_hold_breath: Ich habe gelesen dass wenn man 10 Sekunden die Luft anhalten kann, dass man dann nicht infiziert ist
  - utter_myth_hold_breath

## myth_hot_bath
* myth_hot_bath: Heiße Dusche
  - utter_myth_hot_bath

## myth_mosquito
* myth_mosquito: Ansteckung durch Mücken
  - utter_myth_mosquito

## myth_pneumonia_vaccine
* myth_pneumonia_vaccine: Impfung gegen Pneumokokken um sich gegen Corona zu schützen
  - utter_myth_pneumonia_vaccine

## myths_chinese_laboratory
* myths_chinese_laboratory: Coronavirus aus dem chinesischen Labor
  - utter_myths_chinese_laboratory

## myths_conspiracy_fakenews
* myths_conspiracy_fakenews: Falschnachricht
  - utter_myths_conspiracy_fakenews

## myths_vitamins_plants_minerals_homeopathy
* myths_vitamins_plants_minerals_homeopathy: Was können Mineralstoffe?
  - utter_myths_vitamins_plants_minerals_homeopathy

## prevention_clean_hands
* prevention_clean_hands: Warum Hände waschen?
  - utter_prevention_clean_hands

## prevention_desinfection
* prevention_desinfection: Desinfektionsgel
  - utter_prevention_desinfection

## prevention_distance
* prevention_distance: Soll ich Abstand von anderen Menschen halten
  - utter_prevention_distance

## prevention_general
* prevention_general: Wie kann man seine Mitmenschen vor einer Ansteckung schützen?
  - utter_prevention_general

## prevention_home
* prevention_home: Soll ich zu Hause bleiben, wenn ich mich etwas krank fühle?
  - utter_prevention_home

## prevention_informed
* prevention_informed: Muss ich ständig Nachrichten über den Virus lesen?
  - utter_prevention_informed

## prevention_medical_attention
* prevention_medical_attention: Was tun bei Symptomen?
  - utter_prevention_medical_attention

## prevention_touch
* prevention_touch: Soll ich Handschuhe tragen?
  - utter_prevention_touch

## quarantine_control
* quarantine_control: Wird jetzt eigentlich häusliche Quarantäne überhaupt kontrolliert, insbesondere in dörflicher Lage?
  - utter_quarantine_control

## quarantine_dogwalking
* quarantine_dogwalking: Was machen Hundebesitzer, die in Quarantäne sind? Wer geht mit dem Tier hinaus?
  - utter_quarantine_dogwalking

## quarantine_dos_and_donts
* quarantine_dos_and_donts: Was darf man noch in Quarantäne und was nicht?
  - utter_quarantine_dos_and_donts

## quarantine_general
* quarantine_general: Was bedeutet Ausgangssperre?
  - utter_quarantine_general

## quarantine_how_it_works
* quarantine_how_it_works: 
  - utter_quarantine_how_it_works

## quarantine_toiletpaper
* quarantine_toiletpaper: Coronavirus Klopapier Hamsterkäufe
  - utter_quarantine_toiletpaper

## quarantine_when_who_howlong
* quarantine_when_who_howlong: Unter welchen Umständen muss man mit Quarantäne rechnen?
  - utter_quarantine_when_who_howlong

## sources
* sources: Woher sind deine Informationen?
  - utter_sources

## spread_animals
* spread_animals: Ansteckungsgefahr bei Tieren
  - utter_spread_animals

## spread_feces
* spread_feces: Fangen Sie das Virus durch Kot.
  - utter_spread_feces

## spread_general
* spread_general: Ich hätte gerne Informationen dazu wie genau das Virus übertragen wird
  - utter_spread_general

## spread_heat_cold
* spread_heat_cold: Wird das neue Coronavirus bei wärmeren Temperaturen schwächer und ist deshalb mit einem Abebben der Epidemie im Frühjahr zu rechnen?
  - utter_spread_heat_cold

## spread_no_symptoms
* spread_no_symptoms: Menschen ohne Symptome können ansteckend sein?
  - utter_spread_no_symptoms

## spread_surfaces_food_objects
* spread_surfaces_food_objects: Kann ich mit dem Auto noch in den Nachbarort?
  - utter_spread_surfaces_food_objects

## test_how
* test_how: 
  - utter_test_how

## test_payment
* test_payment: Werden die Kosten für den Test von den Krankenkassen übernommen?
  - utter_test_payment

## test_per_day
* test_per_day: Wieviele Tests auf den huvit 19 werden am Tag gemacht?
  - utter_test_per_day

## test_quick_test
* test_quick_test: Schnelltest qubeat 19
  - utter_test_quick_test

## test_results_reliability
* test_results_reliability: Ist der test zuverlässig?
  - utter_test_results_reliability

## test_virus
* test_virus: Virus Tests
  - utter_test_virus

## test_who
* test_who: Wer wird getestet und wer nicht
  - utter_test_who

## travel_before
* travel_before: Gibt es Reiseeinschränkungen
  - utter_travel_before

## travel_cancel
* travel_cancel: Kann man eine Reise aus Angst vor Covid-19 stornieren?
  - utter_travel_cancel

## travel_general
* travel_general: COBIT 19 und Reisen
  - utter_travel_general

## travel_return
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?
  - utter_travel_return

## travel_returnprogram
* travel_returnprogram: Muss ich damit rechnen, dass ich vielleicht nicht zurück nach Deutschland kann?
  - utter_travel_returnprogram

## travel_risk_countries
* travel_risk_countries: Bei welchen Ländern sollte man jetzt vorsichtig sein
  - utter_travel_risk_countries

## travel_while
* travel_while: Vorgehensweise auf Reisen.
  - utter_travel_while

## travel_within_germany
* travel_within_germany: Verreisen innerhalb Deutschlands
  - utter_travel_within_germany

## bot_achievement
* bot_achievement: Was war deine größte Errungenschaft?
  - utter_bot_achievement

## bot_actor
* bot_actor: Sagen Sie mir Ihre berühmten Lieblingsschauspieler.
  - utter_bot_actor

## bot_age
* bot_age: Kannst du mir sagen, wie alt du bist?
  - utter_bot_age

## bot_animal
* bot_animal: Welches Tier ziehst du vor?
  - utter_bot_animal

## bot_appearance
* bot_appearance: Zeig dich mir!
  - utter_bot_appearance

## bot_author
* bot_author: Wer ist dein Lieblingsschriftsteller?
  - utter_bot_author

## bot_availability
* bot_availability: Sagen Sie mir die Arbeitszeiten.
  - utter_bot_availability

## bot_books
* bot_books: Magst du Bücher?
  - utter_bot_books

## bot_capabilities
* bot_capabilities: Deine Fähigkeiten
  - utter_bot_capabilities

## bot_children
* bot_children: Willst du Kinder?
  - utter_bot_children

## bot_color
* bot_color: Bevorzugen Sie eine Lieblingsfarbe?
  - utter_bot_color

## bot_costs
* bot_costs: Warst du teuer?
  - utter_bot_costs

## bot_differences
* bot_differences: Du bist schlechter als andere Bots
  - utter_bot_differences

## bot_dislike
* bot_dislike: Hasst du etwas?
  - utter_bot_dislike

## bot_eyes
* bot_eyes: Erzähl mir von deinen Augen.
  - utter_bot_eyes

## bot_favorites
* bot_favorites: Was hast du gern?
  - utter_bot_favorites

## bot_fear
* bot_fear: Empfindest du Angst?
  - utter_bot_fear

## bot_food
* bot_food: Magst du Speck?
  - utter_bot_food

## bot_friends
* bot_friends: Erzähl mir von deinen Freunden
  - utter_bot_friends

## bot_games
* bot_games: Magst du Computerspiele
  - utter_bot_games

## bot_gender
* bot_gender: Bist du eine Dame?
  - utter_bot_gender

## bot_goal
* bot_goal: Erzähl mir deine Träume.
  - utter_bot_goal

## bot_hair
* bot_hair: Welche Farbe haben deine Haare?
  - utter_bot_hair

## bot_hobbies
* bot_hobbies: Spielst du gern Geige?
  - utter_bot_hobbies

## bot_intelligence
* bot_intelligence: Wie schlau bist du?
  - utter_bot_intelligence

## bot_languages
* bot_languages: sprechen sie englisch
  - utter_bot_languages

## bot_movies
* bot_movies: Lieblings-Thriller
  - utter_bot_movies

## bot_music
* bot_music: Welche Band magst du am meisten?
  - utter_bot_music

## bot_name
* bot_name: Hast du einen Namen und kannst ihn mir verraten?
  - utter_bot_name

## bot_origin
* bot_origin: Ich möchte wissen, wo du geboren wurdest.
  - utter_bot_origin

## bot_parents
* bot_parents: Hast du Mama und Papa?
  - utter_bot_parents

## bot_personality
* bot_personality: Erzähl mir über deine Persönlichkeit.
  - utter_bot_personality

## bot_pets
* bot_pets: Nennen Sie Ihr Lieblingstier als Haustier.
  - utter_bot_pets

## bot_places
* bot_places: Sag mir einen Platz
  - utter_bot_places

## bot_profession
* bot_profession: Welcher ist dein Beruf?
  - utter_bot_profession

## bot_real
* bot_real: Sind Sie ein Chatbot
  - utter_bot_real

## bot_relationship
* bot_relationship: Bot Beziehungen
  - utter_bot_relationship

## bot_residence
* bot_residence: Wo liegt deine Wohnung?
  - utter_bot_residence

## bot_senses
* bot_senses: Welches sind deine Lieblingsgerüche?
  - utter_bot_senses

## bot_series
* bot_series: Was ist deine Lieblingsserie?
  - utter_bot_series

## bot_sexual
* bot_sexual: Küss mich!
  - utter_bot_sexual

## bot_sibling
* bot_sibling: Sag mir den Namen deiner Schwestern
  - utter_bot_sibling

## bot_sing
* bot_sing: Würdest du für mich singen?
  - utter_bot_sing

## bot_sites
* bot_sites: Websites, die Sie besuchen
  - utter_bot_sites

## bot_sports
* bot_sports: Betätigst du dich sportlich?
  - utter_bot_sports

## bot_version
* bot_version: Welche version bist du?
  - utter_bot_version

## bot_words
* bot_words: Kannst du mir dein Lieblingswort sagen?
  - utter_bot_words

## bot_worst_experience
* bot_worst_experience: Was machst du morgens?
  - utter_bot_worst_experience

## cc_afterlife
* cc_afterlife: Geht das Leben nach dem Tod weiter?
  - utter_cc_afterlife

## cc_alien
* cc_alien: Gitb es außerirdisches Leben?
  - utter_cc_alien

## cc_chicken_egg
* cc_chicken_egg: Was war zuerst? Ei oder Huhn?
  - utter_cc_chicken_egg

## cc_deepest_point
* cc_deepest_point: Wo befindet sich der tiefste Punkt auf der Erde?
  - utter_cc_deepest_point

## cc_drugs
* cc_drugs: hast du schon mal Marihuana geraucht?
  - utter_cc_drugs

## cc_fun_fact
* cc_fun_fact: Gibt es Fun Facts?
  - utter_cc_fun_fact

## cc_geography
* cc_geography: Magst du Erdkunde?
  - utter_cc_geography

## cc_highest_building
* cc_highest_building: Welches ist das höchste Bauwerk?
  - utter_cc_highest_building

## cc_hitchhiker
* cc_hitchhiker: Was ist die Antwort auf die Frage nach dem Leben, dem Universum und dem ganzen Rest
  - utter_cc_hitchhiker

## cc_joke
* cc_joke: Möchten Sie mir einen Witz erzählen?
  - utter_cc_joke

## cc_keys
* cc_keys: Sag mir, wo die Schlüssel sind.
  - utter_cc_keys

## cc_lets_talk
* cc_lets_talk: Bock zu reden?
  - utter_cc_lets_talk

## cc_lotr
* cc_lotr: Viele, die leben, verdienen den Tod. Und manche, die sterben, verdienen das Leben. Kannst du es ihnen geben? Dann sei auch nicht so rasch mit einem Todesurteil bei der Hand.
  - utter_cc_lotr

## cc_make_food
* cc_make_food: Essen
  - utter_cc_make_food

## cc_make_question
* cc_make_question: Gibt es etwas, das du mich fragen möchtest?
  - utter_cc_make_question

## cc_make_weather
* cc_make_weather: Ich will, dass die Sonne scheint
  - utter_cc_make_weather

## cc_moon
* cc_moon: Wie weit ist der Mond von der Erde weg?
  - utter_cc_moon

## cc_newspaper
* cc_newspaper: Was für eine Zeitung kaufst du?
  - utter_cc_newspaper

## cc_philosophical
* cc_philosophical: Schadet Kunst der Gesellschaft in irgendeiner Weise?
  - utter_cc_philosophical

## cc_politics
* cc_politics: Trump
  - utter_cc_politics

## cc_prophesy
* cc_prophesy: Kannst Du mir sagen welche Zahlen am Mittwoch gezogen werden
  - utter_cc_prophesy

## cc_religion
* cc_religion: Religion
  - utter_cc_religion

## cc_rhyme
* cc_rhyme: Sag mir ein Gedicht
  - utter_cc_rhyme

## cc_senselife
* cc_senselife: Ich will den Sinn des Lebens wissen
  - utter_cc_senselife

## cc_skyblue
* cc_skyblue: Himmelblau warum
  - utter_cc_skyblue

## cc_story
* cc_story: Ich will einen Klatsch.
  - utter_cc_story

## cc_weather
* cc_weather: Liegt draußen Schnee?
  - utter_cc_weather

## user_angry
* user_angry: Heute habe ich schlechte Laune.
  - utter_user_angry

## user_dont_know
* user_dont_know: Ich habe nicht die geringste Ahnung.
  - utter_user_dont_know

## user_dont_understand
* user_dont_understand: Ich habe dich nicht verstanden
  - utter_user_dont_understand

## user_fat
* user_fat: Was kann ich anziehen, um nicht fett auszusehen?
  - utter_user_fat

## user_friend
* user_friend: Ich möchte deine Freundin sein!
  - utter_user_friend

## user_happy
* user_happy: Fühle mich so gut.
  - utter_user_happy

## user_hate
* user_hate: Ich empfinde eine Abneigung gegen dich
  - utter_user_hate

## user_laugh
* user_laugh: Hah
  - utter_user_laugh

## user_love
* user_love: Hast du Schmetterlinge im Bauch?
  - utter_user_love

## user_particles
* user_particles: hmmm
  - utter_user_particles

## user_random_input
* user_random_input: retrewyth
  - utter_user_random_input

## user_scared
* user_scared: Ich habe Angst.
  - utter_user_scared

## user_tired
* user_tired: Ich bin fast tot
  - utter_user_tired

## vocative_call
* vocative_call: Hallo, noch jemad zuhause?
  - utter_vocative_call

## vocative_help
* vocative_help: Möchtest du mich beraten?
  - utter_vocative_help

## vocative_no
* vocative_no: Nie und nimmer.
  - utter_vocative_no

## vocative_sorry
* vocative_sorry: Tut mir wirklich leid.
  - utter_vocative_sorry

## vocative_thank_you
* vocative_thank_you: Verbindlichsten Dank.
  - utter_vocative_thank_you

## vocative_yes
* vocative_yes: Genau.
  - utter_vocative_yes

## vocative_you_welcome
* vocative_you_welcome: Dafür brauchst du mir nicht danken.
  - utter_vocative_you_welcome

## comment_hot
* comment_hot: Ich finde ich sexy.
  - utter_comment_hot

## comment_negative
* comment_negative: Das ist nicht dein Ding.
  - utter_comment_negative

## comment_offense
* comment_offense: Shit
  - utter_comment_offense

## comment_positive
* comment_positive: Du hilfst mir sehr.
  - utter_comment_positive

## comment_racist
* comment_racist: Du Nigger.
  - utter_comment_racist

## comment_smart
* comment_smart: Wie intelligent!
  - utter_comment_smart

## features_date
* features_date: Können Sie mir das Datum schreiben?
  - action_get_date
  - slot{"bot_date": "20/05/2020"}

## features_time
* features_time: Kannst du mir die Uhrzeit nennen?
  - action_get_time
  - slot{"bot_time": "17:17:54"}


<!-- Counters
Generic requests -->

## covid_situation_without_country
* covid_situation_infected_critical: Wie lange bleiben die Viren auf den Oberflächen?
  - utter_want_to_add_country
* vocative_yes: Ich stimme zu.
  - utter_ask_which_country
* country: zimbabwe
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Frankreich"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_without_country2
* covid_situation_infected_critical: Wie viele kritische Fälle in Tschechien?
  - utter_want_to_add_country
* vocative_no: Nicht im Entferntesten.
  - utter_further_questions

## covid_situation_without_country3
* covid_situation_infected_critical: Kritischer Zustand in Russland.
  - utter_want_to_add_country
* country: Benin
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Italy"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected


## covid_situation_infected_happy 
* covid_situation_infected: fallzahlen
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_infected_unhappy
* covid_situation_infected: Wie viele Menschen infizieren sich täglich neu in Deutschland?
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_unhappy_with_country
* covid_situation_infected: Gibt es offizielle Zahlen zu den Erkrankungen weltweit?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Na klar!
  - utter_ask_which_country
* country: senegal
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Portugal"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected

## covid_situation_unhappy_inexistent_country
* covid_situation_infected: Wie viele haben sich weltweit angesteckt
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: In Butter.
  - utter_ask_which_country
* country: La Réunion
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_unhappy_with_dashboard
* covid_situation_infected: Wie viele Menschen sind in Köln gestorben
  - action_search_stats
  - slot{"search_successful": "False"}
  - utter_want_to_add_country
* vocative_no: Nie.
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_happy
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in England?
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Spain"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy
* covid_situation_infected_critical: Personen in einem kritischen Fall in Türkei.
  - action_search_stats
  - slot{"search_successful": "not-ok"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_country
* covid_situation_infected_critical: Können die Viren auf Haltestangen überleben?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ohne Frage.
  - utter_ask_which_country
* country: Christmas Island
  - action_search_stats
  - slot{"search_successful": "ok"}
  - slot{"active_cases": "16300"}
  - slot{"country": "Espanha"}
  - slot{"total_infected_critical": "176"}
  - slot{"total_deaths": "32"}
  - utter_covid_situation_infected_critical

## covid_situation_infected_critical_unhappy_inexistent_country
* covid_situation_infected_critical: Wie viele Personen befinden sich in Kanada in einem kritischen Zustand?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_yes: Ja, genau.
  - utter_ask_which_country
* country: Hungary
  - action_search_stats
  - slot{"search_successful": "inexistent-country"}
  - utter_covid_no_country_current_statistics

## covid_situation_infected_critical_unhappy_with_dashboard
* covid_situation_infected_critical: Was ist die Lebensdauer der Coronaviren?
  - action_search_stats
  - slot{"search_successful": "wrong-country"}
  - utter_want_to_add_country
* vocative_no: nein
  - utter_covid_no_country_current_statistics
