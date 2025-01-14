# N-Body Simulations in 2D 

This project presents two distinct implementations of n-body simulations using parallel and distributed protocols:

- [Lua with threads](#?)
- [Python with MPI](#python-implementation-using-mpi)

# Python implementation using MPI

This implementation is based on [this](https://medium.com/swlh/create-your-own-n-body-simulation-with-python-f417234885e9) Medium article, combined with [mpi4py](https://pypi.org/project/mpi4py/).

During every step, the node processes get the masses of the bodies and a slice of the bodies positions to calculate the accelerations of the bodies from the respective slice, based on Newton's law of universal gravitation. 

![image](python/image.png)

In the main loop, the calculated accelerations are reduced to the root process. The positions and velocities are updated using a leap-frog scheme, where first the velocity is updated after a half-step ('half-step kick'), followed by updating the positions ('drift'), and lastly another 'half-step kick'.

The simulation is plotted in real-time, and the performance is measured by the frames per second.

## Prerequisites

To run the simulation, you need to have [MPI](https://www.microsoft.com/en-us/download/details.aspx?id=105289) installed, as well as the [python library](https://pypi.org/project/mpi4py/) for it installed.

```bash
pip install mpi4py
```

## Usage 

```bash
mpiexec -n 4 python n_body_problem_distributed.py
```

Feel free to change the simulation parameters and the number of node processes.

## Benchmarks

