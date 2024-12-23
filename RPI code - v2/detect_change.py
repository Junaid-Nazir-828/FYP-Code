def check_change(newData , previousData):
    if len(newData) != len(previousData):
        return True
    
    for i in range(len(newData)):
        if newData[i]['x1'] != previousData[i]['x1'] or newData[i]['x2'] != previousData[i]['x2'] or newData[i]['y1'] != previousData[i]['y1'] or newData[i]['y2'] != previousData[i]['y2']:
            return True

    return False