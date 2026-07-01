# Bateman Decay Chain Model

Computational modelling of the U-238 → Th-234 → Pa-234 radioactive decay chain using the Bateman equations, solved numerically and validated against analytical solutions.

## Overview

Radioactive decay chains are central to nuclear energy, radiation safety, medical physics, and accelerator experiments. This project models a simplified three-isotope decay chain governed by the Bateman equations, comparing numerical integration against known analytical solutions to validate the computational approach.

## Physics Background

For a nuclide undergoing radioactive decay, the population evolves as:

N(t) = N₀ e^(−λt)

where λ is the decay constant, related to half-life by λ = ln(2) / T½.

For a chain of coupled decays N₁ → N₂ → N₃, the Bateman equations describe the coupled time evolution:

dN₁/dt = −λ₁N₁
dN₂/dt = λ₁N₁ − λ₂N₂
dN₃/dt = λ₂N₂ − λ₃N₃

## Decay Chain Modelled

- **U-238** (t½ ≈ 4.468 billion years)
- **Th-234** (t½ ≈ 24.1 days)
- **Pa-234** (t½ ≈ 6.7 hours)

This chain spans **timescales from hours to billions of years**, making it a genuinely stiff numerical system — small perturbations in fast-decaying species can destabilize naive fixed-step solvers.

## Method

Initial fixed-step RK4 integration was found to be numerically unstable for this system, since the timestep required for the fast-decaying Pa-234 component is many orders of magnitude smaller than the timescale of interest for U-238. The final implementation instead uses `scipy.integrate.solve_ivp` with the **Radau method**, an implicit solver suited to stiff ODE systems, which resolves all three timescales without instability.

Analytical solutions (closed-form exponential expressions from the Bateman equation) are used to independently verify the numerical results.

## Files

- `decay_chain_simulation.py` — numerical simulation and plotting script

## How to Run

```bash
pip install numpy matplotlib scipy
python decay_chain_simulation.py
```

## Results

The simulation shows the expected physical behaviour: U-238 decays negligibly over the simulated timeframe (given its multi-billion-year half-life), while Th-234 and Pa-234 rapidly reach transient equilibrium, each rising and falling on their respective timescales — a hallmark feature of sequential radioactive decay.

## Background

This project was completed as an independent research project during my BS in Computational Physics at the University of the Punjab (Sep 2023 – Feb 2024).

## References

1. Krane, K. S., *Introductory Nuclear Physics*, Wiley.
2. Lamarsh, J. R., *Introduction to Nuclear Engineering*, Prentice Hall.
3. Knoll, G. F., *Radiation Detection and Measurement*, Wiley.
