import json

from py2neo import Graph, Node, Relationship, NodeMatcher

graph = Graph("http://neo4j:neo4j@0127.0.0.1:7474")

selector = NodeMatcher(graph)


# test_properties = {
#     'id': '1',
#     'name': '陈远清',
#     '案件号': '（2017）浙1125刑初148号',
#     '职业': '无业',
#     '户籍所在地': '云和县凤凰山街道解放街202号',
#     '民族': '汉族',
#     '文化程度': '初中文化',
#     '出生日期': '1964年3月17日',
#     '毒品数量': '12.73克',
#     '出生地': '浙江省云和县',
#     '现住址': '云和县浮云街道象山村安置房',
#     '性别': '男',
# }

# a = Node(*['aa', 'bb'], **test_properties)
# # a = Node('aa', **test_properties)
# graph.create(a)
# graph.schema.create_uniqueness_constraint('被告人', 'id')


class MyNode(object):
    def __init__(self, node_dict):
        self.id = node_dict.get('id')
        self.labels = node_dict.get('labels')
        self._update_properties(node_dict.get("id"), node_dict.get('properties'))

    def _update_properties(self, id, properties):
        self.properties = properties
        self.properties['id'] = str(id)

    def __repr__(self) -> str:
        return str(self.__dict__)

    def get_node(self):
        return Node(**self.labels, **self.properties)


class MyRelation(object):
    def __init__(self, relation_dict):
        self.id = relation_dict.get('id')
        self.type = relation_dict.get('type')
        self.startNode = relation_dict.get('startNode')
        self.endNode = relation_dict.get('endNode')
        self._update_properties(relation_dict.get("id"), relation_dict.get('properties'))

    def _update_properties(self, id, properties):
        self.properties = properties
        self.properties['id'] = str(id)

    def __repr__(self) -> str:
        return str(self.__dict__)


with open('./neo4j_demo.json', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())

node_dict = {}  # 节点字典
relationship_dict = {}  # 关系字典
data = data.get('results')[0].get('data')

# 获取所有节点
for _graph in data:
    _graph = _graph.get('graph')
    for node in _graph.get('nodes'):
        n = MyNode(node)
        node_dict[str(n.id)] = n

relationship_dict = {}  # 关系字典
# 获取所有关系
for _graph in data:
    _graph = _graph.get('graph')
    for relation in _graph.get('relationships'):
        startNode = relation.get('startNode')
        endNode = relation.get('endNode')
        relationship_id = str(startNode) + '#' + str(endNode)
        relationship_dict[relationship_id] = MyRelation(relation)

for node_id, node in node_dict.items():
    graph.merge(Node(*node.labels, **node.properties), node.labels[0], "id")

for relationship_id, relationship in relationship_dict.items():
    start_node_id, end_node_id = relationship_id.split('#')
    start_node_labels = node_dict[start_node_id].labels
    end_node_labels = node_dict[end_node_id].labels
    existing_u1 = selector.match(*start_node_labels, id=start_node_id).first()
    existing_u2 = selector.match(*end_node_labels, id=end_node_id).first()
    r = Relationship(existing_u1, relationship.type, existing_u2, **relationship.properties)
    graph.create(r)


def create_graph():
    a = Node('被告人', **{
        "id": "1",
        "毒品数量": "12.73克",
        "职业": "无业",
        "户籍所在地": "云和县凤凰山街道解放街202号",
        "民族": "汉族",
        "文化程度": "初中文化",
        "出生日期": "1964年3月17日",
        "案件号": "（2017）浙1125刑初148号",
        "name": "陈远清",
        "出生地": "浙江省云和县",
        "现住址": "云和县浮云街道象山村安置房",
        "性别": "男"
    })

    b = Node('购买者', **{
        "id": "43",
        "name": "叶建飞"
    })

    r = Relationship(a, '售给', b, **{
        "id": "26",
        "种类": "甲基苯丙胺（冰毒）",
        "数量": "  ",
        "金额": " "
    })

    # print(a, b, r)
    graph.create(r)


if __name__ == '__main__':
    pass
    # create_graph()
