#!/bin/bash
python3 test.py \
  --gpus 0 \
  --n_workers 4 \
  --batch_size 16 \
  --dset_name moving_mnist \
  --ckpt_dir $HOME/DL/DDPAE-video-prediction/ckpt \
  --dset_dir $HOME/DL/DDPAE-video-prediction/datasets \
  --log_every 5 \
  --save_visuals 1 \
  --ckpt_name crop_NC2_lr1.0e-03_bt64_200k
