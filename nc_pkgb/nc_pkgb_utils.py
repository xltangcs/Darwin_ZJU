"""'
NC_PKGB is for the assembly of the interchip communication package.
Utilities of NC_PKGB.
 
"""

from enum import Enum, unique


@unique
class NC_PKGB_FlitType(Enum):
    
    HEAD = 2 
    BODY = 0 
    TAIL = 1
    CMD = 3


@unique
class NC_PKGB_Class(Enum):
    
    SPIKE = 0
    WRITE = 1 
    READ = 2

    TRAFFIC_QUERY = 3 
    SHORT_SPIKE = 4 
    REWARD_SPIKE = 5
    REWARD_SHORT_SPIKE = 6 
    BACKFLOW_QUERY = 7


@unique
class NC_TARGET(Enum):
    NC_CR_NEU_NUM = 0x00000 
    NC_CR_DEDR_NUM = 0x00001 
    NC_CR_WORKMODE = 0x00002 
    NC_CR_RPD = 0x00003 
    NC_CR_STATE = 0x00004 
    NC_CR_PC = 0x00005 
    NC_SR_ERROR = 0x00006
    NC_CR_INTMASK = 0x00007 
    NC_CR_QA = 0x00008 
    NC_CR_RANDMOD = 0x00009 
    NC_CR_RANDSEED = 0x0000a 
    NC_CR_LPARXY = 0x0000b
    NC_CR_LPARRR = 0x0000c 
    NC_CR_WPARA = 0x0000d 
    NC_CR_WPARB = 0x0000e 
    NC_CR_WPARC = 0x0000f 
    NC_CR_WPARD = 0x00010 
    NC_CR_CPARA = 0x00011 
    NC_CR_CPARB = 0X00012 
    NC_CR_CPARC = 0x00013 
    NC_SR_PKGCNT = 0x00014 
    NC_CR_EN = 0x00015 
    NC_CR_VTDEC = 0x00016 
    NC_SR_SPIKEINCNT = 0x00017 
    NC_SR_SPIKEOUTCNT = 0x00018 
    NC_SR_DS0 = 0x00019 
    NC_SR_DS1 = 0x0001a 
    NC_CR_DRH = 0x0001b
    NC_CR_CGEN = 0x0001c 
    NC_CR_LINKSIZE = 0x0001d 
    NC_CR_LI = 0x0001e 
    NC_CR_TN = 0x0001f 
    
    NC_REG_VT = 0X800
    NC_REG_VTH = 0X801 
    NC_REG_I = 0X802 
    NC_REG_RPD = 0X803 
    NC_REG_WGTSUM = 0x804
    NC_REG_RES = 0x805 
    NC_REG_RAND = 0x806 
    NC_REG_WGT = 0x807 
    NC_REG_PRTXA = 0x808 
    NC_REG_PRTYA = 0x809 
    NC_REG_PRTXB = 0x80a
    NC_REG_PRTYB = 0x80b 
    NC_REG_PRTR = 0x80c 
    NC_REG_PAR01 = 0x80d 
    NC_REG_PAR23 = 0x80e 
    NC_REG_PAR45 = 0x80f 


@unique
class NC_REG(Enum):
    NC_REG0 = 0x800 
    NC_REG1 = 0x801 
    NC_REG2 = 0x802 
    NC_REG3 = 0x803 
    NC_REG4 = 0x804 
    NC_REG5 = 0x805 
    NC_REG6 = 0x806 
    NC_REG7 = 0x807 
    NC_REG8 = 0x808 
    NC_REG9 = 0x809 
    NC_REG10 = 0x80a
    NC_REG11 = 0x80b 
    NC_REG12 = 0x80c 
    NC_REG13 = 0x80d 
    NC_REG14 = 0x80e 
    NC_REG15 = 0x80f 


@unique
class NC_BASE_ADDR(Enum):
    NC_CR = 0x0 
    NC_REG = 0x800 
    NC_INST = 0x1000 
    NC_VM = 0x2000 
    NC_WGTSUM = 0x4000 
    NC_DEDR = 0x10000
    NC_AXON = 0x8000


@unique
class NC_STATE(Enum):

    WGTSUM = 0x4000
    VM = 0x2000
    WGTSUM_EVEN = 0x5000



def nc_eval_port(cx, cy):
    distences = [23 - cx,  cy, cx, 23 - cy]

    min_dis = min(distences)

    port = [0, 3, 2, 1]
    
    return port[distences.index(min_dis)]


NC_IN_PORT = [[nc_eval_port(x, y) for y in range(24)] for x in range(24)]