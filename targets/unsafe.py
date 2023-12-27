class RawCommand:
    def __init__(self, cmd):
        self.cmd = cmd

    def run(self):
        eval(self.cmd)


def run(commands):
    for cmd in commands:
        cmd.run()
    return "Success"
