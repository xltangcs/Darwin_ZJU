import sys
sys.path.append("..") 
from nc_pkgb import * 
from hex2bin32 import *

rootfile = "../test_file/"

if __name__ == '__main__':
    outputfile = rootfile + "test_0_0_W.txt"
    with open (outputfile, 'w') as f:
        # def nc_pkgb_write(dst_port, dst_x, dst_y, src_x, src_y, waddr, wdata, route_id=0):
        dst_x, dst_y = 0, 0
        addr = 0x10
        write_data = 0x0000ffff
        dir = 'W'
        
        datas = nc_write_with_dir(dst_x, dst_y, addr, write_data, dir)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_read_with_dir(dst_x, dst_y, addr, dir)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = ['c0000001', 'c0000000']
        for data in datas:
            data = int(data, 16)
            f.write("".join(f"{data:08x}") + "\n")

    gen_bin(outputfile)
