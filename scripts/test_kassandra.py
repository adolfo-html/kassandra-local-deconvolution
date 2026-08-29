# Imports
import pandas as pd
import matplotlib.pyplot as plt
from core.plotting import print_cell_matras, cells_p, print_all_cells_in_one
from core.utils import *

from core.model import DeconvolutionModel


# Import the trained model
import pickle

with open('models/tumor_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Testing if the model is good
print(type(model))
print(model.cell_types)          # or whatever the attribute is
print([m for m in dir(model) if 'predict' in m.lower()])




# Performance testing
dataset = 'GSE107572'
cytof = pd.read_csv('data/GSE107572_cytof.tsv.tar.gz', sep='\t', index_col=0)
expr = pd.read_csv('data/GSE107572_expr.tsv.tar.gz', sep='\t', index_col=0)

preds = model.predict(expr) * 100
preds.loc['Lymphocytes'] = preds.loc[['B_cells', 'T_cells', 'NK_cells']].sum()

plt.rcParams['figure.dpi'] = 80
plt.rcParams["axes.edgecolor"] = "0.0"
plt.rcParams["axes.linewidth"]  = 1.75

x = print_all_cells_in_one(preds, 
                           cytof,
                           pallete=cells_p,
                           title=dataset, min_xlim=0, min_ylim=0)

x = print_cell_matras(preds, cytof,
                  pallete=cells_p, colors_by='index', title='',
                  true_name='', predicted_name='',
                  sub_title_font=18, fontsize_title=30,
                  subplot_ncols=4, ticks_size=17, wspace=0.3, hspace=0.5, min_xlim=0, min_ylim=0)


plt.show()