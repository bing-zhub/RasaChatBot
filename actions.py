from rasa_core.actions.action import Action
from rasa_core.events import SlotSet

class ActionCriminal(Action):
  def name(self):
    return "actions_criminal"

  def run(self, dispacher, tracker, domain):
    case_id = tracker.get_slot('case_id')
    response = "案件号为" + case_id +", 处理别忘了加哦"
    dispacher.utter_message(response)
    return [SlotSet('case_id', case_id)]
