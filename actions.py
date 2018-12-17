from py2neo import Graph
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet



class viewCaseDefendants(Action):
    def name(self):
        return 'action_view_case_defendants'

    def run(self, dispatcher, tracker, domain):
        case = tracker.get_slot('case')

        response = "-----action----查看所有涉案人员, 案件号:{}".format(case)
        dispatcher.utter_message(response)
        return [SlotSet('case', case)]


class viewCaseDefendantsNum(Action):
    def name(self):
        return 'action_view_case_defendants_num'

    def run(self, dispatcher, tracker, domain):
        case = tracker.get_slot('case')

        response = "-----action----查看所有涉案人数, 案件号:{}".format(case)
        dispatcher.utter_message(response)
        return [SlotSet('case', case)]


class viewDefendantData(Action):
    def name(self):
        return 'action_view_defendant_data'

    def run(self, dispatcher, tracker, domain):
        graph = Graph("http://neo4j:admin@localhost:7474")
        defendant = tracker.get_slot('defendant')
        item = tracker.get_slot('item')
        print(defendant)
        person = graph.nodes.match("被告人", name=defendant).first()
        response = "-----action----{}, {}".format(defendant, item)
        # < id >: 0
        # name: 张青红出生地: 浙江省云和县出生日期: 1979
        # 年8月14日性别: 女户籍所在地: 云和县凤凰山街道上前溪100号文化程度: 初中文化案件号: （2017）浙1125刑初148号毒品数量: 31.3
        # 克民族: 汉族现住址: 丽水市莲都区水阁工业区齐垵村20号2楼职业: 务工
        if item == "个人资料":
            response = "{},{}生,户籍所在:{}, :".format(defendant, person['出生日期'], person['户籍所在地'])
        elif item == "出生地":
            response = "{}的出生地是{}:".format(defendant, person['出生地'])
        elif item == "生日":
            response = "{}的生日是{}".format(defendant, person['出生日期'])
        elif item == "性别":
            response = "{}的性别是{}:".format(defendant, person['性别'])
        elif item == "户籍所在地":
            response = "{}的户籍所在地是{}:".format(defendant, person['户籍所在地'])
        elif item == "文化程度":
            response = "{}的文化程度是{}:".format(defendant, person['文化程度'])
        elif item == "贩毒量":
            response = "{}的贩毒量是{}:".format(defendant, person['毒品数量'])
        elif item == "民族":
            response = "{}的民族是{}:".format(defendant, person['民族'])
        elif item == "现住址":
            response = "{}的现住址是{}:".format(defendant, person['现住址'])
        elif item == "职业":
            response = "{}的职业是{}:".format(defendant, person['职业'])


        dispatcher.utter_message(response)
        return [SlotSet('defendant', defendant)]


if __name__ == '__main__':
    # data = graph.match("购买人")
    # for rel in data:
    print(graph.nodes.match("被告人", name="张青红").first()['出生日期'])
