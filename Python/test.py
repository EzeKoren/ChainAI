#%%
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import sys
sys.path.append('F:\ChainAI\Python')
from testfile import main as tf
import json
received = json.loads(tf())
obj = json.loads(received["obj"])
display (obj)
#%%
