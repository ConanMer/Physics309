#!/usr/bin/env python
# coding: utf-8

# # PHYS 309 Assignment 1
# 
# ### Getting started
# 
# <ul>
#     <li>If you do not already have the <a href="https://www.anaconda.com/products/distribution">Anaconda <tt>python</tt> distribution</a>, click the link to install the individual, free version</li>
#     <li>Download this notebook to your own computer, open with <tt>Jupyter</tt> notebook or lab, and complete the missing code. See the <a href="https://docs.jupyter.org/en/latest/start/index.html"><tt>Jupyter</tt> documentation</a> for help.</li>
# </ul>
# 
# <strong>Instead of putting in the values of physical constants such as $c$ and $\epsilon_0$ by hand, use SI values pre-programmed into [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html). 
# For example, $\mu_0$ is <tt>constants.mu_0</tt>. 
# 
# ### Set up <tt>python</tt> environment

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

 # Contains physical constants defined in SI units (default) as well as other systems
from scipy import constants

# Make easily readable plots with large axis labels
plt.rcParams.update({"font.size":16, "axes.labelsize":16, "font.family":"sans-serif", 
                     "font.sans-serif":"Arial"})


# ### Questions
# 
# 
# Recall that the speed of light in vacuum is 
# \begin{equation}
# c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}, \; \; \; \; \; (1)
# \end{equation}
# where $\epsilon_0 = 8.85 \times 10^{-12}$ F/m (Farads per meter)$^{*}$ is the electric permittivity of free space and $\mu_0 = 1.26 \times 10^{-6}$ N/A$^2$ (Newtons per Ampere$^2$)$^{**}$ is the magnetic permeability of free space. The electric field created by a point charge $q$ is
# \begin{equation}
# E = \frac{1}{4 \pi \epsilon_0} \frac{q}{r^2}. \; \; \; \; (2)
# \end{equation}
# Suppose a charged particle is moving at some fraction of the speed of light in vacuum ($v_q = f c; \; 0 < f < 1$) as seen in reference frame $S$. Reference frame $S^{\prime}$ is co-moving with the point charge, so that $\frac{dx^{\prime}}{dt^{\prime}} = v^{\prime}_q = 0$ in frame $S^{\prime}$. To make the math easier, put $q$ at the origin of $S^{\prime}$.
# 
# To understand Einstein's motivation for developing the special theory of relativity, make the <strong>incorrect, erroneous, and wrong</strong> assumption that the Galilean velocity transformation holds true for all values of $f$:
# \begin{equation}
# \frac{dx^{\prime}}{dt^{\prime}} = \frac{dx}{dt} - v_q \; \; \; (3)
# \end{equation}
# 
# <ol>
#     <li>Assume the charged particle is an electron. Using Equation 2, calculate and plot the electric field as a function of distance $r^{\prime}$ from $q$ in frame $S^{\prime}$. Choose an x-axis range that makes sense to you and label both axes with correct units.</li>
# </ol>

# In[3]:


r = np.linspace(0.00001, 0.0001, 30)

q = -1.6E-19
ep = 8.85E-12

E = (1 / (4 * np.pi * ep)) * (q / r ** 2)

plt.plot(r, E)


plt.xlabel('Radius (m)')
plt.ylabel('Electric Field (N/C)')
plt.title('Electric Field across Distance')

plt.show()


# <ol start=2>
#     <li>The Galilean velocity transformation suggests that objects can "catch up" with light, so that light in a vacuum appears to be going slower than the value of $c$ from Equation (1). Make a plot of $c^{\prime}$, the <strong>incorrect</strong> speed of light in frame $S^{\prime}$ according to the Galilean transformation, as a function of $f$. Put units on the axes where appropriate.</li>
# </ol>

# In[4]:


f = np.linspace(0, 1, 100)

mu = 1.26E-6
c = 1 / ((ep * mu) ** (1 / 2))
cprime = c * (1 - f)

plt.plot(f, cprime)

plt.xlabel('f')
plt.ylabel("c' (m/s)")

plt.show()


# <ol start=3>
#     <li>In frame $S^{\prime}$, something has to give: either Equation (1) is no longer true, or the values of $\epsilon_0$ and/or $\mu_0$ have to change. Suppose Equation (1) is still true and $\mu_0 = \mu_0^{\prime}$. Make a plot with two vertically stacked subplots. The top subplot should show $\epsilon_0^{\prime}$ as a function of $f$, while the bottom plot should show the electric field $E^{\prime} = \frac{1}{4 \pi \epsilon_0^{\prime}} \frac{q}{{r^{\prime}}^2}$ at $r^{\prime} = 1 \mu \mathrm{m} = 10^{-6}$ m as a function of $f$. Put units on the axes where appropriate.</li>
# </ol>

