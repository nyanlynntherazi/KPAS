import streamlit as st
import json
import re

def index2burmese(input_string=None):
    json_rules = '[{ "from": "0", "to": "၀" }, { "from": "1", "to": "၁" }, { "from": "2", "to": "၂"}, { "from": "3", "to": "၃"}, { "from": "4", "to": "၄" }, { "from": "5", "to": "၅" }, { "from": "6", "to": "၆" }, { "from": "7", "to": "၇" }, { "from": "8", "to": "၈" }, { "from": "9", "to": "၉"}] '
    rules = json.loads(json_rules)
    for rule in rules:
        input_string = re.sub(rule["from"], rule["to"], input_string)
    return input_string
def remove_leading_dash(input_string=None):
    return re.sub("^-",'',input_string)

def remove_empty_list_member(tmp):
    return [i for i in tmp if i]

def list2string(input_list):
    return "\n".join(input_list)

def execute(input_string):
    output = []
    for i,line in enumerate(remove_empty_list_member(input_string.split('\n'))):
        output.append(f"{index2burmese(str(i))}။ {remove_leading_dash(line)}")
    output[0] = output[0][3:]
    return output


st.title('KPAS')

input_string = st.text_area('paste here')

for line in execute(input_string):
    st.text(line)