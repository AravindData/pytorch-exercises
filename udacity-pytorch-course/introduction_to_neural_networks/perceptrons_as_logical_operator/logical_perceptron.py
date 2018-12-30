import pandas as pd


class Perceptron():

    def __init__(self, weight1, weight2, bias):
        self.weight1 = weight1
        self.weight2 = weight2
        self.bias = bias

    def logical_operator(self, operator_type, correct_outputs):

        test_inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]
        outputs = []

        # Generate and check output
        for test_input, correct_output in zip(test_inputs, correct_outputs):
            linear_combination = self.weight1 * test_input[0] + self.weight2 * test_input[1] + self.bias
            output = int(linear_combination >= 0)
            is_correct_string = 'Yes' if output == correct_output else 'No'
            outputs.append([test_input[0], test_input[1], linear_combination, output, is_correct_string])

        # Print output
        num_wrong = len([output[4] for output in outputs if output[4] == 'No'])
        output_frame = pd.DataFrame(outputs, columns=['Input 1',
                                                      '  Input 2',
                                                      '  Linear Combination',
                                                      '  Activation Output',
                                                      '  Is Correct'])
        print(output_frame.to_string(index=False))

        if not num_wrong:
            return 1, num_wrong
        else:
            return 0, num_wrong

if __name__ == "__main__":

    type_of_logical_opeators = [{"AND": {"values": [1.0, 4.0, -5.0], "correct_output": [False, False, False, True]}}]

    for x in type_of_logical_opeators:
        operator_type = x.keys()[0]
        weight1, weight2, bias = x.values()[0].get('values')
        correct_output = x.values()[0].get('correct_output')

        perceptron = Perceptron(weight1, weight2, bias)
        result, num_wrong = perceptron.logical_operator(operator_type=operator_type,
                                                        correct_outputs=correct_output)
        if result:
            print('Nice!  You got it all correct.\n')
        else:
            print('You got {} wrong.  Keep trying!\n'.format(num_wrong))
