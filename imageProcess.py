import time
mt1 = time.time()
import ads, margins, columnCrop, entryChop, clean

#This is the driver script for all the image processing.

if __name__ == '__main__':
	print('Removing ads...')
	t1 = time.time()
	ads.rmAds('test')
	t2 = time.time()
	print('Done in: ' + str(round(t2-t1, 2)) + ' s')
	print('Cropping margins...')
	t1 = time.time()
	margins.marginCrop('no_ads')
	t2 = time.time()
	print('Done in: ' + str(round(t2-t1, 2)) + ' s')
	#clean.straightenImage('no_ads')
	#margins.marginCrop('deskew')
	#edgeCut.cutEdges('deskew')
	print('Cropping columns...')
	t1 = time.time()
	columnCrop.doCrop('margins_fixed')
	t2 = time.time()
	print('Done in: ' + str(round(t2-t1, 2)) + ' s')
	print('Chopping entries...')
	t1 = time.time()
	entryChop.entryChop('cropped')
	t2 = time.time()
	print('Done in: ' + str(round(t2-t1, 2)) + ' s')

mt2 = time.time()
print('Full runtime: ' + str(round(mt2-mt1, 2)) + ' s')