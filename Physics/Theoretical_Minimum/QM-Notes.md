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

<!-- #region tags=[] -->
# Quantum Mechanics

## Differences from Classical Mechanics
1. States have different logical structure than CM.
2. States and measurements are different unlike CM. e.g. Position and Momemntum can be determined by experiments in CM.

## Spins
Particles have properties attached to it. e.g. mass, electric charge.

Even a specific particle is not completely specified by its position.

Attached to electron is an extra degree of freedom, called spin. Spin is as quantum mechanical as it can and we should not try to visualize it.

## Testing

Propositions: 
$$
\begin{align*}
A &: \sigma_z = +1 \\
B &: \sigma_x = +1 \\
\end{align*}
$$

### Classically,

To test (A or B), one could first **gently** test $\sigma_z$. If it is -1, one would **gently** test $\sigma_x$. The result of doing it otherway (i.e. B or A) will be the same as doing (A or B). The reason is that classically, measurements are gentle. They don't change the state of the system.

### In Quantum Mechanics,

If some entity prepares the spin in $\sigma_z = +1$ state, and we measure `A or B` (whether we use short circuit or not), we will measure it to be true. However, if we measure `B or A`, there is 25% chance that we will measure it to be false.

What about `A and B`? If we conclude that `A and B` is true, can we confirm it again? Answer is no. Since to compute B, we had to measure $\sigma_x$, which ruined measurement of A. Thus we can't confirm it. i.e. experiment is not reproducible.
<!-- #endregion -->

<!-- #region tags=[] -->
## Complex Numbers
<!-- #endregion -->

Two ways to represent them. 

In cartesian coordinates, $z = x + iy$.

In polar coordinates, $z = re^{i\theta}$.

$ x_1 x_2 = (r_1e^{i\theta_1})(r_2e^{i\theta_2}) = r_1 r_2 e^{i(\theta_1 + \theta_2)}$.

$z = x + iy = re^{i\theta}$ 

$z^\ast = x - iy = re^{-i\theta}$ 

$z^\ast z = r^2$, i.e. a real number

### Phase Factors

These are complex numbers whose r componenet is 1. Following holds for them,

$$
\begin{align}
z^\ast z &= 1 \\
z &= e^{i\theta}\\
z &= \cos\theta + i \sin\theta
\end{align}
$$


