import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d
from matplotlib.ticker import MaxNLocator
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

class Arrow3D(FancyArrowPatch):
    """2D arrow between two 3D points."""
    def __init__(self, xs, ys, zs, *args, **kwargs):
        super().__init__((0, 0), (0, 0), *args, **kwargs)
        self._verts3d = xs, ys, zs

    def do_3d_projection(self):
        xs, ys, zs = proj3d.proj_transform(*self._verts3d, self.axes.M)
        self.set_positions((xs[0], ys[0]), (xs[1], ys[1]))
        return np.min(zs)


def draw_origin_axes(ax, xmax, ymax, zmax, xmin=0, ymin=0, zmin=0, nticks=5,
                     labels=("x", "y", "z"), label_size=15, tick_size=10,
                     grid_color="0.85", zorder=2):
    
    lo = np.array([xmin, ymin, zmin], dtype=float)
    hi = np.array([xmax, ymax, zmax], dtype=float)
    span = hi - lo
    ox, oy, oz = np.clip(0.0, lo, hi)

    ax.set_axis_off()
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin, zmax)

    tol = 1e-9 * span
    xt, yt, zt = (t[(t >= a - e) & (t <= b + e)] for t, a, b, e in
                  zip((MaxNLocator(nticks).tick_values(a, b) for a, b in zip(lo, hi)), lo, hi, tol))

    # Grid
    for x in xt:
        ax.plot([x, x], [ymin, ymax], [oz, oz], color=grid_color, lw=0.8, zorder=0)
    for y in yt:
        ax.plot([xmin, xmax], [y, y], [oz, oz], color=grid_color, lw=0.8, zorder=0)

    kw = dict(arrowstyle="-|>", mutation_scale=15, lw=1.2, color="black", shrinkA=0, shrinkB=0, zorder=zorder)
    ex, ey, ez = hi + 0.1 * span
    ax.add_artist(Arrow3D([xmin, ex], [oy, oy], [oz, oz], **kw))
    ax.add_artist(Arrow3D([ox, ox], [ymin, ey], [oz, oz], **kw))
    ax.add_artist(Arrow3D([ox, ox], [oy, oy], [zmin, ez], **kw))

    dx, dy, _ = 0.03 * span
    near = lambda t, o, e: abs(t - o) <= e
    for x in xt:
        ax.plot([x, x], [oy, oy - dy], [oz, oz], color="black", lw=1, zorder=zorder)
        ax.text(x, oy - 3 * dy, oz, f"{x:g}", fontsize=tick_size, ha="center", va="center")
    for y in yt:
        if near(y, oy, tol[1]):
            continue
        ax.plot([ox, ox - dx], [y, y], [oz, oz], color="black", lw=1, zorder=zorder)
        ax.text(ox - 3 * dx, y, oz, f"{y:g}", fontsize=tick_size, ha="center", va="center")
    for z in zt:
        if near(z, oz, tol[2]):
            continue
        ax.plot([ox, ox - dx], [oy, oy], [z, z], color="black", lw=1, zorder=zorder)
        ax.text(ox - 3 * dx, oy, z, f"{z:g}", fontsize=tick_size, ha="right", va="center")

    ax.text(hi[0] + 0.17 * span[0], oy, oz, labels[0], fontsize=label_size, ha="center", va="center")
    ax.text(ox, hi[1] + 0.17 * span[1], oz, labels[1], fontsize=label_size, ha="center", va="center")
    ax.text(ox, oy, hi[2] + 0.18 * span[2], labels[2], fontsize=label_size, ha="center", va="center")


def plot_3d(data_df, sp1, sp2, title, xmax=20, ymax=25, zmax=4, xmin=0, ymin=0, zmin=0, save_filename=None):
    # data_df = np.log(ep_nmf_nbc_acts_medians.loc[[sp1 + "_m_ep", sp2 + "_m_ep", sp1 + "+" + sp2 + "_m_ep"]]) - np.log(ep_nmf_control_median)
    V = data_df.to_numpy()

    # Gram–Schmidt orthogonalization
    basis = []
    for v in V:
        w = v.copy()
        for u in basis:
            w -= np.dot(v, u) * u
        if np.linalg.norm(w) > 1e-20:
            basis.append(w / np.linalg.norm(w))

    # Projection onto 3D basis
    coords = np.array([[np.dot(v, u) for u in basis] for v in V])

    df = pd.DataFrame(data=coords, index=data_df.index, columns=["v1", "v2", "v3"])

    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(projection="3d")
    ax.computed_zorder = False  # draw in the zorder given below, not by depth

    x0, y0, z0 = 0, 0, 0

    x1, y1, z1 = df.loc[sp1 + "_m_ep", "v1"], df.loc[sp1 + "_m_ep", "v2"], df.loc[sp1 + "_m_ep", "v3"]
    x2, y2, z2 = df.loc[sp2 + "_m_ep", "v1"], df.loc[sp2 + "_m_ep", "v2"], df.loc[sp2 + "_m_ep", "v3"]
    x3, y3, z3 = df.loc[sp1 + "+" + sp2 + "_m_ep", "v1"], df.loc[sp1 + "+" + sp2 + "_m_ep", "v2"], df.loc[sp1 + "+" + sp2 + "_m_ep", "v3"]

    # Grid, axes and ticks (zorder 0-2)
    draw_origin_axes(ax, xmax, ymax, zmax, xmin=xmin, ymin=ymin, zmin=zmin)

    # v1-v2 parallelogram
    ax.add_collection3d(Poly3DCollection([np.array([[x0, y0, z0], [x1, y1, z1], [x1+x2, y1+y2, z1+z2], [x2, y2, z2]])],
                                         alpha=0.15, edgecolor='none', color="tab:green", zorder=1))

    # Arrows from origin (0, 0, 0), drawn on top of the axes
    arrow_kw = dict(arrowstyle="-|>", mutation_scale=20, lw=3, shrinkA=0, shrinkB=0, zorder=3)
    for (x, y, z), c in [((x1, y1, z1), "#ff01f5"),
                         ((x2, y2, z2), "#00c6cd"),
                         ((x3, y3, z3), "#ff734e")]:
        ax.add_artist(Arrow3D([x0, x], [y0, y], [z0, z], color=c, **arrow_kw))

    # Drop line from the biculture endpoint to the x-y plane
    ax.plot([x3, x3], [y3, y3], [z0, z3], color="black", linestyle="dotted", lw=1, zorder=4)
    ax.set_box_aspect(None, zoom=0.85)
    plt.title(title, fontsize=15)
    if save_filename:
        plt.savefig(save_filename, bbox_inches="tight")
    plt.show()