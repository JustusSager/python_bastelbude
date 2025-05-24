# Activation functions
def relu(x):
    if x > 0:
        return x
    else:
        return 0


def relu_derivative(x):
    if x > 0:
        return 1
    else:
        return 0
