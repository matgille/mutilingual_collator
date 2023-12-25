"""
Bertalign initialization
"""

__author__ = "Jason (bfsujason@163.com)"
__version__ = "1.1.0"

from bertalign.encoder import Encoder

# See other cross-lingual embedding models at
# https://www.sbert.net/docs/pretrained_models.html


models = {0: "distiluse-base-multilingual-cased-v2", 1: "LaBSE"}
as_list = ""
for key, value in models.items():
    as_list += f"{int(key)}\t{value}\n"
print(as_list)
nb = input(f'Choose a model:')
model = Encoder(models[int(nb)])

from bertalign.aligner import Bertalign
