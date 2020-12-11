## quarantine_how_it_works (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* quarantine_how_it_works: Was ist bei einer Ausgangssperre zu tun?   <!-- predicted: quarantine_general: Was ist bei einer Ausgangssperre zu tun? -->
    - utter_quarantine_how_it_works   <!-- predicted: utter_quarantine_general -->


## covid_current_statistics_happy_path_state (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Wie viele Fälle gibt es in [Berlin](country_district)   <!-- predicted: covid_situation_infected: Wie viele Fälle gibt es in [Berlin]{"entity": "country_state", "value": " Berlin"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "ok"}
    - slot{"region": "Berlin"}
    - slot{"region_confirmed_accum": 130}
    - utter_covid_current_statistics_region


## covid_current_statistics_unhappy_empty_path_state_no (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
    - action_search_stats_region
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Leider nein.
    - utter_covid_no_country_current_statistics


## travel_return (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?   <!-- predicted: travel_return: Was muss ich beachten, wenn ich gerade in [Portugal]{"entity": "country_code", "value": "PT"} war? -->
    - slot{"country_code": "PT"}
    - utter_travel_return


## travel_while (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* travel_while: Was, wenn ich schon vor Ort bin?   <!-- predicted: bot_places: Was, wenn ich schon vor Ort bin? -->
    - utter_travel_while   <!-- predicted: action_default_fallback -->


## bot_animal (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* bot_animal: Welches Tier magst du am liebsten?   <!-- predicted: bot_pets: Welches Tier magst du am liebsten? -->
    - utter_bot_animal   <!-- predicted: utter_bot_pets -->


## covid_current_statistics_unhappy_not_ok_path_state_no (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
    - action_search_stats_region
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Unter keiner Bedingung.
    - utter_covid_no_country_current_statistics


## covid_current_statistics_unhappy_empty_path_state_yes (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
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


## covid_current_statistics_unhappy_not_ok_path_state_yes (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
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


## covid_current_statistics_happy_path_district (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "ok"}
    - slot{"region": "München"}
    - slot{"region_confirmed_accum": "130"}
    - utter_covid_current_statistics_region


## covid_current_statistics_unhappy_empty_path_district_yes (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
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


## covid_current_statistics_unhappy_not_ok_path_district_yes (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
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


## cc_fun_fact (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* cc_fun_fact: Interessante Tatsache.
    - utter_cc_fun_fact   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_path_empty_district_no (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Kommt nicht in die Tüte.
    - utter_covid_no_country_current_statistics


## covid_current_statistics_unhappy_path_not_ok_district_no (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Naa.
    - utter_covid_no_country_current_statistics


## start_1 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* start-dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false


## user_love (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* user_love: Bist Du noch single   <!-- predicted: bot_relationship: Bist Du noch single -->
    - utter_user_love   <!-- predicted: utter_bot_relationship -->


## user_particles (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* user_particles: okay   <!-- predicted: vocative_yes: okay -->
    - utter_user_particles   <!-- predicted: utter_vocative_yes -->


## corona_app_general (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* corona_app_general: Sage mir etwas über die Corona Warn App   <!-- predicted: corona_app_why: Sage mir etwas über die Corona Warn App -->
    - utter_corona_app_general   <!-- predicted: utter_corona_app_why -->


## covid_situation_without_country (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand sind in [Deutschland]{"entity": "country_code", "value": "DE"}?
    - slot{"country_code": "DE"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* vocative_yes: Ich habe keine Einwände.
    - utter_ask_which_country
* country: [Nippon]{"entity": "country_code", "value": "JP"}
    - slot{"country_code": "JP"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Frankreich"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_without_country2 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected_critical: Personen in kritischem Zustand in [Österreich]{"entity": "country_code", "value": "AT"}.
    - slot{"country_code": "AT"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* vocative_no: lieber nicht
    - utter_covid_no_country_current_statistics


## covid_situation_without_country3 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected_critical: Wieviele Personen in [China]{"entity": "country_code", "value": "CN"} sind im kritischen Zustand?
    - slot{"country_code": "CN"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* country: [moldova]{"entity": "country_code", "value": "MD"}
    - slot{"country_code": "MD"}
    - action_search_stats
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Italy"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_infected_unhappy (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_situation_infected: Krankheitsfälle in [Hessen]{"entity": "country_state", "value": " Hessen"}
    - action_search_stats   <!-- predicted: action_search_stats_region -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_dangerous (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_dangerous: Wie hoch ist das Risiko der Infektion?   <!-- predicted: germany_current_situation: Wie hoch ist das Risiko der Infektion? -->
    - utter_covid_dangerous   <!-- predicted: utter_germany_current_situation -->


## start1_1 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* start_dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - slot{"bot_introduced": "True"}
    - utter_greeting_hello_introduced_false


## covid_pregnancy (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* covid_pregnancy: Meine Freundin hat movit 19, was passiert jetzt?   <!-- predicted: covid_procedure_after_infection: Meine Freundin hat movit 19, was passiert jetzt? -->
    - utter_covid_pregnancy   <!-- predicted: utter_covid_procedure_after_infection -->


## germany_food_buy (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* germany_food_buy: Was muss ich einkaufen, wenn ich in Quarantäne bin   <!-- predicted: food_buy: Was muss ich einkaufen, wenn ich in Quarantäne bin -->
    - utter_germany_food_buy   <!-- predicted: action_default_fallback -->


## start_12 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* start: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## germany_food_shortages (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* germany_food_shortages: Muss ich mit Lebensmittelknappheit rechnen?   <!-- predicted: food_shortages: Muss ich mit Lebensmittelknappheit rechnen? -->
    - utter_germany_food_shortages   <!-- predicted: action_default_fallback -->


## start1_12 (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* start_dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## greeting_goodbye (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* greeting_goodbye: Servus!   <!-- predicted: greeting_hello: Servus! -->
    - utter_greeting_goodbye   <!-- predicted: action_check_bot_introduced -->


## mask_obligatory (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* mask_obligatory: Zuhause bleiben Arztbesuche   <!-- predicted: quarantine_general: Zuhause bleiben Arztbesuche -->
    - utter_mask_obligatory   <!-- predicted: utter_quarantine_general -->


## prevention_informed (/tmp/tmpal4xowjm/a914a179cee7459ca29fd2719abe7021_conversation_tests.md)
* prevention_informed: Warum ist es wichtig, informiert zu bleiben?   <!-- predicted: cc_philosophical: Warum ist es wichtig, informiert zu bleiben? -->
    - utter_prevention_informed   <!-- predicted: action_default_fallback -->


