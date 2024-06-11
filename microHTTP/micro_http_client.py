import asyncio
from microHTTP.common import utils
from microHTTP.communication.request import Request
from microHTTP.communication.response import Response

from microHTTP.common.typing import TYPE_CHECKING

if TYPE_CHECKING:
    from asyncio import StreamReader, StreamWriter


class MicroHttpClient:
    def __init__(self, logging=False):
        self.logging = logging

    async def get(self, host: str, url: str, port: int = 80, timeout=5):
        return await self.__send_request(host, url, None, "GET", port, timeout)

    async def send(self, host: str, url: str, data: str | None, method: str, port: int = 80, timeout=5):
        return await self.__send_request(host, url, data, method, port, timeout)

    async def __send_request(self, host: str, url: str, data: str | None, method: str, port: int = 80, timeout=5):
        try:
            reader, writer = await asyncio.open_connection(host, port)
            request = Request(host, url, method=method, payload=data)

            return await self.__handle_communication(request, reader, writer, timeout)

        except Exception as e:
            self.__print_debug(f"error occurred while sending request: {str(e)}", exception=e)

        return None

    async def __handle_communication(self, request: Request,
                                     client_r: StreamReader,
                                     client_w: StreamWriter,
                                     timeout) -> Response | None:
        response = None

        try:
            utils.write_to_stream(client_w, request.get_as_string())
            await client_w.drain()

            response = await asyncio.wait_for(self.__handle_response(client_r), timeout)

        except Exception as e:
            self.__print_debug(f"error occurred: {str(e)}", exception=e)

        finally:
            client_w.close()
            await client_w.wait_closed()

        return response

    async def __handle_response(self, stream_reader: StreamReader) -> Response | None:
        try:
            response_header_string = await utils.load_request_header_from_stream(stream_reader)
            self.__print_debug(f"response header string: {response_header_string}")

            response = Response()
            response.parse_header(response_header_string)

            if response.content_length:
                response_body_string = await stream_reader.readexactly(response.content_length)
                response.parse_body(response_body_string.decode())

            self.__print_debug(f"response body string: {response.body}")

            return response

        except Exception as e:
            self.__print_debug(f"error while parsing response", exception=e)
            return None

    def __print_debug(self, message, exception: Exception | None = None):
        utils.print_debug(message=message, debug_enabled=self.logging, exception=exception)
