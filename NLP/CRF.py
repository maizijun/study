
'''
Target: Given a sequence X ( maybe multidimensioal? ), estimate a sequence y (serial distribution), which has largest log probability,
so it is considered to be a discrimitive model 

Model : p(y|X) = 1/z(x) * Σ exp[ Σ(k) λk * tk(yi-1,yi,x,i) + Σ(l) μl * sl(yi,x,i) ]
function tk implies the correlation info and μl implies the location info

logistic model :
p(y|x) = exp(w*x) / (1+exp(w*x))

so lr model could be considered to be a specific case of crf model ??

algorithm: λk & μk to be estimated, gradient descend 我不会 

python package: sklearn-crfsuite

'''