from automan.api import Problem, Simulation, Automator, mdict, opts2path, filter_cases
import matplotlib.pyplot as plt
import numpy as np

class Jacobi(Problem):
    def get_name(self):
        return 'Jacobi'

    def setup(self):
        options = mdict(size = [10,20,30,100,200,300,700,1000,1500,3000], procedure=["loop","numba","numpy"])
        base_cmd = 'python jacobi_numba.py -o $output_dir/results.npz -n 2000'
        self.cases = [
            Simulation(
                root=self.input_path(opts2path(kw)),
                base_command=base_cmd,
                **kw
            )
            for kw in options
        ]

    def run(self):
        self.make_output_dir()
        self.make_plots()
    
    
    def make_plots(self):
        plt.figure()
        for method in ['loop','numba','numpy']:
            filtered_cases = filter_cases(self.cases, procedure=method)
            times = []
            sizes = []
            for case in filtered_cases:
                with open(case.input_path('stdout.txt')) as file:
                    times.append(float(file.read()))
                sizes.append(case.params['size'])
            plt.plot(sizes,times, label=method)
        plt.grid()
        plt.xlabel('size')
        plt.ylabel('time taken')
        plt.legend()
        plt.savefig(self.output_path('solution.pdf'))
        plt.close()

if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Jacobi]
    )
    automator.run()