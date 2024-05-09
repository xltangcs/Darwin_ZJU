from .nc_pkgb_basic import *

def nc_pkgb_basic_write(dst_port, dst_x, dst_y, src_x, src_y, waddr, wdata, route_id=0):
    wpkg = []
    wdata &= 0xffffffffffff #48bit
    wdata0 = wdata & 0xffffff
    wdata1 = (wdata >> 24) & 0xffffff
    wpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.WRITE, dst_port, dst_x, dst_y, src_x, src_y))
    wpkg.append(nc_pkgb_body0(waddr))
    wpkg.append(nc_pkgb_body1(wdata1))
    wpkg.append(nc_pkgb_tail_write(wdata0))
    
    return wpkg


def nc_pkgb_basic_read(dst_port, dst_x, dst_y, src_x, src_y, raddr, route_id=0):
    rpkg = []
    rpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.READ, dst_port, dst_x, dst_y, src_x, src_y))
    rpkg.append(nc_pkgb_tail_read(raddr))
    return rpkg

def nc_pkgb_write(dst_core_x, dst_core_y, src_core_x, src_core_y, waddr, wdata):
    if src_core_x == -1: # west
        route_id = src_core_y
        if dst_core_x == 0:
            if  src_core_y == dst_core_y:
                dst_port = 0
            elif src_core_x < dst_core_x:
                dst_port = 4
            else:
                dst_port = 2
        else:
            dst_port = 1
        
        dst_x = dst_core_x
        dst_y = dst_core_y - src_core_y
        src_x = abs(dst_core_x - src_core_x)
        src_y = abs(dst_core_y - src_core_y) 
    
    elif src_core_y == -1:
        route_id = src_core_x
        if dst_core_y == 0:
            if  src_core_y == dst_core_y:
                dst_port = 0
            elif src_core_y < dst_core_y:
                dst_port = 3
            else:
                dst_port = 1
        else:
            dst_port = 4

        dst_x = dst_core_x - src_core_x
        dst_y = dst_core_y
        src_x = abs(dst_core_x - src_core_x)
        src_y = abs(dst_core_y - src_core_y) 
    
    return nc_pkgb_basic_write(dst_port=dst_port, dst_x=dst_x, dst_y=dst_y, src_x=src_x, src_y=src_y, waddr=waddr, wdata=wdata, route_id=route_id)


def nc_pkgb_read(dst_core_x, dst_core_y, src_core_x, src_core_y, raddr):
    if src_core_x == -1: # west
        route_id = src_core_y
        if dst_core_x == 0:
            if  src_core_y == dst_core_y:
                dst_port = 0
            elif src_core_x < dst_core_x:
                dst_port = 4
            else:
                dst_port = 2
        else:
            dst_port = 1
        
        dst_x = dst_core_x
        dst_y = dst_core_y - src_core_y
        src_x = abs(dst_core_x - src_core_x)
        src_y = abs(dst_core_y - src_core_y) 
    
    elif src_core_y == -1:
        route_id = src_core_x
        if dst_core_y == 0:
            if  src_core_y == dst_core_y:
                dst_port = 0
            elif src_core_y < dst_core_y:
                dst_port = 3
            else:
                dst_port = 1
        else:
            dst_port = 4

        dst_x = dst_core_x - src_core_x
        dst_y = dst_core_y
        src_x = abs(dst_core_x - src_core_x)
        src_y = abs(dst_core_y - src_core_y) 
    
    return nc_pkgb_basic_read(dst_port=dst_port, dst_x=dst_x, dst_y=dst_y, src_x=src_x, src_y=src_y, raddr=raddr, route_id=route_id)


def nc_pkgb_write_riscv_reg(riscv_reg_id, wdata, wdata_sel, dir: NC_PKGB_Dir):

    dst_port = 0
    route_id = 0

    if dir == NC_PKGB_Dir.WEST:
        src_x = 1
        src_y = 0
        dst_x = 0
        dst_y = 0

    elif dir == NC_PKGB_Dir.NORTH:
        src_x = 0
        src_y = 1
        dst_x = 0
        dst_y = 0

    else :
        return NotImplemented


    wpkg = []
    wdata &= 0xffffffff #32bit
    wdata0 = wdata & 0xffffff
    wdata1 = (wdata >> 24) & 0xff
    wdata_sel = wdata_sel

    wpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.WRITE, dst_port, dst_x, dst_y, src_x, src_y))
    wpkg.append(nc_pkgb_body0_riscv_reg(riscv_reg_id, wdata_sel))
    wpkg.append(nc_pkgb_body1_riscv(wdata1))
    wpkg.append(nc_pkgb_tail_write(wdata0))
    
    return wpkg

def nc_pkgb_read_riscv_reg(riscv_reg_id, wdata_sel, dir: NC_PKGB_Dir):
    dst_port = 0
    route_id = 0

    if dir == NC_PKGB_Dir.WEST:
        src_x = 1
        src_y = 0
        dst_x = 0
        dst_y = 0

    elif dir == NC_PKGB_Dir.NORTH:
        src_x = 0
        src_y = 1
        dst_x = 0
        dst_y = 0

    else :
        return NotImplemented

    rpkg = []
    wdata_sel = wdata_sel
    riscv_reg_id = riscv_reg_id
    
    rpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.WRITE, dst_port, dst_x, dst_y, src_x, src_y))
    rpkg.append(nc_pkgb_tail_read_riscv_reg(riscv_reg_id, wdata_sel ))
    
    return rpkg