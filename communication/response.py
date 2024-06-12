from microHTTP.common.consts import HTTPConsts
import json


class Response:
    def __init__(self):
        self.status_code: int | None = None
        self.protocol: str | None = None
        self.content_length: int = 0
        self.content_type: str | None = None

        self.headers: dict[str, ...] = {}
        self.body: str | None = None

        self.supported_content_types = [HTTPConsts.CONTENT_TYPE_JSON]

    def parse_header(self, header_string: str):
        split_request_string = header_string.replace("\r", "").split("\n")

        if len(split_request_string) > 0:
            protocol, status, *split_message = split_request_string[0].split()
            split_request_string.pop(0)

            self.status_code = int(status)
            self.headers = self.__parse_request_headers_string(split_request_string)

        is_content_length_present = True if HTTPConsts.CONTENT_LENGTH in self.headers.keys() else False
        self.content_length = int(self.headers[HTTPConsts.CONTENT_LENGTH]) if is_content_length_present else 0

        self.content_type = self.headers.get(HTTPConsts.CONTENT_TYPE)

    def __parse_request_headers_string(self, split_request_string: list[str]) -> dict[str, ...]:
        request_struct = {}

        if len(split_request_string) > 0:
            for raw_row in split_request_string:
                row = raw_row.split(":")

                if len(row) == 2:
                    request_struct[row[0].upper()] = row[1].strip()

        return request_struct

    def parse_body(self, body_string: str):
        body = body_string.replace("\r", "").replace("\n", "")
        self.body = json.loads(body) if self.content_type in self.supported_content_types else None
