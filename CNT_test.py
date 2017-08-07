import matplotlib
matplotlib.use('TKagg')
import matplotlib.pyplot as plt
import Tkinter
import numpy as np
import time
from matplotlib.path import Path
from CNT_obj import CNT_obj
from myLinePlotter import myLinePlotter

def main():
	N_points=103
	A=CNT_obj(1,10000,N_points)
	#print A.y_cnt[::6]
	#A.y_cnt[13:-13:6]=(np.random.rand(97)*2-1)*.0001
	A.y_cnt[7:-7:6]=np.sin(np.linspace(0,np.pi,N_points-2	))
	
	A.CNT_myrhs(0,A.y_cnt)
	A.set_h(2*10000)
	
	#plt.ion()
	#fig = plt.figure(figsize=(12, 6), dpi=96, facecolor='w', edgecolor='k')
	
	root = Tkinter.Tk()
	view_gui = myLinePlotter(root)
	view_gui.set_xlim(0,10000)
	view_gui.set_ylim(-2,2)
	tic = time.time()
			
	for i in range(1000000):
		A.timestep()
		#if i % 200 ==0:
			#plt.clf()
		view_gui.set_data(A.r.y[::6],A.r.y[1::6])
			#ax=plt.gca()
			#ax.set_ylim([-1,1])
			#fig.canvas.draw()
			#plt.draw()	
	# A.r.y
	toc = time.time()
				
	print toc-tic

	root.destroy()
	
if __name__ == '__main__':
	main()