from transformers import pipeline
import os, sys
ROOT = os.path.realpath(os.path.realpath(__file__))
sys.path.append(ROOT)

from eutils import timing

SAMPLES = 1000
# Regular transformers pipeline using BERT
@timing
def bert_base_uncased(SAMPLES=SAMPLES):
    print("loading unmasker")
    unmasker = pipeline('fill-mask', model='distilbert-base-uncased')

    def trials(SAMPLES=SAMPLES):
        i = 0
        while i<SAMPLES:
            unmasker("Hello I'm a [MASK] model.") #[0]['sequence']
            i+=1
        return
    
    trials()

if __name__ == "__main__":
    #bert_base_uncased()
    print(ROOT)
    print(sys.path)