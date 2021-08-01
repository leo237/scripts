import logging
import matplotlib.pyplot as plt
import argparse
from typing import List
from enum import Enum
from enum import Enum

class Constants:
	class PlotType(Enum):
		HAILSTONE = 'HAILSTONE'
		PEAK = 'PEAK'
		STOPPING_TIMES = 'STOPPING_TIMES'

class Stats:
	def __init__(self, num : int, total_stopping_time : int, step_values: List[int], peak: int):
		self.num = num
		self.total_stopping_time = total_stopping_time
		self.step_values = step_values
		self.peak = peak

def get_arguments():
	parser = argparse.ArgumentParser(description='Generate 3n+1 graphs')
	parser.add_argument('--num', '-n', type=int, help='Generate 3n+1 function till num ', default=30)
	parser.add_argument('--plot-type', '-p', type=Constants.PlotType, help='What kind of plot type do you want', default=Constants.PlotType.HAILSTONE)
	args = parser.parse_args()
	return args


def func3nPlus1(x):
	is_even = x%2 == 0

	if is_even:
		return int(x/2)
	else:
		return int(3*x + 1)

def recursive_3nPlus1(num):
	res = num
	steps = 0
	peak = 0

	step_values = [res]

	logging.debug("Running function for : {}".format(num))
	while (res > 1):
		# Basic
		res = func3nPlus1(res)
		steps+=1
		
		# Find peak
		if res > peak:
			peak = res

		# For graph
		step_values.append(res)
		
		logging.debug("f(res) : {} | Steps : {}".format(res, steps))
	logging.info("Num : {} | Total Stopping Time : {} | FinalValue : {} | Peak : {}".format(num, steps, res, peak))

	stat = Stats(num=num, total_stopping_time=steps, step_values=step_values, peak=peak)

	return stat

def plot_hailstone(stats : List[Stats]):
	for stat in stats:
		num = stat.num
		y = stat.step_values
		x = [i for i in range(len(y))]
		plt.plot(x,y, label=num)
	
	plt.xlabel("Steps")
	plt.ylabel("f(x)")

	plt.legend()
	plt.show()

def plot_peaks(stats : List[Stats]):
	x = [stat.num for stat in stats]
	y = [stat.peak for stat in stats]

	plot_x_y(x, y, 'num', 'peaks', 'Peaks')

def plot_stopping_times(stats: List[Stats]):
	x = [stat.num for stat in stats]
	y = [stat.total_stopping_time for stat in stats]

	plot_x_y(x, y, 'num', 'total_stopping_time', 'Stopping Times')
	
def plot_x_y(x : List[int], y: List[int], xlabel : str, ylabel:str, title:str = None):
	plt.plot(x, y)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.legend()
	plt.show()



if __name__ == '__main__':
	logging.basicConfig(format='[%(levelname)s] %(asctime)s : %(message)s', level=logging.INFO)
	args = get_arguments()

	plot_type = args.plot_type

	stats = []

	for i in range(args.num):
		stat = recursive_3nPlus1(i)
		stats.append(stat)

	
	# Generate graph
	if plot_type == Constants.PlotType.HAILSTONE:
		plot_hailstone(stats)

	if plot_type == Constants.PlotType.PEAK:
		plot_peaks(stats)
	
	if plot_type == Constants.PlotType.STOPPING_TIMES:
		plot_stopping_times(stats)