#def Pressure_from_Height(P, T, R_d = 287, g = 9.8)
     """Provides incremental change in height given an array for Temperature and Pressure
    
        input:
        ------
        
            P = an array of atmospheric pressure [Pa]
            
            T = an array for Temperature [K]
            
            R_d = gas constant for dry air [J/kg/K]
            
            g = gravity [m/s^2]
    
    
        output:
        -------
        
            delta_Z = scalar value of incrimental height between two "layers" of regional climate model
    
    
    """
    
    #delta_Z = (-R_d*T/g)*(lnP-lnP)
    
    #return delta_Z
    
    
    
    Ideal Atmosphere Pressure Example.ipynb
    
    
    
    
    
    
    # plot the graph

fig, ax = PP.subplots()

ax.plot(p/100, z/1000, label = "Version 2")

ax.plot(p_ref/100, z/1000, label = "Version 1")

ax.set_xlabel("Pressure [hPa]")
ax.set_ylabel("Height [km]")

# add a legend
ax.legend(loc = 'best')

# draw the plot
PP.show()