# Defects-Location-For-Metal-Surface

Object Detection for **Defects location for metal surface dataset** with **fasterrcnn_resnet50_fpn_v2** pretrained feature extraction model. It detects all classes with the whole dataset.


## Example Interface Displays:

![msdd](https://github.com/AbdurrahimNas/Defects-Location-For-Metal-Surface/assets/87318891/20fd2d72-9320-467d-ba2b-e3e2d92bd966)


## How To Use:

```
cd ./Defects-Location-For-Metal-Surface
```

```
code DL4MetalSurface.ipynb 
```

**[Optional]** ~~Change some hyperparameters to suit your needs or make sure your device can handle the computation~~

**[Necessary]** Run the code to create a model 

```
cd ./Defects-Location-For-Metal-Surface/Interface
```

```
py manage.py makemigrations

```

```
py manage.py migrate

```

```
py manage.py runserver

```
**After running the server go to**: [http://127.0.0.1:8000/predict/](http://127.0.0.1:8000/predict/)
