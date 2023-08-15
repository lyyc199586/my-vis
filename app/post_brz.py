""" FEM postprocessing of dynamic Brazilian split tests"""

# %% settings
import sys

sys.path.append("../src")

from utils.exodus import Exodus
from utils.post import FEMPlotter

file_dir = "../../temp/brz_nuc22_p300_a10_l2.5_d5_iref2.e"
exodus = Exodus(file_dir)

# read exodus file
t = exodus.get_time()
verts, faces = exodus.get_mesh()
d = exodus.get_var(var_name="d", timestep=-1)
stress_11 = exodus.get_var(var_name="stress_11", timestep=-1)

#%% plot
import matplotlib.pyplot as plt

plt.style.use("../misc/elsevier.mplstyle")
fig, axes = plt.subplots(1, 3, figsize=(6.4, 2.655))

plot_vars = [None, d, stress_11]
plotter = FEMPlotter(verts, faces)

for i, ax in enumerate(axes):
    _, p = plotter.plot(plot_vars[i], ax=ax, lw=0.1)
    ax.set_aspect("equal")
    if(plot_vars[i] is not None):
        ax.figure.colorbar(p, ax=ax, fraction=0.046, pad=0.1, orientation='horizontal')

axes[0].set_title("Mesh")
axes[1].set_title("Damage")
axes[2].set_title("Stress yy")
fig.suptitle("FEM visualization of Brazilian split test")

# %%
# %% save plot
save_dir = "../example/"
fig.savefig(save_dir + "post_brz.png")
# %%
