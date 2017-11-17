#!python

from models import make_mpc_command
from subprocess import call

vol_to_0 = make_mpc_command(['volume', '0'])
pause = make_mpc_command(['pause'])
play = make_mpc_command(['play'])

call(vol_to_0)
call(pause)
call(play)