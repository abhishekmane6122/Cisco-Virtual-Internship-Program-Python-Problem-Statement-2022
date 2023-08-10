import ipaddress
import sys
import ast
import netaddr
import codecs

input = '["192.45.67.78","255.255.89.2","123.45.67.89","126.98.78.22","23.45.78.67","202.34.61.0","189.56.21.11","192.20.20.20","154.76.89.45","99.56.89.34"]'

# input = input("Enter an ip List: ")
# convert string list input to list
input = ast.literal_eval(input)

# empty list
valid_ip = []
invalid_ip = []
decimal_ip = []

# check valid/invalid ipv4 ip
for i in range(0,len(input)):
    try:
        valid_ip.append(ipaddress.ip_address(input[i]))
        decimal_ip.append(int(netaddr.IPAddress(input[i])))
    except Exception as e:
        invalid_ip.append(ipaddress.ip_address(input[i]))

# convert dec ip to bin,oct,hex ip
binary_ip = [bin(i) for i in decimal_ip]
octal_ip = [oct(i) for i in decimal_ip]
hexadecimal_ip = [hex(i) for i in decimal_ip]

# write the dec,bin,oct,hex ip in a file
f = codecs.open("conversion.txt",'w',encoding='utf8')
for j in range(0,len(decimal_ip)):
    gen_string = str(decimal_ip[j]) + "|" + str(binary_ip[j]) + "|" + str(octal_ip[j]) + "|" + str(hexadecimal_ip[j]) + "\n"
    f.write(gen_string)
    f.flush()

# read/convert conversion.txt file to a list
output_lines = codecs.open("conversion.txt",'r',encoding='utf8').readlines()

# function - pass index and array as parameter
def print_output(i,output_list):
    line = output_list[i].split("|")
    dec_ip = int(line[0])
    bin_ip = line[1]
    oct_ip = line[2]
    hex_ip = line[3]
    print("Decimal IP is {}".format(dec_ip))
    print("Binary IP is {}".format(bin_ip))
    print("Octal IP is {}".format(oct_ip))
    print("Hexadecimal IP is {}".format(hex_ip))


print_output(0,output_lines)
print_output(1,output_lines)




