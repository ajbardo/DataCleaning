# DataCleaning

# 1 Introduction  

## 1.1 Objectives  
This projects looks for solving and issue with the values from a dc sensor that presents an abnormal behaviour with undefined operating equation and noise frequency unknown.  

# 2 Approaches  
## 2.1 Line and slope(0.1)(First stable version):  
1-In a block of points calculate the slope between adjacent points.  
2-Get the mean slope of the line.  
3-Remove the values that present a slope superior to the mean plus error.  
3.1- Considering that if between a registered operation of the sensor, the previous and subsequent values follows the same pattern then the operation registered can be consider a reading error of the sensor.  
4-The values removed will be replaced by the previous value accepted  

## 2.2 Fourier(0.2)(Work in progress):  
1-Obtain all the fouriers alternatives that matches the size of the Sample Rate and Duration with the xf.  
2-Use the prefixed cleaning frequency 0.5 as base value for the value cleaning in the temporal area.  
3-Get the mean for each point of every fourier calculated.  

# 3 Results
## 3.1 Line and slope(0.1):  
- Maintains the line shape and avoids the data loss removing the main sources of heavy noise or sensor errors.  
- As can be seen in the graphs maintain the operations register by the sensor ( maintained value, increase and decrease) but removes the ones marked as errors.  
- Present a minor data loss at the begin of a correct point block, in some scenarios can remove the first value of the point block .  

## 3.2 Fourier(0.2):  
- Loss of at least 80% of the raw-information of the point blocks.  
- Remove successfully all the noise in the sensor measurements.  
- Maintain the line shape.  
