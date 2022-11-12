# server.py
import asyncio
import logging
import sys

from rsocket.helpers import create_future
from rsocket.payload import Payload
from rsocket.request_handler import BaseRequestHandler
from rsocket.rsocket_server import RSocketServer
from rsocket.transports.tcp import TransportTCP

from string_encryption.encrypt import decrypt


class Handler(BaseRequestHandler):
    async def request_response(self, payload: Payload) -> asyncio.Future:
        await asyncio.sleep(0.1)  # Simulate not immediate process
        # have to convert byte array to bytes. lol
        response_string = payload.data.decode()
        response_bytes = str.encode(response_string)
        decrypted_message = decrypt(response_bytes)
        res = "\nServer received: "+response_string[-5:]+"_****"+"\nDecrypted to: "+decrypted_message.decode()
        res_bytes = str.encode(res)
        return create_future(Payload(res_bytes))


async def run_server(server_port):
    logging.info('Starting server at localhost:%s', server_port)

    def session(*connection):
        RSocketServer(TransportTCP(*connection), handler_factory=Handler)

    server = await asyncio.start_server(session, 'localhost', server_port)

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 6565
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(run_server(port))
