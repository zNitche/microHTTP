import sys

from microHTTP.common.typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asyncio import StreamReader, StreamWriter


def print_debug(message: str, debug_enabled: bool = False, exception: Exception | None = None):
    if debug_enabled:
        print(f"[microHTTP] - {message}")

        if exception and isinstance(exception, Exception):
            sys.print_exception(exception)


async def load_request_header_from_stream(stream: StreamReader) -> str:
    request_header_string = ""

    while True:
        request_line = await stream.readline()
        request_line = request_line.decode()

        if request_line == "\r\n" or not request_line:
            break

        request_header_string += request_line

    return request_header_string


def write_to_stream(stream: StreamWriter, data: str, encoding="utf-8"):
    stream.write(bytes(data, encoding))
