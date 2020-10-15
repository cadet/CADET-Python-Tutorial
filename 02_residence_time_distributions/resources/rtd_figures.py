import numpy as np
import scipy.interpolate
import matplotlib.pyplot as plt

def plot_step(c_init, c_step, t_switch, file_name=None):
    """Function for plotting section times demo

    Parameters
    ----------
    c_init : ndarray
        Initial concentration
    c_step : ndarray
        Step concentration
    t_switch : float
        time for concentration step
    file_name : string
        name for saving figure.
    """
    plt.figure()
    
    

    step_fun = lambda t_switch, time: np.array([c_init if t <= t_switch else c_step for t in time])
    
    time = np.linspace(0, 4*t_switch, 1001)

    plt.plot(time, step_fun(t_switch, time))
    
    plt.xticks([])
    plt.yticks([])
        
    plt.ylabel('concentration')
    plt.xlabel('time')
    
    plt.show()
    
    if file_name is not None:
        plt.savefig(file_name)


    
if __name__ == '__main__':
    
    plt.close('all')
    file_name = './step.png'
    plot_step(0, 1, 1, file_name)