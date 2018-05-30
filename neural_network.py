import numpy as np
import scipy.special

class NeuralNetwork:
    # init neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # weight input to hidden, hidden to output
        self.w_ih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.w_ho = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.lr = learning_rate

        # sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # train neural network
    def train():
        pass

    def query():
        pass
