from test_suite.test_case_reg.common_templates import Templates
from utils.api_library import Status

class Test_Cases_Gorest(object):

    def test_gorest_users(self):
        """ Test to CREATE new user by updating the name and email id """

        url = Templates.get_config_val("PostGoRestUsers")
        headers = Templates.set_headers_val("GOREST")
        Templates.request_update_personal_info("gorest", "PostGoRestUsers")
        resp_code, resp_body, resp_time, resp_header = Templates.post_response_headers(url, "gorest", "PostGoRestUsers", headers)
        assert resp_code == Status.CREATED, "The response code isn't equal the expected code"
        assert resp_body['id'], "The id is not present"
        id = resp_body['id']

        """ Test to GET new user details by ID from Post response """

        url = Templates.get_config_val("GetGoRestUsers").format(id)
        headers = Templates.set_headers_val("GOREST")
        resp_code, resp_body, resp_time, resp_header = Templates.get_response(url, headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_gorest_users_active(self):
        """ Test to CREATE new user and update status from inactive to active """

        url = Templates.get_config_val("PostGoRestUsers")
        headers = Templates.set_headers_val("GOREST")
        Templates.request_update_personal_info("gorest", "PostGoRestUsers")
        resp_code, resp_body, resp_time, resp_header = Templates.post_response_headers(url, "gorest",
                                                                                       "PostGoRestUsers", headers)
        assert resp_code == Status.CREATED, "The response code isn't equal the expected code"
        assert resp_body['id'], "The id is not present"

        id = resp_body['id']

        url = Templates.get_config_val("PutGoRestUsers").format(id)
        headers = Templates.set_headers_val("GOREST")
        Templates.request_update_status("gorest", "PutGoRestUsers")
        resp_code, resp_body, resp_time, resp_header = Templates.put_response_headers(url, "gorest", "PutGoRestUsers", headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

    def test_gorest_users_create_delete_get(self):
        """ Test to CREATE new user ,DELETE and verify deleted user using GET request """

        url = Templates.get_config_val("PostGoRestUsers")
        headers = Templates.set_headers_val("GOREST")
        Templates.request_update_personal_info("gorest", "PostGoRestUsers")
        resp_code, resp_body, resp_time, resp_header = Templates.post_response_headers(url, "gorest",
                                                                                       "PostGoRestUsers", headers)
        assert resp_code == Status.CREATED, "The response code isn't equal the expected code"
        assert resp_body['id'], "The id is not present"
        id = resp_body['id']

        """ Test to DELETE created user and verify status """

        url = Templates.get_config_val('DelGoRestUsers').format(id)
        headers = Templates.set_headers_val("GOREST")
        resp_code, resp_body, resp_time, resp_header = Templates.delete_response(url, headers)
        assert resp_code == Status.NO_CONTENT, "The response code isn't equal the expected code"

        """ Test to GET deleted user and verify response code and status """

        url = Templates.get_config_val("GetGoRestUsers").format(id)
        headers = Templates.set_headers_val("GOREST")
        resp_code, resp_body, resp_time, resp_header = Templates.get_response(url, headers)
        assert resp_code == Status.MISSING_SOURCE, "The response code isn't equal the expected code"
        assert resp_body["message"], "Resource not found"

    def test_gorest_users_update_negative_test(self):

        """ Test to GET new user details by ID from Post response """
        test_data = 1234
        url = Templates.get_config_val("GetGoRestUsers").format(test_data)
        headers = Templates.set_headers_val("GOREST")
        resp_code, resp_body, resp_time, resp_header = Templates.get_response(url, headers)
        assert resp_code == Status.SUCCESS, "The response code isn't equal the expected code"

        """ Test to PUT/UPDATE invalid test data """

        url = Templates.get_config_val("PutGoRestUsers1234")
        headers = Templates.set_headers_val("GOREST")
        Templates.request_update_gender_email("gorest", "PutGoRestUsers1234", "6789", "4567")
        resp_code, resp_body, resp_time, resp_header = Templates.put_response_headers(url, "gorest", "PutGoRestUsers1234", headers)
        assert resp_code == Status.UNPROCESSED_ENTITY, "The response code isn't equal the expected code"
        assert resp_body[0]["message"], "can't be blank"
        assert resp_body[1]["message"], "is invalid"
