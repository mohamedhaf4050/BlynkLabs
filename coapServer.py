import asyncio
from aiocoap import resource, Context, Message
from aiocoap.numbers.codes import Code

class HelloWorldResource(resource.Resource):
    async def render_get(self, request):
        payload = "Hello World from CoAP Server!"
        msg = Message(payload=payload.encode(), code=Code.CONTENT)
        return msg

async def main():
    # Create CoAP server
    root = resource.Site()
    root.add_resource(('hello',), HelloWorldResource())

    server = await Context.create_server_context(root, bind=("::", 5595))

    await asyncio.sleep(10000)  # keep server running for a long time

if __name__ == "__main__":
    asyncio.run(main())

