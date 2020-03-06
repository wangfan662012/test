import asyncio
import logging
from datetime import datetime
from aiowebsocket.converses import AioWebSocket


async def startup(uri):
	async with AioWebSocket(uri) as aws:
		converse = aws.manipulator
		message = 'print(123)'
		mes = await converse.receive()
		print('{time}-Client receive: {rec}'
			  .format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), rec=mes))
		await converse.send(message)
		print('{time}-Client send: {message}'
			.format(time=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), message=message))

if __name__ == '__main__':
	remote = 'ws://echo.websocket.org'
	url = 'wss://xiaoke.kaikeba.com/program/_websocket/bf385ea7-26c8-40de-9cf2-25be98d39ac0/68af5f9d-bb74-4e3d-8486-bfcab59ab983/unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw/1582622947225?user_id=unionid_oBB9ps0vzorx4aCj0t5MPOKjooRw&token=scGb2HZqRSSCseeWrCk&workspace=bf385ea7-26c8-40de-9cf2-25be98d39ac0%2F68af5f9d-bb74-4e3d-8486-bfcab59ab983%2Funionid_oBB9ps0vzorx4aCj0t5MPOKjooRw'

	try:
		asyncio.get_event_loop().run_until_complete(startup(url))
	except KeyboardInterrupt as exc:
		logging.info('Quit.')