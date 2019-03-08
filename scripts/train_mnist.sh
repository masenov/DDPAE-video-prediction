#!/bin/bash
python3.6m train.py \
  --gpus 0 \
  --n_workers 4 \
  --ckpt_dir $HOME/DL/PhysVideo/ckpt \
  --dset_dir $HOME/DL/PhysVideo/models/ddpae/datasets/ \
  --dset_name moving_mnist \
  --n_frames_input 25 \
  --n_frames_output 10 \
  --evaluate_every 20 \
  --lr_init 1e-3 \
  --lr_decay 1 \
  --n_iters 200000 \
  --batch_size 64 \
  --n_components 2 \
  --stn_scale_prior 2 \
  --ckpt_name 200k
