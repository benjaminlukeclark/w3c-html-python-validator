from src.HTMLFileHandler import HTMLFileHandler
import random
import string


def test_init():
    html_file_handler = HTMLFileHandler()
    assert (len(html_file_handler.return_html_array()) == 0)


def test_add_to_array():
    html_file_handler = HTMLFileHandler()
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(20))
    html_file_handler.add_to_html_array(random_string)
    assert (len(html_file_handler.return_html_array()) == 1)


def test_reset_html_array():
    html_file_handler = HTMLFileHandler()
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(20))
    html_file_handler.add_to_html_array(random_string)
    html_file_handler.reset_html_array()
    assert (len(html_file_handler.return_html_array()) == 0)


def test_return_html_array():
    html_file_handler = HTMLFileHandler()
    assert (html_file_handler.return_html_array() is not None)


def test_find_html_files_from_dir():
    html_file_handler = HTMLFileHandler()
    html_file_handler.find_html_files_from_dir("./test_files")
    assert (len(html_file_handler.return_html_array()) == 2)


if __name__ == "__main__":
    test_init()
    test_add_to_array()
    test_find_html_files_from_dir()
    test_return_html_array()
    test_reset_html_array()
