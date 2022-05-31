---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.13.4
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

## Notation

$ F_i(\{q\}) $ is the force on ith particle. $ \{q\} $ is the set of cordinates of all particles.

If there are N particles in the system,

Configration space:  3N dimensional space, records positions.

State space: 6N dimensional space, records position and velocity.

Phase space: 6N dimesnional space, records momentum and velocity.



<!-- #region tags=[] -->
## Newton's second law

gives us 6N equations.

$$
\begin{align*}
\dot{p_i} &= F_i(\{q\}) \\
\dot{q_i} &= \frac{p_i}{m_i}
\end{align*}
$$

Thus, if forces are known, we can compute trajectory in 6N dimensional configration space.


if we denote $ p = \sum_{i=1}^{i=N} p_i $,

## Newton's third law,

    every force has equal and opposite reaction
    
can be used to derive conservation of momentum.

$\dot{p} = 0$.

What this tells us is if we start our trajectory at some 6N-D point in configration space, all the points in the trajectory have the same momentum. In some sense, system evolves on a contour of constant momentum.




<!-- #endregion -->

<!-- #region tags=[] -->
## Energy

Potential Energy Principle: All forces derive from a potential energy function $V(\{q\})$.
<!-- #endregion -->

For particle moving in 1 dimension, 

$ F(q) = -\frac{dV(q)}{dq}$.

Potential energy can be computed as $V(q) = \int_{-\infty}^q F(q') dq'$.

Potential energy is not conserved. Sum of potential energy and kinetic energy are conserved.

Kinetic energy: $T = \frac{1}{2} mv^2$.



More than one particles, three dimensions. If the system has N particles, the i in $q_i$ can index any of the 3N elements of the configration space.

Principle:
For **any** system there exists a potential function $V(\{q\})$, such that,

$$
F_i(\{q\}) = - \frac{\partial V(\{q\})}{\partial q_i}
$$

In general mathematics such function need not exist for a collection of $F_i$s. This law represents conservation of energy.


## Lagrangian

### For one particle in one dimension
We are given $q(t_0)$ and $q(t_1)$.

$L(q, \dot{q}) = T - V = \frac{1}{2}m\dot{q}^2 - V(\{q\})$

Action $A = \int_{t_0}^{t_1} L  dt$.

Principle of least action tells that the particle chooses a trajectory (the function q) which minimizes the the action.

Principle of least action gives Euler-Lagrange equations.

$$
\frac{d}{dt} \frac{\partial L}{\partial \dot{q}} - \frac{\partial L}{\partial {q}} = 0
$$

### For multidimensional motion of many particles
Euler-Lagrange equations are given by,

$L(\{q\}, \{\dot{q}\}) = \sum_i \frac{1}{2}m_i\dot{q_i}^2 - V(\{q\})$.

$$
\frac{d}{dt} \frac{\partial L}{\partial \dot{q_i}} - \frac{\partial L}{\partial {q_i}} = 0
$$

Lagrangian packs all the equations of the motions concisely.

$\frac{\partial L}{\partial \dot{q_i}}$ is called generalized momentum conjugate to $q_i$. This can be motiviated by thinking of $q_i$ as cartesian coordinates and $L = \frac{1}{2}m\dot{x}^2$. Depending upon the Lagrangian, conjugate momentum may not have familiar form, but it is always difined by the formula $p_i =\frac{\partial L}{\partial \dot{q_i}}$.

So, if the Lagrangian does not depend on $q_i$, $\dot{p_i} = 0$, i.e. the conjugate momentum is conserved. Such coordinates are called cyclic coordinates.

#### Another example of cylic coordinates

$ L = \frac{m}{2}(\dot{x_1}^2 + \dot{x_2}^2 ) + V(x_1 - x_2)$. It does look like that L is a function of $x_1$ and $x_2$, so neither of these is cyclic coordinate. But, if we do change of variables,
$$
\begin{align*}
x_+ &=  \frac{x_1+x_2}{2} \\
x_- &=  \frac{x_1-x_2}{2} 
\end{align*}
$$

the Lagrangian can be rewritten as,  $L = m(\dot{x_+}^2 + \dot{x_-}^2 ) + V(x_-)$. Now the momentum conjugate to $x_+$ is conserved. $p_+ = 2m\dot{x_+} = m(\dot{x_1} + \dot{x_2})$, so the total momentum is conserved.

```python

```
