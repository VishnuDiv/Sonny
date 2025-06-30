import mido
import time
import random
import synth_stop 
# print(mido.get_output_names()) : to get the list of available MIDI output ports

outport = mido.open_output('POLY D') # my synth

# Send a MIDI note on message (Middle C)
note_on = mido.Message('note_on', note=60, velocity=64)
outport.send(note_on)

# Send note off (after a short delay)
import time
time.sleep(1)
note_off = mido.Message('note_off', note=60)
outport.send(note_off)


# Setup
OUTPUT_NAME = [name for name in mido.get_output_names() if "POLY D" in name][0]
outport = mido.open_output(OUTPUT_NAME)

# Tempo
bpm = 180
beat_duration = 50 / bpm

# Define chords as MIDI note numbers
chords = {
    'Cmaj7':  [60, 64, 67, 71],   # C E G B
    'Am7':    [57, 60, 64, 67],   # A C E G
    'Dm7':    [62, 65, 69, 72],   # D F A C
    'G7':     [55, 59, 62, 65],   # G B D F
}

# Helper to send a note
def send_note(note, velocity, duration):
    outport.send(mido.Message('note_on', note=note, velocity=velocity))
    time.sleep(duration)
    outport.send(mido.Message('note_off', note=note))

# Main arpeggiator loop
try:
    print("Playing arpeggiated chord progression. Press Ctrl+C to stop.")
    while True:
        for chord_name, notes in chords.items():
            print(f"Chord: {chord_name}")
            random.shuffle(notes)  # Randomize arpeggio order

            for note in notes:
                velocity = random.randint(50, 127)  # Human dynamics
                # duration = beat_duration * random.choice([0.25, 0.5, 0.75])
                send_note(note, velocity, beat_duration)

            # time.sleep(beat_duration * 2)  # Pause between chords

except KeyboardInterrupt:
    synth_stop.stop_notes()
    print("Stopped.")