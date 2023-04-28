class EventClass:
    def __init__(self, ascii_set, function, description):
        self.ascii_set = ascii_set
        self.function = function
        self.description = description


events = [
    # finger buttons
    'I1',  # 0
    'I2',  # 1
    'I3',  # 2
    'I4',  # 3
    'I5',  # 4
    'I6',  # 5
    'I7',  # 6

    'M1',  # 7
    'M2',  # 8
    'M3',  # 9
    'M4',  # 10

    'R1',  # 11
    'R2',  # 12
    'R3',  # 13
    'R4',  # 14

    'P1',  # 15
    'P2',  # 16
    'P3',  # 17
    'P4',  # 18
    'P5',  # 19

    # thumb buttons
    'T11',  # 20
    'T12',  # 21
    'T13',  # 22
    'T14',  # 23
    'T15',  # 24

    'T21',  # 25
    'T22',  # 26
    'T23',  # 27
    'T24',  # 28
    'T25',  # 29

    'T33',  # 30

    # joystick
    'JM',  # 31
    'JS',  # 32

    'JF1',  # 33
    'JF2',  # 34

    'JB1',  # 35
    'JB2',  # 36

    'JL1',  # 37
    'JL2',  # 38

    'JR1',  # 39
    'JR2',  # 40

    # scroll wheel
    'WF',  # 41
    'WM',  # 42
    'WB',  # 43

    # mouse speed
    'MH',  # 44
    'MV'   # 45
]

left_events_dict = {}
right_events_dict = {}

for i, event in enumerate(events):
    # print(f'i {i}   b {event}')
    if event == 'MH' or event == 'MV':
        event_object = EventClass(bytearray(b'\x64'), '-', '-')
    else:
        event_object = EventClass(bytearray(b'\x30'), '-', '-')
    left_events_dict[f'L{event}'] = event_object
    right_events_dict[f'R{event}'] = event_object

# print(left_events_dict)
# print(right_events_dict)
#
# print(right_events_dict['RI1'].ascii_set)
# print(right_events_dict['RMH'].ascii_set)
# print(right_events_dict['RMV'].ascii_set)
#
# print(left_events_dict['LI1'].ascii_set)
# print(left_events_dict['LMH'].ascii_set)
# print(left_events_dict['LMV'].ascii_set)
