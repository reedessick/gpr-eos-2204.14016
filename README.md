# gpr-eos-2204.14016

a repository to store nonparametric extensions of [2204.14016](https://arxiv.org/abs/2204.14016) to higher densities.

---

Initial EoS data was provided by Jonas Keller (j.keller@theorie.ikp.physik.tu-darmstadt.de) over email.
These correspond to MBTA calculations for matter in beta equilibrium at 2 different orders.

  * `data/EMN450_N2LO_MBPT3_beta_equilibrium_eft_bands.dat`
  * `data/EMN450_N3LO_MBPT3_beta_equilibrium_eft_bands.dat`

The upper and lower bounds on pressure and energy density are symmetric about the mean, and so I have additionally extracted these means and converted to "astrophysical units" (CGS) within

  * `data/EMN450_N2LO_MBPT3_beta_equilibrium_eft_bands.csv`
  * `data/EMN450_N3LO_MBPT3_beta_equilibrium_eft_bands.csv`

via

```
./dat2csv *.dat
```

One can then construct simple Gaussian process models to emulate the each EFT calculation's uncertainty via

```
./csv2gp *.csv
```

This executable allows the user to choose a scale parameter and a correlation length parameter that are then built into the estimated covariance kernel.

Finally, one can draw a sample set from each emulator for the auxiliary variable and combine this with an uncertainty on the pressure at a reference density in order to generate a sample set of pressure-baryon density-energy density curves.
These are checked against the original bounds to confirm the emulator behaves as desired.
The relevant executable is `gp2eos`.
