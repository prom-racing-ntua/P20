byte = '01010110'
which_bits = '10100110'
message = byte * 256


def bitwise_operation(source, get_bits):
    bits = int(get_bits, 2) # binary string to int
    source_in_bits = int(source, 2) 
    result = source_in_bits & bits
    #result = bin(result)[2:]
    result = ('{:0%db}'%len(get_bits)).format(result) # this was the fastest of the 3
    #result = format(result, 'b')
    return result


out = bitwise_operation(message, which_bits)
print(out) 

