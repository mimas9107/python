import numpy as np
from sklearn.decomposition import PCA

x = np.array( [ [ 1, 1 ], [ 2, 4 ], [ 4, 2 ], [ 5, 5 ] ] )
mean_vec = np.mean( x, axis = 0 )
cov_mat = ( x - mean_vec ).T.dot( x - mean_vec ) / x.shape[0]
eig_vals, eig_vecs = np.linalg.eig( cov_mat )
pca = PCA( 2 )
pca.fit( x )
y = pca.transform( x )
print( "Mean Vector:\n", mean_vec )
print( "Covariance Matrix:\n", cov_mat )
print( "Eigenvalues\n", eig_vals )
print( "Eigenvectors\n", eig_vecs )
print( "Transform:\n", y )