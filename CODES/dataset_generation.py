import os
import shutil
import cv2

IMAGES_DATASET = "../DATA/images"
VIDEOS_DATASET = "../DATA/videos"
OUTPUT_DATASET = "../DATA/IMAGE_DATASET"

CATEGORIES = ['regular', 'covid', 'pneumonia']
PROBE = ['convex', 'linear']

if __name__ == "__main__":
	def category(sec):
		if sec == "Cov":
			return "covid"
		elif sec == "Pne":
			return "pneumonia"
		elif sec == "Reg":
			return "regular"
		else:
			return "wrong label"

	# Creating directories
	os.makedirs(OUTPUT_DATASET)
	for cat in CATEGORIES:
		os.makedirs(os.path.join(OUTPUT_DATASET, cat))

	# copying images from images folder to IMAGE_DATASET
	for pro in PROBE:
		for im in os.listdir(os.path.join(IMAGES_DATASET, pro)):
			label = category(im[:3])
			if label in CATEGORIES:
				shutil.copy(os.path.join(IMAGES_DATASET, pro, im), os.path.join(OUTPUT_DATASET, label))

	# Processing the videos
	for pro in PROBE:
		for vi in os.listdir(os.path.join(VIDEOS_DATASET, pro)):
			label = category(vi[:3])
			if label not in CATEGORIES:
				continue

			path = os.path.join(VIDEOS_DATASET, pro, vi)
			out_path = os.path.join(OUTPUT_DATASET, label)
			
			vid = cv2.VideoCapture(path)
			framerate = vid.get(5)

			every_x_image = int(framerate / 5)

			n = 0
			while vid.isOpened() and n < 30:	# take a maximum of 30 frames from each video.
				frame_number = vid.get(1)  #current frame number
				ret, frame = vid.read()
				if (ret != True):
					break
				if (frame_number % every_x_image == 0):	# taking every 5th frame.
					filename = os.path.join( out_path, vi + "_frame%d.jpg" % frame_number )
					cv2.imwrite(filename, frame)
					n += 1
			vid.release()

