# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionScholarship(Action):
    def name(self) -> Text:
        return "action_scholarship"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Question regarding scholarship in 'Deggendorf Institute of Technology' for students: https://www.th-deg.de/en/study-with-us/funding"
        )

        return []


class ActionScholarshipRequirements(Action):
    def name(self) -> Text:
        return "action_scholarship_requirements"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="this depends on each case and on each study programme. Please send an email to welcome@th-deg.de  "
        )

        return []


class ActionUniWebsite(Action):
    def name(self) -> Text:
        return "action_uni_website"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The official website of the Deggendorf Institute of Technology is: https://www.th-deg.de"
        )

        return []


class ActionAccomodation(Action):
    def name(self) -> Text:
        return "action_accomodation"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The website for the Accomodation in Deggendorf Institute of Technology is: https://www.th-deg.de/en/study-with-us/accommodation"
        )

        return []


class ActionVoluentrywork(Action):
    def name(self) -> Text:
        return "action_voluentry_work"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The website for the Voluentry work in Deggendorf Institute of Technology is: https://www.th-deg.de/study-support"
        )

        return []


class ActionStartingBusiness(Action):
    def name(self) -> Text:
        return "action_starting_business"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="The website for Starting Bussiness in Deggendorf Institute of Technology is: https://www.th-deg.de/starting-a-business"
        )

        return []


class ActionLanguageCourses(Action):
    def name(self) -> Text:
        return "action_language_courses"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="You can find all the information about the language courses at the Deggendorf Institute of Technology here: https://www.th-deg.de/language-and-electives-centre"
        )

        return []


class ActionAvailableCourses(Action):
    def name(self) -> Text:
        return "action_available_courses"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To find more about the courses offered at the Deggendorf Institute of Technology, please visit: https://www.th-deg.de/study-programmes"
        )

        return []


class ActionAvailableJob(Action):
    def name(self) -> Text:
        return "action_available_job"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="To find more about the job offered at the Deggendorf Institute of Technology, please visit: https://www.th-deg.de/en/students/career"
        )

        return []


class ActionCareerService(Action):
    def name(self) -> Text:
        return "action_career_service"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Please use this email to contact the career service: stefanie.moeginger@th-deg.de"
        )

        return []


class ActionAskingEverythingOk(Action):
    def name(self) -> Text:
        return "action_asking_everything_ok"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(
            text="Do you need any more assistance? If you have further questions to the Deggendorf Institute of Technology, feel free to ask. Otherwise, goodbye and best of luck!"
        )

        return []


class ActionClubSelection(Action):
    def name(self) -> Text:
        return "action_club_selection"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="There are many different clubs available")

        return []
