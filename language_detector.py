import fasttext
import sys
import importlib
from importlib import reload
importlib.reload(sys)
sys.getdefaultencoding()
lid_model = fasttext.load_model('lid.176.bin')

#test
#lid_model.predict("மதியும் மடந்தை முகனு மறியா பதியிற் கலங்கிய மீன்.")