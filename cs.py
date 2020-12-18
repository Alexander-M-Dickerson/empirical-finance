def corwin_schultz(df):

    D = pd.DataFrame()
    k = 3 - (2 * np.sqrt(2))
    
    D['H'] = df.high
    D['L'] = df.low
    
    
    D['H_lagged'] = df.high.shift(1)   
    D['L_lagged'] = df.low.shift(1)
    
    D['beta'] = np.log(D.H/D.L)**2 + np.log(D.H_lagged/D.L_lagged)**2
     
    D['minL'] = D[['L','L_lagged']].min(axis = 1)
    D['maxH'] = D[['H','H_lagged']].max(axis = 1)
    D['gamma'] = np.log((D['maxH']/D['minL']))**2
    
    
    D['alpha'] = ( ( np.sqrt(2*D.beta) - np.sqrt(D.beta) ) / (k) ) - np.sqrt( D.gamma/k     )
    
    D['S'] = (2 * (np.exp(D.alpha)-1) ) / (1 + np.exp(D.alpha))
    mask = ( D.S < 0)
    D.S[D.S < 0] = 0
    D['sroll'] = D.S.rolling(21).mean()
    D.S[D.S == 0] = D.sroll
    return(D['S'])
