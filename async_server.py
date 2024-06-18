import asyncio


async def handle_client(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received {message} from {addr}")

    print("Send: %r" % message)
    writer.write(data)
    await writer.drain()

    print("Closing the connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)

    addr = server.sockets[0].getsockname()
    print(f"Serving on {addr}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
