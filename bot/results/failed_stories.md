## quarantine_how_it_works (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* quarantine_how_it_works:    <!-- predicted: None:  -->
    - utter_quarantine_how_it_works   <!-- predicted: action_default_fallback -->


## quarantine_when_who_howlong (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* quarantine_when_who_howlong: Unter welchen Umständen muss man mit Quarantäne rechnen?
    - utter_quarantine_when_who_howlong   <!-- predicted: action_default_fallback -->


## sources (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* sources: Woher sind deine Informationen?
    - utter_sources   <!-- predicted: action_default_fallback -->


## covid_current_statistics_happy_path_state (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen weltweit sind mit dem Virus infiziert
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "ok"}
    - slot{"region": "Berlin"}
    - slot{"region_confirmed_accum": 130}
    - utter_covid_current_statistics_region


## spread_surfaces_food_objects (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* spread_surfaces_food_objects: Kann ich mit dem Auto noch in den Nachbarort?   <!-- predicted: germany_neighbors_close_borders: Kann ich mit dem Auto noch in den Nachbarort? -->
    - utter_spread_surfaces_food_objects   <!-- predicted: utter_germany_neighbors_close_borders -->


## test_how (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* test_how:    <!-- predicted: None:  -->
    - utter_test_how   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_empty_path_state_no (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: COVID-19 Fälle nach Altersgruppe und Geschlecht
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Eigentlich nicht
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_vocative_no -->


## travel_return (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?   <!-- predicted: travel_return: Was muss ich beachten, wenn ich gerade in [Portugal]{"entity": "country_code", "value": "PT"} war? -->
    - slot{"country_code": "PT"}
    - utter_travel_return


## covid_current_statistics_unhappy_not_ok_path_state_no (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: wie viele Menschen sind in Deutschland betroffen
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Keinesfalls.
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_vocative_no -->


## covid_current_statistics_unhappy_empty_path_state_yes (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Infizierte gibt es in Baden-Württemberg   <!-- predicted: covid_situation_infected: Wie viele Infizierte gibt es in [Baden-Württemberg](country_state) -->
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_yes: Machen Sie das.
    - action_search_stats   <!-- predicted: utter_vocative_yes -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Deutschland"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## bot_games (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* bot_games: Magst du Computerspiele   <!-- predicted: bot_hobbies: Magst du Computerspiele -->
    - utter_bot_games   <!-- predicted: utter_bot_hobbies -->


## covid_current_statistics_unhappy_not_ok_path_state_yes (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wo finde ich aktuelle Zahlen?
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_yes: Wie Sie wollen.
    - action_search_stats   <!-- predicted: utter_vocative_yes -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Deutschland"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_current_statistics_happy_path_district (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind am Virus gestorben
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "ok"}
    - slot{"region": "München"}
    - slot{"region_confirmed_accum": "130"}
    - utter_covid_current_statistics_region


