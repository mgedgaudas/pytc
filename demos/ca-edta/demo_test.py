import pytc

# Load in integrated heats from an ITC experiment
e = pytc.ITCExperiment("./tris-01.DH",pytc.indiv_models.SingleSite)

# Create the global fitter, add the experiment, and fit
g = pytc.GlobalFit()
g.add_experiment(e)
g.fit()

# Print the results out
g.plot()
g.corner_plot()
print(g.fit_as_csv)