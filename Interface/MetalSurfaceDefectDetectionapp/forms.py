from django.forms import ModelForm
from MetalSurfaceDefectDetectionapp.models import Detection


class DetectionForm(ModelForm):

    class Meta:
        model=Detection
        fields=["image"]