import requests

from enum import Enum

class Line(Enum):
    일호선 = 1001
    이호선 = 1002
    삼호선 = 1003
    사호선 = 1004
    오호선 = 1005
    육호선 = 1006
    칠호선 = 1007
    팔호선 = 1008
    구호선 = 1009
    공항철도 = 1065
    경의중앙선 = 1063
    경춘선 = 1067
    신분당선 = 1077
    분당선 = 1075
    우이신설선 = 1092
    서해선 = 1093
    경강선 = 1081
    
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
        
    return result

def getLines(station):
    url = "http://swopenapi.seoul.go.kr/api/subway//6557475641776e7331303455684e4559/json/realtimeStationArrival/0/20/"
    url  = url + "/" + station

    request = requests.get(url=url)

    data: dict = request.json()
    
    arrival_data: list = data["realtimeArrivalList"]

    lines: list = arrival_data[0]["subwayList"].split(',')

    result = []

    for line in lines:
        
        num = line
        json = {getName(line): line}
        result.append(json)
    
    print(result)

    return result
