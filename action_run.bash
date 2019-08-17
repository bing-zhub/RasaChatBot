#!/usr/bin/env bash

# 无需后端neo4j 后端支持
python -m rasa_core_sdk.endpoint --actions actions

# 带neo4j后端支持，需要先将demo数据插入到neo4j
#python -m rasa_core_sdk.endpoint --actions actions_with_neo4j