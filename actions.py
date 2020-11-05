from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet


# 查看案例被告
class ViewCaseDefendants(Action):
    def name(self):
        """
        Return the name for this node.

        Args:
            self: (todo): write your description
        """
        return 'action_view_case_defendants'

    def run(self, dispatcher, tracker, domain):
        """
        Run the given slot.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        dispatcher.utter_message("[查询案件被告人, ViewCaseDefendants中进行更新] - " + case)
        return [SlotSet('case', case)]


# 查看涉案人员
class ViewCaseDefendantsNum(Action):
    def name(self):
        """
        Return the name for this node.

        Args:
            self: (todo): write your description
        """
        return 'action_view_case_defendants_num'

    def run(self, dispatcher, tracker, domain):
        """
        Run the given domain.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        dispatcher.utter_message("[查询涉案人员数目, ViewCaseDefendantsNum中进行更新] - " + case)


# 查看被告信息
class ViewDefendantData(Action):
    def name(self):
        """
        Return the name for this node.

        Args:
            self: (todo): write your description
        """
        return 'action_view_defendant_data'

    def run(self, dispatcher, tracker, domain):
        """
        Runs a participant.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        defendant = tracker.get_slot('defendant')
        dispatcher.utter_message("[查询涉案人员信息, ViewDefendantData中进行更新] - " + defendant)
        return [SlotSet('defendant', defendant)]


# 查看案件详情
class ViewCaseDetail(Action):
    def name(self):
        """
        Return the name for this node.

        Args:
            self: (todo): write your description
        """
        return 'action_view_case_detail'

    def run(self, dispatcher, tracker, domain):
        """
        Run the given slot.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        dispatcher.utter_message("[查询案件详情, ViewCaseDetail中进行更新] - " + case)
        return [SlotSet('case', case)]
