import json

import requests
from py2neo import Graph, NodeMatcher
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

graph = Graph("http://neo4j:neo4j@127.0.0.1:7474")
selector = NodeMatcher(graph)


# MATCH path = (n)-[r]->(m) where n.案件号 =~ '.*浙1125刑初148号.*' RETURN path
def retrieveDataFromNeo4j(cyber):
    """
    Downloads a dictionary of a given cyber4

    Args:
        cyber: (todo): write your description
    """
    url = 'http://neo4j:neo4j@127.0.0.1:7474/db/data/transaction/commit'
    body = {"statements": [{"statement": cyber, "resultDataContents": ["graph"]}]}
    headers = {'content-type': "application/json; charset=utf-8"}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    return response.text


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
        Run a participant.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        if (case == None):
            dispatcher.utter_message("服务器开小差了")
            return []
        all_defendants = ""
        a = list(selector.match("被告人", 案件号__contains=case))
        for _ in a:
            if (a[a.__len__() - 1] == _):
                all_defendants = all_defendants + _['name'] + "."
            else:
                all_defendants = all_defendants + _['name'] + ','
        response = "{}案件, 有涉案人员:{}".format(case, all_defendants)
        dispatcher.utter_message(response)
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
        Run the utterances.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        if (case == None):
            dispatcher.utter_message("服务器开小差了")
            return []
        n = list(selector.match("被告人", 案件号__contains=case)).__len__()

        if (n == 0):
            response = "没有这个案件, 查证后再说吧~"
        else:
            response = "{}案件共有{}个涉案人员".format(case, n)
        graph_data = retrieveDataFromNeo4j("MATCH path = (n)-[r]->(m) where n.案件号 =~ '.*{}.*' RETURN path".format(case))
        dispatcher.utter_message(response)
        return [SlotSet('case', case)]


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
        item = tracker.get_slot('item')
        person = graph.nodes.match("被告人", name=defendant).first()
        response = "这个系统还够完善, 没有找到{}关于'{}'的信息, 抱歉哦..".format(defendant, item)
        if (item == None or defendant == None):
            dispatcher.utter_message("服务器开小差了")
            return []

        # < id >: 0
        # name: 张青红出生地: 浙江省云和县出生日期: 1979
        # 年8月14日性别: 女户籍所在地: 云和县凤凰山街道上前溪100号文化程度: 初中文化案件号: （2017）浙1125刑初148号毒品数量: 31.3
        # 克民族: 汉族现住址: 丽水市莲都区水阁工业区齐垵村20号2楼职业: 务工
        if item.find("个人资料") != -1:
            response = "{},{},{}生,户籍所在:{}, {}程度, 现住{}, 贩毒{}".format(defendant, person['性别'], person['出生日期'],
                                                                    person['户籍所在地'], person['文化程度'], person['现住址'],
                                                                    person['毒品数量'])
        elif item.find("出生地") != -1:
            response = "{}的出生地是{}".format(defendant, person['出生地'])
        elif item.find("生日") != -1:
            response = "{}的生日是{}".format(defendant, person['出生日期'])
        elif item.find("性别") != -1:
            response = "{}的性别是:{}".format(defendant, person['性别'])
        elif item.find("户籍所在地") != -1:
            response = "{}的户籍所在地是:{}".format(defendant, person['户籍所在地'])
        elif item.find("文化程度") != -1:
            response = "{}的文化程度是:{}".format(defendant, person['文化程度'])
        elif item.find("贩毒量") != -1:
            response = "{}的贩毒量是:{}".format(defendant, person['毒品数量'])
        elif item.find("民族") != -1:
            response = "{}的民族是:{}".format(defendant, person['民族'])
        elif item.find("现住址") != -1:
            response = "{}的现住址是:{}".format(defendant, person['现住址'])
        elif item.find("职业") != -1:
            response = "{}的职业是:{}".format(defendant, person['职业'])

        graph_data = retrieveDataFromNeo4j(
            "MATCH path = (n)-[r]->(m) where n.name =~ '.*{}.*' RETURN path".format(defendant))
        dispatcher.utter_message(response)
        return [SlotSet('defendant', defendant)]


# 查看案件详情
class ViewCaseDetail(Action):  # TODO
    def name(self):
        """
        Return the name for this node.

        Args:
            self: (todo): write your description
        """
        return 'action_view_case_detail'

    def run(self, dispatcher, tracker, domain):
        """
        Runs : class.

        Args:
            self: (todo): write your description
            dispatcher: (todo): write your description
            tracker: (todo): write your description
            domain: (str): write your description
        """
        case = tracker.get_slot('case')
        if (case == None):
            dispatcher.utter_message("服务器开小差了")
            return []
        found = graph.nodes.match("被告人", 案件号__contains=case)
        n = list(found).__len__()
        if (n == 0):
            response = "没有找到这个案件, 是不是案件号错了"
        else:
            graph_data = retrieveDataFromNeo4j(
                "MATCH path = (n)-[r]->(m) where n.案件号 =~ '.*{}.*' RETURN path".format(case))
        dispatcher.utter_message(response)
        return [SlotSet('case', case)]


if __name__ == '__main__':
    selector = NodeMatcher(graph)
    all_defendants = ""
    a = list(selector.match("被告人", 案件号__endswith="浙1125刑初148号"))
    for _ in a:
        if (a[a.__len__() - 1] == _):
            all_defendants = all_defendants + _['name'] + "."
        else:
            all_defendants = all_defendants + _['name'] + ','

    print(all_defendants)
