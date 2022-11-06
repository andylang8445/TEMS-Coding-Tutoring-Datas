def roomAssignment(schedule:list):
    schedule.sort(key = lambda x: (x[1], x[0]))

    cnt = 0
    end = 0
    for meeting in schedule:
        if meeting[0] >= end:
            cnt += 1
            end = meeting[1]

    return cnt