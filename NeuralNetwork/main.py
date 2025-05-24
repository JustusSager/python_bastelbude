import numpy as np

import functions

xor_training_examples = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
xor_targets = np.array([
    [0],
    [1],
    [1],
    [0]
])


if __name__ == "__main__":
    xor_training_examples_num = xor_training_examples.shape[0]  # Number of training examples
    print('XOR Shape of trainings examples\n', xor_training_examples_num)

    # Add a bias node with values one
    xor_training_examples = np.hstack([np.ones([xor_training_examples_num, 1]), xor_training_examples])
    print('XOR prepared training examples:\n', xor_training_examples)

    # define layer sizes
    input_layer_size = 2 + 1  # +1 for bias node
    hidden_layer_size = 5
    output_layer_size = 1

    # define weight matrix shape
    wih_shape = (input_layer_size, hidden_layer_size)
    who_shape = (hidden_layer_size, output_layer_size)

    # initalize weight matrix with random numbers
    np.random.seed(6)  # Seed with fixed random values, so that we can reproduce the test
    standard_deviation = 0.1
    wih = np.random.normal(scale=standard_deviation, size=wih_shape)
    who = np.random.normal(scale=standard_deviation, size=who_shape)

    print('Initial weights: input->hidden\n', wih)
    print('Initial weights: hidden->output\n', who)

    # test with 3rd training example
    x = xor_training_examples[2]
    y = xor_targets[2]
    print(x, y)


