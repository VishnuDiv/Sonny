import mido

# Open the correct output port
def stop_notes():
    OUTPUT_NAME = [name for name in mido.get_output_names() if "POLY D" in name][0]
    outport = mido.open_output(OUTPUT_NAME)

    # Send All Notes Off on all channels (just in case)
    for channel in range(16):
        outport.send(mido.Message('control_change', control=123, value=0, channel=channel))

    print("All notes off.")
