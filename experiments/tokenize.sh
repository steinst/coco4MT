dataset=$1
SPM=/usr/bin/spm_encode
MODEL=../mbart50.pretrained/sentence.bpe.model
${SPM} --model=${MODEL} < ${dataset} > ${dataset}.spm
