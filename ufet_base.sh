#!/bin/bash

#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --time=24:00:00
#SBATCH --partition=blanca-curc-gpu
#SBATCH --gres=gpu:1
#SBATCH --output=Crowd_test_bin3-%j.out
#SBATCH --mail-type="ALL"
#SBATCH --mail-user="asum8093@colorado.edu"

module purge

module load anaconda
module load cuda/12.1.1
#cd /rc_scratch/asum8093/open_type/resources/
#wget http://nlp.stanford.edu/data/glove.840B.300d.zip
#unzip glove.840B.300d.zip -d ./

#wget http://nlp.cs.washington.edu/entity_type/data/ultrafine_acl18.tar.gz

#tar -xvzf ultrafine_acl18.tar.gz

#cd ../

cd /rc_scratch/asum8093/open_type/
conda activate py38-pt1131-cuda117
pip install tensorboard
#mkdir models

echo "== This is the scripting step! =="

#python3 main.py MODEL_1 -lstm_type single -enhanced_mention -data_setup joint -add_crowd -multitask
#python3 main.py crowd_v4 -lstm_type single -goal open -enhanced_mention -train_data crowd/train.json -dev_data crowd/dev.json
python3 main.py crowd_v4_test -lstm_type single -enhanced_mention -add_crowd -mode test -reload_model_name crowd_v4 -eval_data crowd/merged_output.json -load
#python3 main.py onto -lstm_type single -goal onto -enhanced_mention -num_epoch 5 #works

#python3 main.py MODEL_ID -lstm_type single -enhanced_mention -data_setup joint -add_crowd -multitask -mode test -reload_model_name MODEL_NAME_TIMESTAMP -eval_data crowd/test.json -load

echo "== End of Job =="