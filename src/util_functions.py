import os
import sys
from enum import Enum
from datetime import datetime


# This class contains common utility functions.
class Utilities(object):
    # Reads the input file content
    @classmethod
    def read_file(cls, fileName):
        lines = []
        try:
            with open(cls.__filePath(fileName)) as file:
                for line in file:
                    lines.append(line)
        except FileNotFoundError:
            Utilities.log(f"File '{fileName}' not found")
        return lines

    # Writes the content to output file
    @classmethod
    def write_file(cls, fileName, line):
        try:
            with open(cls.__filePath(fileName), Constants.WRITE_MODE.value) as file:
                file.write(f'{line} {Constants.CR_LF.value}')
                print(line)
        except FileNotFoundError:
            Utilities.log(f"File '{fileName}' not found")

    #  Writes the logs to log file
    @classmethod
    def log(cls, line):
        fileName = Constants.LOG_FILE.value
        with open(cls.__filePath(fileName), Constants.APPEND_MODE.value) as file:
            file.write(f'{cls.__current_time()} {line} {Constants.CR_LF.value}')
            print(line)

    # finds the absolute path from relative path
    @staticmethod
    def __filePath(fileName):
        dirName = os.path.dirname(__file__)
        fileName = os.path.join(dirName, fileName)
        return fileName

    # returns the formatted current time, used for logging
    @staticmethod
    def __current_time():
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S.%f ")
        return current_time

    # logs output in output file
    @staticmethod
    def log_output(source, destination, path, distance, time_taken):
        output = f"Shortest route from DC '{source}' to reach Warehouse '{destination}' is [{path}]\n" \
                 f"and it has minimum travel distance {distance} km \nand it will take him {time_taken} " \
                 f"minutes to travel from DC to Warehouse.\n"
        Utilities.write_file(Constants.OUTPUT_FILE.value, output)

    # logs the error to output file
    @staticmethod
    def log_error(source, destination):
        Utilities.write_file(Constants.OUTPUT_FILE.value, f"Shortest path not found between DC {source} and "
                                                          f"warehouse {destination}")


# constants used in the application
class Constants (Enum):
    INPUT_FILE = '../input/inputPS3.txt'
    OUTPUT_FILE = '../output/outputPS3.txt'
    LOG_FILE = '../log/logs.txt'
    READ_MODE = 'r'
    WRITE_MODE = 'w'
    APPEND_MODE = 'a'
    CR_LF = '\n'
    EMPTY_STRING = ''
    INPUT_SEPARATOR = '/'
    PATH_SEPARATOR = ','
    MINUTES_IN_HOUR = 60
    DEFAULT_SPEED = 40  # 40 km/h
    ADJACENCY_INFO_TOKEN_LENGTH = 3
    NODE_INFO_TOKEN_LENGTH = 2
    MAX_INFINITY = sys.maxsize
    DC_NODE = 'DC Node:'
    WH_NODE = 'WH Node:'
    NODE_INPUT_TOKEN = ':'
    SOURCE_NODE_INDEX = 0
    DESTINATION_NODE_INDEX = 1
    DISTANCE_INDEX = 2





