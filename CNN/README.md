#    Convolutional Neural Networks
Helps in handling large amount of data, bring down data into small matrices called feature matrics. It helps in scaling down an image. In CNN we wants to use these filter for
extraction and don't want to decide weights in of the filter, just want to an algorithm to randomly start with random weights and adjust automatic. The matrics(filter) is called Kernels. 3x3 and 5x5 normal shape of filter. 1x1 is advanced. Convolution will reduce size of image matrix and keep value intact. We will keep on doing convulation until we get a minimal state.

##  Importing 
Import `Sequential`, which is basically a constructor that helps us bind all the layers. 

- **Conv2D  -**    
- **MaxPool2D -**
- **Flatten -**   Conerting image matric into an array
- **Dense -** Fully connected neuro-network.
```ruby
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Flatten, Dense
from tensorflow.keras.utils import to_categorical
```















### Kernels is a matrix and in CNN its used as weight/filter.

OUTPUT IMAGE -> ``(n-f+1) * (n-f-1)``      
**n --> size of image**,                           
**f --> size of filter**

FILTERS can extract information horizontally as well as vertically.

sobel derivative - uses sobel filter(fixed set of filter)
