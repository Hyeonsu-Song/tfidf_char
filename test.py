data = {20693249: ['송하윤'],
        20693274: ['송하윤'],
        20693276: ['송하윤', '이서진'],
        20693310: ['김지수', '지우'],
        20693313: ['지우'],
        20693314: ['김지수', '지우'],
        20693318: ['김지수']}

data_list = list(data.values())

for i in range(len(data)):
    print(data_list[i], type(data_list[i]))
    data_list[i] = ' '.join(data_list[i])
    print(data_list[i])