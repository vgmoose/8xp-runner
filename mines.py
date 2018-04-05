from tibasic import ti

G=0
H=0
R=0

MINE = [0]*11
MINE[10] = 27
MINE[3] = 2
MINE[4] = 999999
MINE[9] = 1

if MINE[2] == 0:
	ti.ClrHome()
	ti.Disp("This PRGM uses", "Pic0 and [A]/[B]", "If there's", "important info", "there, move it", "to another VAR", "or it'll be")
	ti.Output(8, 1, "deleted!")
	K = 0
#	while K!=21 and K!=105
#		K = ti.getKey()
	
input()
