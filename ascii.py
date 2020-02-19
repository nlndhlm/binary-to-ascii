# ASCII-konverterer
# fra 8-bits binærkode til 7-bits ascii-symboler

from ascii_table_8bit import table as at


# denne må skrives som en string, grunnet 'trailing 0's' ikke er mulig for int
loff = "010011001100001110111000011011100110111001100101011101000010000001110101011101000110010001100001011011100110111001101001011011100110011100101100001000000111000001110010011000010110101101110011011010010111001101110000011011000110000101110011011100110010000001101111011001110010000001100110011000010111001101110100001000000110101001101111011000100110001000101110"

sentence = loff

##########################################

# input: tall fra totallssystemet
# output: tall fra titallssystemet
def binary_to_decimal(num):
    
    binary_num = list(str(num))
    binary_num = binary_num[::-1]

    decimal_num = 0

    for i in range(len(binary_num)):
        decimal_num = decimal_num + (int(binary_num[i]) * 2**i)


    return(decimal_num)

# print(binary_to_decimal(n))



# input: tall fra titallssystemet
# output: ascii symbol fra korresponderende plass
def num_to_ascii(num):
    return(at[num])

# print(num_to_ascii(binary_to_decimal(n)))


# angir hvor setningen skal deles opp
bits = 8

list_of_bits = [sentence[i:i+bits] for i in range(0, len(sentence), bits)]
print(list_of_bits)

##import re
##
##list_of_bits = re.findall('........', sentence)

##for bit in list_of_bits:
##    print(num_to_ascii(binary_to_decimal(bit)))

for byte in range(len(list_of_bits)):
    #print(binary_to_decimal(list_of_bits[byte]))
    print(num_to_ascii(binary_to_decimal(list_of_bits[byte])))
    
