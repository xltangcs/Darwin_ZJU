from .nc_pkgb_utils import *
'''
nc_pkgb_head
nc_pkgb_body0
nc_pkgb_body0_riscv_reg
nc_pkgb_body0_riscv_sram
nc_pkgb_body1
nc_pkgb_body1_riscv
nc_pkgb_tail_write
nc_pkgb_tail_read
nc_pkgb_tail_read_riscv_reg
nc_pkgb_tail_read_riscv_sram

'''


def nc_pkgb_head(
                route_id: int,
                pkgb_class: NC_PKGB_Class, 
                dst_port: int, 
                dst_x, dst_y, src_x, src_y):
    """ 
    Assemble package head.

    Args:
        route_id: Index of router. ∈[0, 23]
        pkgb_class: NC_PKGB_CLASS
        dst_x
        dst_y
        src_x
        src_y
    
    Returns:
        flit

    """

    flit_type = NC_PKGB_FlitType.HEAD.value
    route_id = route_id 
    pkgb_class = pkgb_class.value
    dst_port = dst_port
    signx = 1 if dst_x < 0 else 0
    signy = 1 if dst_y < 0 else 0
    dst_x = abs(dst_x)
    dst_y = abs(dst_y)

    src_x = src_x
    src_y = src_y 

    ra = 0 

    binary_str = "{:02b}{:05b}{:03b}{:03b}{:01b}{:04b}{:01b}{:04b}{:04b}{:04b}{:01b}\n".format(flit_type, route_id, pkgb_class, dst_port, signx, dst_x, signy, dst_y, src_x, src_y, ra)

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_body0(waddr: int):
    """ 
    Assemble package body0.

    Args:
        waddr: Target address
    
    Returns:
        flit

    """

    flit_type = NC_PKGB_FlitType.BODY.value

    relay_id = 0 
    relay_link = 0 
    rd = 0 

    waddr = waddr 

    resv  = 0

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:017b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, waddr, resv) 

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_body0_riscv_reg(riscv_reg_id, reg_data_sel):
    """ 
    Assemble package body0.

    Args:
        
    
    Returns:
        flit

    """

    flit_type = NC_PKGB_FlitType.BODY.value

    relay_id = 0 
    relay_link = 0 
    rd = 0 

    reg_sram_sel = 0
    riscv_reg_id = riscv_reg_id
    reg_data_sel = reg_data_sel

    resv  = 0

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:01b}{:08b}{:08b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram_sel, riscv_reg_id, reg_data_sel, resv) 

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_body0_riscv_sram(sram_waddr, sram_high_or_low):
    """ 
    Assemble package body0.

    Args:
        
    
    Returns:
        flit

    """

    flit_type = NC_PKGB_FlitType.BODY.value

    relay_id = 0 
    relay_link = 0 
    rd = 0 

    reg_sram_sel = 1
    sram_waddr = sram_waddr
    sram_high_or_low = sram_high_or_low

    resv  = 0

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:01b}{:015b}{:01b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram_sel, sram_waddr, sram_high_or_low, resv) 
    
    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_body1(wdata1=0):
    """ 
    Assemble package body1.

    Args:
        wdata1: Upper 24 bits of data
    
    Returns:
        flit
        
    """
    flit_type = NC_PKGB_FlitType.BODY.value
    resv1 = 0 
    wdata1 = wdata1 
    resv2 = 0 

    binary_str = "{:02b}{:03b}{:024b}{:03b}\n".format(flit_type, resv1, wdata1, resv2) 

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_body1_riscv(wdata1=0):
    """ 
    Assemble package body1.

    Args:
       wdata1: High 8 bits of riscv data 
    
    Returns:
        flit
        
    """
    flit_type = NC_PKGB_FlitType.BODY.value
    resv1 = 0 
    wdata1 = wdata1 
    resv2 = 0 

    binary_str = "{:02b}{:03b}{:016b}{:08b}{:03b}\n".format(flit_type, resv1, 0, wdata1, resv2) 

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_tail_write(wdata0=0):
    """ 
    Assemble package tail for write.

    Args:
        wdata0: Lower 24 bits of data 
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    wdata0 = wdata0
    resv = 0 

    binary_str = "{:02b}{:03b}{:024b}{:03b}\n".format(flit_type, relay_id, wdata0, resv)

    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_read(raddr=0):
    """ 
    Assemble package tail for read.

    Args:
        raddr: read address
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    relay_link = 0 
    rd = 0 
    raddr = raddr  
    resv = 0 

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:017b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, raddr, resv)
    
    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_tail_read_riscv_reg(reg_id, reg_data_sel):
    """ 
    Assemble package tail for read.

    Args:
        raddr: read address
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    relay_link = 0 
    rd = 0 

    reg_sram_sel = 0
    reg_id = reg_id  
    reg_data_sel = reg_data_sel

    resv = 0 

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:01b}{:08b}{:08b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram_sel, reg_id, reg_data_sel, resv) 

    return int(binary_str, 2) & 0xffffffff

def nc_pkgb_tail_read_riscv_sram(sram_raddr, sram_high_or_low):
    """ 
    Assemble package tail for read.

    Args:
        raddr: read address
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    relay_link = 0 
    rd = 0 

    reg_sram_sel = 1
    sram_raddr = sram_raddr  
    sram_high_or_low = sram_high_or_low  

    resv = 0 

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:01b}{:015b}{:01b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram_sel, sram_raddr, sram_high_or_low, resv) 

    return int(binary_str, 2) & 0xffffffff