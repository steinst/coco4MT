# Download data and mbart model
git clone https://github.com/ananyaganesh/coco4mt-shared-task.git
mv coco4mt-shared-task ../.
wget https://dl.fbaipublicfiles.com/fairseq/models/mbart50/mbart50.pretrained.tar.gz
tar -xvf mbart50.pretrained.tar.gz
mv mbart50.pretrained ../.

# Preprocess data
mkdir ../train
cp ../coco4mt-shared-task/hr_dataset/eng/train.txt ../train/train.en_XX
cp ../coco4mt-shared-task/hr_dataset/deu/train.txt ../train/train.de_DE
cp ../coco4mt-shared-task/hr_dataset/ind/train.txt ../train/train.id_ID
cp ../coco4mt-shared-task/hr_dataset/kor/train.txt ../train/train.ko_KR
mkdir ../test
cp ../coco4mt-shared-task/hr_dataset/eng/test.txt ../test/test.en_XX
cp ../coco4mt-shared-task/hr_dataset/deu/test.txt ../test/test.de_DE
cp ../coco4mt-shared-task/hr_dataset/ind/test.txt ../test/test.id_ID
cp ../coco4mt-shared-task/hr_dataset/kor/test.txt ../test/test.ko_KR
mkdir ../validation
cp ../coco4mt-shared-task/hr_dataset/eng/dev.txt ../validation/valid.en_XX
cp ../coco4mt-shared-task/hr_dataset/deu/dev.txt ../validation/valid.de_DE
cp ../coco4mt-shared-task/hr_dataset/ind/dev.txt ../validation/valid.id_ID
cp ../coco4mt-shared-task/hr_dataset/kor/dev.txt ../validation/valid.ko_KR
python3 select_nonempty_lines.py ../train/ train en_XX
python3 select_nonempty_lines.py ../test/ test en_XX,de_DE,id_ID,ko_KR
python3 select_nonempty_lines.py ../validation/ valid en_XX,de_DE,id_ID,ko_KR
sort ../train/train.en_XX.notnull | uniq > ../train/train.en_XX.notnull.uniq
# add script that generates the line numbers for the unique lines file
