## insight path
* greet
  - utter_greet
* retrieve
  - actionInsight

## addition path
* greet
  - utter_greet
* setConfig
  - utter_ask_key
* inputKey{"key": "profile"}
  - attribute_form
  - form{"name": "attribute_form"}
  - form{"name": null}
  
## preflight path
* greet
  - utter_greet
* doPreflight
  - preflightChecks

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot
