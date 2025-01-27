class Log:
    def __init__(self):
        self.log_file = ""
        self.is_setup = False
        self.log_queue = []

    def setup(self, log_file: str):
        self.log_file = log_file
        self.is_setup = True
        self.flushLogQueue()

    def flushLogQueue(self):
        # todo better handling, append to end, remove first item like a real queue
        # While queue not empty, add to queue to prevent new logs from being lost during flush
        for msg in self.log_queue:
            self.writeFile(msg)

    def log(self, msg: str):
        print(msg)
        self.writeFile(msg)

    def writeFile(self, msg: str):
        if (self.is_setup == True):
            with open(self.log_file, "a") as f:
                f.write(msg + "\n")
        else:
            self.log_queue.append(msg)
