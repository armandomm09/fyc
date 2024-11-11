import os
import subprocess
import cv2
from ultralytics import YOLO
from constants import *
from training import continue_training, train_from_scratch
from process import analyze_video_folder, analyze_realtime, analyze_native_yolo, analyze_video
from utils import rename_and_order_files
import os
from process import FallDetector
from database import PSQLManager

manager = PSQLManager(DATABASE_CONFIG_PATH)
detector = FallDetector(TRAINED_MODEL_BEST_PATH, YOLO_V_11_PATH, manager)
detector.analyze_video("media/in_videos/video7.mp4", "media/out_videos/video7.mp4", save=True, open_in_finder=True)

results = manager.get_all_cv_fall_readings()

print(results[0])