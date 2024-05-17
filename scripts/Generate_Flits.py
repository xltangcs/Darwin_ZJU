import sys
sys.path.append("..") 
from Darwin3_pkgb import * 
from hex2bin32 import *
from utils import *

# filepath = "test.txt"
# f = open(filepath, "w")

def set_clock(src_core_x = -1, src_core_y = 0) :
        wdata = 0xffffffff
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xb, wdata=wdata, wdata_sel=0x0f)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xb, wdata=wdata, wdata_sel=0xf0)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xc, wdata=wdata, wdata_sel=0x0f)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xc, wdata=wdata, wdata_sel=0xf0)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xd, wdata=wdata, wdata_sel=0x0f)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0xd, wdata=wdata, wdata_sel=0xf0)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")


        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0x2, wdata=0x00aa00, wdata_sel=0x0f)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0x2, wdata=0x00ae02, wdata_sel=0x0f)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0x3, wdata=0x310000, wdata_sel=0xf0)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_write_riscv_reg(src_core_x = src_core_x,src_core_y = src_core_y,dst_core_x=0,dst_core_y=0, riscv_reg_id=0x0, wdata=0x10000d, wdata_sel=0xf0)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")

def write_read_core(src_core_x, src_core_y, dst_core_x, dst_core_y):
    datas = []
    datas.extend(nc_pkgb_write(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, waddr=0x1000, wdata=0x1234, relay_id=0, relay_link=0, rd=0))
    datas.extend(nc_pkgb_read(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, raddr=0x1000, relay_id=0, relay_link=0, rd=0))
    for data in datas:
        f.write("{:08x}\n".format(data))

def read_core(src_core_x, src_core_y, dst_core_x, dst_core_y):
    datas = []
    datas.extend(nc_pkgb_read(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, raddr=0x8000, relay_id=1, relay_link=0, rd=0))
    for data in datas:
        f.write("{:08x}\n".format(data))

def write_read_riscv(src_core_x, src_core_y, dst_core_x, dst_core_y):
    datas = []
    datas.extend(nc_pkgb_write_riscv_reg(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, riscv_reg_id=0xb, wdata = 0x12345678,wdata_sel=0x0f))
    datas.extend(nc_pkgb_read_riscv_reg(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, riscv_reg_id=0xb, wdata_sel=0x0f))
    for data in datas:
        f.write("{:08x}\n".format(data))

def config_relay(src_core_x, src_core_y, dst_core_x, dst_core_y):
    datas = []
    datas.extend(nc_pkgb_write(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, waddr=0x02, wdata=0x00))
    datas.extend(nc_pkgb_write(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, waddr=0x0, wdata=0xf1))
    datas.extend(nc_pkgb_write(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, waddr=0x8000, wdata=0x01, relay_id=1))
    relay_rule = create_relay_rule(LCF=1, dst_x = 10, dst_y = 0, src_x=-15, src_y=0)
    datas.extend(nc_pkgb_write(src_core_x=src_core_x,src_core_y=src_core_y,dst_core_x=dst_core_x,dst_core_y=dst_core_y, waddr=0x8001, wdata=relay_rule, relay_id=1))

    for data in datas:
        f.write("{:08x}\n".format(data))


if __name__ == '__main__':
    rootfile = "../test_SOW/"
    outputName = "rw_24_0_w.txt" 
    filepath = rootfile + outputName
    f = open(filepath, "w")

    # config_relay(-1,0,14,0)
    # write_read_core(-1,0,14,0)
    # read_core(-1,0,14,0)
    write_read_riscv(-1,0,14,0)



    f.close()
    gen_bin(filepath)
   
