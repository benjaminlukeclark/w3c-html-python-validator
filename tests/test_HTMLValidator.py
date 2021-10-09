from src.HTMLFileHandler import HTMLFileHandler
from src.HTMLValidator import HTMLValidator


def test_init():
    html_validator = HTMLValidator()
    assert (html_validator is not None)


def test_valid_html():
    html_validator = HTMLValidator()
    html_file_handler = HTMLFileHandler()
    html_file_handler.find_html_files_from_dir("./test_files/indent_0/valid.html")
    for file in html_file_handler.return_html_array():
        file_validation_return = html_validator.validate_html_file(file)
        assert (file_validation_return["messages"] == [])


def test_invalid_html():
    html_validator = HTMLValidator()
    html_file_handler = HTMLFileHandler()
    html_file_handler.find_html_files_from_dir("./test_files/indent_0/indent_1/invalid.html")
    for file in html_file_handler.return_html_array():
        file_validation_return = html_validator.validate_html_file(file)
        assert (file_validation_return["messages"][0]["type"] == "error")


if __name__ == "__main__":
    test_init()
    test_valid_html()
