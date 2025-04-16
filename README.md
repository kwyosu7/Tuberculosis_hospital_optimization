# Tuberculosis Hospital Optimization

This repository contains the code used in the study **"Consideration of age effect on optimizing hospital distribution to reduce tuberculosis fatalities"**. The code supports the construction of an age-stratified, high-resolution dataset and the optimization of hospital distribution strategies in South Korea.

## Repository Structure

<!-- - `data/`: Raw and processed TB data (2014–2022), including hospital counts and age-stratified fatality proportions.-->
- `scripts/`: Python scripts used for data preprocessing, demographic inference, and optimization.
- `figures/`: Code to reproduce key figures from the manuscript.
- `results/`: Outputs of simulations and optimization routines.

## Key Features

- Reconstructs high-resolution TB data from low-resolution demographic sources.
- Models TB fatality as a function of hospital density.
- Implements optimization framework with an age-weighted objective function.
- Includes figure generation scripts for visualization.

## Requirements

This repository is built using Python 3. The main packages required are:
- `pandas`
- `numpy`
- `matplotlib`
- `scipy`

## License

This repository is released under the MIT License.

## Citation

If you use this code or dataset in your research, please cite the corresponding paper (DOI will be added upon publication).
