## prevention_medical_attention (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* prevention_medical_attention: Was tun bei Symptomen?   <!-- predicted: covid_symptoms: Was tun bei Symptomen? -->
    - utter_prevention_medical_attention   <!-- predicted: action_default_fallback -->


## quarantine_how_it_works (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* quarantine_how_it_works:    <!-- predicted: None:  -->
    - utter_quarantine_how_it_works   <!-- predicted: action_default_fallback -->


## covid_current_statistics_happy_path_state (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen weltweit sind mit dem Virus infiziert   <!-- predicted: covid_current_statistics: Wie viele Menschen weltweit sind mit dem Virus infiziert -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "ok"}
    - slot{"region": "Berlin"}
    - slot{"region_confirmed_accum": 130}
    - utter_covid_current_statistics_region


## spread_surfaces_food_objects (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* spread_surfaces_food_objects: Kann ich mit dem Auto noch in den Nachbarort?   <!-- predicted: germany_neighbors_close_borders: Kann ich mit dem Auto noch in den Nachbarort? -->
    - utter_spread_surfaces_food_objects   <!-- predicted: utter_germany_neighbors_close_borders -->


## test_how (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* test_how:    <!-- predicted: None:  -->
    - utter_test_how   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_empty_path_state_no (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: COVID-19 Fälle nach Altersgruppe und Geschlecht   <!-- predicted: covid_current_statistics: COVID-19 Fälle nach Altersgruppe und Geschlecht -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Eigentlich nicht
    - utter_covid_no_country_current_statistics


## travel_return (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?   <!-- predicted: travel_return: Was muss ich beachten, wenn ich gerade in [Portugal]{"entity": "country_code", "value": "PT"} war? -->
    - slot{"country_code": "PT"}
    - utter_travel_return


## covid_current_statistics_unhappy_not_ok_path_state_no (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: wie viele Menschen sind in Deutschland betroffen   <!-- predicted: covid_current_statistics: wie viele Menschen sind in Deutschland betroffen -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Keinesfalls.
    - utter_covid_no_country_current_statistics


## bot_animal (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* bot_animal: Welches Tier ziehst du vor?   <!-- predicted: bot_pets: Welches Tier ziehst du vor? -->
    - utter_bot_animal   <!-- predicted: utter_bot_pets -->


## bot_author (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* bot_author: Wer ist dein Lieblingsschriftsteller?   <!-- predicted: bot_books: Wer ist dein Lieblingsschriftsteller? -->
    - utter_bot_author   <!-- predicted: utter_bot_books -->


## covid_current_statistics_unhappy_empty_path_state_yes (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Infizierte gibt es in Baden-Württemberg   <!-- predicted: covid_current_statistics: Wie viele Infizierte gibt es in [Baden-Württemberg]{"entity": "country_district", "value": " Baden-W\u00fcrttemberg"} -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
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


## covid_current_statistics_unhappy_not_ok_path_state_yes (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wo finde ich aktuelle Zahlen?   <!-- predicted: covid_current_statistics: Wo finde ich aktuelle Zahlen? -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
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


## bot_games (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* bot_games: Magst du Computerspiele   <!-- predicted: bot_hobbies: Magst du Computerspiele -->
    - utter_bot_games   <!-- predicted: utter_bot_hobbies -->


## covid_current_statistics_happy_path_district (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind am Virus gestorben   <!-- predicted: covid_current_statistics: Wie viele Menschen sind am Virus gestorben -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "ok"}
    - slot{"region": "München"}
    - slot{"region_confirmed_accum": "130"}
    - utter_covid_current_statistics_region


## covid_current_statistics_unhappy_empty_path_district_yes (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Anzahl der Toten in Brasilien   <!-- predicted: covid_current_statistics: Anzahl der Toten in [Brasilien]{"entity": "country_code", "value": "BR"} -->
    - slot{"country_code": "BR"}
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
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


## covid_current_statistics_unhappy_not_ok_path_district_yes (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: wie schauen die zahlen in Frankreich aus   <!-- predicted: covid_current_statistics: wie schauen die zahlen in [Frankreich]{"entity": "country_code", "value": "FR"} aus -->
    - slot{"country_code": "FR"}
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
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


## bot_worst_experience (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* bot_worst_experience: Was machst du morgens?   <!-- predicted: vocative_call: Was machst du morgens? -->
    - utter_bot_worst_experience   <!-- predicted: utter_vocative_call -->


## covid_current_statistics_unhappy_path_empty_district_no (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Weißt du wie viele Erkrankte es weltweit gibt?   <!-- predicted: covid_current_statistics: Weißt du wie viele Erkrankte es weltweit gibt? -->
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Nicht wirklich
    - utter_covid_no_country_current_statistics


## covid_current_statistics_unhappy_path_not_ok_district_no (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in Indien gestorben   <!-- predicted: covid_current_statistics: Wie viele Menschen sind in [Indien]{"entity": "country_code", "value": "IN"} gestorben -->
    - slot{"country_code": "IN"}
    - action_search_stats_region   <!-- predicted: action_default_fallback -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Nee.
    - utter_covid_no_country_current_statistics


## cc_religion (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* cc_religion: Religion   <!-- predicted: gradual_opening_religious: Religion -->
    - utter_cc_religion   <!-- predicted: utter_gradual_opening_religious -->


## user_scared (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* user_scared: Ich habe Angst.   <!-- predicted: covid_worry: Ich habe Angst. -->
    - utter_user_scared   <!-- predicted: utter_covid_worry -->


## covid_situation_without_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Wie lange bleiben die Viren auf den Oberflächen?   <!-- predicted: spread_surfaces_food_objects: Wie lange bleiben die Viren auf den Oberflächen? -->
    - utter_want_to_add_country   <!-- predicted: utter_spread_surfaces_food_objects -->
* vocative_yes: Ich stimme zu.
    - utter_ask_which_country
* country: zimbabwe   <!-- predicted: country: [zimbabwe]{"entity": "country_code", "value": "ZW"} -->
    - slot{"country_code": "ZW"}
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Frankreich"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_without_country2 (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele kritische Fälle in Tschechien?   <!-- predicted: covid_situation_infected_critical: Wie viele kritische Fälle in [Tschechien]{"entity": "country_code", "value": "CZ"}? -->
    - slot{"country_code": "CZ"}
    - utter_want_to_add_country
* vocative_no: Nicht im Entferntesten.
    - utter_further_questions   <!-- predicted: utter_covid_no_country_current_statistics -->


## covid_situation_without_country3 (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Kritischer Zustand in Russland.   <!-- predicted: covid_situation_infected_critical: Kritischer Zustand in [Russland]{"entity": "country_code", "value": "RU"}. -->
    - slot{"country_code": "RU"}
    - utter_want_to_add_country
* country: Benin   <!-- predicted: country: [Benin]{"entity": "country_code", "value": "BJ"} -->
    - slot{"country_code": "BJ"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Italy"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_infected_happy (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: fallzahlen   <!-- predicted: covid_current_statistics: fallzahlen -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected   <!-- predicted: utter_covid_situation_infected_critical -->


## covid_situation_infected_unhappy (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen infizieren sich täglich neu in Deutschland?   <!-- predicted: covid_current_statistics: Wie viele Menschen infizieren sich täglich neu in Deutschland? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_unhappy_with_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Gibt es offizielle Zahlen zu den Erkrankungen weltweit?   <!-- predicted: covid_current_statistics: Gibt es offizielle Zahlen zu den Erkrankungen weltweit? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Na klar!
    - utter_ask_which_country
* country: senegal   <!-- predicted: country: [senegal]{"entity": "country_code", "value": "SN"} -->
    - slot{"country_code": "SN"}
    - action_search_stats   <!-- predicted: utter_ask_which_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_unhappy_inexistent_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele haben sich weltweit angesteckt   <!-- predicted: covid_current_statistics: Wie viele haben sich weltweit angesteckt -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: In Butter.
    - utter_ask_which_country
* country: La Réunion   <!-- predicted: country: [La Réunion]{"entity": "country_code", "value": "RE"} -->
    - slot{"country_code": "RE"}
    - action_search_stats   <!-- predicted: utter_ask_which_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## covid_situation_unhappy_with_dashboard (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in Köln gestorben   <!-- predicted: covid_current_statistics: Wie viele Menschen sind in [Köln]{"entity": "country_district", "value": " K\u00f6ln"} gestorben -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "False"}
    - utter_want_to_add_country
* vocative_no: Nie.
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_happy (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in England?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in [England]{"entity": "country_code", "value": "GB"}? -->
    - slot{"country_code": "GB"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Spain"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected_critical


## covid_situation_infected_critical_unhappy (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Personen in einem kritischen Fall in Türkei.   <!-- predicted: covid_situation_infected_critical: Personen in einem kritischen Fall in [Türkei]{"entity": "country_code", "value": "TR"}. -->
    - slot{"country_code": "TR"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_unhappy_with_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Können die Viren auf Haltestangen überleben?   <!-- predicted: cc_senselife: Können die Viren auf Haltestangen überleben? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ohne Frage.
    - utter_ask_which_country
* country: Christmas Island   <!-- predicted: country: [Christmas Island]{"entity": "country_code", "value": "CX"} -->
    - slot{"country_code": "CX"}
    - action_search_stats   <!-- predicted: utter_ask_which_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected_critical   <!-- predicted: utter_covid_situation_infected -->


## covid_situation_infected_critical_unhappy_inexistent_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen befinden sich in Kanada in einem kritischen Zustand?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen befinden sich in [Kanada]{"entity": "country_code", "value": "CA"} in einem kritischen Zustand? -->
    - slot{"country_code": "CA"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ja, genau.
    - utter_ask_which_country
* country: Hungary   <!-- predicted: country: [Hungary]{"entity": "country_code", "value": "HU"} -->
    - slot{"country_code": "HU"}
    - action_search_stats   <!-- predicted: utter_ask_which_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_unhappy_with_dashboard (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Was ist die Lebensdauer der Coronaviren?   <!-- predicted: germany_lockdown_crisis_howlong: Was ist die Lebensdauer der Coronaviren? -->
    - action_search_stats   <!-- predicted: action_default_fallback -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_no: nein
    - utter_covid_no_country_current_statistics


## start1_1 (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* start_dialogue: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - slot{"bot_introduced": "True"}
    - utter_greeting_hello_introduced_false


## covid_procedure_after_infection (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_procedure_after_infection:    <!-- predicted: None:  -->
    - utter_covid_procedure_after_infection   <!-- predicted: action_default_fallback -->


## covid_situation_infected (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen infizieren sich täglich in Deutschland?   <!-- predicted: covid_current_statistics: Wie viele Menschen infizieren sich täglich in Deutschland? -->
    - utter_covid_situation_infected   <!-- predicted: action_default_fallback -->


## covid_situation_infected_critical (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen befinden sich in einem kritischen Zustand in England?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen befinden sich in einem kritischen Zustand in [England]{"entity": "country_code", "value": "GB"}? -->
    - slot{"country_code": "GB"}
    - utter_covid_situation_infected_critical   <!-- predicted: utter_want_to_add_country -->


## covid_unknown_cases (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_unknown_cases:    <!-- predicted: None:  -->
    - utter_covid_unknown_cases   <!-- predicted: action_default_fallback -->


## start_12 (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* start: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## germany_food_buy (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_food_buy: Welche Lebensmittel sollte ich für die Quarantäne vorrätig zu Hause haben   <!-- predicted: quarantine_general: Welche Lebensmittel sollte ich für die Quarantäne vorrätig zu Hause haben -->
    - utter_germany_food_buy   <!-- predicted: action_default_fallback -->


## germany_food_shortages (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_food_shortages: Sind Lebensmittel Engpässe zu befürchten   <!-- predicted: spread_surfaces_food_objects: Sind Lebensmittel Engpässe zu befürchten -->
    - utter_germany_food_shortages   <!-- predicted: utter_spread_surfaces_food_objects -->


## germany_hotline (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_hotline: Telefonnummer bitte   <!-- predicted: myths_vitamins_plants_minerals_homeopathy: Telefonnummer bitte -->
    - utter_germany_hotline   <!-- predicted: action_default_fallback -->


## germany_nomoney (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_nomoney: Was bietet mir das Hilfspaket, wenn ich meinen Kredit oder meine Versicherung nicht mehr bezahlen kann?   <!-- predicted: cc_philosophical: Was bietet mir das Hilfspaket, wenn ich meinen Kredit oder meine Versicherung nicht mehr bezahlen kann? -->
    - utter_germany_nomoney   <!-- predicted: utter_cc_philosophical -->


## germany_pandemic (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_pandemic: Pandemie in Deutschland   <!-- predicted: germany_consequences: Pandemie in Deutschland -->
    - utter_germany_pandemic   <!-- predicted: action_default_fallback -->


## germany_spread_water (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* germany_spread_water: Coronavirus und Reisen per Bahn   <!-- predicted: travel_general: Coronavirus und Reisen per Bahn -->
    - utter_germany_spread_water   <!-- predicted: utter_travel_general -->


## gradual_opening_cinema_concert_theatre (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* gradual_opening_cinema_concert_theatre: Was ist mit Friseuren   <!-- predicted: prevention_informed: Was ist mit Friseuren -->
    - utter_gradual_opening_cinema_concert_theatre   <!-- predicted: action_default_fallback -->


## mask_protection (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* mask_protection:    <!-- predicted: None:  -->
    - utter_mask_protection   <!-- predicted: action_default_fallback -->


## covid_current_situation_get_news (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_current_situation: Lage in - Wie ist die Situation in Kolumbien   <!-- predicted: covid_current_situation: Lage in - Wie ist die Situation in [Kolumbien]{"entity": "country_code", "value": "CO"} -->
    - slot{"country_code": "CO"}
    - action_get_news_request


## covid_current_situation_get_news_entity_country (/tmp/tmpe1t8rd5t/47ef77c16f704eec8ababf5f6a152bdf_conversation_tests.md)
* covid_current_situation: Was ist mit Bolivien?   <!-- predicted: covid_current_situation: Was ist mit [Bolivien]{"entity": "country_code", "value": "BO"}? -->
    - slot{"country_code": "BO"}
    - action_get_news_request


