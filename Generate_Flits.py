from nc_pkgb import * 
from hex2bin32 import *

rootfile = "./test_file/"

if __name__ == '__main__':
    outputfile = rootfile + "test_1_0.txt"
    with open (outputfile, 'w') as f:
        #datas = nc_write(2, 0, 0x0, 0x0000_0012)
        # def nc_pkgb_write(dst_port, dst_x, dst_y, src_x, src_y, waddr, wdata, route_id=0):
        datas = nc_write_with_dir(1, 0, 0x10, 0x0000ffff, 'W')
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_read_with_dir(1, 0, 0x10, 'W')
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = ['c0000001', 'c0000000']
        for data in datas:
            data = int(data, 16)
            f.write("".join(f"{data:08x}") + "\n")

    gen_bin(outputfile)
