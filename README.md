# DOTA vs AOE image classifier

Simple image classifier. Predicts if a given image is a screen from DOTA game or AOE game with over 99% accuracy.

Model implemented using Keras python library. Details of the model are below.

| Layer (type)                  | Output Shape         | # of Params     |
| ------------------------------|----------------------|----------------:|
| input_1 (InputLayer)          |(None, 72, 128, 3)    |                0|
| max_pooling2d_1 (MaxPooling2) |(None, 36, 64, 3)     |                0|
| flatten_1 (Flatten)           |(None, 6912)          |                0|
| dense_1 (Dense)               |(None, 1)             |             6913|
| activation_1 (Activation)     |(None, 1)             |                0|

Total params: 6,913
Trainable params: 6,913
Non-trainable params: 0
