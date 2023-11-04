class QSignal:
    def __init__(self, input, operators):
        self.input = input
        self.operators = operators

    def get_output(self):
        output = self.input
        for i in self.operators:
            output = self.operators[i].get_output(output)
        return output
