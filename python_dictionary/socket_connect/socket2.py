import asyncio
import websockets
import threading

url = 'wss://xiaoke.kaikeba.com/program/_websocket/bf385ea7-26c8-40de-9cf2-25be98d39ac0/68af5f9d-bb74-4e3d-8486-bfcab59ab983/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1582622947225?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=scGb2HZqRSSCseeWrCk&workspace=bf385ea7-26c8-40de-9cf2-25be98d39ac0%2F68af5f9d-bb74-4e3d-8486-bfcab59ab983%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw'


async def recv_msg():
	async with websockets.connect(url) as websocket:
		while True:
			while True:
				message = await websocket.recv()
				print(message)
				if message == '["stdout", "$"]':
					# await websocket.send(b'print(123)')
					break
			ms = [b'222',b'123', b'in']
			for m in ms:
				await websocket.send(m)
				print(m)
				if ms == 'in':
					continue



# async def send():
# 	async with websockets.connect(url) as websocket:
# 		while True:
# 			# print('work_4 on loop:%s' % id(loop))
# 			message = '1111'
# 			if message=='exit':
# 				break
# 			# print(message)
# 			await websocket.send(message)
# 			await asyncio.sleep(4)


thread_loop = asyncio.get_event_loop()
# future = asyncio.gather(recv(), send())
thread_loop.run_until_complete(recv_msg())
