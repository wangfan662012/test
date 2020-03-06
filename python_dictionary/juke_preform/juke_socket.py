# encoding: utf-8
import socketio
import asyncio
import time


loop = asyncio.get_event_loop()
sio = socketio.AsyncClient()
start_timer = None
token = "87393aa6d41145798712769471d7b6ce"


async def send_ping():
    global start_timer
    start_timer = time.time()
    await sio.emit("jukeMessage", {"code": "1000", "msgId": "", "body": ""})


@sio.on('connect')
async def on_connect():
    print('connected to server')
    await send_ping()


@sio.on('pong_from_server')
async def on_pong(data):
    global start_timer
    latency = time.time() - start_timer
    print('latency is {0:.2f} ms'.format(latency * 1000))
    await send_ping()


async def message_handler(msg):
    print('Received message: ', msg)
    if msg['ready']:
        pass
    else:
        await sio.emit("jukeMessage", {"code": 2000, "body": "{\"token\": \"%s\", \"type\": \"GM\", \"clientId\":\"1\", \"clientType\":\"pc-web\"}" % token})


async def message_handler1(msg1):
    print("received message:", msg1)
    if msg1['code'] == 2001:
        print("login sss")
        await sio.emit("jukeMessage", {"code": "9999", "msgId": msg1['msgId'], "body": "{\"messageCode\":2001}"})



async def start_server():
    await sio.connect(f'wss://juke-test3-node1.kuick.cn:1316/socket.io/?loginToken={token}')
    print(sio.connection_headers)
    print(sio.connection_url)
    print(sio.connection_transports)

    sio.on('jukeProxyPrepared', message_handler)
    sio.on("jukeMessage", message_handler1)
    await sio.wait()


def stat_main():
    loop.run_until_complete(start_server())

for i in range(5):
    stat_main()