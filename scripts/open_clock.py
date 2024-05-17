import sys
sys.path.append("..") 
from Darwin3_pkgb import * 

def setbit(data, x, a):
    if a == 1:
        return data | (1 << x)
    elif a == 0:
        return data & ~(1 << x)
    else:
        raise ValueError("a must be 0 or 1")
    
def open_clock(core_x, core_y, frequency = 333):
    '''
    frequency: MHz
    '''
    group = (core_y//4) * 6 + core_x // 4
    tile = core_x%4

    pos = group * 4 + tile

    if pos < 64:
        reg_id = 0xb
        if pos < 32:
            wdata_sel = 0xf0
        else:
            wdata_sel = 0x0f
    elif pos >=64 and pos < 128:
        reg_id = 0xc
        if pos < 96:
            wdata_sel = 0xf0
        else:
            wdata_sel = 0x0f
    else:
        reg_id = 0xd
        wdata_sel = 0x0f

    print(pos)
    wdata = setbit(0, pos%32, 1)
    print('{:08X}'.format(wdata))


    pkgb = []
    pkgb.append(nc_pkgb_write_riscv_reg(riscv_reg_id=reg_id, wdata=wdata, wdata_sel=wdata_sel, dir = NC_PKGB_Dir.WEST))
    
    return pkgb

if __name__ == '__main__':
    print(open_clock(5,0))