$$\renewcommand{\bra}[1]{\left\langle{#1}\right|}$$
$$\renewcommand{\ket}[1]{\left|{#1}\right\rangle}$$
$$\renewcommand{\braket}[1]{\left\langle{#1}\right\rangle}$$

<!-- #region tags=[] -->
## Vector Spaces
<!-- #endregion -->

<!-- #region jp-MarkdownHeadingCollapsed=true tags=[] -->
Vector spaces is familiar concept from abstract linear algebra.

### Complex Conjugate of space V 

For every $\ket{A}$ there exists $\bra{A}$ in conjugate space. This space has following properties.

1. The conjugate of $\ket{A} + \ket{B}$ is $\bra{A}+\bra{B}$.
2. Conjugate of $z\ket{A}$ is $z^\ast \bra{A} = \bra{A}z^\ast $.

In the concrete case where ket space is column vectors, bra space is denoted as row vectors.

i.e. if 

$$
\begin{align*}
\ket{A} = \begin{bmatrix}
\alpha_1 \\
\alpha_2 \\
\vdots \\
\alpha_n
\end{bmatrix}
\end{align*}
$$

then
$$
\begin{align*}
\bra{A} = \begin{bmatrix}
\alpha_1^\ast  & \alpha_2^\ast  & \dots & \alpha_n^\ast 
\end{bmatrix}.
\end{align*}
$$

<!-- #endregion -->

### Inner Products


Inner product is always between bras and kets. It is written like $\braket{B|A}$. The result is a complex numbers.

#### Axioms of inner product.
1. Inner product is linear. $\bra{C} + (\ket{A}+\ket{B}) = \braket{C|A} + \braket{C|B}$.
2. $\braket{B|A} = \braket{A|B}^\ast $.

#### Special vectors
1. Normalized: $\braket{A|A} = 1$.
2. Orhthogonal: $\braket{B|A} = 0$.


### Orhtonormal Basis.

Let our space be N dimensional. And let the orthonomal basis denoted by $\ket{i}$.

$$
\ket{A} = \sum_i \alpha_i \ket{i},
$$

where, $\alpha_j = \braket{j|A}$. (To derive this, multiply both sides by $\bra{j}$.


# States


In CM, knowing the state means knowing everything that is necessary to predict the future. 

In QM, knowing the state means knowing as much as can be known about how the system was prepared.


Apparatus $\cal{A}$ can be oriented on any axis. If we orient it along z axis, the measured spin will either be +1 or -1. 

$\sigma_z = \pm 1$. We can denote +1 as state $\ket{u}$ and -1 as $\ket{d}$.

Similarly $\sigma_x = \pm 1$, can be denoted by  $\ket{r}$ and -1 as $\ket{l}$. And $\sigma_y = \pm 1$, can be denoted by  $\ket{o}$ and -1 as $\ket{i}$.

If two states are orthogonal than these two states can be determined together. For example, if $\sigma_z$ was prepared to be in $\ket{u}$, for any subsequent measurements probability that $\ket{d}$ is detected is 0. Thus for binary spin, the state space is two dimensional. For now we can take $\ket{u}, \ket{d}$ as the basis vectors.

Then, the generic state $\ket{A} = \alpha_u \ket{u} + \alpha_d \ket{d}$. Where $\alpha_i = \braket{i|A}$.

The meaning of,
- $\alpha_u^\ast \alpha_u$: If the spin was prepared in $\ket{A}$ state, $\alpha_u^\ast \alpha_u$ is the probability that $\sigma_z = +1$.
- $\alpha_d^\ast \alpha_d$: is the probability that $\sigma_z = -1$.

Since probabilities must add to 1, $\alpha_u^\ast \alpha_u + \alpha_d^\ast \alpha_d = 1$. It is equivalent to saying that $\ket{A}$ is normalized, i.e. $\braket{A|A} = 1$.

General principle of quantum systems: the state of a system is represented by a unit (normalized) vector in a vector space of states. Moreover, the squared magnitudes of the components of the state-vector, **along particular basis vectors**, represent probabilities for various experimental outcomes. 


### Representing $\ket{r}$ and $\ket{l}$ using above basis vectors

We know that if A initially prepares the state in $\ket{r}$, $\sigma_z = \pm 1$ with equal probability. Hence, $\alpha_u^\ast \alpha_u =\alpha_d^\ast \alpha_d = \frac{1}{2}$. One choice is to have $\alpha_u = \alpha_d = \frac{1}{\sqrt{2}}$.

$\ket{r} = \frac{1}{\sqrt{2}} \ket{u} + \frac{1}{\sqrt{2}} \ket{d}$. (There are is still ambiguity, called phase ambiguity.)

To solve for $\ket{l}$ the above process repeats. But, in addition, $\braket{l|r} = 0$. One choice is $[\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}]$. But it is not the only choice. Even for fixed choice for $\ket{r}$, you can multiply above choice by a phase factor ($z = e^{i\theta}$), and still satisfy the two constraints. Later, we will find out that no measurable quantity is sensitive to the overall phase-factor, and therefore we can ignore it when specifying states. 

### Representing $\ket{i}$ and $\ket{o}$ using above basis vectors

To solve for $\ket{i}$ and $\ket{o}$, we need same conditions as we needed above. But we also need additional constrains. For example, if A prepares the state in $\ket{i}$,$\sigma_x = \pm1$, with equal probability. Also $\braket{i|o} = 0$.

The following solution solves for these constraints (up to phase-factor ambiguity).

$\ket{i} = \frac{1}{\sqrt{2}} \ket{u} + \frac{i}{\sqrt{2}} \ket{d}$.

$\ket{o} = \frac{1}{\sqrt{2}} \ket{u} - \frac{i}{\sqrt{2}} \ket{d}$.



With the previous discussion, the vectors can be represented in column format as below.

$$
\begin{align*}
\ket{u} &= \begin{bmatrix} 1 \\ 0 \end{bmatrix}, \ket{d} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \\
\end{align*}
$$

<!-- #region -->
### Matricies

If we have a basis $\ket{i}$, a vector $\ket{A}$ can be rewritten as,

$$ \ket{A} = \sum_i \alpha_i \ket{i} = \sum_i \ket{i} \braket{i|A} $$.

Similarly,
$$ \bra{A} = \sum_i \braket{A|i}\bra{i}  $$.



Axiom: Physical observables are described by linear operators.

Observables are the things that we can measure. e.g., coordinates of a particle; the energy, momentum, or angular momentum of a system; or the electric field at a point in space.

$$
\begin{align*}
M \ket{A} &= \ket{B} \\
M \sum_j \alpha_j \ket{j} &= \sum_j \beta_j \ket{j} \\
\sum_j \alpha_j M\ket{j} &= \sum_j \beta_j \ket{j} \text{;;assuming M is linear} \\
\sum_j \alpha_j \bra{k} M \ket{j} &= \sum_j \beta_j \braket{k|j} \text{;;multiply both sides by} \bra{k} \\
\sum_j \alpha_j m_{kj} &= \beta_k\\
\end{align*}
$$

Note that each $m_{kj}$ is a complex number. We can think of M in terms of matrix (defined by a choice of basis vectors).

#### Eigenvectors and Eigenvalues

$M \ket{\lambda} = \lambda \ket{\lambda}$. $\lambda$ is an eigenvalue, and $\ket{\lambda}$ is an eigenvector.

#### Linear operators on bra vectors

$$ 
\begin{align*}
\bra{B}  &= \begin{bmatrix} b_1^\ast  & b_2^\ast  & b_3^\ast \end{bmatrix} \\
M &= \begin{bmatrix}
m_{11} & m_{12} & m_{13} \\
m_{21} & m_{22} & m_{23} \\
m_{31} & m_{32} & m_{33} \\
\end{bmatrix}
\end{align*}
$$

Than $\bra{B} M$ is just row vector multiplied by matrix M.

#### Hermitian Conjugate
$$
\begin{align*}
M^\dagger &= (M^T)^\ast  \\
M \ket{A} &= \ket{B} \\
\bra{A} M^\dagger &= \bra{B} \\
\end{align*}
$$

#### Hermitian Operators
- Observables quantities in classcial mechanics are real numbers. i.e. they are their own complex conjugate.
- Observables in quantum mechanics (i.e. linear operators) are also their own complex conjugates. Such operators are called Hermitian Operators. $M^\dagger = M$.

##### Properties of Hermitian Operators
- Their eigenvalues are real.
- Their eigenvectors form an orthonormal basis. (i.e. their eigenvectors are orthonormal and they form a basis)
<!-- #endregion -->

## Principles
1. The observable or measurable quantities of QM are represented by a linear operator L. 
2. The possible readings of the measurements are eigenvalues $\lambda_i$. The state for which reading is **unambiguously** $\lambda_i$ is the corresponding eigenvector $\ket{\lambda_i}$.
3. Unambiguously distinguishable states are represented by orthogonal vectors. e.g. $\braket{u|d} = 0$.
4. If $\ket{A}$ is the state vector of the system, and the observable L is measured, the probability of observing $\lambda_i$ is given by $\braket{A|\lambda_i}\braket{\lambda_i|A}$.

Since the readings (i.e., eigenvalues) are real and eigenvectors are orthogonal, the operator L must be hermitian.

P1 says that $\sigma_x, \sigma_y, \text{and} \sigma_z$ are identified with a specific linear operator in 2D space of states describing the states.
P2 says that the actual measurments can take discrete values. E.g., energy of atom will be one of the established energy levels of the atom.


### 3-Vector Operator $\sigma$

- Just as a spin-measuring apparatus can only answer questions about a spin's orientation in a specific direction, a spin operator can only provide information about the spin component in a specific direction. 
- To physically measure spin in a different direction, we need to rotate the apparatus to point in the new direction. The same idea applies to the spin operator—if we want it to tell us about the spin component in a new direction, it too must be "rotated" but this kind of rotation is accomplished mathematically.

### Operator Matrices
Using above four principles, and solving linear equations, we can derive them.

$$
\sigma_z = \begin{bmatrix}
1 & 0 \\
0 & -1 
\end{bmatrix}, \sigma_x = \begin{bmatrix}
0 & 1 \\
1 & 0 
\end{bmatrix}, \sigma_y = \begin{bmatrix}
0 & -i \\
i & 0 
\end{bmatrix} \text{.}
$$

These along with Identity matrix are called Pauli Matrices.

IMPORTANT: Applying the operator L to state $\ket{A}$ does not change the state to $L\ket{A}$. $L\ket{A}$ is actually a supuerposition and tells us the probabilities of basis states. When we actually measure using L, the system is changed to one of the eignestates unambiguously.

There is nothing special about these three operators. We can take any direction $\hat{n} = (n_x, n_y, n_z)$, orient the apparatus A along $\hat n$, activate A, and measure the component of the spin along $\hat n$. That means there has to be an operator that represents this operation. Indeed, this operator is given by $\sigma_n = \sigma \cdot \hat n$, where $\sigma = (\sigma_x, \sigma_y, \sigma_z)$.

$$
\sigma_n = \begin{bmatrix}
n_z & (n_x - i n_y) \\
(n_x + i n_y) & -n_z
\end{bmatrix}
$$


### Spin-Polarization Principle

For any state $\ket{A} = \alpha_u \ket{u} + \alpha_d \ket{d}$, there exists some direction $\hat n$ such that $\sigma \cdot \hat n = \ket{A}$.

States of the spins are characterized by a polarization vector, and along the polarization vector the component of the spin is predictably +1.





### Time Development Operator


Let the closed system be in state $\ket{\Psi(t)}$. Thus, state can be different at different times. 

The time development operator $U(t)$ tells us how the system evolves with time.

$$\ket{\Psi(t)} = U(t) \ket{\Psi(0)}$$.

Thus, the time evolution of the state is deterministic.

Quantum mechanics assumes,
1. that U(t) is a linear operator.
2. If two states are orthonormal, they remain orthonormal in the evolution. i.e., $\braket{\Psi(0)|\Phi(0)} =0 \implies \braket{\Psi(t)|\Phi(t)} = 0$.

As a consequence of these two assumptions, it is easy to prove that $U(t)^{\dagger}U(t) = I$. Such operator is called unitary operator.

Principle 5: Time evolution of state vectors is unitary.

Unitarity also implies that as time evolves, the overlap (inner product) between two states remains the same.

Quantum Mechanics also assumes that time evolution is continuous.

Thus, for small time $\epsilon, U(\epsilon) = I - i \epsilon H$. Using the unitarity condition  $U(t)^{\dagger}U(t) = I$, we can show that $H^{\dagger} = H$.

Thus, H is hermitian. i.e., it is an obeservable, and has complete set of orthonormal eigenvectors.

We will see that, the eigenvalues of H are the values that result from measuring the energy levels of the quantum system. Thus, it has resemblance to the hamiltonian from the classical mechanics.

Using the continuity assumption inside $\ket{\Psi(t)} = U(t) \ket{\Psi(0)}$, we can derive, 

$$ \frac{d \ket{\Psi}}{dt} = -iH\ket{\Psi}$$.

This equation is known as Generalized Schrodinger equation or time-dependent schrodinger's equation. If we know the Hamiltonian of the system, we can know how the state of the undisturbed system evolves with the time.

#### Plank's constant
h = 6.6 * 1e-34 kgm^2/s1.

$\hbar = \frac{h}{2\pi} = 1.054571726 \dots x 10^{-34} \frac{kgm^2}{s}$ 

In the gen. schrodinger's eqn, lhs has units of 1/time, whereas rhs has units of energy (kgm^2/s^2, because H is hamiltonian). This is wrong. However multiplying lhs by Plank's constant, units are proper. Thus, the correct Generalized schrodinger's equation is $$ \hbar \frac{d \ket{\Psi}}{dt} = -iH\ket{\Psi}$$.



#### Expectation
If L is an observable, the expectation is defined as $\braket{L} = \sum_i P(\lambda_i) \lambda_i$.

When state of the system is $\ket{A} = \sum_i \alpha_i \lambda_i$, the expecation can be computed as $\braket{L} = \sum_i \alpha_i^\ast \alpha_i \lambda_i = \braket{A|L|A}$.

Try to apply this for state $\ket{r}$ and observable =$\sigma_z$. The arithmetic should result in value 0.

#### Effect of the phase factor.

We can multiply the state vectors by a phase factor $e^{i\theta}$ for any $\theta$. This does no make any difference. Although, probability amplitude will change i.e., $\alpha_i \to e^{i\theta} \alpha_i$, the probability does not change, i.e., $\alpha_i^\ast \alpha_i$ remains unchanged. Similarly, the expectation of the observable does not change.


#### Change in the expectation

$\frac{d \braket{\Psi(t)|L|\Psi(t)}}{dt} = \braket{\dot\Psi(t)|L|\Psi(t)} + \braket{\Psi(t)|L|\dot\Psi(t)}$. Using generalized schrodinger's equations, 

$\frac{d \braket{\Psi(t)|L|\Psi(t)}}{dt} = \frac{i}{\hbar} \braket{\Psi(t)|HL - LH|\Psi(t)}$.

Linear operators don't commute, so HL != LH.

**Commutator**: Given two operators L, and M, LM - ML is called the commutator of L with M, and is denoted by [L, M]. Note that [L, M] = -[M, L].

Thus, $\frac{d}{dt} \braket{L} = \frac{-i}{\hbar} \braket{[L, H]}$.

It is easy to prove that $i[L, H]$ is also Hermitian. Thus, a valid observable.

This has resemblance to classical mechanics. $\dot{F} = \{F, H\}$.


### Conservation in quantum mechanics

To say that an observable Q is conserved is to say that expected value $\braket{Q}$ does not change with time. A stronger condition is that any moment $\braket{Q^m}$ does not change with time.

$\braket{Q}$ does not change ammounts to $[Q, H] = 0$. That is Q commutes with H. Using the properties of commutator, it is easy to prove that $[Q^m, H] = 0$ for any $m \ge 1$.

It turns out that if $[Q, H] = 0$ then for **any** function of Q, $[f(Q), H] = 0$.

H is also conserved, as $[H, H] = 0$. H is defined to be the energy of the quantum system.


### Solving Schrodinger's equation

Time dependent Schrodinger's equation is $ \hbar \frac{d \ket{\Psi}}{dt} = -iH\ket{\Psi}$. 

Since H represents enrgy, the oberservable values of energy are eigenvalues of H. Call them $\ket{E_j}$ and $E_j$.

$$
    H \ket{E_j} = E_j \ket{E_j}
$$

These are call time-independent schrodinger's equations.

We can write $\ket{\Psi{(t)}} = \sum_j \alpha_j(t) \ket{E_j}$.

Thus, $\ket{\dot\Psi{(t)}} = \sum_j \dot\alpha_j(t) \ket{E_j}$.

Using time-dependent Schrodinger's equation, we can solve for $\dot\alpha_j(t)$. It has the form $\dot\alpha_j(t) = -\frac{i}{\hbar}E_j \alpha_j(t)$. Which has the solution $\alpha_j(t) = \alpha_j(0) e^{\frac{-i}{\hbar} E_j t}$.

But, $\alpha_j(0) = \braket{E_j|\Psi(0)}$.

So, $\Psi(t) = \sum_j \ket{E_j}\braket{E_j|\Psi(0)} e^{-\frac{i}{\hbar}E_j t}$.

#### General Recipe

1. Get the H somehow.
2. Find the $\ket{E_j}$ and $E_j$.
3. Prepare the system in initial state $\Psi(0)$.
4. Use above solution to find the state at any later time.
5. If you have some other operator L, you can "predict" the outcome of measuring future state using the eigenvectors of L. i.e., the probability the outcome of measuring L is $\lambda_i$ is precisely $|\braket{\lambda_i|\Psi(t)}|^2$.


## Complex systems

There are systems for which there are more than two observables, and they all can be measured simultaneously. Single spin is **not** such system. Though there are three observables $\sigma_{\{x,y,z\}}$. Only one of them can be observed at a time.

Particle moving in three dimensions, all three dimensions x, y, and z can be measured simultaneously.

Other such system is a system of two particles. Let's denote these two observables as L and M.
If we measure both spins, we leave the system in a state which is simultaneously eigenvector of both L and M. Let the eigenvectors of L be denoted as $\lambda_i$ and same for M with $\mu_a$.

In order to have simultaneous eigenvectors $\ket{\lambda, \mu}$, L and M must commute with each other. i.e., $LM \ket{\lambda, \mu} = ML\ket{\lambda, \mu}$. i.e., $[L, M]\ket{\lambda, \mu} = 0$. Since this statement is true of any basis eigenvector $\ket{\lambda, \mu}$, we know that $[L, M] = 0$.

Thus, if we have complete basis of simultaneous eigenvectors, the observables commute. Converse is also true. If observables commute, they have a complete basis of simultaneous eigenvectors. This statement is true for any number of observables in the system, and not just two.





Suppose, we have a basis of states $\ket{a,b,c, \dots}$ for some complex system. 

$$\ket{\Psi} = \sum_{a,b,c,\dots} \psi{(a,b,c, \dots)} \ket{a,b,c, \dots}$$

Where, $\psi{(a,b,c, \dots)} = \braket{a,b,c, \dots|\Psi}$. This $\psi$ is called a wave function.

$P(a,b,c, \dots) = \psi^\ast{(a,b,c, \dots)} \psi{(a,b,c, \dots)}$. This is the probability of observing the value $a,b,c,\dots$ of commuting observables $A,B,C,\dots$.


If a state is an eigenvector of operator A, which does not commute with B, then it will not be an eigenvector for B. Thus, if A and B don't commute, there will be uncertainity in either A or B if not both.



### Quantifying Uncertainty

The system is in state $\ket\Psi$. We want to observe some A. A can be thought as a random variable. The possible outcomes are eigenvalues of A, with predefined probabilities. Thus $\braket{A}$ is well defined, and is the expected value of A. We can also find the variance of A! This quantifies the uncertainty of A. 

First define $\bar{A} = A - \braket{A}I$. This is also an Hermitian operator, so has real eigenvalues. If $a$ is an eigenvalue of A, $\bar{a} = a - \braket{A}$ is an eigenvalue of $\bar{A}$.

Thus the variance, denoted as $(\Delta A)^2 = \sum_a \bar{a}^2 P(a)$.

A little bit of algebra shows that this is equivalent to $\braket{\bar{A}^2} = \braket{\Psi|\bar{A}^2|\Psi}$.


### Uncertainty Principle

From triangle inequality $|x| + |y| \ge |x+y|$, one can derive $2|x||y| \ge |\braket{x|y} + \braket{y|x}|$. (Hint: Square both sides, and expand).

Putting, $x = A\Psi$ and $y = iB\Psi$, we get $\Delta{A} \Delta{B} \ge \frac{1}{2} | \braket{\Psi|[A, B]|\Psi}$. (Hint: Though formula is true in general, it is easy to derive by assuming that $\braket{A} = \braket{B} = 0$, in which case $(\Delta{A})^2 = \braket{A^2}$.




## Composite System

Atom is made of nucleons and electrons, each is a quantum system of it's own. We want to study composite system.

For the moment we assume there are two systems, A and B (a.k.a. Alices's sytem and Bob's sytem, respectively).
A has states from staet space $S_A$, which has dimensionality of $N_A$. Same for system B. 

The combined system has statespace $S = S_A \otimes S_B$, which has dimensionality $N_A N_B$. $\otimes$ is a tensor product. The states of S are denoted as $\ket{ab}$, where $a \in S_A$ and $b \in S_B$.

```python

```
