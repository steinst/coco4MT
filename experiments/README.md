We first tokenize the English sentences
We than run the greedy algorithm to select the most informative sentences

### Sentence length and diversity
We first tokenize the English sentences

bash tokenize.sh ../train/train.en_XX.notnull.uniq
python3 greedy_ngrams.py ../train/train.en_XX.notnull.uniq.spm 1
python3 greedy_ngrams.py ../train/train.en_XX.notnull.uniq.spm 2
python3 greedy_ngrams.py ../train/train.en_XX.notnull.uniq.spm 3

### Semantic Similarity
paste ../train/train.en_XX.notnull.uniq ../train/train.de_DE.notnull.uniq > ../train/train.en_XX_de_DE.notnull.uniq
paste ../train/train.en_XX.notnull.uniq ../train/train.id_ID.notnull.uniq > ../train/train.en_XX_id_ID.notnull.uniq
paste ../train/train.en_XX.notnull.uniq ../train/train.ko_KR.notnull.uniq > ../train/train.en_XX_ko_KR.notnull.uniq
python3 labse_scoring.py ../train/train.en_XX_de_DE.notnull.uniq ../train/train.en_XX_de_DE.notnull.uniq.labse
python3 labse_scoring.py ../train/train.en_XX_id_ID.notnull.uniq ../train/train.en_XX_id_ID.notnull.uniq.labse
python3 labse_scoring.py ../train/train.en_XX_ko_KR.notnull.uniq ../train/train.en_XX_ko_KR.notnull.uniq.labse
python3 remove_low_labse_scoring.py ../train/train.en_XX_de_DE.notnull.uniq.labse ../train/train.en_XX_de_DE.notnull.uniq.labse_worst_removed
python3 remove_low_labse_scoring.py ../train/train.en_XX_id_ID.notnull.uniq.labse ../train/train.en_XX_id_ID.notnull.uniq.labse_worst_removed
python3 remove_low_labse_scoring.py ../train/train.en_XX_ko_KR.notnull.uniq.labse ../train/train.en_XX_ko_KR.notnull.uniq.labse_worst_removed
# add script to remove sentences that are not in all three files and create a line number file

### Misalignments in the training data
# add translation scripts
# add calculate Chrf++ scripts 
# add remove by Chrf++
