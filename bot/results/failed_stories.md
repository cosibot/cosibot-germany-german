## covid_current_statistics_happy_path_state (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Wie viele Fälle gibt es in [Berlin](country_district)   <!-- predicted: covid_situation_infected: Wie viele Fälle gibt es in [Berlin]{"entity": "country_state", "value": " Berlin"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "ok"}
    - slot{"region": "Berlin"}
    - slot{"region_confirmed_accum": 130}
    - utter_covid_current_statistics_region


## test_how (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* test_how: Wie funktioniert der Test   <!-- predicted: test_per_day: Wie funktioniert der Test -->
    - utter_test_how   <!-- predicted: utter_test_per_day -->


## covid_current_statistics_unhappy_empty_path_state_no (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
    - action_search_stats_region
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Leider nein.
    - utter_covid_no_country_current_statistics


## travel_return (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* travel_return: Was muss ich beachten, wenn ich gerade in Portugal war?   <!-- predicted: travel_return: Was muss ich beachten, wenn ich gerade in [Portugal]{"entity": "country_code", "value": "PT"} war? -->
    - slot{"country_code": "PT"}
    - utter_travel_return


## bot_animal (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* bot_animal: Welches Tier magst du am liebsten?
    - utter_bot_animal   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_not_ok_path_state_no (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Wie viele Menschen sind in [Thüringen](country_state) gestorben   <!-- predicted: covid_situation_infected: Wie viele Menschen sind in [Thüringen]{"entity": "country_state", "value": " Th\u00fcringen"} gestorben -->
    - action_search_stats_region
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Bremen"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Unter keiner Bedingung.
    - utter_covid_no_country_current_statistics


## bot_author (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* bot_author: Was ist dein Lieblingsautor?   <!-- predicted: bot_books: Was ist dein Lieblingsautor? -->
    - utter_bot_author   <!-- predicted: action_default_fallback -->


## bot_developers (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* bot_developers: wer hat dich gebaut
    - utter_bot_developers   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_empty_path_state_yes (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
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


## bot_gender (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* bot_gender: Bist du ein Mädchen   <!-- predicted: cc_drugs: Bist du ein Mädchen -->
    - utter_bot_gender   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_not_ok_path_state_yes (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
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


## covid_current_statistics_happy_path_district (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "ok"}
    - slot{"region": "München"}
    - slot{"region_confirmed_accum": "130"}
    - utter_covid_current_statistics_region


## covid_current_statistics_unhappy_empty_path_district_yes (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
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


## covid_current_statistics_unhappy_not_ok_path_district_yes (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
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


## cc_geography (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* cc_geography: Wo ist [China]{"entity": "country_code", "value": "CN"}?
    - slot{"country_code": "CN"}
    - utter_cc_geography   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_path_empty_district_no (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "empty"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Kommt nicht in die Tüte.
    - utter_covid_no_country_current_statistics


## cc_make_weather (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* cc_make_weather: Könnten Sie das Wetter ändern?   <!-- predicted: cc_keys: Könnten Sie das Wetter ändern? -->
    - utter_cc_make_weather   <!-- predicted: action_default_fallback -->


## covid_current_statistics_unhappy_path_not_ok_district_no (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Todesfälle in [Darmstadt](country_district)   <!-- predicted: covid_situation_infected: Todesfälle in [Darmstadt]{"entity": "country_district", "value": " Darmstadt"} -->
    - action_search_stats_region
    - slot{"region_search_successful": "not-ok"}
    - slot{"region": "Frankfurt"}
    - slot{"country_code": "DE"}
    - utter_region_nodata
* vocative_no: Naa.
    - utter_covid_no_country_current_statistics


## start_1 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* start-dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - slot{"bot_introduced": true}
    - utter_greeting_hello_introduced_false


## vocative_no (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* vocative_no: Nichts.   <!-- predicted: nothingmore: Nichts. -->
    - utter_vocative_no   <!-- predicted: action_default_fallback -->


## covid_situation_without_country (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand sind in [Deutschland]{"entity": "country_code", "value": "DE"}?
    - slot{"country_code": "DE"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* vocative_yes: Ich habe keine Einwände.
    - utter_ask_which_country
* country: Nippon   <!-- predicted: country: [Nippon]{"entity": "country_code", "value": "JP"} -->
    - slot{"country_code": "JP"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Frankreich"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_without_country2 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected_critical: Personen in kritischem Zustand in [Österreich]{"entity": "country_code", "value": "AT"}.
    - slot{"country_code": "AT"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* vocative_no: lieber nicht
    - utter_covid_no_country_current_statistics


## covid_situation_without_country3 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected_critical: Wieviele Personen in [China]{"entity": "country_code", "value": "CN"} sind im kritischen Zustand?
    - slot{"country_code": "CN"}
    - utter_want_to_add_country   <!-- predicted: action_search_stats -->
* country: moldova   <!-- predicted: country: [moldova]{"entity": "country_code", "value": "MD"} -->
    - slot{"country_code": "MD"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Italy"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_infected_unhappy (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Krankheitsfälle in [Hessen]{"entity": "country_state", "value": " Hessen"}
    - action_search_stats   <!-- predicted: action_search_stats_region -->
    - slot{"search_successful": "not-ok"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_unhappy_with_country (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Wie viele Infizierte gibt es in [Neuseeland]{"entity": "country_code", "value": "NZ"}
    - slot{"country_code": "NZ"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Akzeptiere.
    - utter_ask_which_country
* country: Kiribati   <!-- predicted: country: [Kiribati]{"entity": "country_code", "value": "KI"} -->
    - slot{"country_code": "KI"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Portugal"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected


## covid_situation_unhappy_inexistent_country (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected: Wie sind die Fallzahlen in [Österreich]{"entity": "country_code", "value": "AT"}
    - slot{"country_code": "AT"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ja, gern.
    - utter_ask_which_country
* country: Gambia   <!-- predicted: country: [Gambia]{"entity": "country_code", "value": "GM"} -->
    - slot{"country_code": "GM"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## covid_situation_infected_critical_unhappy_with_country (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Menschen befinden sich in [Italien]{"entity": "country_code", "value": "IT"} in kritischem Zustand
    - slot{"country_code": "IT"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Ich habe nichts dagegen.
    - utter_ask_which_country
* country: Cuba   <!-- predicted: country: [Cuba]{"entity": "country_code", "value": "CU"} -->
    - slot{"country_code": "CU"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "ok"}
    - slot{"active_cases": "16300"}
    - slot{"country": "Espanha"}
    - slot{"total_infected_critical": "176"}
    - slot{"total_deaths": "32"}
    - utter_covid_situation_infected_critical   <!-- predicted: utter_covid_situation_infected -->


## covid_situation_infected_critical_unhappy_inexistent_country (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_situation_infected_critical: Wie viele Personen in kritischem Zustand in [England]{"entity": "country_code", "value": "GB"}?
    - slot{"country_code": "GB"}
    - action_search_stats
    - slot{"search_successful": "wrong-country"}
    - utter_want_to_add_country
* vocative_yes: Jap.
    - utter_ask_which_country
* country: Paraguay   <!-- predicted: country: [Paraguay]{"entity": "country_code", "value": "PY"} -->
    - slot{"country_code": "PY"}
    - action_search_stats   <!-- predicted: utter_want_to_add_country -->
    - slot{"search_successful": "inexistent-country"}
    - utter_covid_no_country_current_statistics


## start1_1 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* start_dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - slot{"bot_introduced": "True"}
    - utter_greeting_hello_introduced_false   <!-- predicted: action_listen -->


## covid_pregnancy (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* covid_pregnancy: Meine Freundin hat movit 19, was passiert jetzt?   <!-- predicted: covid_procedure_after_infection: Meine Freundin hat movit 19, was passiert jetzt? -->
    - utter_covid_pregnancy   <!-- predicted: utter_covid_procedure_after_infection -->


## germany_food_buy (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* germany_food_buy: Was muss ich einkaufen, wenn ich in Quarantäne bin   <!-- predicted: quarantine_dos_and_donts: Was muss ich einkaufen, wenn ich in Quarantäne bin -->
    - utter_germany_food_buy   <!-- predicted: utter_quarantine_dos_and_donts -->


## start_12 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* start: /start-dialogue   <!-- predicted: start-dialogue: /start-dialogue -->
    - action_check_bot_introduced
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## germany_food_shortages (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* germany_food_shortages: Muss ich mit Lebensmittelknappheit rechnen?   <!-- predicted: prevention_supermarket: Muss ich mit Lebensmittelknappheit rechnen? -->
    - utter_germany_food_shortages   <!-- predicted: action_default_fallback -->


## germany_hotline (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* germany_hotline: Wen kann ich anrufen?   <!-- predicted: covid_preexisting_illness: Wen kann ich anrufen? -->
    - utter_germany_hotline   <!-- predicted: utter_covid_preexisting_illness -->


## start1_12 (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* start_dialogue:    <!-- predicted: None:  -->
    - action_check_bot_introduced   <!-- predicted: action_default_fallback -->
    - action_listen   <!-- predicted: utter_greeting_hello_introduced_false -->


## greeting_goodbye (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* greeting_goodbye: Servus!   <!-- predicted: greeting_hello: Servus! -->
    - utter_greeting_goodbye   <!-- predicted: action_check_bot_introduced -->


## mask_protection (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* mask_protection: Mundschutz Masken   <!-- predicted: mask_obligatory: Mundschutz Masken -->
    - utter_mask_protection   <!-- predicted: action_default_fallback -->


## myths_chinese_laboratory (/tmp/tmpcu239shs/db08c4c3996b4153afb3575e17531c2e_conversation_tests.md)
* myths_chinese_laboratory: Das Coronavirus ist eine Biowaffe   <!-- predicted: myths_conspiracy_fakenews: Das Coronavirus ist eine Biowaffe -->
    - utter_myths_chinese_laboratory   <!-- predicted: utter_myths_conspiracy_fakenews -->


