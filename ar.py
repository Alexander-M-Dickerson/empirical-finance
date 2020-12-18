def abdi_ranaldo(df):
    
    # Initialisation of constants
    D = pd.DataFrame()
       
    D['H'] = df.high
    D['L'] = df.low
    D['C'] = df.close
    
    D['H_lagged'] = df.high.shift(1)   
    D['L_lagged'] = df.low.shift(1)
        
    D['n_lagged']  =  (np.log(D['H_lagged']) + np.log(D['L_lagged']))/2
    D['n_forward'] =  (np.log(D['H']) + np.log(D['L']))/2
    
    D['S'] = 4*(np.log(D['C']) - D['n_lagged'])*(np.log(D['C']) - D['n_forward'])
    
    mask = ( D.S < 0)
    D.S[D.S < 0] = 0
    D['sroll'] = D.S.rolling(21).mean()
    D.S[D.S == 0] = D.sroll
    D['S'] = np.sqrt(D['S'])
    
    return( D['S'] )
