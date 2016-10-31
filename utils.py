#!/usr/bin/env python
# -*- coding: utf 8 -*-
"""
Functions for importing Canstrat ASCII files.

:copyright: 2016 Agile Geoscience
:license: Apache 2.0
"""

import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


def norm(m):
    return m.T @ m


def misfit(d, d_pred):
    misfit = (d_pred - d).T @ (d_pred - d)
    return np.asscalar(misfit)


def plot_all(m, d, m_est, d_pred, equalize=True):
    """
    Helper function for plotting. You can ignore this.
    """
    fig = plt.figure(figsize=(10,6))

    ax0 = fig.add_subplot(2,2,1)
    ax0.plot(m)
    t = "$\mathrm{{Model}}\ \mathbf{{m}}.\ \mathrm{{norm}}\ {:.3f}$"
    ax0.set_title(t.format(norm(m)))
    ax0_mi, ax0_ma = ax0.get_ylim()

    ax1 = fig.add_subplot(2,2,2)
    ax1.plot(d, 'o', mew=0)
    ax1.set_title("$\mathrm{Data}\ \mathbf{d}$")
    ax1_mi, ax1_ma = ax1.get_ylim()

    ax2 = fig.add_subplot(2,2,3)
    ax2.plot(m, alpha=0.25)
    ax2.plot(m_est)
    t = "$\mathrm{{Estimated\ model}}\ \mathbf{{\hat{{m}}}}.\ \mathrm{{norm}}\ {:.3f}$"
    ax2.set_title(t.format(norm(m_est)))
    ax2_mi, ax2_ma = ax2.get_ylim()

    ax3 = fig.add_subplot(2,2,4)
    ax3.plot(d, 'o', mew=0, alpha=0.25)
    ax3.plot(d_pred, 'o', mew=0)
    t = "$\mathrm{{Predicted\ data}}\ \mathbf{{d}}_\mathrm{{pred}}.\ \mathrm{{misfit}}\ {:.3f}$"
    ax3.set_title(t.format(misfit(d, d_pred)))
    ax3_mi, ax3_ma = ax3.get_ylim()

    if equalize:
        ax0.set_ylim(min(ax0_mi, ax2_mi) - 0.1,
                     max(ax0_ma, ax2_ma) + 0.1)

        ax2.set_ylim(min(ax0_mi, ax2_mi) - 0.1,
                     max(ax0_ma, ax2_ma) + 0.1)

        ax1.set_ylim(min(ax1_mi, ax3_mi) - 0.1,
                     max(ax1_ma, ax3_ma) + 0.1)

        ax3.set_ylim(min(ax1_mi, ax3_mi) - 0.1,
                     max(ax1_ma, ax3_ma) + 0.1)

    plt.show()
