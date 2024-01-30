# playground
Miscellaneous scripts and notebooks for data scraping, visualisation, statistics, machine learning.



## Statistics and mathematics

[algebra_fitting_polynomials](/statistics/algebra_fitting_polynomials.ipynb) - ordinary and generalised least squares, with a full matrix of covariance, and covariance on the best-fit result

[algebra_mean_with_correlations](/statistics/algebra_mean_with_correlations.ipynb) - spelled out math to compute the mean (and associated covariance matrix describe its uncertainty) for data with correlated errors

[prior_likelihood_conflict](/statistics/prior_likelihood_conflict.ipynb) - illustration of the combination of Gaussians and t-distributions (as likelihoods, or prior-likelihood), showing the importance of the behaviour of the tails.

[statistical_copulae](/statistics/statistical_copulae.ipynb) - intuitive introduction to empirical copulae as joint cumulative distributions, examples of Gaussian, Student-t, and actual APOGEE data.

## Astronomy

[cube_galaxy_sky](/statistics/cube_galaxy_sky.ipynb) - maximum likelihood, forward modelling using a selection function

[gmm_ngc_2506](/statistics/gmm_ngc_2506.ipynb) - query Gaia data, use sklearn to fit a GMM to the proper motions, pick cluster members

[gaia_archive_queries](/statistics/gaia_archive_queries.ipynb) - examples of simple and advanced ADQL queries and programmatic access to the Gaia archive

## Data science

Examples using Python libraries for data scraping, cleaning, visualisation, processing.

[geotagged_photos_venezia](geotagged_photos_venezia.ipynb) - FlickrAPI, convert date+time strings to `datetime` objects, get dayofyear, dayofweek etc.

[ads_citations_to_gaia_papers](ads_citations_to_gaia_papers.ipynb) - use ADS API and pandas to display monthly citations to *Gaia* data release papers

[hierarchical_clustering_sp500](hierarchical_clustering_sp500.ipynb) - pandas, pct_change, pivot, correlations. scipy, hierarchical clustering, dendrograms. 

[rookies_bball_ref_2024_race](/nba/rookies_bball_ref_2024_race.ipynb) - urllib and BeautifulSoup to get html tags from a table, pandas to read tables from multiple pages

[scrape_all_rookie_stats](/nba/scrape_all_rookie_stats.ipynb) - pandas to read tables, flatten nested columns





