import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def kmeans_clusters(file_name, sheet_name, qtd_clusters=3):
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    
    features = ['idh', 'atletas', 'população']
    data = df[features]
    
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    kmeans = KMeans(n_clusters=qtd_clusters, random_state=42)
    kmeans.fit(data_scaled)
    
    df['Cluster'] = kmeans.labels_
    
    output_file_name = 'saida_kmeans.xlsx'
    df.to_excel(output_file_name, index=False)
    return df, kmeans

file_name = 'dados.xlsx'
sheet_name = 'Dados'
num_clusters = 3 


df_result, kmeans_model = kmeans_clusters(file_name, sheet_name, num_clusters)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x_column = 'idh'
y_column = 'atletas'
z_column = 'população'

x = df_result[x_column]
y = df_result[y_column]
z = df_result[z_column]
clusters = df_result['Cluster']

scatter = ax.scatter(x, y, z, c=clusters, cmap='viridis')
ax.set_title('K-means Clustering 3D')
ax.set_xlabel(x_column)
ax.set_ylabel(y_column)
ax.set_zlabel(z_column)

legend1 = ax.legend(*scatter.legend_elements(), title="Clusters")
ax.add_artist(legend1)
plt.show()
