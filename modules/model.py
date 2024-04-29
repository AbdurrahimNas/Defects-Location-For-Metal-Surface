
import torchvision


def create_model():

  weights = torchvision.models.detection.FasterRCNN_ResNet50_FPN_V2_Weights.COCO_V1
  model = torchvision.models.detection.fasterrcnn_resnet50_fpn_v2(
      pretrained=True,
      )
  model.roi_heads.box_predictor
  transform = weights.transforms()
  num_classes = 11
  in_features = model.roi_heads.box_predictor.cls_score.in_features
  model.roi_heads.box_predictor = torchvision.models.detection.faster_rcnn.FastRCNNPredictor(in_features, num_classes)


  return model, transform
