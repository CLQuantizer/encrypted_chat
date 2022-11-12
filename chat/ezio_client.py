# client.py
import asyncio
import logging
import sys

from reactivestreams.subscriber import DefaultSubscriber
from rsocket.helpers import single_transport_provider
from rsocket.payload import Payload
from rsocket.rsocket_client import RSocketClient
from rsocket.transports.tcp import TransportTCP

from string_encryption.encrypt import encrypt


class StreamSubscriber(DefaultSubscriber):

    def on_next(self, value, is_complete=False):
        logging.info('RS: {}'.format(value))
        self.subscription.request(1)


async def main(server_port):
    logging.info('Connecting to server at localhost:%s', server_port)
    connection = await asyncio.open_connection('localhost', server_port)

    async with RSocketClient(single_transport_provider(TransportTCP(*connection))) as client:
        async def run_request_response():
            while True:
                await asyncio.sleep(0.5)
                print("Hi Ezio, please send your message to the server")
                message = input()
                payload = Payload(encrypt(message))
                try:
                    result = await client.request_response(payload)
                    logging.info('Response: {}'.format(result.data.decode()))
                except asyncio.CancelledError:
                    pass

        task = asyncio.create_task(run_request_response())
        # if I were to cancel
        # await asyncio.sleep(2)
        # task.cancel()
        await task


if __name__ == '__main__':
    port = sys.argv[1] if len(sys.argv) > 1 else 6565
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main(port))
