from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class viewCaseDefendants(Action):
	def name(self):
		return 'action_view_case_defendants'
		
	def run(self, dispatcher, tracker, domain):
		case = tracker.get_slot('case')
	
		response = "-----action----查看所有涉案人员, 案件号:{}".format(case)
		dispatcher.utter_message(response)
		return [SlotSet('case',case)]

class viewCaseDefendantsNum(Action):
	def name(self):
		return 'action_view_case_defendants_num'
		
	def run(self, dispatcher, tracker, domain):
		case = tracker.get_slot('case')
	
		response = "-----action----查看所有涉案人数, 案件号:{}".format(case)
		dispatcher.utter_message(response)
		return [SlotSet('case',case)]

class viewDefendantData(Action):
	def name(self):
		return 'action_view_defendant_data'
	
	def run(self, dispatcher, tracker, domain):
		defendant = tracker.get_slot('defendant')
		item = tracker.get_slot('item')
		# if item == "出生地":
		# response = "-----action----{}, {}".format(defendant,item)
		# elif item == "生日":
		# elif item == "个人资料":
		# elif item == "性别":
		# elif item == "户籍所在地":
		# elif item == "文化程度":
		# elif item == "贩毒量":
		# elif item == "民族":
		# elif item == "现住址":
		# elif item == "职业":
		response = "-----action----{}, {}".format(defendant,item)		
		dispatcher.utter_message(response)
		return [SlotSet('defendant', defendant)]
