import sys
import torch
from transformers import BertModel, BertTokenizerFast
import torch.nn.functional as F

infile = sys.argv[1]
outfile = sys.argv[2]

files = open(infile, 'r')
fileLines = files.readlines()

proc_device = 'cuda'

tokenizer = BertTokenizerFast.from_pretrained("setu4993/LaBSE")
model = BertModel.from_pretrained("setu4993/LaBSE")
model = model.eval()
model.to(proc_device)

def similarity(embeddings_1, embeddings_2):
    normalized_embeddings_1 = F.normalize(embeddings_1, p=2)
    normalized_embeddings_2 = F.normalize(embeddings_2, p=2)
    return torch.matmul(normalized_embeddings_1, normalized_embeddings_2.transpose(0, 1))

source_lines = []
target_lines = []

ctr = 0
with open(outfile, 'w') as wo:
    for sentencepair in fileLines:
        ctr += 1
        curr = sentencepair.strip().split('\t')
        if len(curr) == 2:
            source_sent = curr[0]
            target_sent = curr[1]

            if (len(source_sent) > 1) and (len(target_sent) > 1):
                try:
                    target_inputs = tokenizer([target_sent], return_tensors="pt", padding=True)
                    source_inputs = tokenizer([source_sent], return_tensors="pt", padding=True)
                    target_inputs = target_inputs.to(proc_device)
                    source_inputs = source_inputs.to(proc_device)

                    with torch.no_grad():
                        target_outputs = model(**target_inputs)
                        source_outputs = model(**source_inputs)

                        target_embeddings = target_outputs.pooler_output
                        source_embeddings = source_outputs.pooler_output

                        x = similarity(target_embeddings, source_embeddings)
                        wo.write(source_sent.strip() + '\t' + target_sent.strip() + '\t' + str(x).split(']]')[0].split('[[')[1] + '\n')
                except:
                    wo.write(source_sent.strip() + '\t' + target_sent.strip() + '\t0.0\n')
