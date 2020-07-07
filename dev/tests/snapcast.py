import asyncio
import snapcast.control

loop = asyncio.get_event_loop()
server = loop.run_until_complete(snapcast.control.create_server(loop, '10.4.32.240'))

# print all client names
for client in server.clients:
  print(client.friendly_name)

# set volume for client #0 to 50%
#client = server.clients[0]
#loop.run_until_complete(server.client_volume(client.identifier, {'percent': 50, 'muted': False}))