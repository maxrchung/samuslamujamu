import time

class Ability:
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.available = 0

    def ready(self):
        now = time.time()
        if now > self.available:
            self.available = now + self.cooldown
            return True
        return False
