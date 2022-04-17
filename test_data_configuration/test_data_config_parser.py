import configparser
import os
import sys

'''This is a class with helper functions which will parse the values from the test data configuration files'''


class MyConfigParser(object):

    def __init__(self, projectname, env, protocol):
        self.productname = projectname
        self.env = env
        self.protocol = protocol
        self.config = configparser.ConfigParser()
        if __name__ == '__main__':
            path = os.path.split(sys.argv[0][0])
        else:
            path = os.path.split(__file__)[0]
        self.config.read(os.path.join(path, self.productname+"/"+ self.productname + '_test_data.conf'))
        print(self.config.read(os.path.join(path, self.productname+"/"+ self.productname + '_test_data.conf')))

    def build_headers(self, headertype):
        global auth_token
        try:
            auth_token = self.config.get(self.env, "auth_token")
        except configparser.NoOptionError:
            print("Exception occured")

        if headertype == "GOREST":
            headers = {
                "Authorization": "Bearer "+ auth_token,
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        else:
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json"
            }
        return headers

    def endpoint_parser(self, endpoint_name):
        end_point = self.config.get("url", endpoint_name)
        return end_point

    def main_url(self):
        protocol = self.config.get(self.protocol, "protocol")
        domain = self.config.get(self.env, "domain")
        main_url = protocol + domain
        return main_url
