from .nc_pkgb_basic import *



def nc_pkgb_write(dst_port, dst_x, dst_y, src_x, src_y, waddr, wdata, route_id=0):

    wpkg = []
    wdata0 = wdata & 0xffffff
    wdata1 = (wdata >> 24) & 0xffffff
    wpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.WRITE, dst_port, dst_x, dst_y, src_x, src_y))
    wpkg.append(nc_pkgb_body0(waddr))
    wpkg.append(nc_pkgb_body1(wdata1))
    wpkg.append(nc_pkgb_tail_write(wdata0))
    
    return wpkg


def nc_pkgb_read(dst_port, dst_x, dst_y, src_x, src_y, raddr, route_id=0):
    rpkg = []
    rpkg.append(nc_pkgb_head(route_id, NC_PKGB_Class.READ, dst_port, dst_x, dst_y, src_x, src_y))
    rpkg.append(nc_pkgb_tail_read(raddr))
    return rpkg

def nc_write_with_dir(core_x, core_y, addr, data, dir):
    if dir == 'W':
        src_x = core_x + 1
        src_y = 0
        dst_x = core_x
        dst_y = 0
        dst_port = 1 # East
        route_id = core_y
    elif dir == 'N':
        src_x = 0
        src_y = core_y + 1
        dst_x = 0
        dst_y = core_y
        dst_port = 4 # South
        route_id = core_x

    return nc_pkgb_write(dst_port, dst_x, dst_y, src_x, src_y, addr, data, route_id)

def nc_read_with_dir(core_x, core_y, addr, dir):
    if dir == 'W':
        src_x = core_x + 1
        src_y = 0
        dst_x = core_x
        dst_y = 0
        dst_port = 1 # East
        route_id = core_y
    elif dir == 'N':
        src_x = 0
        src_y = core_y + 1
        dst_x = 0
        dst_y = core_y
        dst_port = 4 # South
        route_id = core_x

    return nc_pkgb_read(dst_port, dst_x, dst_y, src_x, src_y, addr, route_id)
