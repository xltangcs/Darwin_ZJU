import sys
sys.path.append("..") 
from Darwin3_pkgb import * 
from hex2bin32 import *

rootfile = "../test_file/"
outputName = "test.txt"


def setbit(data, x, a):
    if a == 1:
        return data | (1 << x)
    elif a == 0:
        return data & ~(1 << x)
    else:
        raise ValueError("a must be 0 or 1")
    


if __name__ == '__main__':
    filepath = rootfile + outputName

    with open (filepath, 'w') as f:

        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x2, wdata=0x14da00, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x2, wdata=0x14de02, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x3, wdata=0x310000, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x0, wdata=0x10000d, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")

        # datas = nc_pkgb_write(src_core_x=-1, src_core_y=0,dst_core_x=0,dst_core_y=0,waddr=0x0a, wdata=0xffffffff)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        
        # datas = nc_pkgb_read(src_core_x=-1, src_core_y=0,dst_core_x=0,dst_core_y=0,raddr=0x0a)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")

        datas = ['c0000001', 'c0000000']
        for data in datas:
            data = int(data, 16)
            f.write("".join(f"{data:08x}") + "\n")

    gen_bin(filepath)
   
