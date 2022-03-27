from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler




class clusters:
    def __init__(self , min_samples , eps):
        self.min_samples = min_samples
        self.eps = eps


    def applyPCA(self , df) :
        '''Applying PCA for DBSCAN'''
        df = self.scale(df)
        pca = PCA(n_components=5)
        pca_X = pca.fit_transform(df)

        return pca_X

    def scale( self , df):
        '''scaling the data'''
        scaler = StandardScaler()
        scaled_df = scaler.fit_transform(df)
        return scaled_df

    def makeclusters(self , df):
        ''' Make clusters from the data '''
        reduced_X =  self.applyPCA(df)
        dbscan = DBSCAN(min_samples= self.min_samples, eps=self.eps)
        # grid_model = GridSearchCV(dbscan , {'min_samples': self.min_samples, 'eps':self.eps} )
        # grid_model.fit(df)
        dbscan.fit(reduced_X)
        return df

