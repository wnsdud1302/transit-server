import requests
import json
def getName(line: str) -> str:
    if line == '1001':
        return "1호선"
    elif line == '1002':
        return "2호선"
    elif line == '1003':
        return "3호선"
    elif line == '1004':
        return "4호선"
    elif line == '1005':
        return "5호선"
    elif line == '1006':
        return "6호선"
    elif line == '1007':
        return "7호선"
    elif line == '1008':
        return "8호선"
    elif line == '1009':
        return "9호선"
    elif line == '1065':
        return "공항철도"
    elif line == '1063':
        return "경의중앙선"
    elif line == '1067':
        return "경춘선"
    elif line == '1077':
        return "신분당선"
    elif line == '1075':
        return "분당선"
    elif line == '1092':
        return "우이신설선"
    elif line == '1093':
        return "서해선"
    elif line == '1081':
        return "경강선"


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

    print(len(result))
    
    if len(result) == 1:
        result.append({"종착역": "도착정보 없음",
                "도착시간": "도착정보 없음",
                "현재역": "도착정보 없음"})
        
    
    return result

def getLines(station: str):
    url = "http://swopenapi.seoul.go.kr/api/subway//6557475641776e7331303455684e4559/json/realtimeStationArrival/0/20/"
    url  = url + "/" + station

    request = requests.get(url=url)

    data: dict = request.json()
    
    arrival_data: list = data["realtimeArrivalList"]

    lines: list = arrival_data[0]["subwayList"].split(',')

    result = []

    for line in lines:
        result.append([getName(line), line])

    result = dict(result)
    return result

def getNearStation(lat, lng):

    with open('station_coordinate.json', 'r', encoding="utf-8") as f:
        json_data = json.load(f)

    def filterCoordinate(item):
        corlat = item.get('lat')
        corlong = item.get('lng')

        return corlat > lat - 0.02 and corlat < lat + 0.02 and corlong > lng - 0.015 and corlong < lng + 0.015


    filtered = list(filter(lambda item: item.get('lat') is not None, json_data))

    filtered = list(filter(filterCoordinate, filtered))

    data = dict()

    for item in filtered:
        new = {item.get('name'): item.get('line')}
        data.update(new)

    return data
