'''Create an object with the environment values  and  particular journey name '''
import os
import random

import names
import string
import sys
from datetime import datetime

from utils import json_parser
from utils.api_library import ApiMethods
from test_data_configuration.test_data_config_parser import MyConfigParser

# global headers

global config_value
sys.path.append(os.path.abspath('../'))

''' Configuring environment & application variable as a input parameter '''
application_name = "gorest"
environment_type = "test"

'''Create an object with the environment values  and  particular journey name '''
config_value = MyConfigParser(application_name, environment_type, "protocol_https")

'Getting initial URL from configuration file'
main_url = config_value.main_url()

''' Building the headers from the configuration file '''
headers = config_value.build_headers("headers_CDE")

''' Object for to access all the library functions '''
libclient = ApiMethods(main_url)


class Templates():

    @staticmethod
    def set_headers_val(option):
        new_headers = config_value.build_headers(option)
        return new_headers

    @staticmethod
    def get_config_val(name_endpoint):
        end_point = config_value.endpoint_parser(name_endpoint)
        return end_point

    @staticmethod
    def post_response_headers(endpoint, api, resp_path, method_headers):
        body = json_parser.create_payload_for_product(api, resp_path)
        return libclient.post_response_data(endpoint, body, method_headers, auth=None, mock=None)

    @staticmethod
    def get_response(endpoint, method_headers):
        return libclient.get_response_data(endpoint, method_headers, auth=None, mock=None)

    @staticmethod
    def put_response_headers(endpoint, api, resp_path, method_headers):
        body = json_parser.create_payload_for_product(api, resp_path)
        return libclient.put_response_data(endpoint, body, method_headers, auth=None, mock=None)

    @staticmethod
    def delete_response(endpoint, headers):
        return libclient.delete_response_data(endpoint, headers, auth=None, mock=None)

    @staticmethod
    def request_update_personal_info(api, resp_path):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'template/requests/' + api))
        tmp = json_parser.JsonParser.read_json_file_to_dict(file_path + '/', resp_path)

        new_name = names.get_full_name(gender='male')
        result = ''.join((random.choice(string.ascii_lowercase) for x in range(9)))
        email = result + "_nn@test.com"
        new_email = email
        new_body = json_parser.set_json_value("name", new_name, tmp)
        new_body2 = json_parser.set_json_value("email", new_email, new_body)
        tmp2 = json_parser.JsonParser.dict_to_json(new_body2)
        json_parser.JsonParser.write_json_file(file_path, resp_path, tmp2)

    @staticmethod
    def request_update_status(api, resp_path):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'template/requests/' + api))
        tmp = json_parser.JsonParser.read_json_file_to_dict(file_path + '/', resp_path)
        new_body = json_parser.set_json_value("status", "active", tmp)
        tmp = json_parser.JsonParser.dict_to_json(new_body)
        json_parser.JsonParser.write_json_file(file_path, resp_path, tmp)

    @staticmethod
    def request_update_gender_email(api, resp_path, gender, email):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'template/requests/' + api))
        tmp = json_parser.JsonParser.read_json_file_to_dict(file_path + '/', resp_path)
        new_body = json_parser.set_json_value("gender", gender, tmp)
        new_body2 = json_parser.set_json_value("email", email, new_body)
        tmp2 = json_parser.JsonParser.dict_to_json(new_body2)
        json_parser.JsonParser.write_json_file(file_path, resp_path, tmp2)