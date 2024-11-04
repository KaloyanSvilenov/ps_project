class Logic:
    def __init__(self, start, length):

        self.start = int(start)
        self.length = int(length)

        with open('example.txt', 'r', encoding='utf-8') as file:
            self.str = file.read()

    def generateTable(self):

        str_text = self.str[self.start:(self.start + self.length)]
        str_bytes = str_text.encode('utf-8')
        num_chunk = self.length // 64
        extra_chunk_ln = self.length % 64
        txt = ""
        step = 64
        for i in range(0, num_chunk*64+1, step):
            if i == (num_chunk * 64): step = extra_chunk_ln
            chunk_hex = str_bytes[i:i + step].hex(sep=" ", bytes_per_sep=1)
            chunk_str = str_text[i:i + step]

            txt += f"\n | {chunk_str}\n | {chunk_hex}\n=> {step}\n"

        return txt