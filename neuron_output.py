def neuron_output(inputs, weights, bias):
    total = 0.0
    for x, w in zip(inputs, weights):
        total += x * w
    total += bias
    return total


inputs = [2.0, 3.0]
weights = [0.5, -1.0]
bias = 1.0

output = neuron_output(inputs, weights, bias)
print(output)