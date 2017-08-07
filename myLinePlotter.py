import Tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure	
import matplotlib.pyplot as plt
import time
import numpy as np

class myLinePlotter:
	
	def __init__(self):
		
		root = Tkinter.Tk()
		# Create a container
		
		frame = Tkinter.Frame(root)
		
		# create a figure
		
		fig = plt.figure(figsize=(12, 6), dpi=96, facecolor='w', edgecolor='k')
		
		self.ax = fig.add_axes([.1,.1,.8,.8])
		#initialize left plot
		#self.plot = ax.plot(np)
		#plt.ion()
		self.plot, =self.ax.plot(np.zeros(400),np.zeros(400))
		#self.ax.axis('off')
		self.ax.get_xaxis().set_visible(False)
		self.ax.get_yaxis().set_visible(False)
		#self.plot.set_clim(0,1)
	
		#builds the gui
		self.canvas = FigureCanvasTkAgg(fig,master=root)
		self.canvas.show()
		self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)
		frame.pack()

		
	def set_data(self,X_in,Y_in):
		self.plot.set_xdata(X_in)
		self.plot.set_ydata(Y_in)
		#self.plot.draw()
		self.canvas.draw()
		self.canvas.flush_events()
		
		
	def set_xlim(self,lowerlim,upperlim):
		self.ax.set_xlim([lowerlim,upperlim])
	
	def set_ylim(self,lowerlim,upperlim):
		self.ax.set_ylim([lowerlim,upperlim])
		