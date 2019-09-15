# coding = utf-8
# using namespace std
import json
from typing import AnyStr
from os import listdir


class ConfigFile(object):
    """
    """
    source_config: AnyStr = "./core/config.json"  # at the vision of the APP_ROOT
    configurations = dict()
    got_data = False

    class UnloadConfig(Exception):
        args = "The system can't do that action without a connection with the configurations file!"

    class InvalidConfigField(KeyError):
        args = "That's not a valid field for the configurations file!"

    class InvalidPath(FileNotFoundError):
        args = "That file can't be found on the system!"

    @staticmethod
    def check_folder_valid(folder_path: str) -> bool:
        """
        """
        have_bar = False
        for char in folder_path:
            have_bar = bool(char == "/")
        try:
            listdir(folder_path)
        except FileNotFoundError: return False
        return have_bar

    def __init__(self, file_config: AnyStr = "./core/config.json"):
        """
        """
