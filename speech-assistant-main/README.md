Vaghasiya, Om

DIT Chatbot - "DIT_JO"

## Project Description

This is a Bot which will give you information about the questions which you have in your mind. It will mainly help with the information on scholarship, job, volueentry work, course selection, club and accomodation. It is super easy to use and it will help you a lot.

The link to our Wiki's Homepage is : https://mygit.th-deg.de/assistance-systems/speech-assistant/-/wikis/home

## Installation

In order to use this chatbot offline on your personal system, follow the below steps:

- Download or clone this repository using following command:

```
git clone https://mygit.th-deg.de/assistance-systems/speech-assistant/
```

- Go to the cloned directory and install virtualenv package (if you don't have it already)

```
cd speech-assistant
pip install virtualenv
```

- Create a new virtual environment in current directory with specified version of Python and activate it

```
virtualenv "my_env_name" --python=python3.8
.\my_env_name\Scripts\activate.bat
```

`Note: Python3.8 is the recommanded Python version for this project. Install and add it to PATH incase there are any errors.`

- Next step is to install Rasa and train the model

## Basic Usage

- Next step is to install Rasa and train the model

```
pip install rasa
rasa train
```

- To connect port, open another terminal, activate virtual environment and run following command

```
rasa run actions
```

- Open previous terminal and enter following command to start interacting with chatbot

```
rasa shell
```

**Example dialog**

H - Hi

B - I am DIT_Jo bot and i .....

H - scholarship

B - Are you a student

H - yes

B - Go this link to find info

H - good

B - do you need more help

H - no

B - bye

H - goodbye

## Implementation of the Request

## Work 

Om Vaghasiya:

1. Worked on domain, nlu and stories.
2. Created example dialogs and converted it into a flow
3. Created critical user journeys and documented it.
4. Created test stories for model.
5. Created Wiki and added all the data.
6. Created a system and 3 user personas.
7. Created dialogs and converted it into a flow.
8. Creted rules for chatbot.
9. Implemented classes in actions for chatbot to reply accordingly.
10. Created a system and 3 user personas.
