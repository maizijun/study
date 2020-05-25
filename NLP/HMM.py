'''
Target: given observation y, latent variable range r1 to rk, we want to estimate ri corresponding to yi，
most usually in taggging problem

model hypothesis: we have a series situation r1,r2,...rk, and each two have a transition probability,
so we have a trasition matrix R and an initial probability distribtuion pie，for each situation, we can 
get its observation, from situation, so we can get a situ-obser transition matrix B,
and probabity can be represented as P(pie,R,B)

parameter estimation: EM-iter

apply: given a series of y, we want to estimate situation ri, so as to maximize R, and dynamic programming would help a lot 

'''