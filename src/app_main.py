# This is the main program for launching the shortest path program.

from util_functions import Utilities, Constants
from shortest_path import ShortestPathCalculator

if __name__ == '__main__':
    calc = ShortestPathCalculator()
    distance, path, time_taken = calc.run()
    if distance is not Constants.MAX_INFINITY.value:
        Utilities.log_output(calc.source, calc.destination, path, distance, time_taken)
    else:
        Utilities.log_error(calc.source, calc.destination)
