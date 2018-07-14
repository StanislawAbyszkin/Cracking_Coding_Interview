# How many ways to decode message?
# Given mapping a->1, b->2, c->3 ... z->26
# When you receive message '12' what is it's possible decoded version?
# Ans: '12' can be decoded to 'ab' and 'l'

char2int = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
}

int2char = {}

# Creating reversed dictionary for quick lookup of character from integer
for key, value in char2int.iteritems():
    int2char[value] = key


# helper function to
def convert_to_int(char_array):
    my_str = ''
    for item in char_array:
        my_str += str(char2int[item])

    return my_str


def decode(message, current_decode, current_index):
    total = 0
    if len(convert_to_int(current_decode)) == len(message):
        print current_decode
        return 1
    # add one integer from message
    if current_index + 1 <= len(message):
        int_to_add = int(message[current_index: current_index + 1])
        if int_to_add in int2char:
            total += decode(message,
                            current_decode + int2char[int_to_add],
                            current_index + 1)

    # add two integers from message
    if current_index + 2 <= len(message):
        int_to_add = int(message[current_index: current_index + 2])
        if int_to_add in int2char:
            total += decode(message,
                            current_decode + int2char[int_to_add],
                            current_index + 2)
    return total


if __name__ == '__main__':
    print decode('12326', '', 0)  # should return 6
    print decode('12', '', 0)  # should return 2
    print decode('02', '', 0)  # should return 0
    print decode('30', '', 0)  # should return 0
