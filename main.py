#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\r\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vOWI0MTE4NDAtNGUzMS0xMWVhLTlhMjktNWJhODJiM2ZjOGNi\",\r\n  \"markdown\": \"Hello\",\r\n  \"attachments\": [\r\n    {\r\n      \"contentType\": \"application/vnd.microsoft.card.adaptive\",\r\n      \"content\":\r\n\r\n\r\n\r\n\r\n\r\n{\r\n    \"type\": \"AdaptiveCard\",\r\n    \"body\": [\r\n        {\r\n            \"type\": \"Container\",\r\n            \"style\": \"emphasis\",\r\n            \"items\": [\r\n                {\r\n                    \"type\": \"ColumnSet\",\r\n                    \"columns\": [\r\n                        {\r\n                            \"type\": \"Column\",\r\n                            \"items\": [\r\n                                {\r\n                                    \"type\": \"TextBlock\",\r\n                                    \"size\": \"Large\",\r\n                                    \"weight\": \"Bolder\",\r\n                                    \"text\": \"**クエストの依頼**\"\r\n                                }\r\n                            ],\r\n                            \"width\": \"stretch\"\r\n                        }\r\n                    ]\r\n                }\r\n            ],\r\n            \"bleed\": true\r\n        },\r\n        {\r\n            \"type\": \"Container\",\r\n            \"items\": [\r\n                {\r\n                    \"type\": \"ColumnSet\",\r\n                    \"columns\": [\r\n                        {\r\n                            \"type\": \"Column\",\r\n                            \"items\": [\r\n                                {\r\n                                    \"type\": \"TextBlock\",\r\n                                    \"size\": \"ExtraLarge\",\r\n                                    \"text\": \"Cisco Collaboration DX の対応\",\r\n                                    \"wrap\": true\r\n                                },\r\n                                {\r\n                                    \"type\": \"TextBlock\",\r\n                                    \"spacing\": \"Small\",\r\n                                    \"size\": \"Small\",\r\n                                    \"weight\": \"Bolder\",\r\n                                    \"color\": \"Accent\",\r\n                                    \"text\": \"\"\r\n                                }\r\n                            ],\r\n                            \"width\": \"stretch\",\r\n                            \"style\": \"warning\"\r\n                        }\r\n                    ]\r\n                },\r\n                {\r\n                    \"type\": \"FactSet\",\r\n                    \"spacing\": \"Large\",\r\n                    \"facts\": [\r\n                        {\r\n                            \"title\": \"機器\",\r\n                            \"value\": \"*Collaboratioon DX*\"\r\n                        },\r\n                        {\r\n                            \"title\": \"発生時刻\",\r\n                            \"value\": \"2020/02/14\"\r\n                        },\r\n                        {\r\n                            \"title\": \"重要度\",\r\n                            \"value\": \"A\"\r\n                        },\r\n                        {\r\n                            \"title\": \"内容\",\r\n                            \"value\": \"-----。\"\r\n                        },\r\n                        {\r\n                            \"title\": \"所要時間\",\r\n                            \"value\": \"3時間\"\r\n                        },\r\n                        {\r\n                            \"title\": \"報酬\",\r\n                            \"value\": \"X万円\"\r\n                        }\r\n                    ]\r\n                }\r\n            ]\r\n        },\r\n        {\r\n            \"type\": \"Container\",\r\n            \"items\": [\r\n                {\r\n                    \"type\": \"ActionSet\",\r\n                    \"actions\": [\r\n                        {\r\n                            \"type\": \"Action.Submit\",\r\n                            \"title\": \"承諾\",\r\n                            \"style\": \"positive\",\r\n                            \"data\": {\r\n                                \"id\": \"_qkQW8dJlUeLVi7ZMEzYVw\",\r\n                                \"action\": \"approve\"\r\n                            }\r\n                        },\r\n                        {\r\n                            \"type\": \"Action.ShowCard\",\r\n                            \"title\": \"拒否\",\r\n                            \"style\": \"destructive\",\r\n                            \"card\": {\r\n                                \"type\": \"AdaptiveCard\",\r\n                                \"body\": [\r\n                                    {\r\n                                        \"type\": \"Input.Text\",\r\n                                        \"id\": \"RejectCommentID\",\r\n                                        \"placeholder\": \"Please specify an appropriate reason for rejection.\",\r\n                                        \"isMultiline\": true\r\n                                    }\r\n                                ],\r\n                                \"actions\": [\r\n                                    {\r\n                                        \"type\": \"Action.Submit\",\r\n                                        \"title\": \"Send\",\r\n                                        \"data\": {\r\n                                            \"id\": \"_qkQW8dJlUeLVi7ZMEzYVw\",\r\n                                            \"action\": \"reject\"\r\n                                        }\r\n                                    }\r\n                                ],\r\n                                \"$schema\": \"http://adaptivecards.io/schemas/adaptive-card.json\"\r\n                            }\r\n                        }\r\n                    ]\r\n                }\r\n            ]\r\n        }\r\n    ],\r\n    \"$schema\": \"http://adaptivecards.io/schemas/adaptive-card.json\",\r\n    \"version\": \"1.1\",\r\n    \"fallbackText\": \"This card requires Adaptive Cards v1.2 support to be rendered properly.\"\r\n}\r\n    }\r\n  ]\r\n}"
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer ZDk4ZTE4MmMtOWFlMy00ZWFmLWI1OTMtZmI3ZDk2MmZiY2QyNzlhNDIzOTItYzVl_PF84_consumer'
}

response = requests.request("POST", url, headers=headers, data = payload.encode('utf-8'))
#(url,data = text.encode('utf-8'), headers = headers)

print(response.text.encode('utf8'))
