

####################################################################################################################################
####################################################################################################################################


# To do:  Check to see if a column is unique (i.e. index) and recreate with unique < maybe use sample without replacement?>

#def __init__(self, plugin=TrivialPlugin, verbose=True):
#    self.verbose = verbose
#    self.seed = 10293510
#    self.plugin = plugin
#    self.synthesis_methods = ('Trivial', 'KDE', 'DataSynthesizer')

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#from KungFauxPandas import *

def faux_read_sql( sql, con, plugin=TrivialPlugin, index_col=None, coerce_float=True, params=None, parse_dates=None, columns=None, chunksize=None):
    

    import pandas as pd
    
    self.sql = sql
    self.con = con
    self.df_in = pd.read_sql(sql, con, index_col, coerce_float, params, parse_dates, columns, chunksize)
    self.df_out = self.plugin.fauxify(self.df_in)

    return self.df_out

####################################################################################################################################