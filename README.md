# Interest-Rate-Derivative-Pricing-with-Finite-Differences

This project provides a framework for pricing interest rate derivatives using finite difference methods. It implements various short-rate models and pricing engines for common derivatives.

# Project Structure

-   .vscode/: VS Code specific settings.

-   data/: Sample market data, yield curves, etc.

-   src/: Main source code.

    -   __init__.py: Makes the src directory a Python package.

    -   models/: Interest rate models (Vasicek, CIR, etc.).

    -   pricers/: Finite difference pricing engines for various derivatives.

    -   utils/: Helper functions for data loading, grid creation, etc.

    -   main.py: Main script to run pricing simulations.

-   tests/: Unit and integration tests.

-   requirements.txt: Lists project dependencies.

# Getting Started

## Clone the repository:

git clone <repository_url>
cd interest-rate-derivative-pricing

## Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install dependencies:

pip install -r requirements.txt

## Run a simulation:

python src/main.py

# Usage
-   Modify data/yield_curve.csv to use your own market data.

-   Configure the pricing parameters in src/main.py.

-   Explore the notebooks directory for examples and visualizations.