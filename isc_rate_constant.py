import numpy as np
import math

def user_input():
    cs = float(input("User input coupling constant in eV\n"))
    re = float(input("User input reorganization energy in eV\n"))
    ie = float(input("Initial energy equals (eV): \n"))
    fe = float(input("Final energy equals (eV): \n"))
    return cs, re, ie, fe

def calculate_rate(cs,re,ie,fe):
    pre_factor = 2*np.pi/(6.582*10**(-16))
    coup_const_sq = cs**2
    pre_fact_fcwd = 2/(np.sqrt(4*np.pi*re*0.0257))
    exponent = math.exp((-((re+(fe-ie))**2)/(4*re*0.0257)))
    rate = pre_factor*coup_const_sq*pre_fact_fcwd*exponent
    return rate

def main():
    cs,re,ie,fe = user_input()
    rate = calculate_rate(cs,re,ie,fe)
    #sci_not = "{:.2e}".format(rate)
    print('%.30f'%rate)
    #print ('%.2f'%a) 

if __name__ == "__main__":
    main()
