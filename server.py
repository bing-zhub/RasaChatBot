from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)
tmp = """{
            "results": [
                {
                    "columns": [
                        "path"
                    ],
                    "data": [
                        {
                            "graph": {
                                "nodes": [
                                    {
                                        "id": "1",
                                        "labels": [
                                            "被告人"
                                        ],
                                        "properties": {
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
                                        }
                                    },
                                    {
                                        "id": "21",
                                        "labels": [
                                            "购买者"
                                        ],
                                        "properties": {
                                            "name": "项宗远"
                                        }
                                    }
                                ],
                                "relationships": [
                                    {
                                        "id": "20",
                                        "type": "售给",
                                        "startNode": "1",
                                        "endNode": "21",
                                        "properties": {
                                            "种类": "甲基苯丙胺（冰毒）",
                                            "数量": "  ",
                                            "金额": " "
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }],
            "errors": []
        }"""

@sio.on('connect')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('data')
async def message(sid, data):
    await sio.emit('reply', data)

@sio.on('disconnect')
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    web.run_app(app)