from urllib import request
import json


class HTMLValidator:
    def __init__(self):
        self.__w3_validator_url = "https://validator.w3.org/nu/?out=json"
        self.__headers = {
            "Content-Type": "text/html",
            "charset": "utf-8"
        }

    def validate_html_file(self, path_to_file):
        """
        Validates HTML for given file at path
        :param path_to_file: WindowsPath (or equal) reference to a file
        :return:  blank JSON for valid HTML, otherwise returns array of JSON error messages
        """
        return self.__call_w3_validator(bytes(open(path_to_file).read(), "utf-8"))

    def __add_headers_to_validator(self, request_object):
        """
        Adds standard headers to validator
        :param request_object: urllib.request.Requests object to add headers to
        :return:
        """
        for key, value in self.__headers.items():
            request_object.add_header(key, value)

    def __call_w3_validator(self, html):
        """
        Passes provided HTML to W3 validator for validation
        :param html: bytes representation of html to valid
        :return: JSON representation of results
        """
        req = request.Request(self.__w3_validator_url, data=html)
        self.__add_headers_to_validator(req)
        req_data = request.urlopen(req).read()
        # After read, format bytes to proper string so we can return json
        req_string = req_data.decode('utf8').replace("'", '"')
        return json.loads(req_string)
