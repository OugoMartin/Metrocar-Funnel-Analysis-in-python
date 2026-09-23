# Metrocar Funnel Analysis in Python

A product-analytics case study for measuring user progression through a ride-booking funnel and identifying where users drop out.

## Business question
How effectively do users move from opening the app to completing a ride, and which stage represents the largest loss in the funnel?

## Funnel
The Python script defines four stages:
1. `app_opened`
2. `ride_requested`
3. `driver_assigned`
4. `ride_completed`

It calculates stage counts, stage-to-stage conversion rates, drop-off rates, overall completion, identifies the largest drop, creates funnel visualizations, and exports a metrics summary.

## Primary artifact
- `Metrocar Funnel Analysis in python.py` — analysis script.

## Expected input
The script expects `metrocar_funnel_analysis_query.csv`, which is not currently committed to this repository. Because the source data is absent, this README does not claim numerical conversion results.

## Important correction
The previous README described an unrelated A/B test with 52,314 users and claimed that Variant B significantly outperformed Variant A. Those claims were not supported by the Metrocar script in this repository and have been removed.

## Reproducibility issue
The script currently imports `matplotlib as plt` before using `plt.figure()`; it later imports `matplotlib.pyplot as plt`. Move the pyplot import to the top before plotting when the source is next revised. The funnel-count calculation should also be validated against the actual input schema because `df.notnull().sum()` counts every dataframe column, not only the four declared funnel stages.

## Next improvements
Commit or document access to the source dataset, validate one user/event definition per funnel stage, add segment analysis, save charts to an `outputs/` directory, and add tests for funnel calculations.

## Skills demonstrated
Python · pandas · Product Analytics · Funnel Analysis · Conversion Analysis · Data Visualization

## Author
Martin Ngare
