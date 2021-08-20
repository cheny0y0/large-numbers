long double hyper(long double m, unsigned long n, long double r)
{
    if ( n == 1 )
    {
        return m + r ;
    }
    else if ( n == 2 )
    {
        return m * r ;
    }
    else
    {
        long double res ;
        res = 1.0 ;
        for ( unsigned long i = 0; i < r; i++ )
        {
            res = hyper(m, n-1, res) ;
        } ;
        return res ;
    } ;
} ;
