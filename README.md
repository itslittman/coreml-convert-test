# coreml-convert-test

I'm running all this in a conda environment, set up as described here: https://developer.apple.com/metal/tensorflow-plugin/ ,
with:

tensorflow-macos=2.5.0
tensorflow-deps=2.5.0
tensorflow-metal=0.1.0
numpy = 1.19.5
coremltools = 6.1
and the newest pandas version. My machine is the newest macbook pro, M1 Max, 32 GPU cores, if that matters.


Just download the repo as a folder and run the scripts from the command line in the folder. I provided sample input for model1, ran the model, sorted the output (as required by the module), used that as input for model2; ran model2, and provided sample output. So I need to get the same outputs but with a coreML converted version of the model.
