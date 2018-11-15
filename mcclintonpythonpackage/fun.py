import pandas as pd
import dendropy

"""This function allows the multiple sequence alignments to be shown together with the trees. The newick format."""
def fun(filepath):
    pd.options.display.max_colwidth = 1000000
    salamanders = pd.read_json(filepath)
    salamanders

    pd.options.display.max_colwidth = 1000000
    newick_tree = salamanders.newick.to_string(index=False)
    newick_tree