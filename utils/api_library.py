import json
import requests
import time

''' Class for all variables used in test script '''


class Status:
    CREATED = 201
    SUCCESS = 200
    NO_CONTENT = 204
    UNPROCESSED_ENTITY = 422
    UNAUTHORISED = 401
    SERVER_ERROR = 500
    MISSING_SOURCE = 404
    # FORBIDDEN = 403

''' Class for all api methods used in test script '''

class ApiMethods:
    def __init__(self, appurl):
        self.appurl = appurl

    def get_response_data(self, url, headers, auth, mock):
        if mock != None :
            aurl = url
        else:
            aurl = self.appurl + url
        start = time.time()
        print("AURL: " + aurl)
        print("HEADER: " + str(headers))
        resp = requests.get(aurl, headers=headers, auth=auth)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            print(output)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header

    def post_response_data(self, url, body, headers, auth, mock, files=None ):
        if mock != None:
            aurl = url
        else:
            aurl = self.appurl + url
        start = time.time()
        print(aurl)
        resp = requests.post(aurl, body, headers=headers, files=files, auth=auth)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            print (output)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header

    def post_response_with_data(self, url, headers, auth, mock, files):
        if mock != None:
            aurl = url
        else:
            aurl = self.appurl + url

        start = time.time()
        print(aurl)
        resp = requests.post(aurl, headers=headers, files=files)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            print(output)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header

    def put_response_data(self, url, body, headers,auth, mock,  files=None):
        if mock != None:
            aurl = url
        else:
            aurl = self.appurl + url
        start = time.time()
        print(aurl)
        resp = requests.put(aurl, body, headers=headers, files=files,auth=auth)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            print (output)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header

    def delete_response_data(self, url, headers, auth, mock):
        if mock != None :
            aurl = url
        else:
            aurl = self.appurl + url
        start = time.time()
        print("AURL: " + aurl)
        print("HEADER: " + str(headers))
        resp = requests.delete(aurl, headers=headers, auth=auth)
        resp_header = resp.headers
        resp_time = time.time() - start
        try:
            output = json.loads(resp.text)
            print(output)
            return resp.status_code, output, resp_time, resp_header
        except:
            return resp.status_code, None, resp_time, resp_header
