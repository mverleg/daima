
from matplotlib.pyplot import show
from os.path import expanduser
from os.path import join
from write_speed.plot import plot_times
from write_speed.write import write_data_timing


if __name__ == '__main__':
	mem_times = write_data_timing(pth='/dev/shm/wrt_spd_tst', size=3*1024**3)
	hd_times = write_data_timing(pth=join(expanduser('~'), 'wrt_spd_tst'), size=6*1024**3)
	nfs_times = write_data_timing(pth=join(expanduser('~'), 'alice/wrt_spd_tst'), size=1024**3//10)
	tmp_times = write_data_timing(pth='/tmp/wrt_spd_tst', size=3*1024**3)
	plot_times(
		times=(mem_times, hd_times, nfs_times, tmp_times),
		labels=('memory', 'hard disc', 'network', '/tmp'),
	)
	fig, ax = plot_times(
		times=(mem_times[1:], hd_times[1:], nfs_times[1:], tmp_times[1:]),
		labels=('memory', 'hard disc', 'network', '/tmp'),
	)
	ax.set_xscale('log')
	ax.set_yscale('log')
	fig, ax = plot_times(
		times=(mem_times[1:], hd_times[1:], nfs_times[1:], tmp_times[1:]),
		labels=('memory', 'hard disc', 'network', '/tmp'),
	)
	ax.set_yscale('log')


if __name__ == '__main__':
	show()


