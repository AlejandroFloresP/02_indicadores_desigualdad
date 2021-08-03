# Script de python dedicado a crear las funciones necesarias para trabajar con la encuesta ENIGH

import pandas as pd
from pandas._libs.lib import is_integer
import numpy as np

def enigh(grupo,year):
    '''Funcion que genera un dataframe con los microdatos de la encuesta ENIGH
    Toma como argumentos el grupo de datos y el año que necesitemos'''
    
    url ='https://www.inegi.org.mx/contenidos/programas/enigh/nc/'+year+'/microdatos/enigh'+year+'_ns_'+grupo +'_csv.zip'
    df = pd.read_csv(url)
    
    return df

def weighted_qcut(values, weights, q, **kwargs):
    'Return weighted quantile cuts from a given series, values.'
    if is_integer(q):
        quantiles = np.linspace(0, 1, q + 1)
    else:
        quantiles = q
    order = weights.iloc[values.argsort()].cumsum()
    bins = pd.cut(order / order.iloc[-1], quantiles, **kwargs)
    
    return bins.sort_index()

# def gini()