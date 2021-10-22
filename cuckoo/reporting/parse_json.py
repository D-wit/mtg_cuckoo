import sys
import json

def parse(path,parsed_name):
    with open(path, 'r') as f:
        report_json = json.load(f)
        with open("/home/mtg-cuckoo/parsed_report/"+str(parsed_name)+".json", "w") as file:
            try:
                json.dump((report_json['target']['file']),file,indent = 4)
                json.dump((report_json['info']['started']),file,indent = 4)
                json.dump((report_json['info']['id']),file,indent = 4)
                for i in range(0,len(report_json['signatures'])):
                    json.dump((report_json['signatures'][i]['ttp']),file,indent=4)
                    json.dump((report_json['signatures'][i]['marks']),file,indent=4)
                for j in range(0,len(report_json['behavior']['processes'])):
                    json.dump((report_json['behavior']['processes'][j]['processes_path']))
                    for k in range(0,len(report_json['behavior']['processes'][j]['calls'])):
                        json.dump((report_json['behavior']['processes'][j]['calls'][k]),file,indent = 4)
            except KeyError:
                pass
