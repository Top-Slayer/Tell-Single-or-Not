import os

folder = ["types/คนเจ้าชู้", "types/คนรักเดียวใจเดียว", "types/คนโสด"]
i = int(0)
while i < len(folder):
    for filename in os.listdir(folder[i]):
        file_path = os.path.join(folder[i], filename)
        os.remove(file_path)
    i += 1