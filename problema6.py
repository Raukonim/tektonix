# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 14:18:58 2015

@author: a.fajula
"""
from pylab import*

#   placa rota + respecte   latitud     longitud    vel. angular[deg/Myr]
taula_pols=[ 
    [ 48.8,  -73.9, 0.85],  #0'NA-P'
    [ 38.7, -107.4, 2.21],  #1'Cc-P'
    [ 29.8, -121.3, 1.49],  #2'Cc-NA'
    [  5.6, -124.4,  .97],  #3'Cc-Nz'
    [ 56.6,  -87.9, 1.54],  #4'Nz-P'
    [ 43.2,  -95.0,  .60],  #5'Nz-Ant'
    [ 87.7,   75.2,  .3 ],  #6'Ant-SA'
    [ 64.7,  -80.2,  .96],  #7'Ant-P'
    [ 59.1,  -94.8,  .84],  #8'Nz-SA'
    [ 60.7,   -5.8, 1.25],  #9'In-P'
    [ 18.7,   32.7,  .67],  #10'In-Ant'
    [ 17.3,   46.0,  .64],  #11'In-Af'
    [ 19.7,   38.5,  .7 ],  #12'In-Eur'
    [  9.5,  -41.7,  .15],  #13'Af-Ant'
    [ 80.4,   56.4,  .25],  #14'Af-NA'
    [ 25.2,  -21.2,  .1 ],  #15'Af-Eur'
    [ 66.6,  -37.3,  .36],  #16'Af-SA'
    [ 25.6,  -53.8,  .17],  #17'NA-SA'
    [ 65.8,  132.4,  .23],  #18'Eur-NA'
    [ 60.6,  -78.9,  .98],  #19'Eur-P'
    [  7.1,   63.9,  .47],  #21'In-Ar'
    [ 30.8,    6.4,  .26],  #21'Ar-Af'
    [-33.8,  -70.5,  .22],  #22'NA-Ca'
    [ 23.6, -115.5, 1.54],  #23'Cc-Ca'
    [ 47.3,  -97.6,  .71],  #24'Nz-Ca'
    [ 75.5,   60.8,  .2 ],  #25'Ca-SA'
    [ 29.8,   -1.6,  .36]   #26'Ar-Eur'
]

# mapa interactiu plaques i coordenades: http://earthquake.usgs.gov/earthquakes/map/

taula_estudi=array([
    [ 54,    169,  0],
    [ 52,   -169,  0],
    [ 38,   -122,  0],
    [ 26,   -110,  0],
    [-13,   -112,  4],
    [-36,   -110,  0],
    [-59,   -150,  7],
    [-45,    169,  9],
    [-55,    159,  9],
    [-52,    140, 10],
    [-28,     74, 10],
    [  7,     60, 11],
    [ 22,     38, 21],
    [-55,      5, 13],
    [-52,      5, 13],
    [  9,    -40, 16],
    [ 35,    -35, 14],
    [ 66,    -18, 18],
    [ 36,     -8, 15],
    [ 35,     25, 15],
    [-12,    120, 12],
    [ 35,     72, 12],
    [-35,    -74,  8],
    [ -4,    -82,  3],
    [ 20,   -106,  2]
])

def deg2rad(deg):
    #rad=zeros(shape(deg))
    
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
# convertim les dades dels pols a radians i rad/Myr
dades_pol_punt=zeros((25,3))
for i in range(25):    
    dades_pol_punt[i,:]=taula_pols[taula_estudi[i,2]]

taula_final=zeros((25,19))
taula_final[:,0]=taula_estudi[:,0]                  #latitud
taula_final[:,1]=deg2rad(taula_final[:,0])          #latitud rad
taula_final[:,2]=taula_estudi[:,1]                  #longitud
taula_final[:,3]=deg2rad(taula_final[:,2])          #longitud rad
taula_final[:,4]=taula_estudi[:,2]                  #plaques
taula_final[:,5]=dades_pol_punt[:,0]                #latitud pol
taula_final[:,6]=deg2rad(taula_final[:,5])          #latitud pol rad
taula_final[:,7]=dades_pol_punt[:,1]                #longitud pol
taula_final[:,8]=deg2rad(taula_final[:,7])          #longitud pol rad
taula_final[:,9]=dades_pol_punt[:,2]                #longitud pol
taula_final[:,10]=deg2rad(taula_final[:,9])         #longitud pol rad
#coordenades a
taula_final[:,11]=0
taula_final[:,12]=0
taula_final[:,13]=0
taula_final[:,14]=0
taula_final[:,15]=0
taula_final[:,16]=0
taula_final[:,17]=0
taula_final[:,18]=0