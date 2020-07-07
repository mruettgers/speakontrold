import pulsectl


pulse = pulsectl.Pulse('speakontrold')

sink_input_name = 'line-in-local'

sink_input = next(x for x in pulse.sink_input_list() if x.name == sink_input_name)
volume = sink_input.volume
print(volume.values) # list of per-channel values (floats)
print(volume.value_flat) # average level across channels (float)

pulse.volume_set_all_chans(sink_input, 0.2)
pulse.volume_change_all_chans(sink_input, 0.1)