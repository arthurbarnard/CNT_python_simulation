import matplotlib
matplotlib.use('TKagg')
import matplotlib.pyplot as plt
import Tkinter
import numpy as np
import time
import scipy.io
from matplotlib.path import Path
from CNT_obj import CNT_obj
from myLinePlotter import myLinePlotter

def main():
	
	
	N_points=102
	diameter=3
	Length=10000
	timestep=2000
	xmin,xmax=100,10100
	ymin,ymax=-160,50
	Nsteps=int(1E7)
	initfile='thermalized_init_0.mat'
	fname_out='G:/CNT_simulations/python_RG8_integrate_0.txt'

	
	#initialize CNT properties
	thisCNT=CNT_obj(diameter,Length,N_points)
	thisCNT.set_h(timestep)
	
	
	#load in initial shape of CNT
	fout = open(fname_out,'wb')
	mat = scipy.io.loadmat(initfile)
	if 'X' in mat: X=np.squeeze(mat['X'])
	thisCNT.set_y(X)

	view_gui = myLinePlotter()
	view_gui.set_xlim(xmin,xmax)
	view_gui.set_ylim(ymin,ymax)
	
	
	tic = time.time()		
	for i in range(Nsteps):
		
		#integrate ode
		thisCNT.timestep()
		#plot result
		view_gui.set_data(thisCNT.r.y[::6],thisCNT.r.y[2::6])
		#write to binary file
		fout.write(thisCNT.r.y)

	toc = time.time()
				
	print toc-tic

	root.destroy()
	
if __name__ == '__main__':
	main()