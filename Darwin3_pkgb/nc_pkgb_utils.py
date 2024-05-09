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
class NC_PKGB_Dir(Enum):
    
    WEST = 0,
    EAST = 1, 
    NORTH = 2,
    SOURTH = 3