import scanpy as sc
import pandas as pd

adata = sc.read_h5ad(r"C:\Users\jtspy\OneDrive\Desktop\PersonalProject\NSCLC_Project\NSCLC-scRNA-Analysis\data\raw\figshare\raw_counts.h5ad")

metadata = pd.read_csv(
    "data/raw/figshare/Metadata.csv",
    index_col=0
)

# Basic info

adata.obs = metadata


adata.write(
    r"C:\Users\jtspy\OneDrive\Desktop\PersonalProject\NSCLC_Project\NSCLC-scRNA-Analysis\data\raw\figshare\raw_counts_with_metadata.h5ad"
)

'''
sc.pl.violin(
    adata,
    keys=["nCount_RNA", "nFeature_RNA", "Percent_mt"],
    jitter=0.4,
    multi_panel=True
)
'''

min_counts = 500
max_counts = 50000

min_genes = 300
max_mt = 15

# Make a copy so we can always revert
adata_qc = adata.copy()

# Apply filters for cells only (we will filter genes later)
adata_qc = adata_qc[
    (adata_qc.obs["nCount_RNA"] >= 500) &
    (adata_qc.obs["nCount_RNA"] <= 50000) &
    (adata_qc.obs["nFeature_RNA"] >= 300) &
    (adata_qc.obs["Percent_mt"] <= 15),
    :
]

print(f"Cells before QC: {adata.n_obs}")
print(f"Cells after QC:  {adata_qc.n_obs}")

sc.pl.violin(
    adata_qc,
    keys=["nCount_RNA", "nFeature_RNA", "Percent_mt"],
    jitter=0.4,
    multi_panel=True
)

