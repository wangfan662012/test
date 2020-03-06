#!/usr/bin/env python

import asyncio
import websockets

url = 'wss://xiaoke.kaikeba.com/program/_websocket/bf385ea7-26c8-40de-9cf2-25be98d39ac0/68af5f9d-bb74-4e3d-8486-bfcab59ab983/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1582622947225?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=scGb2HZqRSSCseeWrCk&workspace=bf385ea7-26c8-40de-9cf2-25be98d39ac0%2F68af5f9d-bb74-4e3d-8486-bfcab59ab983%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw'



async with websockets.connect(url) as websocket:
	async def recv_msg():
		while True:
			msg = await websocket.recv()
			print(msg)
	async def send_msg():
			while True:
				await websocket.send('print(123)')
				print(websocket.messages)

asyncio.get_event_loop().run_until_complete(recv_msg())
asyncio.get_event_loop().run_until_complete(send_msg())

