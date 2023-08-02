import sys
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

file_in = sys.argv[1]
target_language = sys.argv[2]

device = "cuda:0" if torch.cuda.is_available() else "cpu"

model = MBartForConditionalGeneration.from_pretrained('../mbart50.pretrained/model.pt')
model = model.to(device)
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

with open(file_in) as fi, open(file_in + '.trans.' + target_language, 'w') as fo:
 ctr = 0
 for line in fi:
  ctr += 1
  tokenizer.src_lang = "en_XX"
  encoded_en = tokenizer(line.strip(), return_tensors="pt").to(device)
  generated_tokens = model.generate(
   **encoded_en,
   forced_bos_token_id=tokenizer.lang_code_to_id[target_language]
  )
  out = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
  print(str(ctr), end="\r")
  fo.write(out[0] + '\n')
