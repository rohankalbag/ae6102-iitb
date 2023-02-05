from automan.api import Problem, Simulation, Automator, mdict, opts2path, filter_cases
import matplotlib.pyplot as plt
import numpy as np


class Jacobi(Problem):
    def get_name(self):
        return 'jacobi'

    def setup(self):
        options = mdict(size = [10, 25, 50, 95], procedure=["loop","numba","numpy"])
        base_cmd = 'python jacobi_numba.py -o $output_dir/data.npz -n 100'
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
        x = np.array([10, 25, 50, 95])
        methods = ["loop","numba","numpy"]
        d = {}
        d["loop"] = []
        d["numba"] = []
        d["numpy"] = []
        for size in x:
            for method in methods:
                filtered_cases = filter_cases(self.cases, size=size, procedure=method)
                for case in filtered_cases:
                    with open(case.input_path('stdout.txt')) as file:
                        d[method].append(float(file.read()))
        plt.grid()
        plt.title('jacobi')
        plt.xlabel('size')
        plt.ylabel('time_taken')
        y_loop = np.array(d["loop"])
        y_numba = np.array(d["numba"])
        y_numpy = np.array(d["numpy"])
        plt.plot(x, y_loop, label="loop")
        plt.plot(x, y_numpy, label="numpy")
        plt.plot(x, y_numba, label="numba")
        plt.legend()
        plt.savefig(self.output_path('perf.png'))
        plt.close()
        np.savez(self.output_path('perf.npz'), x=x, y_loop=y_loop, y_numpy=y_numpy, y_numba=y_numba)

class Julia(Problem):
    def get_name(self):
        return 'julia'

    def setup(self):
        options = mdict(x_pixels = [320, 480, 640, 800], procedure=["numpy", "numba"])
        base_cmd = 'python julia_numba.py -o $output_dir/data.npz -n 100'
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
        x = np.array([320, 480, 640, 800])
        methods = ["numpy", "numba"]
        d = {}
        d["numba"] = []
        d["numpy"] = []
        for pix in x:
            for method in methods:
                filtered_cases = filter_cases(self.cases, x_pixels=pix, procedure=method)
                for case in filtered_cases:
                    with open(case.input_path('stdout.txt')) as file:
                        d[method].append(float(file.read()))
        plt.grid()
        plt.title('julia')
        plt.xlabel('x-pixels')
        plt.ylabel('time_taken')
        y_numba = np.array(d["numba"])
        y_numpy = np.array(d["numpy"])
        plt.plot(x, y_numpy, label="numpy")
        plt.plot(x, y_numba, label="numba")
        plt.legend()
        plt.savefig(self.output_path('perf.png'))
        plt.close()
        np.savez(self.output_path('perf.npz'), x=x, y_numpy=y_numpy, y_numba=y_numba)




if __name__ == '__main__':
    automator = Automator(
        simulation_dir='outputs',
        output_dir='manuscript/figures',
        all_problems=[Jacobi, Julia]
    )
    automator.run()