# Create and submit jobs to run simulation experiments on the UA HPC
# Written and tested on Python 3, but will likely work on 2.7

class Experiment:
    """ Class that defines a single simulation experiment """
    def __init__(self, experiment_dir ):
        self.out_dir = experiment_dir
        """ TODO: get variants from tumorsim """
        # Quick change