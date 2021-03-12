import requests
import json
import time

session = requests.Session()


def call_sync(request, is_checked=False):
    if request.method == "GET":
        # print("call_sync url : " , request.host + request.url)
        response = session.get(request.host + request.url, headers=request.header)
        if is_checked is True:
            return response.text
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        # check_response(dict_data)
        return dict_data
        # return request.json_parser(dict_data)

    elif request.method == "POST":
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        dict_data = json.loads(response.text, encoding="utf-8")
        # print("call_sync  === recv data : ", dict_data)
        # check_response(dict_data)
        return dict_data
        # return request.json_parser(dict_data)


def call_sync_performance_test(request, is_checked=False):
    if request.method == "GET":
        inner_start_time = time.time()
        response = session.get(request.host + request.url, headers=request.header)
        inner_end_time = time.time()
        cost_manual = round(inner_end_time - inner_start_time, 6)
        req_cost = response.elapsed.total_seconds()

        if is_checked is True:
            return response.text
        if response.status_code == 200:
            dict_data = json.loads(response.text, encoding="utf-8")
            return dict_data, req_cost, cost_manual
        else:
            return None, req_cost, cost_manual
        # return request.json_parser(dict_data)

    elif request.method == "POST":
        inner_start_time = time.time()
        response = session.post(request.host + request.url, data=json.dumps(request.post_body), headers=request.header)
        inner_end_time = time.time()
        cost_manual = round(inner_end_time - inner_start_time, 6)
        req_cost = response.elapsed.total_seconds()
        if response.status_code == 200:
            dict_data = json.loads(response.text, encoding="utf-8")
            return dict_data, req_cost, cost_manual
        else:
            return None, req_cost, cost_manual
        # print("call_sync  === recv data : ", dict_data)
        # check_response(dict_data)

        # return request.json_parser(dict_data)
