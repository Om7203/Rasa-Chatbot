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

Basically we checked for the right fit for the persona
We have one system persona and 3 user persona which was done with the discussion between both the students.
We have made 6 use cases and we have added that in our use-cases in our wiki although you can find more in the code.
We have found the technical prerequisites and added in our wiki.
Example dilogs are there in the the dialog flow in the wiki and you can find more in the wiki.
A overall dialog flow is created in the dialog flow section in wiki.
Starting the code you will find different files with names different extensions as yml and python that runs the bot where the data is stored.

## Work done

Om Vaghasiya:

1. Worked on domain, nlu and stories.
2. Created example dialogs and converted it into a flow
3. Created critical user journeys and documented it.
4. Created test stories for model.
5. Created Wiki and added all the data.
6. Created a system and 3 user personas.(helped each other)

Jenil Kevadiya:

1. Worked on domain, nlu and stories.
2. Created dialogs and converted it into a flow.
3. Creted rules for chatbot.
4. Implemented classes in actions for chatbot to reply accordingly.
5. Created a system and 3 user personas.(helped each other)

Overall, both helped each other at every step and guided each other and have created this project.
