import matplotlib.pyplot as plt
from argopy import DataFetcher as ArgoDataFetcher


argo_loader = ArgoDataFetcher()
argo_loader = ArgoDataFetcher(backend='erddap')
argo_loader = ArgoDataFetcher(cachedir='tmp')

ds = argo_loader.region([-85,-45,10.,20.,0,100.,'2012-01','2014-12']).to_xarray()


fig, ax = plt.subplots(figsize=(15,8))
ax.plot(ds.longitude,ds.latitude)