import sys
sys.path.append("..") 
from Darwin3_pkgb import * 
from hex2bin32 import *


def setbit(data, x, a):
    if a == 1:
        return data | (1 << x)
    elif a == 0:
        return data & ~(1 << x)
    else:
        raise ValueError("a must be 0 or 1")

def set_clock(f) :
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0x00000000, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0x00000000, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0x00000000, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0x00000000, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0x00000000, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0x00000000, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")


        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xc, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xd, wdata=0xffffffff, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
        # for data in datas:
        #     f.write("".join(f"{data:08x}") + "\n")


            datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x2, wdata=0x00aa00, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
            for data in datas:
                f.write("".join(f"{data:08x}") + "\n")
            datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x2, wdata=0x00ae02, wdata_sel=0x0f, dir = NC_PKGB_Dir.WEST)
            for data in datas:
                f.write("".join(f"{data:08x}") + "\n")
            datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x3, wdata=0x310000, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
            for data in datas:
                f.write("".join(f"{data:08x}") + "\n")
            datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0x0, wdata=0x10000d, wdata_sel=0xf0, dir = NC_PKGB_Dir.WEST)
            for data in datas:
                f.write("".join(f"{data:08x}") + "\n")


def rw_test(f) :
    datas = nc_pkgb_write(src_core_x=-1,src_core_y=0,dst_core_x=1,dst_core_y=0, waddr=0x1000, wdata=0x12345678)
    for data in datas:
        f.write("".join(f"{data:08x}") + "\n")
    datas = nc_pkgb_read(src_core_x=-1,src_core_y=0,dst_core_x=1,dst_core_y=0,raddr=0x1000)
    for data in datas:
        f.write("".join(f"{data:08x}") + "\n")

def config_relay(f):
    datas = []
    datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x02, wdata=0x00))

    datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x0, wdata=0xf1))
    datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x8000, wdata=0x01, relay_id=1))
    relay_rule = create_relay_rule(LCF=1, dst_x = 6, dst_y = 0, RY=0 ,RF=0, src_x=-15,src_y=0)
    datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x8001, wdata=relay_rule, relay_id=1))


    # datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=1, waddr=0x02, wdata=0x00))
    # datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=1, waddr=0x0, wdata=0xf2))
    # datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=1, waddr=0x8000, wdata=0x01, relay_id=2))
    # relay_rule = create_relay_rule(LCF=1, src_x=-15, src_y=0)
    # datas.extend(nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=1, waddr=0x8001, wdata=relay_rule, relay_id=2))


    for data in datas:
        f.write("{:08x}\n".format(data))
        # f.write("".join(f"{data:08x}") + "\n")

if __name__ == '__main__':
    rootfile = "../test_SOW/"
    outputName = "test_rw_0_0.txt"  
    filepath = rootfile + outputName

    with open (filepath, 'w') as f:
        # rw_test(f)
        # flit_end(f)

        # config_relay(f)
        # datas = nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x1000, wdata=1234, relay_id=0, relay_link=0, rd=0)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))

        # datas = nc_pkgb_read(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, raddr=0x1000, relay_id=0, relay_link=0, rd=0)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))

        # datas = nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x00, wdata=0xf0)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))

        # datas = nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x02, wdata=0x00)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))

        # datas = nc_pkgb_write(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, waddr=0x8000, wdata=0x01, relay_id=0)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))

        # datas = nc_pkgb_read(src_core_x=-1,src_core_y=2,dst_core_x=14,dst_core_y=2, raddr=0x8000, relay_id=0)
        # for data in datas:
        #     f.write("{:08x}\n".format(data))
        
        datas = nc_pkgb_write_riscv_reg(riscv_reg_id=0xb, wdata=0xffffffff, wdata_sel=0x0f, dir = NC_PKGB_Dir.NORTH)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        datas = nc_pkgb_read_riscv_reg(riscv_reg_id=0xb, wdata_sel=0x0f, dir = NC_PKGB_Dir.NORTH)
        for data in datas:
            f.write("".join(f"{data:08x}") + "\n")
        # datas = nc_pkgb_write(src_core_x=-1,src_core_y=1,dst_core_x=1,dst_core_y=2, waddr=0x1000, wdata = 0x5678)
        # for data in datas:
        #      f.write("{:08x}\n".format(data))
        # datas = nc_pkgb_read(src_core_x=-1,src_core_y=1,dst_core_x=1,dst_core_y=2, raddr=0x1000)
        # for data in datas:
        #      f.write("{:08x}\n".format(data))
        
    gen_bin(filepath)
   
