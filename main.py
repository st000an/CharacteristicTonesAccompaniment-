from mido import Message, MidiFile, MidiTrack

bpm = int(input("intput bpm:"))
def play_note(note, length, track, base_num=0, delay=0, velocity=1.0, channel=0,base_note=60,scale_para = [0, 2, 2, 1, 2, 2, 2, 1]):
    meta_time = 60 * 1000 / bpm

    note=note %len(scale_para)
    track.append(Message('note_on', note=base_note + base_num*12 + sum(scale_para[0:note]),
                         velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num*12 + sum(scale_para[0:note]),
                         velocity=round(64*velocity), time=round(meta_time*length), channel=channel))

def play_2note(note1,note2, length,  track,base_num1=0,base_num2=0, delay=0, velocity=1.0, channel=0,base_note = 60,scale_para = [0, 2, 2, 1, 2, 2, 2, 1]):
    meta_time = 60 * 1000/ bpm
    
    note1=note1 %len(scale_para)
    note2=note2 %len(scale_para)
    track.append(Message('note_on', note=base_note + base_num1*12 + sum(scale_para[0:note1]),
                         velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_on', note=base_note + base_num2*12 + sum(scale_para[0:note2]),
                         velocity=round(64*velocity), time=round(delay*meta_time), channel=channel))
    track.append(Message('note_off', note=base_note + base_num1*12 + sum(scale_para[0:note1]),
                         velocity=round(64*velocity), time=round(meta_time*length), channel=channel))
    track.append(Message('note_off', note=base_note + base_num2*12 + sum(scale_para[0:note2]),
                         velocity=round(64*velocity), time=0, channel=channel))



scale_para=[0, 2, 2, 1, 2, 2, 2, 1]

mid = MidiFile()
track = MidiTrack()
track2 = MidiTrack()
mid.tracks.append(track)
mid.tracks.append(track2)
track.append(Message('program_change', program=17, time=0))
track2.append(Message('program_change', program=2, time=0))

playtime = int(input("intput playtime:"))
baseNote = int(input("intput baseNote:"))

for i in range(0,playtime):
 play_2note(4,1, 2,track, base_num1=0,base_num2=0, channel=1,base_note = baseNote,scale_para=scale_para)
 play_2note(7,4, 2, track,base_num1=-1,base_num2=0, channel=1,base_note = baseNote,scale_para=scale_para)
 play_2note(3,7, 4,track,  base_num1=0,base_num2=-1,channel=1,base_note = baseNote,scale_para=scale_para)
 play_note(2, 2, track2,base_num=-2 , channel=1,base_note = baseNote,scale_para=scale_para)
 play_note(5, 2, track2, base_num=-2 ,channel=1,base_note = baseNote,scale_para=scale_para)
 play_note(1, 4, track2,base_num=-2,  channel=1,base_note = baseNote,scale_para=scale_para)

mid.save('output-mido.mid')
