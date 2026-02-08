import scanpy as sc

adata = sc.read_h5ad(r"C:\Users\jtspy\OneDrive\Desktop\PersonalProject\NSCLC_Project\NSCLC-scRNA-Analysis\data\raw\figshare\raw_counts.h5ad")

# Basic info
print(adata)

print(adata.X[:5, :5].toarray())

print(adata.obs.head())