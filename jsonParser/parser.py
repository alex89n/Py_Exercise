import json
import os

csv_file = "err_cloud.csv"
if os.path.isfile(csv_file):
    os.remove(csv_file)

# json_file = "parser_proba.json"
json_file = "log.json"
with open(json_file, 'r') as file:
    data = json.load(file)
    
    
# # oblo csv    
# csv_param = ["doc400", "SN", "SID", "doc400", "3.2.2"]    
# # schwaiger csv    
csv_param = ["ha102", "SN", "SID", "ha102-fw", "4.0.0"]    
# # keemple csv    
# csv_param = ["doc400", "SN", "SID", "kp-gw-01", "3.1.2"]

for i in xrange(len(data["fails"])):
    if data["fails"][i]["err"]["code"] == 11000:
        error = "Duplicate key"
        print("{}. {} {} - err: {}").format(i+1, data["fails"][i]["data"]["name"], data["fails"][i]["data"]["secureId"], error)
    else:
        print("{}. {} {} - err: {}").format(i+1, data["fails"][i]["data"]["name"], data["fails"][i]["data"]["secureId"], data["fails"][i]["err"]["errmsg"])
    
    with open(csv_file, 'a') as csv:
        str = ("{};{};{};{};{}\n").format(csv_param[0], data["fails"][i]["data"]["name"], data["fails"][i]["data"]["secureId"], csv_param[3], csv_param[4]) 
        csv.write(str)

        
        
        
# print type(data)
# print "###############################"
# print("{} - {}").format(data["fails"][0]["data"]["name"],data["fails"][0]["data"]["secureId"])
# print("{} - {}").format(data["fails"][1]["data"]["name"],data["fails"][1]["data"]["secureId"])
# print("{} - {}").format(data["fails"][2]["data"]["name"],data["fails"][2]["data"]["secureId"])
# print("{} - {}").format(data["fails"][3]["data"]["name"],data["fails"][3]["data"]["secureId"])
# print("{} - {}").format(data["fails"][4]["data"]["name"],data["fails"][4]["data"]["secureId"])

# print("\n\n{}").format(len(data["fails"]))

