import re
from collections import deque


class Logerror:

    def __init__(self):
        pass

    @staticmethod
    def open_file(file_path: str) -> list:
        """Open a log file, read all lines and return all content in a list"""
        with open(file_path, mode="r", encoding="utf-8", errors="ignore") as f:
            file_content = f.readlines()
            f.close()
        return file_content

    @staticmethod
    def filter_content(
        file_content: list, start_pattern: str, mid_pattern: str, last_pattern: str
    ) -> list:
        """Filter the content from open_file() based on patterns"""

        index_content = deque()
        cleaned_content = []
        for index, content in enumerate(file_content):
            line = content.splitlines().pop()
            cleaned_content.append(line)
            if (
                line.lower().startswith(start_pattern)
                and re.search(mid_pattern, line)
                and line.endswith(last_pattern)
            ):
                index_content.appendleft(index)

        day_log_content = []
        while len(index_content) > 1:
            start_index = index_content.pop()
            day_log_content.append(cleaned_content[start_index : index_content[-1]])

        last_index = index_content.pop()
        day_log_content.append(cleaned_content[last_index:])

        return day_log_content

    @staticmethod
    def identify_errors(content: list) -> list:
        """Return a content list with all identified patterns"""

        error_log = []
        for log in content:
            if [x for x in log if re.search("did not execute", x)]:
                error_log.append(log)

        error_process = []
        for log in error_log:
            error_process.append([x for x in log if str(x).startswith("Subject")])

        return error_process
