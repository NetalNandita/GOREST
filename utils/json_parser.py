import json
import os
import time

class JsonParser:

    def dict_to_json(self):
        """
        This method will be used to generate json string from Dict
        :return: dictionary in json formatted string
        """
        json_output = json.dumps(self)
        return json_output

    @staticmethod
    def read_json_file_to_dict(file_location, file_name):
        """
        This method will be used to read Json file in distionary format
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: dict type of json data
        """
        with open(file_location + file_name + '.json') as f:
            data = json.load(f)
        return data

    @staticmethod
    def write_json_file(file_location, file_name, data):
        """
        This method will be used to read json file in string format
        :param file_location: Location till parent folder
        :param file_name: file name (without .json in name)
        :return: json string
        """
        with open(file_location + '/' + file_name + '.json',"w") as f:
            f.write(str(data))

def create_payload_for_product(productname, operationname, scenario='main'):
    """
    This method will be used to read json from template folder
    :param operatonname: Product (service) name
    :param scenario: (optional) scenario name if a service has more than one type of requests
    :return: json payload in string format
    """

    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'template/requests'))
    print("Jason Parser Filepath", file_path)
    payload = JsonParser.read_json_file_to_dict(file_path, '/' + productname + '/' + operationname )
    print("payload created  : %s" % payload)
    return json.dumps(payload)

def set_json_value(key, value, json_dict):
    """
    This method will be used to set or change a value at given key in Json string.
    :param key: Key for the value in following format "parent:child:actualkey"
    :param value: Value to be updated at given key
    :param json_dict: input dict from where value need to be fetched.
    :return: updated json string with value
    """
    keylist = key.split(':')
    temp_json = json_dict[keylist[0]]

    if len(keylist) == 1:
        json_dict[key] = value
    elif isinstance(temp_json,list):
        key_item = keylist.pop(0)
        json_dict = set_json_value(key_item, set_json_value(":".join(keylist), value, temp_json), json_dict)
    else:
        key_item = keylist.pop(0)
        json_dict = set_json_value(key_item, set_json_value(":".join(keylist), value, temp_json), json_dict)
        print("Json :: ")
        print(json_dict)
    return json_dict
















