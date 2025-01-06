import pytc

import types

def list_modules(module_name):
    try:
        module = __import__(module_name, globals(), locals(), [module_name.split('.')[-1]])
    except ImportError:
        return
    print(module_name)
    for name in dir(module):
        if type(getattr(module, name)) == types.ModuleType:
            list_modules('.'.join([module_name, name]))
            
list_modules("pytc")

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