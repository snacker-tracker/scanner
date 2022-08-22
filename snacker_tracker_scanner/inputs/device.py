from evdev import InputDevice, categorize, ecodes

class EVDecoder:
    codes = {
        0: [None, None],
        1: ['ESC', 'ESC'],
        2: ['1', '!'],
        3: ['2', '@'],
        4: ['3', '#'],
        5: ['4', '$'],
        6: ['5', '%'],
        7: ['6', '^'],
        8: ['7', '&'],
        9: ['8', '*'],
        10: ['9', '('],
        11: ['0', ')'],
        12: ['-', '_'],
        13: ['=', '+'],
        14: ['BKSP', 'BKSP'],
        15: ['TAB', 'TAB'],
        16: ['q', 'Q'],
        17: ['w', 'W'],
        18: ['e', 'E'],
        19: ['r', 'R'],
        20: ['t', 'T'],
        21: ['y', 'Y'],
        22: ['u', 'U'],
        23: ['i', 'I'],
        24: ['o', 'O'],
        25: ['p', 'P'],
        26: ['[', '{'],
        27: [']', '}'],
        28: ['CRLF', 'CRLF'],
        29: ['LCTRL', 'LCTRL'],
        30: ['a', 'A'],
        31: ['s', 'S'],
        32: ['d', 'D'],
        33: ['f', 'F'],
        34: ['g', 'G'],
        35: ['h', 'H'],
        36: ['j', 'J'],
        37: ['k', 'K'],
        38: ['l', 'L'],
        39: [';', ':'],
        40: ['"', "'"],
        41: ['`', '~'],
        42: ['LSHFT', 'LSHFT'],
        43: ['\\', '|'],
        44: ['z', 'Z'],
        45: ['x', 'X'],
        46: ['c', 'C'],
        47: ['v', 'V'],
        48: ['b', 'B'],
        49: ['n', 'N'],
        50: ['m', 'M'],
        51: [',', '<'],
        52: ['.', '>'],
        53: ['/', '?'],
        54: ['RSHFT', 'RSHFT'],
        56: ['LALT', 'LALT'],
        57: [' ', ' '],
        100: ['RALT', 'RALT'],
    }

    def __init__(self):
        self.reset()

    def reset(self):
        self.caps = False
        self.buffer = []

    def add(self, event):
        data = event

        if data.scancode == 42:
            self.caps = data.keystate

        if data.keystate == 1:  # Down events only
            key_lookup = u'{}'.format(self.codes.get(data.scancode)[self.caps])

            if data.scancode not in [1, 14, 15, 28, 29, 42, 54, 56, 100]:
                self.buffer.append(key_lookup)

        if(data.scancode == 28):
            joined = "".join(self.buffer)
            self.reset()
            return joined
        else:
            return None

class Device(object):
    def __init__(self, device):
       self.dev = InputDevice(device)
       self.dev.grab()
       self.decoder = EVDecoder()

    def events(self):
        for event in self.dev.read_loop():
            if event.type == ecodes.EV_KEY:
                data = categorize(event)
                returned = self.decoder.add(data)

                if returned is not None:
                    yield returned
