# coreml-convert-test
DL_models is the other script referenced in the main one. The script I've been working with is edited_script_with_convert.py
 ---I edited the original script (original_Script.py) to only use CPU for prediction (the GPU is around 2x slower than CPU when running the model as-is) 

My command is:      python edited_script_with_convert.py -i input.txt -m pretrained_model.h5 -o output.txt


I'm running all this in a conda environment, set up as described here: https://developer.apple.com/metal/tensorflow-plugin/ ,
with:

tensorflow-macos=2.5.0
tensorflow-deps=2.5.0
tensorflow-metal=0.1.0
numpy = 1.19.5
coremltools = 6.1
and the newest pandas version. My machine is the newest macbook pro, M1 Max, 32 GPU cores, if that matters.
