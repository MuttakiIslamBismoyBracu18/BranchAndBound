def largest_number_of_vehicles(data):
    w = data[0]
    n = data[1]
    v_weight = data[2:]

    memo = {}

    def find_max_vehicles(i, remaining_weight, front_vehicles):
        if i == n:
            return front_vehicles

        if (i, remaining_weight, front_vehicles) in memo:
            return memo[(i, remaining_weight, front_vehicles)]

        upper_bound = bound(i, remaining_weight, front_vehicles)

        if upper_bound < front_vehicles:
            return front_vehicles

        skip_branch = find_max_vehicles(i + 1, remaining_weight, front_vehicles)

        if remaining_weight >= v_weight[i]:
            back_branch = find_max_vehicles(i + 1, remaining_weight - v_weight[i], front_vehicles)

            front_branch = find_max_vehicles(i + 1, remaining_weight - v_weight[i], front_vehicles + 1)
        else:
            back_branch = skip_branch
            front_branch = skip_branch

        solution = max(skip_branch, back_branch, front_branch)

        memo[(i, remaining_weight, front_vehicles)] = solution
        return solution

    def bound(i, remaining_weight, front_vehicles):
        vehicles_left = n - i
        if vehicles_left == 0:
            return front_vehicles
        remaining_weight -= sum(v_weight[i:i + vehicles_left])
        if remaining_weight < 0:
            return front_vehicles
        return front_vehicles + min(vehicles_left, remaining_weight // min(v_weight[i:i + vehicles_left]))

    return find_max_vehicles(0, w, 0)


input_data = list(map(int, input("Enter input data as a space-separated list: ").split()))
result = largest_number_of_vehicles(input_data)
print(result)
