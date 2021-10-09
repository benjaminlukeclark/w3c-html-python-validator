from pathlib import Path


class HTMLFileHandler:
    def __init__(self):
        """
        Class that can iterate over dictionary and store all handlers for all .html files present
        """
        self.__html_files_array = None
        self.reset_html_array()

    def add_to_html_array(self, file):
        """
        Add to the internal html file array
        :param file: WindowsPath (or equal) reference to a file
        :return:
        """
        self.__html_files_array.append(file)

    def reset_html_array(self):
        """
        Reset internal html to 0 entries
        :return:
        """
        self.__html_files_array = []

    def return_html_array(self):
        """
        Return internal html array of WindowsPath (or equal) handlers for all html files
        :return:
        """
        return self.__html_files_array

    def find_html_files_from_dir(self, directory):
        """
        Populate internal array with WindowsPath (or equal) handlers for all HTML files (recursive) in given directory
        :param directory: Directory to search recursively
        :return:
        """
        for file in Path(directory).rglob('*.html'):
            self.add_to_html_array(file)
