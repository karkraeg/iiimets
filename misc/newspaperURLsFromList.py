# %%
import pickle

inf = 'bsb_newspapers_01.txt'
m = ['https://api.digitale-sammlungen.de/iiif/presentation/v2/' + line.rstrip('\n') + '/manifest' for line in open(inf)]

with open('bsb_newspapers_01.pkl', 'wb') as f:
    pickle.dump(m, f)
# %%
