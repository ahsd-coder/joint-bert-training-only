import openai # 调用大模型
import json

# https://bailian.console.aliyun.com/?tab=api#/api/?type=model&url=2712576
client = openai.OpenAI(
    # https://bailian.console.aliyun.com/?tab=model#/api-key
    api_key="sk-247421c217474fee969fc6b5ef2bd8c8",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

completion = client.chat.completions.create(
    model="qwen-plus",
    messages=[
#         {"role": "system", "content": """你是一个专业信息抽取专家，请对下面的文本抽取他的领域类别、意图类型、实体标签
# - 待选的领域类别：music / app / radio / lottery / stock / novel / weather / match / map / website / news / message / contacts / translation / tvchannel / cinemas / cookbook / joke / riddle / telephone / video / train / poetry / flight / epg / health / email / bus / story
# - 待选的意图类别：OPEN / SEARCH / REPLAY_ALL / NUMBER_QUERY / DIAL / CLOSEPRICE_QUERY / SEND / LAUNCH / PLAY / REPLY / RISERATE_QUERY / DOWNLOAD / QUERY / LOOK_BACK / CREATE / FORWARD / DATE_QUERY / SENDCONTACTS / DEFAULT / TRANSLATION / VIEW / NaN / ROUTE / POSITION
# - 待选的实体标签：code / Src / startDate_dateOrig / film / endLoc_city / artistRole / location_country / location_area / author / startLoc_city / season / dishNamet / media / datetime_date / episode / teleOperator / questionWord / receiver / ingredient / name / startDate_time / startDate_date / location_province / endLoc_poi / artist / dynasty / area / location_poi / relIssue / Dest / content / keyword / target / startLoc_area / tvchannel / type / song / queryField / awayName / headNum / homeName / decade / payment / popularity / tag / startLoc_poi / date / startLoc_province / endLoc_province / location_city / absIssue / utensil / scoreDescr / dishName / endLoc_area / resolution / yesterday / timeDescr / category / subfocus / theatre / datetime_time

# 最终输出格式填充下面的json， domain 是 领域标签， intent 是 意图标签，slots 是实体识别结果和标签。

# ```json
# {
#     "domain": ,
#     "intent": ,
#     "slots": {
#       "待选实体类型": "实体原始名词",
#     }
# }
# ```
# """},
    {
    "role":"system", "content":"""
    你是一个高效的NLU（自然语言理解）解析专家。你的任务是从用户的输入中提取“意图”和“槽位（实体）”。
     Task: 1.识别用户的意图（如：OPEN / SEARCH / REPLAY_ALL / NUMBER_QUERY / DIAL / CLOSEPRICE_QUERY / SEND / LAUNCH / PLAY / REPLY / RISERATE_QUERY / DOWNLOAD / QUERY / LOOK_BACK / CREATE / FORWARD / DATE_QUERY / SENDCONTACTS / DEFAULT / TRANSLATION / VIEW / NaN / ROUTE / POSITION）。
           2.识别并提取槽位实体（如：code / Src / startDate_dateOrig / film / endLoc_city / artistRole / location_country / location_area / author / startLoc_city / season / dishNamet / media / datetime_date / episode / teleOperator / questionWord / receiver / ingredient / name / startDate_time / startDate_date / location_province / endLoc_poi / artist / dynasty / area / location_poi / relIssue / Dest / content / keyword / target / startLoc_area / tvchannel / type / song / queryField / awayName / headNum / homeName / decade / payment / popularity / tag / startLoc_poi / date / startLoc_province / endLoc_province / location_city / absIssue / utensil / scoreDescr / dishName / endLoc_area / resolution / yesterday / timeDescr / category / subfocus / theatre / datetime_time）

     Output Format（JSON ONLY）：{"intent":"意图名称": ""， "slots":{"实体类型":"实体值"}}
     Examples: 用户输入：“帮我播放周杰伦的青花瓷”， 输出：{"intent":"PLAY", "slots":{"artist":"周杰伦", "song":"青花瓷"}}
     """},

    {"role": "user", "content": "糖醋鲤鱼怎么做啊？你只负责吃，c则c。"},

    ]
)
result = completion.choices
print(result)

"""
```json
{    
    "domain": "bus",
    "intent": "QUERY",
    "slots": {
        "startLoc_city": "许昌",
        "endLoc_city": "中山"
    }
}
```
"""