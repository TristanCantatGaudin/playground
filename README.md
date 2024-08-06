# playground
Miscellaneous scripts and notebooks for data scraping, visualisation, statistics, machine learning.



## Statistics and mathematics

[algebra_fitting_polynomials](/statistics/algebra_fitting_polynomials.ipynb) - ordinary and generalised least squares, with a full matrix of covariance, and covariance on the best-fit result

[algebra_mean_with_correlations](/statistics/algebra_mean_with_correlations.ipynb) - spelled out math to compute the mean (and associated covariance matrix describe its uncertainty) for data with correlated errors

[prior_likelihood_conflict](/statistics/prior_likelihood_conflict.ipynb) - illustration of the combination of Gaussians and t-distributions (as likelihoods, or prior-likelihood), showing the importance of the behaviour of the tails.

[statistical_copulae](/statistics/statistical_copulae.ipynb) - intuitive introduction to empirical copulae as joint cumulative distributions, examples of Gaussian, Student-t, and actual APOGEE data.

[maximum_likelihood_parallax](/statistics/maximum_likelihood_parallax.ipynb) - brute force illustration of estimating the mean and intrinsic dispersion of a 1D distribution of points with individual measurement errors

[gaussian_processes_for_dummies](/statistics/gaussian_processes_for_dummies.ipynb)


## Astronomy

[composite_Gaia_cmd](composite_Gaia_cmd.ipynb) - astroquery for Vizier, twinx and twiny axes, rcParams options

![image](/img/img_cmd.png)

[cube_galaxy_sky](/statistics/cube_galaxy_sky.ipynb) - maximum likelihood, forward modelling using a selection function

[gmm_ngc_2506](gmm_ngc_2506.ipynb) - query Gaia data, use sklearn to fit a GMM to the proper motions, pick cluster members

![image](/img/img_gmm_ngc2506.png)

[gaia_archive_queries](gaia_archive_queries.ipynb) - examples of simple and advanced ADQL queries and programmatic access to the Gaia archive

## Data science and visualisation

Examples using Python libraries for data scraping, cleaning, visualisation, processing.

[geotagged_photos_venezia](geotagged_photos_venezia.ipynb) - FlickrAPI, convert date+time strings to `datetime` objects, get dayofyear, dayofweek etc.

![image](/img/img_venezia.png)

[google_trends](google_trends.ipynb) - use pytrends package to plot search volumes

![image](/img/img_google_trends.png)

[ads_citations_to_gaia_papers](ads_citations_to_gaia_papers.ipynb) - use ADS API and pandas to display monthly citations to *Gaia* data release papers. Updated daily at [this repo](https://github.com/TristanCantatGaudin/ADS-Gaia-Citations) including a [standalone HTML](https://tristancantatgaudin.github.io/ADS-Gaia-Citations/ads-citations-plotly.html) generated with plotly.

![image](https://raw.githubusercontent.com/TristanCantatGaudin/ADS-Gaia-Citations/main/citations_per_month.png)

[hierarchical_clustering_sp500](hierarchical_clustering_sp500.ipynb) - pandas, pct_change, pivot, correlations. scipy, hierarchical clustering, dendrograms. 

[nba_shot_charts_hexbin](/nba/nba_shot_charts_hexbin.ipynb) - manipulate matplotlib `hexbin` plots, tweak bin size and color

![image](/nba/hexbin_shot_charts.png)

[rookies_bball_ref_2024_race](/nba/rookies_bball_ref_2024_race.ipynb) - urllib and BeautifulSoup to get html tags from a table, pandas to read tables from multiple pages

[scrape_all_rookie_stats](/nba/scrape_all_rookie_stats.ipynb) - pandas to read tables, flatten nested columns

[google_trends_eclipse_2024](google_trends_eclipse_2024.ipynb) - plotly chloropleth maps, show export to standalone HTML page (interactive version [HERE](https://tristancantatgaudin.github.io/docs/google_trends_eclipse_2024.html))

<img src="https://github.com/TristanCantatGaudin/playground/blob/main/img/google_trends_eclipse_2024.png?raw=true" width=400 height=280 />


[max_temp_three_cities](max_temp_three_cities.ipynb) - package `meteostat` for historical weather, `cmasher` for the cool colour map, colorbar outside the subplots.

[bar_chart_color_rain.ipynb) - package `meteostat` for historical weather, glow, font, legend.

<img src="https://github.com/TristanCantatGaudin/playground/blob/main/img/rain.png?raw=true" width=600 height=280 />





