from sys import stdout

from time import time
from os import urandom, remove


def write_data_timing(*, fh=None, pth=None, size=1024**3, blocksize=4*1024, pth_remove=True, timeout=60):
	if not fh:
		assert pth, 'provide fh or pth'
		fh = open(pth, 'wb+')
	assert fh.writable(), 'fh not writable'
	stdout.write('writing {0:}MB to {1:}... '.format(size // 1024**2, pth or fh))
	data = urandom(blocksize)
	times = [0.]
	t_start = time()
	for k in range(0, size, blocksize):
		fh.write(data)
		times.append(time() - t_start)
		if time() - t_start > timeout:
			print('timed out after {0:.3f}, wrote {1:}MB'.format(time() - t_start, (k * blocksize) // 1024**2))
			break
	else:
		fh.flush()
		print('took {0:.3f}s'.format(time() - t_start))
	if pth:
		fh.close()
		if pth_remove:
			remove(pth)
	return times


