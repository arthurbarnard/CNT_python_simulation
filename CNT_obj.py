import numpy as np
from scipy.integrate import ode
from numba import jitclass          # import the decorator
from numba import int32, float32    # import the types



class CNT_obj:
	
	gam_cnt=0
	K_cnt=0
	kap_cnt=0
	sigma=7.767E-25
	kb=1.38E-29
	temp_cnt=0
	h_cnt=0
	X0_cnt=0
	temp_cnt=0
	t_cnt=0
	
	def __init__(self,d_in, L_in, Npoints_in):
		self.L_cnt=L_in
		self.Npoints=Npoints_in
		self.N_cnt=self.Npoints*6
		self.X0_cnt=self.L_cnt/(self.Npoints-3.0)
		self.set_d(d_in)
		self.y_cnt=np.zeros(self.N_cnt)
		self.f_cnt=np.zeros(self.N_cnt,dtype=np.double)
		self.y_cnt[::6]=np.linspace(0,self.Npoints-1,self.Npoints)*self.X0_cnt
		print self.X0_cnt
		self.d=np.zeros(self.Npoints-1)
		self.Del=np.zeros(self.N_cnt-6)
		
		#self.CNT_jit=autojit(self.CNT_myrhs)
		
		#self.r=ode(self.CNT_myrhs).set_integrator('vode',method='BDF',atol=1E-5)
		self.r=ode(self.CNT_myrhs).set_integrator('dop853',rtol=1E-8,nsteps=1E6)
		self.r.set_initial_value(self.y_cnt,0)
	
		
		
	def CNT_myrhs(self,t,y):
		self.d*=0
		self.Del[0::6]=y[6::6]-y[0:-6:6]
		self.Del[1::6]=y[7::6]-y[1:-6:6]
		self.Del[2::6]=y[8::6]-y[2:-6:6]
		self.d=np.sqrt(self.Del[0::6]**2+self.Del[1::6]**2+self.Del[2::6]**2)
		
		self.f_cnt[0::6]=y[3::6]
		self.f_cnt[1::6]=y[4::6]
		self.f_cnt[2::6]=y[5::6]
			
		
		
		rr0=self.Del[:-6:6]*self.Del[6::6]
			
		rr1=rr0[0]
		rr2=rr0[1]
		

		d0=self.d[:-3:]
		d1=self.d[1:-2:]
		d2=self.d[2:-1:]
		d3=self.d[3::]		
		
			
		i=2
		
		#print len(self.f_cnt[(i+15):-9:6]),len(self.Del[(i+12):-9:6])		
		for i in range(3):
			
			#print i
			
			self.f_cnt[(i+15):-9:6]=-self.gam_cnt*y[(i+15):-9:6]+self.K_cnt*(self.Del[(i+12):-9:6]*(1-self.X0_cnt/d2)-
			
				self.Del[(i+6):-15:6]*(1-self.X0_cnt/d1))+self.kap_cnt*((self.Del[(i):-21:6]-
			
				self.Del[(i+6):-15:6]*rr0[:-2:]/d1/d1)/d0/d1-(self.Del[(i+18):-3:6]-self.Del[(i+12):-9:6]*rr0[2::]/d2/d2)/d3/d2+
				
				(self.Del[(i+12):-9:6]*(1+rr0[1:-1:]/d2/d2)-self.Del[(i+6):-15:6]*(1+rr0[1:-1:]/d1/d1))/d1/d2)
			

				
		return self.f_cnt
		
		
		
	# def CNT_myrhs(self,t,y):
		# for n in range(self.Npoints-1):
			# self.d[n]=0
			
			# for i in range(3):
				# temp=y[(n+1)*6+i]-y[n*6+i]
				# self.Del[n*6+i]=temp
				# temp*=temp
				# self.d[n]+=temp
				
			# self.d[n]=np.sqrt(self.d[n])
			
		# rr=self.Del[6]*self.Del[0]+self.Del[7]*self.Del[1]+self.Del[8]*self.Del[2]
		# rr1=self.Del[12]*self.Del[6]+self.Del[13]*self.Del[7]+self.Del[14]*self.Del[8]
		# rr2=self.Del[12]*self.Del[18]+self.Del[13]*self.Del[19]+self.Del[14]*self.Del[20]
		
		# for n in range(12,self.N_cnt-12,6):

			# self.f_cnt[n]=y[n+3]
			# self.f_cnt[n+1]=y[n+4]
			# self.f_cnt[n+2]=y[n+5]

			# d0=self.d[n/6-2]
			# d1=self.d[n/6-1]
			# d01=d1*d0
			# d11=d1*d1
			# d2=self.d[n/6]
			# d12=d1*d2
			# d22=d2*d2
			# d3=self.d[n/6+1]
			# d32=d3*d2
			
			# for i in range(3):
				# m=n+i
				# self.f_cnt[m+3]=-self.gam_cnt*y[m+3]+self.K_cnt*(self.Del[m]*(1-self.X0_cnt/d2)-
					# self.Del[m-6]*(1-self.X0_cnt/d1))+self.kap_cnt*((self.Del[m-12]-
					# self.Del[m-6]*rr/d11)/d01-(self.Del[m+6]-self.Del[m]*rr2/d22)/d32+
					# (self.Del[m]*(1+rr1/d22)-self.Del[m-6]*(1+rr1/d11))/d12)
				
				
		# return self.f_cnt
			
			
	def timestep(self):
	
		for i in range (15, self.N_cnt-12,6):
			self.y_cnt[i]+=self.sig_cnt*(2*np.random.rand()-1);
			self.y_cnt[i+1]+=self.sig_cnt*(2*np.random.rand()-1);
			self.y_cnt[i+2]+=self.sig_cnt*(2*np.random.rand()-1);
		
		self.r.integrate(self.r.t+self.h_cnt)
		
	def set_y(self,y_in):
		self.y_cnt=y_in
		self.r.set_initial_value(self.y_cnt,0)
	def set_F(self, F_in):

		self.F_cnt=F_in
		self.Fper_cnt=self.F_cnt/(self.Npoints-3.0)

	def set_gam(self, gam_in):

		self.gam_cnt=gam_in
		self.update_sig()


	def set_h(self, h_in):
	
		self.h_cnt=h_in
		self.update_sig()


	def set_temp(self,temp_in):

		self.temp_cnt=temp_in
		self.update_sig()
		
	
	def set_d(self, d_in):
	
		self.d_cnt=d_in
		self.update_Ks()
		self.update_sig()
		
		
	def update_sig(self):

		self.sig_cnt=np.sqrt(self.h_cnt*self.temp_cnt/self.sigma*self.kb/np.pi/self.d_cnt/self.X0_cnt*self.gam_cnt*6.0)


	def update_Ks(self):

		self.K_cnt=446/self.X0_cnt/self.X0_cnt;
		self.kap_cnt=self.K_cnt*self.d_cnt*self.d_cnt/8.0;

	def get_sig(self):

		return self.sig_cnt
	
		