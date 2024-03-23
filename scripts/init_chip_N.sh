#!/bin/sh

source ./scripts/restart_dma

python3 ./scripts/flits_sender.py ./chip_test/reset_clock/default_clock_N.bin 2
python3 ./scripts/flits_sender.py ./chip_test/reset_clock/pll_clock_N.bin 2