# These codes help in reading big files without affecting much memory usage
#

# creating a big text file...
content = "From Python's official documents: link The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size (in bytes). A negative buffering means to use the system default, which is usually line buffered for tty devices and fully buffered for other files. If omitted, the system default is used... " + '\n'
with open("D:\\TMP\\large_file1.txt" , "a") as f:
    for i in range(2000):
        f.write(content)


# reading the file using fileinput library
import fileinput
for line in fileinput.input("D:\\TMP\\large_file1.txt", encoding="utf-8"):
    print(line.strip('\n'))


# reading the file using buffers
"""From Python's official documents: The optional buffering argument specifies the file’s desired buffer size: 0 means unbuffered, 1 means line buffered, any other positive value means use a buffer of (approximately) that size (in bytes). A negative buffering means to use the system default"""
with open("D:\\TMP\\large_file1.txt", 'r', buffering=10) as f:
    for line in f:
        print(line.strip('\n'))


# class to read header, tail, backwards any file: TO BE TESTED
class File(file):
    """ An helper class for file reading  """

    def __init__(self, *args, **kwargs):
        super(File, self).__init__(*args, **kwargs)
        self.BLOCKSIZE = 4096

    def head(self, lines_2find=1):
        self.seek(0)                            #Rewind file
        return [super(File, self).next() for x in xrange(lines_2find)]

    def tail(self, lines_2find=1):
        self.seek(0, 2)                         #Go to end of file
        bytes_in_file = self.tell()
        lines_found, total_bytes_scanned = 0, 0
        while (lines_2find + 1 > lines_found and
               bytes_in_file > total_bytes_scanned):
            byte_block = min(
                self.BLOCKSIZE,
                bytes_in_file - total_bytes_scanned)
            self.seek( -(byte_block + total_bytes_scanned), 2)
            total_bytes_scanned += byte_block
            lines_found += self.read(self.BLOCKSIZE).count('\n')
        self.seek(-total_bytes_scanned, 2)
        line_list = list(self.readlines())
        return line_list[-lines_2find:]

    def backward(self):
        self.seek(0, 2)                         #Go to end of file
        blocksize = self.BLOCKSIZE
        last_row = ''
        while self.tell() != 0:
            try:
                self.seek(-blocksize, 1)
            except IOError:
                blocksize = self.tell()
                self.seek(-blocksize, 1)
            block = self.read(blocksize)
            self.seek(-blocksize, 1)
            rows = block.split('\n')
            rows[-1] = rows[-1] + last_row
            while rows:
                last_row = rows.pop(-1)
                if rows and last_row:
                    yield last_row
        yield last_row

with File("D:\\TMP\\large_file1.txt") as f:
    print(f.head(5))
    print(f.tail(5))
    for row in f.backward():
        print(row)



# reading file's head only
from itertools import islice
with open("D:\\TMP\\large_file1.txt") as f:
    for line in islice(f, 2): # last value "2" means the last n lines read in the file
        print(line)


# reading small file's tail only
from collections import deque
with open("D:\\TMP\\large_file1.txt") as f:
    for line in deque(f, maxlen=3):
        print(line)


# reading big file's tail only: TO BE TESTED
def tail(fname, lines):
    """Read last N lines from file fname."""
    f = open(fname, 'r')
    BUFSIZ = 1024
    f.seek(0, os.SEEK_END)
    fsize = f.tell()
    block = -1
    data = ""
    exit = False
    while not exit:
        step = (block * BUFSIZ)
        if abs(step) >= fsize:
            f.seek(0)
            exit = True
        else:
            f.seek(step, os.SEEK_END)
        data = f.read().strip()
        if data.count('\n') >= lines:
            break
        else:
            block -= 1
    return data.splitlines()[-lines:]

tail("D:\\TMP\\large_file1.txt", 1)


# ???
import data_loading_utils.py.py
file_name = "D:\\TMP\\large_file1.txt"
CHUNK_SIZE = 1000000

def process_lines(data, eof, file_name):
    # check if end of file reached
    if not eof:
        # process data, data is one single line of the file
        print(data)
    else:
        # end of file reached
        print("...EOF...")

data_loading_utils.read_lines_from_file_as_data_chunks("D:\\TMP\\large_file1.txt", chunk_size=CHUNK_SIZE, callback=self.process_lines)


# reading files per chunks: TO BE TESTED
def readInChunks(fileObj, chunkSize=1024):
    while True:
        data = fileObj.read(chunkSize)
        if not data:
            break
        while data[-1:] != '\n':
            data+=fileObj.read(1)
            print(f"-{data}")
        yield data # see what to do with yield

readInChunks("D:\\TMP\\large_file1.txt", 1024)


