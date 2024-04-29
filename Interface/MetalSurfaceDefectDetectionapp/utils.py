import torch
import torchvision 
from PIL import Image
import matplotlib.pyplot as plt

def create_model():
  weights = torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights.COCO_V1
  model = torchvision.models.detection.fasterrcnn_resnet50_fpn_v2(
      pretrained=True,
      )
  model.roi_heads.box_predictor
  num_classes = 11
  transforms = weights.transforms()
  in_features = model.roi_heads.box_predictor.cls_score.in_features
  model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)
  return model, transforms

def defect_detection(img_path, model_path="./DL4MetalSurface.pth"):
    model, transforms = create_model()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.load_state_dict(torch.load(map_location=device, f=model_path))
    model.to(device)
  
    img = Image.open(img_path)
    converted_img = transforms(img)
    model.eval()
    with torch.inference_mode():
        prediction = model(converted_img.unsqueeze(dim=1).to(device))[0]

    return prediction