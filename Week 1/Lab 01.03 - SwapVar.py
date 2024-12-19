"""SwapVar"""

def convert_string_to_tuples(text_in):
    """convert_string_to_tuples"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

def swapvar(data):
    """SwapVar"""
    return (data[1], data[0])

laongdao_data = convert_string_to_tuples(input())
print(swapvar(laongdao_data))