## bot_series (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* bot_series: Was ist deine Lieblingsserie?   <!-- predicted: bot_movies: Was ist deine Lieblingsserie? -->
    - utter_bot_series   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_empty_path_district_yes (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Anzahl der Toten in Brasilien   <!-- predicted: covid_situation_infected: Anzahl der Toten in [Brasilien]{"entity": "country_code", "value": "BR"} -->
    - slot{"country_code": "BR"}
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_yes: Alle Mal.
    - action_search_stats   <!-- predicted: utter_vocative_yes -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Deutschland"}
    - slot{"total_infected_critical": "176"}
    - utter_covid_situation_infected


## bot_worst_experience (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* bot_worst_experience: Was machst du morgens?   <!-- predicted: features_date: Was machst du morgens? -->
    - utter_bot_worst_experience   <!-- predicted: action_get_date -->


## covid_current_statistics_unhappy_not_ok_path_district_yes (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: wie schauen die zahlen in Frankreich aus   <!-- predicted: covid_situation_infected: wie schauen die zahlen in [Frankreich]{"entity": "country_code", "value": "FR"} aus -->
    - slot{"country_code": "FR"}
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_yes: Haargenau.
    - action_search_stats   <!-- predicted: utter_vocative_yes -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Deutschland"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_current_statistics_unhappy_path_empty_district_no (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Weißt du wie viele Erkrankte es weltweit gibt?
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Nicht wirklich
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_vocative_no -->


## covid_current_statistics_unhappy_path_not_ok_district_no (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in Indien gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Indien]{"entity": "country_code", "value": "IN"} gestorben -->
    - slot{"country_code": "IN"}
    - action_search_stats_region   <!-- predicted: utter_want_to_add_country -->
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Nee.
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_vocative_no -->


## cc_story (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* cc_story: Ich will einen Klatsch.   <!-- predicted: cc_joke: Ich will einen Klatsch. -->
    - utter_cc_story   <!-- predicted: utter_cc_joke -->


## user_tired (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* user_tired: Ich bin fast tot
    - utter_user_tired   <!-- predicted: action_default_fallback -->


## comment_smart (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* comment_smart: Wie intelligent!   <!-- predicted: bot_intelligence: Wie intelligent! -->
    - utter_comment_smart   <!-- predicted: utter_bot_intelligence -->


## covid_situation_without_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Wie lange bleiben die Viren auf den Oberflächen?   <!-- predicted: germany_preparation: Wie lange bleiben die Viren auf den Oberflächen? -->
    - utter_want_to_add_country   <!-- predicted: action_default_fallback -->
* vocative_yes: Ich stimme zu.
    - utter_ask_which_country
* country: zimbabwe   <!-- predicted: country: [zimbabwe]{"entity": "country_code", "value": "ZW"} -->
    - slot{"country_code": "ZW"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Frankreich"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected   <!-- predicted: utter_covid_situation_infected_critical -->


## covid_situation_without_country2 (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele kritische Fälle in Tschechien?   <!-- predicted: covid_situation_infected_critical: Wie viele kritische Fälle in [Tschechien]{"entity": "country_code", "value": "CZ"}? -->
    - slot{"country_code": "CZ"}
    - utter_want_to_add_country   <!-- predicted: utter_covid_situation_infected_critical -->
* vocative_no: Nicht im Entferntesten.
    - utter_further_questions


## covid_situation_without_country3 (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Kritischer Zustand in Russland.   <!-- predicted: covid_situation_infected_critical: Kritischer Zustand in [Russland]{"entity": "country_code", "value": "RU"}. -->
    - slot{"country_code": "RU"}
    - utter_want_to_add_country   <!-- predicted: utter_covid_situation_infected_critical -->
* country: Benin   <!-- predicted: country: [Benin]{"entity": "country_code", "value": "BJ"} -->
    - slot{"country_code": "BJ"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Italy"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_infected_happy (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: fallzahlen
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_infected_unhappy (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen infizieren sich täglich neu in Deutschland?
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_unhappy_with_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Gibt es offizielle Zahlen zu den Erkrankungen weltweit?
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Na klar!
    - utter_ask_which_country
* country: senegal   <!-- predicted: country: [senegal]{"entity": "country_code", "value": "SN"} -->
    - slot{"country_code": "SN"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected   <!-- predicted: utter_covid_situation_infected_critical -->


## covid_situation_unhappy_inexistent_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele haben sich weltweit angesteckt
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: In Butter.
    - utter_ask_which_country
* country: La Réunion   <!-- predicted: country: [La Réunion]{"entity": "country_code", "value": "RE"} -->
    - slot{"country_code": "RE"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## covid_situation_unhappy_with_dashboard (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in Köln gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Köln](country_district) gestorben -->
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "False"}
    - utter_want_to_add_country
* vocative_no: Nie.
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_further_questions -->


## covid_situation_infected_critical_happy (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in England?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in [England]{"entity": "country_code", "value": "GB"}? -->
    - slot{"country_code": "GB"}
    - action_search_stats   <!-- predicted: utter_covid_situation_infected_critical -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Spain"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected_critical


## covid_situation_infected_critical_unhappy (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Personen in einem kritischen Fall in Türkei.   <!-- predicted: covid_situation_infected_critical: Personen in einem kritischen Fall in [Türkei]{"entity": "country_code", "value": "TR"}. -->
    - slot{"country_code": "TR"}
    - action_search_stats   <!-- predicted: utter_covid_situation_infected_critical -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_unhappy_with_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Können die Viren auf Haltestangen überleben?   <!-- predicted: test_per_day: Können die Viren auf Haltestangen überleben? -->
    - action_search_stats   <!-- predicted: utter_test_per_day -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ohne Frage.
    - utter_ask_which_country
* country: Christmas Island   <!-- predicted: country: [Christmas Island]{"entity": "country_code", "value": "CX"} -->
    - slot{"country_code": "CX"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected_critical


## covid_situation_infected_critical_unhappy_inexistent_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen befinden sich in Kanada in einem kritischen Zustand?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen befinden sich in [Kanada]{"entity": "country_code", "value": "CA"} in einem kritischen Zustand? -->
    - slot{"country_code": "CA"}
    - action_search_stats   <!-- predicted: utter_covid_situation_infected_critical -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ja, genau.
    - utter_ask_which_country
* country: Hungary   <!-- predicted: country: [Hungary]{"entity": "country_code", "value": "HU"} -->
    - slot{"country_code": "HU"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_unhappy_with_dashboard (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Was ist die Lebensdauer der Coronaviren?   <!-- predicted: cc_afterlife: Was ist die Lebensdauer der Coronaviren? -->
    - action_search_stats   <!-- predicted: utter_cc_afterlife -->
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_no: nein
    - utter_covid_no_country_current_statistics   <!-- predicted: utter_further_questions -->


## start1_1 (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* start_dialogue: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - slot{"bot_introduced": "True"}
    - utter_greeting_hello_introduced_false   <!-- predicted: action_listen -->


## covid_procedure_after_infection (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_procedure_after_infection:    <!-- predicted: None:  -->
    - utter_covid_procedure_after_infection   <!-- predicted: action_default_fallback -->


## covid_situation_infected (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen infizieren sich täglich in Deutschland?
    - utter_covid_situation_infected   <!-- predicted: utter_want_to_add_country -->


## covid_situation_infected_critical (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen befinden sich in einem kritischen Zustand in England?   <!-- predicted: covid_situation_infected_critical: Wie viele Personen befinden sich in einem kritischen Zustand in [England]{"entity": "country_code", "value": "GB"}? -->
    - slot{"country_code": "GB"}
    - utter_covid_situation_infected_critical


## covid_unknown_cases (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_unknown_cases:    <!-- predicted: None:  -->
    - utter_covid_unknown_cases   <!-- predicted: action_default_fallback -->


## start_12 (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* start: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## germany_spread_water (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* germany_spread_water: Coronavirus und Reisen per Bahn   <!-- predicted: travel_general: Coronavirus und Reisen per Bahn -->
    - utter_germany_spread_water   <!-- predicted: utter_travel_general -->


## gradual_opening_cinema_concert_theatre (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* gradual_opening_cinema_concert_theatre: Was ist mit Friseuren   <!-- predicted: gradual_opening_restaurants: Was ist mit Friseuren -->
    - utter_gradual_opening_cinema_concert_theatre   <!-- predicted: action_default_fallback -->


## mask_protection (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* mask_protection:    <!-- predicted: None:  -->
    - utter_mask_protection   <!-- predicted: action_default_fallback -->


## covid_current_situation_get_news (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_current_situation: Lage in - Wie ist die Situation in Kolumbien   <!-- predicted: covid_current_situation: Lage in - Wie ist die Situation in [Kolumbien]{"entity": "country_code", "value": "CO"} -->
    - slot{"country_code": "CO"}
    - action_get_news_request


## covid_current_situation_get_news_entity_country (/tmp/tmpio32nte8/1bd0cb70da1f4769bcc30db727863fbf_conversation_tests.md)
* covid_current_situation: Was ist mit Bolivien?   <!-- predicted: covid_current_situation: Was ist mit [Bolivien]{"entity": "country_code", "value": "BO"}? -->
    - slot{"country_code": "BO"}
    - action_get_news_request


