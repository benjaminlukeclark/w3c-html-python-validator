from HTMLFileHandler import HTMLFileHandler
from HTMLValidator import HTMLValidator

if __name__ == "__main__":
    html_file_handler = HTMLFileHandler()
    html_file_handler.find_html_files_from_dir("../tests/test_files")
    html_validator = HTMLValidator()
    for file in html_file_handler.return_html_array():
        file_validation_return = html_validator.validate_html_file(file)

