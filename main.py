def largest_number_of_vehicles(data):
    max_w = data[0]
    n = data[1]
    w = data[2:]

    memo = {}

    def branch_and_bound(i, weight_sum, v_count):
        if (i, weight_sum, v_count) in memo:
            return memo[(i, weight_sum, v_count)]
        if i == n:
            return v_count
        if weight_sum + w[i] <= max_w:
            front_branch = branch_and_bound(i + 1, weight_sum + w[i], v_count + 1)
            back_branch = branch_and_bound(i + 1, weight_sum, v_count)
            output = max(front_branch, back_branch)
        else:
            output = branch_and_bound(i + 1, weight_sum, v_count)
        memo[(i, weight_sum, v_count)] = output
        return output
    return branch_and_bound(0, 0, 0)


input_data = list(map(int, input("Enter input data as a space-separated list: ").split()))
result = largest_number_of_vehicles(input_data)
print(result)