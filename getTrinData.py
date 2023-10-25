import requests

def get_train_data(line, station, updnline):
    url = "http://swopenapi.seoul.go.kr/api/subway//6557475641776e7331303455684e4559/json/realtimeStationArrival/0/20/"
    url  = url + "/" + station
    request = requests.get(url=url)
    
    data = request.json()
    
    arrival_data = data["realtimeArrivalList"]

    updn_data = list()

    for item in arrival_data:
        if item["updnLine"] == updnline:
            updn_data.append(item)
    
    line_data = list()

    for item in updn_data:
        if item["subwayId"] == line:

            filtered = {k: v for k, v in item.items() if v is not None}

            filtered = {k: v for k, v in item.items() if k == "arvlMsg2" or k == "arvlMsg3" or k == "bstatnNm"}

            line_data.append(filtered)
    
    result = list()

    for item in line_data:
        json = {"종착역": item["bstatnNm"],
                "도착시간": item["arvlMsg2"],
                "현재역": item["arvlMsg3"]}
        result.append(json)
        
    return result
