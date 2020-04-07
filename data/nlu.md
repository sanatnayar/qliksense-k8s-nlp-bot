## intent:greet
- hello
- hi
- good morning
- good evening
- hey

## intent:retrieve
 - I wanted to see my [CR](cluster_element)
 - Can I see my [CR](cluster_element)
 - Can I see the qliksense operator [CRD](cluster_element)
 - Can I see the qliksense operator [custom_resource_definition](cluster_element)
 - I wanted to see the [spec](cluster_element)
 - I wanted to see my [CR](cluster_element)
 - Can I see a [list](cluster_element) of my contexts
 - I want to see [all](cluster_element) my contexts
 - Show me [all](cluster_element) my configs
 - Can I see the [CR](cluster_element) 

## intent:retrieveCR
 - I wanted to see my CR
 - Can I see my CR
 - I wanted to see the spec
 - I wanted to see my CRi 
 - Can I see a [list](cluster_element) of my contexts
 - I want to see [all](cluster_element) my contexts
 - Show me [all](cluster_element) my configs
 - Can I see the [CR](cluster_element)


## intent:tutorial
 - Can I know more about [kubernetes] (technology)
 - I want some resources to learn more about [gke] (technology)
 - what is a [custom resource] (technology)
 - How can I learn more about 

## intent: inputKey
 - [ManifestsRoot](key)
 - [RotateKeys](key)
 - [StorageClass](key)
 - [NameSpace](key)
 - [Profile](key)
 - Change attribute [ManifestsRoot](key)
 - Change attribute [RotateKeys](key)
 - Change attribute [StorageClass](key)
 - Change attribute [NameSpace](key)
 - Change attribute [Profile](key)

 ## intent: inputValue
 - [gcp](value)
 - [aws](value)
 - [eks](value)

## intent: setConfig
 - I wish to add to my spec
 - I want to set an attribute in the custom resource
 - add to my cr spec
 - set an attribute
 - i want to change my cr
 - i want to edit my cr
 - i want to change to my spec
 - i want to edit my spec


## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yes
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?


## regex:value
- (.*?)