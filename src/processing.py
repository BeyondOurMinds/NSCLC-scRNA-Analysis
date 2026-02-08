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


sc.pl.violin(
    adata,
    keys=["nCount_RNA", "nFeature_RNA", "Percent_mt"],
    jitter=0.4,
    multi_panel=True
)
