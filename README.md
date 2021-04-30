# Reinforcement Learning Car Project

# EN

## Car 
![Center](https://github.com/mkemalgokce/CarProject/blob/master/Assets/mycar.bmp/ "Car")

- Car has 5 sensors and each sensor gets distance between car and specific color code. The neural network gets this distance values(5 values) and predicts car moves.

## Sensors
<img width="158" alt="image" src="https://user-images.githubusercontent.com/46056478/116737824-5ea93e00-a9fa-11eb-8e8d-4a190a43c75e.png">

* Car has 5 sensors. Left, right, front, front right and front left.
* Each sensor has distance data. The datas are float numbers between 0 and 1.
* If data equals zero, it shows min distance between car and specific color code.
* If data equals zero, it shows max distance between car and specific color code.

##### Specific code --> obstacle color code = (100,100,100) and finish line color code = (0,255,0) in my code.

## Neural Network
- My neural network has 3 layers.

<img src="https://user-images.githubusercontent.com/46056478/116734911-84ccdf00-a9f6-11eb-8cee-2e36c76c59fd.png" width="500" height="500">

* First layer, Input Layer : 5 Neurons
* Second layer, Hidden Layer : 48 Neurons , activation = relu
* Last layer , Output Layer : 2 Neurons
* Optimizer = Adam , loss = mean square error

# TR

## Araba   
![Center](https://github.com/mkemalgokce/CarProject/blob/master/Assets/mycar.bmp/ "Araba")


- Arabanın 5 adet sensörü var ve her sensör verilen renk kodunun arabaya uzaklığını hesaplar. Bu hesaplanan değerleri (5 değer) yapay sinir ağı modeline verip elde edilen tahmin değerlerine göre araba hareket eder.

## Sensörler
<img width="158" alt="image" src="https://user-images.githubusercontent.com/46056478/116737824-5ea93e00-a9fa-11eb-8e8d-4a190a43c75e.png">

* Arabada toplam 5 adet sensör var. Sol, sağ, ön, ön sağ, ön sol olmak üzere.
* Her sensörün verisi vardır. Veriler 0 ile 1 arasında float tipindeki sayılardan oluşuyor. Eğer verilen renk değeri ile araba arasındaki uzaklık 1 ile ifade ediliyorsa, cisim arabadan max uzaklıktadır, fakat uzaklık 0 a eşitse cisimle araba iç içe pozisyondadır.
* 
## Yapay Sinir Ağı

- Kullandığım yapay sinir ağı 3 katmandan oluşuyor.

<img src="https://user-images.githubusercontent.com/46056478/116734911-84ccdf00-a9f6-11eb-8cee-2e36c76c59fd.png" width="500" height="500">

* Ilk katman Input Layer : 5 Nöron
* Ikinci katman Hidden Layer : 48 Nöron , aktivasyon fonksiyonu = relu
* Son katman Output Layer : 2 Nöron
* Optimizer = Adam , loss = Ortalama kare hatası

##### Giriş katmanı 5 tane sensör verisi alıyor.
##### Çıkış katmanı arabanın hangi yöne (sol, sağ) doğru döneceğini tahmin ediyor.

# Game Images
<img width="596" alt="image" src="https://user-images.githubusercontent.com/46056478/116738153-c2cc0200-a9fa-11eb-8caf-ceb31c22c612.png">

<img width="526" alt="image" src="https://user-images.githubusercontent.com/46056478/116737692-315c9000-a9fa-11eb-97d0-aada0b72b36e.png">

# Libraries:
* Pygame
* Keras
* Numpy
* Math

# Youtube Video 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/6KPFmQggDpo/0.jpg)](https://www.youtube.com/watch?v=6KPFmQggDpo)
