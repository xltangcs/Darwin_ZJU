import sys
from struct import pack
def gen_bin(hex_in):
    #print(hex_in)
    bin_out = hex_in.replace(".txt","").replace(".hex","") + ".bin"
    with open(hex_in,"r") as hex_f:
        bin_f = open(bin_out, "wb")
        for line in hex_f.readlines():
            line.replace("\n","")
            if (line[0] not in "0123456789abcdefABCDEF"):
                continue
            #for i in range(int(len(line)/2)):
            #    b = eval("0x" + line[2*i:2*i+2])
            #    bin_f.write(pack('B', b))
            value = eval("0x"+line)
            print('{:08X}'.format(value))
            bin_f.write(pack('I',value))
        bin_f.close()
    hex_f.close()

if __name__ == "__main__":
    input_file = "test.txt"
    if (len(sys.argv) == 2):
        input_file = sys.argv[1]

    gen_bin(input_file)