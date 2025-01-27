streams_no = int(input("how many streams?: "))
streams = []
for _ in range(streams_no):
    streams.append(int(input("size of stream?: ")))
while command != 77:
    command = int(input("Whats your command?: "))
    if command == 99:
        stream_choice = int(input("which stream to split"))
        stream_percent = int(input("which percentage to split"))
        