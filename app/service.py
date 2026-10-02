import time

class Service:
    def __init__(self):
        self.memories = []

    def run(self, value: str):
        item = {
            "text": value,
            "scope": "demo",
            "importance": 0.5,
            "created_at": time.time(),
        }
        self.memories.append(item)
        return {"stored": item, "recall": list(reversed(self.memories[-5:]))}
