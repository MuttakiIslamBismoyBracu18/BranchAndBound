def largest_number_of_vehicles(data):
    w = data[0]
    n = data[1]
    v_weight = data[2:]

    def find_max_vehicles(i, current_weight, front, back):
        if i == n:
            return 0

        take_front = 0
        take_back = 0

        if current_weight + v_weight[i] <= w:
            if front is None:
                take_front = 1 + find_max_vehicles(i + 1, current_weight + v_weight[i], v_weight[i], v_weight[i])
            elif v_weight[i] < front:  # Front Branch
                take_front = 1 + find_max_vehicles(i + 1, current_weight + v_weight[i], v_weight[i], back)
            elif v_weight[i] > back:  # Back Branch
                take_back = 1 + find_max_vehicles(i + 1, current_weight + v_weight[i], front, v_weight[i])
        skip = find_max_vehicles(i + 1, current_weight, front, back)  # Skip Branch

        return max(take_front, take_back, skip)

    return find_max_vehicles(0, 0, None, None)


input_data = list(map(int, input("Enter input data as a space-separated list: ").split()))
result = largest_number_of_vehicles(input_data)
print(result)