# In[5]:


c = 1 / ((ep * mu) ** (1 / 2))
eprime = 1 / (cprime ** 2 * mu)

rprime = 1E-6
Eprime = (1 / (4 * np.pi * eprime)) * (q / (rprime ** 2))

fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

ax[0].plot(f, eprime, label="epsilon'")
ax[1].plot(f, Eprime, label="Electric Field'")

ax[1].set_xlabel('f')
ax[0].set_ylabel('Electric Permittivity (F/m)')
ax[1].set_ylabel('Electric Field (N/C)')

ax[0].legend()
ax[1].legend()

plt.show()


# <ol start=4>
#     <li>Now assume $f = 0.5$. In the same plot window, plot $E^{\prime}(r^{\prime})$ given by Equation 2 (same curve as in Problem 1) <em>and</em> $E^{\prime}(r^{\prime})$ calculated as in Problem 3, where $\epsilon_0^{\prime}$ is a function of $f$. Do you notice a problem?</li>
# </ol>

# In[6]:


r = np.linspace(0.00001, 0.0001, 100)

E = 1 / (4 * np.pi * ep) * (q / r ** 2)
Eprime = (1 / (4 * np.pi * eprime)) * (q / r ** 2)

plt.figure(figsize=(8, 6))

plt.plot(r, E, label='E')
plt.plot(r, Eprime, label="E'")

plt.xlabel('f')
plt.ylabel('Electric Field (N/C)')
plt.grid(True)
plt.legend()

plt.show()


# <ol start=5>
#     <li>To resolve the issues revealed by the plot from Problem 4, you may suggest setting $\epsilon_0^{\prime} = \epsilon_0$ and allowing $\mu_0^{\prime}$ to vary with $f$. Let's explore that solution. To accompany the point charge in problems 1-4, add a current loop that's also at rest in frame $S^{\prime}$. Recall that the magnitude of the magnetic field strength at the center of the loop in frame $S$ is $B = \frac{\mu_0 I}{2R}$, where $I$ is the current and $R$ is the radius of the loop. Suppose $I = 1$ A and $R = 1$ m. Assume $E^{\prime} = E$, $B^{\prime} = B$, and $c^{\prime}$ depends on $f$ as in problem 2. Plot $\mu_0$ as a function of $f$.</li>
# </ol>

# In[7]:


muprime = 1 / (cprime ** 2 * ep)

plt.plot(f, muprime)

plt.xlabel('f')
plt.ylabel('Magnetic Permeability (N/A^2)')


# <ol start=6>
# <li>If we calculate $c^{\prime}$ using the Galilean transformation in Equation 3, is there any value of $f$ for which $E^{\prime} = E$ <strong>and</strong> $B^{\prime} = B$? Make a graph to illustrate your answer.</li>
# </ol>

# In[8]:


Eprime = (1 / (4 * np.pi * eprime)) * (q / (rprime ** 2))
E_correct = 1 / (4 * np.pi * ep) * (q / rprime ** 2)

Bprime = 1 * muprime /(rprime * 2)
B_correct = mu * 1 / (2 * rprime)

fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

ax[0].plot(f, Eprime, label="E'")
ax[0].plot(f, E_correct*np.ones(len(f)), label="E' Correct Value", ls='--')

ax[1].semilogy(f, Bprime, label="B'")
ax[1].semilogy(f, B_correct*np.ones(len(f)), label="B' Correct Value", ls='--')

ax[1].set_xlabel('f')
ax[0].set_ylabel('Electric Field (N/C)')
ax[1].set_ylabel('Magnetic Field (N/Am)')

ax[0].legend()
ax[1].legend()

plt.show()


# Conceptual questions about the conflict between the Galilean velocity transformation and E&M are in the written homework assignment.

# $^{*}$Farad = Coulomb/Volt: Farad is the unit of capacitance, which measures the amount of charge necessary to increase the electric potential of a system by 1 Volt. Farads/meter measure how much capacitance you get per meter of free space between yourself and a charged particle.
# 
# $^{**}$Newtons/Ampere$^2$ = Newtons/(Coulombs/second)$^2$. $\mu_0$ measures how effective inductance is at creating magnetic force in free space.

# In[ ]:




