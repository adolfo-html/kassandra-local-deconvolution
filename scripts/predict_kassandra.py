# This is the python script for PREDICTING with the *trained* Kassandra model.
# So if you don't have a saved pkl file in the models folder, run the train_kassandra.py script first to generate it.
# Then this will work

import pickle
from pathlib import Path

model_path = Path('models/tumor_model.pkl')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

import pandas as pd

# Import the plotting functions
import matplotlib.pyplot as plt
from core.plotting import print_cell_matras, cells_p, print_all_cells_in_one



from core.model import DeconvolutionModel

# This imports tr_to_genes and renorm_expressions functions
from core.utils import *

# Model prediction with datasets

# First, we have to convert transcripts to genes
expr = pd.read_csv('input/abundance.tsv', sep='\t', index_col=0)
expr = tr_to_genes(expr, tr_ids_path='data/tumor_model_transcripts.txt')
expr = renorm_expressions(expr, 'data/genes_in_expression.txt')

# Then run the model on this trained model
preds = model.predict(expr) * 100
preds.loc['Lymphocytes'] = preds.loc[['B_cells', 'T_cells', 'NK_cells']].sum()
preds.loc['Stromal'] = preds.loc[['Endothelium', 'Fibroblasts']].sum()
preds_df = pd.DataFrame(preds)

# Save results
preds_df.to_csv('output/deconvolution_percentages.tsv', sep = '\t', header = True, index = True)



# Plotting results

dataset = "SRX31879952"
"""
This part is here for when you actually have the expr and cytof data to compare predictions to.
Kassandra's other official testing examples on their notebook have these - *actual* cell %s.
In my project, I only found the bulk RNA-seq data, so I was only able to run the model and get predictions. Actual cell %s for this example aren't available at this time

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
"""