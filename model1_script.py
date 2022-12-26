#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# required
signals_input = 'input_for_model1.p'
DL_model = 'model_1.h5'
label = 'test'
file_out = 'model_1_output.txt'


from tensorflow.keras import Input
from tensorflow.keras.models import Model
import _pickle as cPickle
from defs import build_Jasper
import numpy as np
import os
import sys
import subprocess

# load the trainned model
inputs = Input(shape=(100, 2))
output = build_Jasper(inputs,Deep=True)
model = Model(inputs=inputs, outputs=output)


model.load_weights(DL_model)


### load the stored data
total_lines = 0
counter = 0
IDs_signals = {}

with open(signals_input, 'rb') as signal_in:  
    with open(file_out, 'a') as f_out:
        while True:
            try:
                counter +=1
                if counter <= total_lines:
                    seen_signal = cPickle.load(signal_in)
                    continue
                IDs_signals.update(cPickle.load(signal_in))
                
                # to avoid loading everything predict every 10k singnals
                if counter%20000 == 0:
                    if IDs_signals:
                       
                        predictions = model.predict(np.array(list(IDs_signals.values())))
                        keys = list(IDs_signals.keys())
                        
                        for indv_predit in enumerate(predictions.reshape(len(predictions))):
                            print(keys[indv_predit[0]]+'\t'+ \
                                  str(indv_predit[1])+'\t'+ \
                                  label,
                                  file=f_out)
                   
                        IDs_signals = {}
                    else:
                        continue
            except Exception as ex:
                print(ex)
                
                if IDs_signals:
                    predictions = model.predict(np.array(list(IDs_signals.values())))
                    keys = list(IDs_signals.keys())
                    
                    for indv_predit in enumerate(predictions.reshape(len(predictions))):
                        
                        print(keys[indv_predit[0]]+'\t'+ \
                              str(indv_predit[1])+'\t'+ \
                              label, 
                              file=f_out)
               
                    IDs_signals = {}
    
                print('All signals have been processed', counter)
                break
