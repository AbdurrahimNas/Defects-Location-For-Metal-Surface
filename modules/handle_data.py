
from zipfile import ZipFile
import pandas as pd
from google.colab import drive
import xml.etree.ElementTree as ET
import os
from pathlib import Path

def create_df():
  drive.mount("/content/drive/")

  with ZipFile("./drive/MyDrive/defects location for metal surface.zip", "r") as zip:
    zip.extractall()

  pth = Path("./defects location for metal surface/label/label")
  lst = []
  for xml_file in os.listdir("./defects location for metal surface/label/label"):
    dummy_list = []
    if len(ET.parse(pth/xml_file).findall("object")) == 1:
      dummy_list.append(ET.parse(pth/xml_file).findtext("filename"))
      dummy_list.append(ET.parse(pth/xml_file).findtext("folder"))
      dummy_list.append(ET.parse(pth/xml_file).findtext("object/bndbox/xmin"))
      dummy_list.append(ET.parse(pth/xml_file).findtext("object/bndbox/ymin"))
      dummy_list.append(ET.parse(pth/xml_file).findtext("object/bndbox/xmax"))
      dummy_list.append(ET.parse(pth/xml_file).findtext("object/bndbox/ymax"))
      lst.append(dummy_list)
    else:
      for i in range(len(ET.parse(pth/xml_file).findall("object"))):
        dummy_list = []
        dummy_list.append(ET.parse(pth/xml_file).findtext("filename"))
        dummy_list.append(ET.parse(pth/xml_file).findtext("folder"))
        dummy_list.append(ET.parse(pth/xml_file).findall("object")[i].findtext("bndbox/xmin"))
        dummy_list.append(ET.parse(pth/xml_file).findall("object")[i].findtext("bndbox/ymin"))
        dummy_list.append(ET.parse(pth/xml_file).findall("object")[i].findtext("bndbox/xmax"))
        dummy_list.append(ET.parse(pth/xml_file).findall("object")[i].findtext("bndbox/ymax"))
        lst.append(dummy_list)

  data = pd.DataFrame(lst, columns=["filename", "class_idx", "xmin", "ymin", "xmax", "ymax"])

  data['class_idx'][data[(data["class_idx"] == "all") & (["img_07_4406645900" in i for i in data["filename"]])].index] = "6"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_07_4406743300_00001" in i for i in data["filename"]])].index] = "2"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_07_4406743300" in i for i in data["filename"]])].index] = "6"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425609500" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_436067700" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_06_425613600" in i for i in data["filename"]])].index] = "1"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425507400" in i for i in data["filename"]])].index] = "5"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425614400" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425614600_00001" in i for i in data["filename"]])].index] = "2"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425637900" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425616300" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425637800" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_08_3403334300" in i for i in data["filename"]])].index] = "2"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425640000" in i for i in data["filename"]])].index] = "4"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_02_425501900" in i for i in data["filename"]])].index] = "1"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_06_425637900" in i for i in data["filename"]])].index] = "1"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_429539000" in i for i in data["filename"]])].index] = "9"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425000300" in i for i in data["filename"]])].index] = "4"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_07_4406772100" in i for i in data["filename"]])].index] = "2"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425616200" in i for i in data["filename"]])].index] = "3"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_4402116900" in i for i in data["filename"]])].index] = "9"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_06_425638500_00714" in i for i in data["filename"]])].index] = "1"
  data['class_idx'][data[(data["class_idx"] == "all") & (["img_01_425639800_00874" in i for i in data["filename"]])].index] = "3"

  data[["class_idx", "xmin", "ymin", "xmax", "ymax"]] =  data[["class_idx", "xmin", "ymin", "xmax", "ymax"]].astype(dtype=int)
  data["class_idx"] = [i-1 for i in data["class_idx"]]

  return data
