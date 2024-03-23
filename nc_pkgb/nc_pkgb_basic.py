from .nc_pkgb_utils import *


def nc_pkgb_head(route_id: int, 
                 pkgb_class: NC_PKGB_Class, 
                 dst_port: int, 
                 dst_x, dst_y, src_x, src_y, output_type="hex"):
    """ 
    Assemble package head.

    Args:
        route_id: Index of router. ∈[0, 23]
        pkgb_class: NC_PKGB_CLASS
        dst_x
        dst_y
        output_type: "hex" or "bin"
        src_x and src_y is abs(xs - xd), abs(ys - yd)
    
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

    #return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_body0(waddr=0, output_type="hex"):
    """ 
    Assemble package body0.

    Args:
        waddr: Target address
        output_type: "hex" or "bin"
    
    Returns:
        flit

    """

    flit_type = NC_PKGB_FlitType.BODY.value
    relay_id = 0 
    relay_link = 0 
    rd = 0 
    waddr = waddr 

    resv  = 0

    binary_str = "{:02b}{:04b}{:06b}{:01b}{:017b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, waddr, resv) 

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_body1(wdata1=0, output_type="hex"):
    """ 
    Assemble package body1.

    Args:
        wdata1: Upper 24 bits of data
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """
    flit_type = NC_PKGB_FlitType.BODY.value
    resv1 = 0 
    wdata1 = wdata1 
    resv2 = 0 

    binary_str = "{:02b}{:03b}{:024b}{:03b}\n".format(flit_type, resv1, wdata1, resv2) 

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_write(wdata0=0, output_type="hex"):
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

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_read(raddr=0, output_type="hex"):
    """ 
    Assemble package tail for read.

    Args:
        raddr: read address
        output_type: "hex" or "bin"
    
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

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_spike(neu_id=0, dedr_id=0, output_type="hex"):
    """ 
    Assemble package tail for read.

    Args:
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    resv = 0 

    binary_str = "{:02b}{:015b}{:012b}{:03b}\n".format(flit_type, dedr_id, neu_id, resv)

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_body0_riscv_reg(reg_addr=0, reg_sel=0, output_type="hex"):
    """ 
    Assemble package tail for write.

    Args:
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.BODY.value
    relay_id = 0 
    relay_link = 0 
    rd = 0 
    reg_sram = 0

    resv  = 0

    binary_str = "{:02b}{:04b}{:06b}{:01b}{:01b}{:08b}{:08b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram, reg_addr, reg_sel, resv) 

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_body1_riscv(wdata1=0, output_type="hex"):
    """ 
    Assemble package tail for write.

    Args:
        wdata1: High 8 bits of riscv data 
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.BODY.value
    relay_id = 0 
    resv = 0 

    binary_str = "{:02b}{:03b}{:016b}{:08b}{:03b}\n".format(flit_type, relay_id, 0, wdata1, resv)

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_write_riscv_reg(wdata0=0, output_type="hex"):
    """ 
    Assemble package tail for write.

    Args:
        wdata0: Lower 24 bits of riscv data 
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    wdata0 = wdata0
    resv = 0 

    binary_str = "{:02b}{:03b}{:024b}{:03b}\n".format(flit_type, relay_id, wdata0, resv)

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff


def nc_pkgb_tail_read_riscv_reg(reg_addr=0, reg_sel = 0, output_type="hex"):
    """ 
    Assemble package tail for write.

    Args:
        output_type: "hex" or "bin"
    
    Returns:
        flit
        
    """

    flit_type = NC_PKGB_FlitType.TAIL.value
    relay_id = 0 
    relay_link = 0
    rd = 0
    reg_sram_sel = 0
    resv = 0 

    binary_str = "{:02b}{:03b}{:06b}{:01b}{:01b}{:08b}{:08b}{:03b}\n".format(flit_type, relay_id, relay_link, rd, reg_sram_sel, reg_addr, reg_sel, resv)

    # return binary_str if output_type == "bin" else "0x{:08x}\n".format(int(binary_str, 2))
    return int(binary_str, 2) & 0xffffffff