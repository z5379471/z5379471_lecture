WEEK 1
# Downloads Qantas share price beginning 1 January 2020
import yfinance                                           # (1)
tic = "cba.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('cba_stk_prc.csv')                              # (7)
print(tic)

a= "1"+"2"
print(a)

a=1+2
print(a)
print(type(a))

b=1/2
print(b)
print(type(b))

a=2
b=3*a
print(b)

print(1/2==0.5)

a1 =1
print(a1)

_a=1
print(_a)

a2=6
a2=a2+8
print(a2)
