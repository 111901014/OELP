import os
import shutil
import cv2

IMAGES_DATASET = "../DATA/images"
VIDEOS_DATASET = "../DATA/videos"
OUTPUT_DATASET = "../DATA/IMAGE_DATASET"

CATEGORIES = ['regular', 'covid', 'pneumonia']
PROBE = ['linear', 'convex']

split = 98

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
		os.makedirs(os.path.join(OUTPUT_DATASET, 'train_'+cat))
		os.makedirs(os.path.join(OUTPUT_DATASET, 'test_'+cat))

	# copying images from images folder to IMAGE_DATASET
	for pro in PROBE:
		images = os.listdir(os.path.join(IMAGES_DATASET, pro))
		n = len(images) 
		for im in range(n):
			if im < (n*split/100) :
				label = category(images[im][:3])
				if label in CATEGORIES:
					shutil.copy(os.path.join(IMAGES_DATASET, pro, images[im]), os.path.join(OUTPUT_DATASET, 'test_'+label))
			else :
				label = category(images[im][:3])
				if label in CATEGORIES:
					shutil.copy(os.path.join(IMAGES_DATASET, pro, images[im]), os.path.join(OUTPUT_DATASET, 'train_'+label))

	# Processing the videos
	for pro in PROBE:
		videos = os.listdir(os.path.join(VIDEOS_DATASET, pro))
		n = len(videos) 
		for vi in range(n):
			if vi < (n*split/100) :
				label = category(videos[vi][:3])
				if label not in CATEGORIES:
					continue

				path = os.path.join(VIDEOS_DATASET, pro, videos[vi])
				out_path = os.path.join(OUTPUT_DATASET, 'test_'+label)
				
				vid = cv2.VideoCapture(path)
				framerate = vid.get(5)

				every_x_image = int(framerate / 5)

				n = 0
				while vid.isOpened() and n < 20:	# take a maximum of 30 frames from each video.
					frame_number = vid.get(1)  #current frame number
					ret, frame = vid.read()
					if (ret != True):
						break
					if (frame_number % every_x_image == 0):	# taking every 5th frame.
						filename = os.path.join( out_path, videos[vi] + "_frame%d.jpg" % frame_number )
						cv2.imwrite(filename, frame)
						n += 1
				vid.release()
			else :
				label = category(videos[vi][:3])
				if label not in CATEGORIES:
					continue

				path = os.path.join(VIDEOS_DATASET, pro, videos[vi])
				out_path = os.path.join(OUTPUT_DATASET, 'train_'+label)
				
				vid = cv2.VideoCapture(path)
				framerate = vid.get(5)

				every_x_image = int(framerate / 5)

				n = 0
				while vid.isOpened() and n < 20:	# take a maximum of 30 frames from each video.
					frame_number = vid.get(1)  #current frame number
					ret, frame = vid.read()
					if (ret != True):
						break
					if (frame_number % every_x_image == 0):	# taking every 5th frame.
						filename = os.path.join( out_path, videos[vi] + "_frame%d.jpg" % frame_number )
						cv2.imwrite(filename, frame)
						n += 1
				vid.release()

