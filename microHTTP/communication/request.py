from microHTTP.common.consts import HTTPConsts


class Request:
    def __init__(self,
                 host: str,
                 url: str,
                 method: str,
                 content_type: str = HTTPConsts.CONTENT_TYPE_JSON,
                 payload: str | None = None):

        self.host = host
        self.url = url
        self.method = method

        self.content_type: str = content_type

        self.__headers: dict[str, ...] = {}
        self.payload: str | None = payload

    def get_headers_string(self) -> str:
        header_rows = [f"{self.method} {self.url} HTTP/1.1", f"HOST: {self.host}"]

        for header, value in self.__headers.items():
            header_rows.append(f"{header}: {value}")

        if self.method != "GET":
            self.add_header(HTTPConsts.CONTENT_TYPE, self.content_type)
            self.add_header(HTTPConsts.CONTENT_LENGTH, self.get_content_length())

        header_string = "\r\n".join(header_rows)

        return header_string

    def get_content_length(self) -> int:
        return len(self.payload) if self.payload else 0

    @property
    def headers(self):
        return self.__headers.copy()

    def add_header(self, name: str, value):
        normalized_name = name.upper()

        if normalized_name not in self.__headers.keys():
            self.__headers[normalized_name] = value

    def get_body(self) -> str:
        return self.payload if self.payload else ""

    def get_as_string(self) -> str:
        headers = self.get_headers_string()
        body = self.get_body()

        return f"{headers}\r\n\r\n{body}"
