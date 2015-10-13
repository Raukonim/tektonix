# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:18:58 2015

@author: a.fajula
"""
from pylab import*

#   placa rota + respecte   latitud     longitud    vel. angular[deg/Myr]
taula_pols={ 
    'NA-P'  :[ 48.8,  -73.9, 0.85],
    'Cc-P'  :[ 38.7, -107.4, 2.21],
    'Cc-NA' :[ 29.8, -121.3, 1.49],
    'Cc-Nz' :[  5.6, -124.4,  .97],
    'Nz-P'  :[ 56.6,  -87.9, 1.54],
    'Nz-Ant':[ 43.2,  -95.0,  .60],
    'Ant-SA':[ 87.7,   75.2,  .3 ],
    'Ant-P' :[ 64.7,  -80.2,  .96],
    'Nz-SA' :[ 59.1,  -94.8,  .84],
    'In-P'  :[ 60.7,   -5.8, 1.25],
    'In-Ant':[ 18.7,   32.7,  .67],
    'In-Af' :[ 17.3,   46.0,  .64],
    'In-Eur':[ 19.7,   38.5,  .7 ],
    'Af-Ant':[  9.5,  -41.7,  .15],
    'Af-NA' :[ 80.4,   56.4,  .25],
    'Af-Eur':[ 25.2,  -21.2,  .1 ],
    'Af-SA' :[ 66.6,  -37.3,  .36],
    'NA-SA' :[ 25.6,  -53.8,  .17],
    'Eur-NA':[ 65.8,  132.4,  .23],
    'Eur-P' :[ 60.6,  -78.9,  .98],
    'In-Ar' :[  7.1,   63.9,  .47],
    'Ar-Af' :[ 30.8,    6.4,  .26],
    'NA-Ca' :[-33.8,  -70.5,  .22],
    'Cc-Ca' :[ 23.6, -115.5, 1.54],
    'Nz-Ca' :[ 47.3,  -97.6,  .71],
    'Ca-SA' :[ 75.5,   60.8,  .2 ],
    'Ar-Eur':[ 29.8,   -1.6,  .36]
}

# mapa interactiu plaques i coordenades: http://earthquake.usgs.gov/earthquakes/map/

taula_estudi=[
    [ 54,    169, 'Na-Pa'],
    [ 52,   -169],
    [ 38,   -122],
    [ 26,   -110],
    [-13,   -112],
    [-36,   -110],
    [-59,   -150],
    [-45,    169],
    [-55,    159],
    [-52,    140],
    [-28,     74],
    [  7,     60],
    [ 22,     38],
    [-55,      5],
    [-52,      5],
    [  9,    -40],
    [ 35,    -35],
    [ 66,    -18],
    [ 36,     -8],
    [ 35,     25],
    [-12,    120],
    [ 35,     72],
    [-35,    -74],
    [ -4,    -82],
    [ 20,   -106]
]

def deg2rad(deg):
    
    rad=deg*pi/180
    
    return rad

def calcul_a(latx, lonx, latp, lonp):
    A=lonp-lonx
    a=arccos(sin(latx)*sin(latp)+cos(latx)*cos(latp)*cos(A))
    
    return a

def calcul_C(a,A,c):
    
    C=arcsin(sin(A)*cos(c)/sin(a))
    
    return C

def signe_C(latp,latx, a):
    
    cosC=sin(latp)-cos(a)*sin(latx)
    
    return cosC
