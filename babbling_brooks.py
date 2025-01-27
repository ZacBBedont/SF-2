streams_no = int(input("how many streams?: "))
streams = []
command = 0

for _ in range(streams_no):
    streams.append(int(input("size of stream?: ")))
while command != 77:
    command = int(input("Whats your command?: "))
    if command == 99:
        stream_choice = int(input("which stream to split: "))
        stream_percent = int(input("which percentage to split: "))
        streams.insert(stream_choice-1, streams[stream_choice-1]*(100-stream_percent)/100)
        streams[stream_choice] = streams[stream_choice]* (stream_percent/100)
        print(streams)
    elif command == 88:
        stream_joined = int(input("What stream to join?: "))
        streams[stream_joined] += streams[stream_joined-1]
        streams.pop(stream_joined-1)
        print(streams)
print(*streams)