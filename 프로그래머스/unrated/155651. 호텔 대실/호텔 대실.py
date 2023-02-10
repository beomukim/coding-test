def solution(book_time):
    answer = 0
    def change(time):
        return int(time[:2]) * 60 + int(time[3:])
    
    room_in = [(change(b[0]), 0) for b in book_time]
    room_out = [(change(b[1]) + 10, 1) for b in book_time]
    room = room_in + room_out
    res = 0
    room.sort(key=lambda x:x[1], reverse=True)
    room.sort(key=lambda x:x[0])
    print(room)
    for r in room:
        if r[1] == 0:
            res += 1
        else:
            res -= 1
        
        if res > answer:
            answer = res
    return answer

