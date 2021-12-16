from note import *
import random

ns = NoteSet()
for i in range(200):
    pitch = random.randrange(40, 80)
    time = random.uniform(0, 10)
    dur = random.uniform(.1, 1)
    vol = random.uniform(.1, .8)
    ns.add(Note(time, dur, pitch, vol))
ns.write_midi("random.midi")
