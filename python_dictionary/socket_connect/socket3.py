import asyncio
import websockets
import threading

url = 'wss://xiaoke.kaikeba.com/program/_websocket/bf385ea7-26c8-40de-9cf2-25be98d39ac0/68af5f9d-bb74-4e3d-8486-bfcab59ab983/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1582622947225?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=scGb2HZqRSSCseeWrCk&workspace=bf385ea7-26c8-40de-9cf2-25be98d39ac0%2F68af5f9d-bb74-4e3d-8486-bfcab59ab983%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw'


async def recv_msg():
	async with websockets.connect(url) as websocket:
		# while True:
		print('work_2 on loop:%s' % id(loop))
		for msg in websocket.messages:
			await websocket.recv()
			print(msg)
			if msg == '["stdout", "$"]':
				break

async def send_msg():
	async with websockets.connect(url) as websocket:
		while True:
			print('work_4 on loop:%s' % id(loop))
			message = '1111'
			if message=='exit':
				break
			# print(message)
			await websocket.send(message)


@asyncio.coroutine
def hello():
	asyncio.set_event_loop(loop)
	print('Hello world! (%s)' % threading.currentThread())
	# loop.run_until_complete(recv_msg())
	threading.Thread(target=recv_msg).start()
	yield from asyncio.sleep(3)
	# loop.run_until_complete(send_msg())
	threading.Thread(target=send_msg).start()
	print('Hello again! (%s)' % threading.currentThread())


if __name__ == '__main__':
	loop = asyncio.new_event_loop()
	tasks = [hello(), hello()]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()







# future = asyncio.gather(recv(), send())
# loop.run_until_complete(future)

# import threading
# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
