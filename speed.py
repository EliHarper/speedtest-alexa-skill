class Speed:

    def __init__(self, ping, up, down):
        self.ping = ping
        self.up = up
        self.down = down

    def __repr__(self):
        return '<Speed: {}>'.format(self.down)