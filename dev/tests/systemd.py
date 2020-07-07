from pystemd.systemd1 import Unit
import time

unit_local = Unit(b'pulseaudio-linein-local.service')
unit_local.load()

unit_stream = Unit(b'pulseaudio-linein-stream.service')
unit_stream.load()

print(unit_local.ActiveState)
print(unit_stream.ActiveState)


if (unit_local.ActiveState == b'active'):
	print('Stopping local...')
	unit_local.Stop(b'replace')
	print('Starting stream...')
	unit_stream.Start(b'replace')
elif (unit_stream.ActiveState == b'active'):
	print('Stopping stream...')
	unit_stream.Stop(b'replace')
	print('Starting local...')
	unit_local.Start(b'replace')
else:
	unit_stream.Start(b'replace')


print(unit_local.ActiveState)
print(unit_stream.ActiveState)
