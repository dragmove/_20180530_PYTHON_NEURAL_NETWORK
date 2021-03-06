import numpy
from scipy.special import expit as sigmoid
import matplotlib.pyplot


class NeuralNetwork:
    # init neural network
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = output_nodes

        # weight input to hidden, hidden to output
        self.w_ih = numpy.random.normal(
            0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.w_ho = numpy.random.normal(
            0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        self.lr = learning_rate

        # sigmoid function
        self.activation_function = lambda x: sigmoid(x)
        
        pass

    # train neural network
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T  # get column vector
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.w_ih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.w_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = numpy.dot(self.w_ho.T, output_errors)

        # update weight
        self.w_ho += self.lr * \
            numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                   numpy.transpose(hidden_outputs))

        self.w_ih += self.lr * \
            numpy.dot((hidden_errors * hidden_outputs *
                    (1.0 - hidden_outputs)), numpy.transpose(inputs))

        pass

    def query(self, inputs_list):
        inputs = numpy.array(inputs_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.w_ih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.w_ho, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        return final_outputs
