from HTMLFileHandler import HTMLFileHandler
from HTMLValidator import HTMLValidator
from pprint import pprint
import json
import argparse
import sys

parser = argparse.ArgumentParser(description='Validate HTML files in a directory.')
parser.add_argument('directory', metavar='d', type=str,
                    help='directory to recursively search for files')

args = parser.parse_args()

if __name__ == "__main__":
    html_file_handler = HTMLFileHandler()
    html_file_handler.find_html_files_from_dir(args.directory)
    html_validator = HTMLValidator()
    html_results = {}
    error_recorded = False
    for file in html_file_handler.return_html_array():
        file_validation_return = html_validator.validate_html_file(file)
        if file_validation_return["messages"] == []:
            result = {
                "result": "HTML validate"
            }
        else:
            if not error_recorded:
                error_recorded = True
            result = {
                "result": "Invalid HTML, one or more errors reported",
                "errors": []
            }
            for message in file_validation_return["messages"]:
                result["errors"].append({
                    "type": message["type"],
                    "line": message["lastLine"],
                    "column": message["lastColumn"],
                    "message": message["message"],
                    "extract": message["extract"]
                })

        html_results['/'.join(file.parts)] = result

    pprint(json.dumps(html_results), indent=4)
    if error_recorded:
        sys.exit("One of more HTML files failed validation")




