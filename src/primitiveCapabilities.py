class PrimitiveCapabilities():
    def __init__(self):
        pass

    def run(self, capability, data):
        response = 0
        if(capability=="$max"):
            response = self.max(data)

        if(capability=="$min"):
            response = self.min(data)

        if(capability=="$average"):
            response = self.average(data)

        return response

    def max(self, data):
        max = 0
        for value in data:
            if(max<value):
                max = value
        return max

    def min(self, data):
        min = 0xFFFF
        for value in data:
            if(min>value):
                min = value
        return min

    def average(self, data):
        sum = 0
        i = 0
        for value in data:
            sum = sum + value
            i = i+1
        return sum/i