
from matplotlib.pyplot import subplots


def plot_times(times, labels=()):
	fig, ax = subplots(figsize=(7, 6))
	# fig.tight_layout()
	if not labels:
		labels = tuple('times #{0:d}'.format(k + 1) for k in range(len(times)))
	for tvals, label in zip(times, labels):
		ax.plot(tvals, label=label)
	ax.set_xlabel('size (blocks)')
	ax.set_ylabel('time (s)')
	ax.legend(loc='upper left')
	return fig, ax


