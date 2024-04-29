from django.shortcuts import render
from MetalSurfaceDefectDetectionapp.models import Detection
from MetalSurfaceDefectDetectionapp.forms import DetectionForm
from MetalSurfaceDefectDetectionapp.utils import defect_detection
import matplotlib.pyplot as plt 
from PIL import Image 
import matplotlib
import matplotlib.cm as cm
# Create your views here.


def predict(request):

    class_names = [
    "punching_hole", "welding_line", "crescent_gap",
    "water_spot", "oil_spot", "silk_spot",
    "inclusion", "rolled_pit", "crease", "waist folding"
    ]
    if request.method == "POST":
        form = DetectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            image = Detection.objects.last()
            pred = defect_detection(image.image.path)
            img = Image.open("."+image.image.url)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(img, cmap=cm.gray)

            for idx, i in enumerate(pred["boxes"][:5]):
                if pred["scores"].cpu().numpy()[idx] > .1:
                    box = i.cpu().numpy()
                    rect = matplotlib.patches.Rectangle(
                        (box[0],  box[1]),
                        box[2] - box[0],
                        box[3] - box[1],
                        linewidth=1, edgecolor="r", facecolor="none")
                    ax.text(box[0], box[3], class_names[pred["labels"].cpu().numpy()[idx]], verticalalignment="top", color="red", fontsize=9, weight="bold")
                    ax.add_patch(rect)
            plt.tick_params(left = False, right = False , labelleft = False , 
                labelbottom = False, bottom = False) 
            
            plt.savefig("."+image.image.url,bbox_inches='tight',pad_inches=0.0, dpi=200)
            return render(request, "MetalSurfaceDefectDetectionapp/predict.html", {"form": form, "image":image, "pred":pred,})

    form = DetectionForm()
    return render(request, "MetalSurfaceDefectDetectionapp/predict.html", {"form": form}) 


def list_classes(request):
    
    return render(request, "MetalSurfaceDefectDetectionapp/classes.html", {})