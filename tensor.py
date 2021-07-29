
class Tensor:

    # Constructor for Tensor object that callse shape_data
    def __init__(self, data, shape):
        self.data = data
        self.shape = shape
        self.tensor = self.shape_data(data, shape)

    # Method that creates the nested list of our Tensor class
    def shape_data(self, data, shape):
        # If shape is empty, return an empty list
        if not shape:
            return []
        # If shape only has one value, return a list of data elements of the size of that single shape value
        if len(shape) == 1 and data:
            return data[0:shape[0]]
        # If shape only has one value but data is empty, return a list of zeroes of the size of that single shape value
        if len(shape) == 1 and not data:
            zero_array = []
            for x in range(shape[0]):
                zero_array.append(0.0)
            return zero_array

        # If our data and shape lists do not fit in to the previous cases, we will use recursion to build our nested list
        tensor = []
        # Disregard the final element in shape since we have already stored it in the element_count variable
        modified_copy_of_shape = shape[0:len(shape)-1]
        tensor = add_lists(tensor, modified_copy_of_shape)
        return tensor

# Method defined outside of Tensor class that will call itself repeatedly
def add_lists(tensor, modified_copy_of_shape):
    # Base case - Once we have reached the base case of recursion, when modified_copy_of_shape only has one element,
    # we will create the amount of lists equal to the value of that single element and these lists will be of size element_count;
    # As these lists are created, we will pop the data elements from the reversed data_array we created around line 79 into these lists
    if len(modified_copy_of_shape) == 1:
        for x in range(modified_copy_of_shape[0]):
            new_array = []
            for i in range(element_count):
                # If we run out of data values to pop, insert zeroes instead
                if not reverse_data:
                    new_array.append(0.0)
                    continue
                new_array.append(reverse_data.pop())
            tensor.append(new_array)
        return tensor

    # Recursion step - At this recursion level we will call add_lists the number of times as dictated by modified_copy_of_shape[0];
    # As we recurse further, the first value of the current modified_copy_of_shape at any given level will be left out each time we progress a recursion level
    # until the base case is reached.
    for x in range(modified_copy_of_shape[0]):
        tensor.append(add_lists([],modified_copy_of_shape[1:len(modified_copy_of_shape)]))

    return tensor

# START OF MAIN PROGRAM
Typed_data_input = 1
Typed_shape_input = 1
data_array = []
shape_array = []

# Ask user for data input to form data list
while(True):
    Typed_data_input = input("Enter data: (Enter the letter a if done): ")
    if Typed_data_input == 'a':
        break
    data_array.append(float(Typed_data_input))

# Ask user for shape input to form shape list
while(True):
    Typed_shape_input = input("Enter shape: (Enter the letter a if done): ")
    if Typed_shape_input == 'a':
        break
    shape_array.append(int(Typed_shape_input))

# Reversing data list as we will pop the data elements later in order to insert our elements into the nested
# list we will create based off the shape list
reverse_data = data_array[::-1]

# Stores the size that we should group our elements by, which is the final value in the shape array
# For example, data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3] and shape0 = [2, 3, 2]
# produces [[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]
# Since the final value of shape0 is 2, we should group our data into groups of 2
if shape_array:
    element_count = shape_array[-1]

# Create a Tensor object
tensor_1 = Tensor(data_array,shape_array)

# Output the Tensor object we created
print("output:")
print(tensor_1.tensor)
