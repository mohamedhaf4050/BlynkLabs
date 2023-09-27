import asyncio
from aiocoap import Context, Message
from aiocoap.numbers.codes import Code, GET

async def main():
    protocol = await Context.create_client_context()

    
    request = Message(code=GET, uri=f'coap://192.168.1.44:5595/hello')

    try:
        response = await protocol.request(request).response
        print('Received response: ', (response.payload))
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)

if __name__ == "__main__":
    asyncio.run(main())



