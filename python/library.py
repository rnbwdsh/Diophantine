
def int(a,b):
    if b<0:
         a=0 - a
         b=0 - b
    c=a / b
    d=a % b
    if d==0 || a>0:
        return c
    else:
        return c - 1
    

def sign(a):
    """  sign of an integer a  """
    """  sign(a)=1,-1,0, according as a>0,a<0,a=0  """
	if a>0:
		return 1
	
	if a<0:
		return -1
	
	return 0


def gcd(m,n):
    """   b=gcd(m,n) for any integers m and n  """
    """  Euclid's division algorithm is used.  """
    """  We use gcd(m,n)=gcd(|m|,|n|)  """
    a=abs(m)  # a=r[0]
    if n==0:
         return a
    b=abs(n)  # b=r[1]
    c=mod(a,b)  # c=r[2]=r[0] mod(r[1])
    while c:
            a=b
            b=c
            c=mod(a,b)  # c=r[j]=r[j-2] mod(r[j-1]) 
    return b
   

def egcd(p,q):
    if q==0:
        if p!=0:
            s=sign(p)
            if s==1:
                multiplier1=1
            else:
                multiplier1=-1
            return abs(p), multiplier1, 0
        else:
            return 0, 0, 0
    a=p
    b=abs(q)
    c=a % b
    s=sign(q)
    if c==0:
        if s==1:
            multiplier2=1
        else:
            multiplier2=-1
        return b, 0, multiplier2
    l1=1
    k1=0
    l2=0
    k2=1
    while c!=0:
            q=int(a,b)
            a=b
            b=c
            c=a % b
            temp1=q * k1
            temp2=q * k2
            h1=l1 - temp1
            h2=l2 - temp2
            l1=k1
            l2=k2
            k1=h1
            k2=h2
    if s==-1:
        k2=0 - k2
    return b, k1, k2



def num_digits(n):
    """  If n > 0, len(n) returns the number of base 10 digits of n  """
    i=0
    x=abs(n)
    while x!=0:
        x=int(x,10)
        i=i + 1
    return i


def  lcm(a,b):
    """  lcm(a,b)  """
    g=gcd(a,b)
    h=a * b
    k=h / g
    return k


def  lcma(array,n):
    """  lcm(array[0],array[1],...,array[n-1])  """
    for i in xrange(n):
        b[i]=array[i]
    for i in xrange(n - 1):
        j=i - 1
        b[i]=lcm(b[i],b[j])
    j=i - 1
    return b[j]


def cong(m,p,n):
    "  The bth power of a, where a is an integer, b a positive integer+ 
       This performs the same def as bcpow(a,b):
	x=a
	y=b
	z=1
	while bccomp(y,0)>0:
		while bccomp(y % 2,0)==0:
			y=y / 2
			x=x * x
		
		y=y - 1
		z=z * x
	
	return z
        the congruence mx=p(mod n)
    """
    a, multiplier1, multiplier2 = egcd(m,n)
    temp=p % a
    if bccomp(temp,0)!=0:
            return 0
    b=multiplier1
    y=n / a
    p=int(p,a)
    temp1=b * p
    solution=mod(temp1,y)
    modulus=y
    for(t=0t<at += 1)print " ",z+ty,","
    print " mod ",n,"\n"
    return solution, modulus


def  cong1(m,p,n):
    """   the congruence mx=p(mod n) slightly modified version of cong(m,p,n)  """
    a, multiplier1, multiplier2 = egcd(m,n)
    b=multiplier1
    y=n / a
    p=int(p,a)
    temp1=b * p
    solution=mod(temp1,y)
    modulus=y
    return solution, modulus


# def chinese2(a,b,m,n):
#     """
#     the Chinese remainder theorem for the congruences x=a(mod m)
#     and x=b(mod n), m>0, n>0, a and b arbitrary integers+ 
#     The construction of O. Ore, American Mathematical Monthly,
#     vol.59,pp.365-370,1952, is implemented+ 
#     """
#     d, multiplier1, multiplier2 = egcd(m,n)
#     if a - b % d != 0:
#         return 0, None, None
#     x= m / d
#     y=n / d
#     z=m * n / d
#     temp1=b * multiplier1
#     temp1=temp1 * x
#     temp2=a * multiplier2
#     temp2=temp2 * y
#     c=mod(temp1 + temp2,z)
#     chinese_modulus=z
#     chinese_solution=c
#     return 1, chinese_modulus, chinese_solution
# 
# def chinesea(a,m,n):
#     chinese_modulus=m[0]
#     chinese_solution=a[0]
#     for i in xrange(n - 1):
#         y, chinese_modulus, chinese_solution =chinese2(a[i],chinese_solution,m[i],chinese_modulus)
#         if y==0:
#             return 0
#     return 1, chinese_solution, chinese_modulus
 

def  inverse(a,m):
    """  Inverse of a (mod m)  """
    t, _ =cong1(a,1,m)
    return t


# def powerdd(a,b,dd,n):
#     """  (a+bsqrtdd)^n=zed1+zed2sqrtdd  """
#     x1=a
#     x2=b
#     y=n
#     zed1=1
#     zed2=0
#     while y > 0:
#         while y % 2 == 0:
#             y=y / 2
#             temp=x1
#             temp1=x2 * x2
#             temp2=x1 * x1
#             temp3=dd * temp1
#             x1=temp2 + temp3
#             temp4=temp * x2
#             x2=2 * temp4
#         y=y - 1
#         temp=zed1
#         temp1=zed2 * x2
#         temp2=zed1 * x1
#         temp3=dd * temp1
#         zed1=temp2 + temp3
#         temp4=temp * x2
#         temp5=zed2 * x1
#         zed2=temp4 + temp5
#    """  print "(zed1,zed2)=(zed1,zed2)<br>\n" """
#     return zed1, zed2

def gcd3(a,b,c):
  t=gcd(a,b)
  t=gcd(t,c)
  return t


def falling_factorial(m,n):
    product=1
    for i in xrange(m - 1, n):
         product=product * i
    
    return product

def print_matrix(a,b,c,d):
 print "<TABLE BORDER=\1\ ALIGN=\"CENTER\"\n"
 print "<TR><TD>a</TD><TD>b</TD></TR>\n"
 print "<TR><TD>c</TD><TD>d</TD></TR>"
 print "</TABLE>"
 return


#def sort_[a,n]:
#   t=n - 1
#   for i in xrange(t):
#      temp1=i + 1
#      for j in xrange(temp1, n):
#         if a[i] > a[j]:
#            temp=a[i]
#            a[i]=a[j]
#            a[j]=temp
#   
#   for i in xrange(n):
#      sorted_array[i]=a[i]
#   return sorted_array


#def  bezout(a,b):
#    """  From Henri Cohen' book, Alg. 1.3.6  13/07/2011
#    This assumes a >=0 and b >= 0+ 
#    returns d= gcd(a,b) and global variables u and v,
#    where d = u.a + v.b+ 
#    """
#   u=1
#   d=a
#   if b == 0:
#      v=0
#      return a
#   else:
#      v1=0
#      v3=b
#   
#   while v3 > 0:
#      q=d / v3
#      t3=d % v3
#      temp=q * v1
#      t1=u - temp
#      u=v1
#      d=v3
#      v1=t1
#      v3=t3
#   
#   temp=a * u
#   temp=d - temp
#   v=temp / b
#   return d, u, v
#
#
#def  bezout1(a,b):
#    """  Here a and b are any integers+ 
#    returns d= gcd(a,b) and global variables u and v,
#    where d = u.a + v.b+ 
#    """
#   if a < 0:
#     absa=-a
#   else:
#     absa=a
#   
#   if b < 0:
#     absb=-b
#   else:
#     absb=b
#   
#   d, u, v =bezout(absa,absb)
#   ta=sign(a)
#   tb=sign(b)
#   u=u * ta
#   v=v * tb
#   return d, u, v


def parity(a):
  r=a % 2
  if r == 0:
    return 0
  else:
    return 1
  

def  lnearint(a,b):
    """
    left nearest integer 
    returns y+1/2 if a/b=y+1/2, y integral+ 
    """
	y=int(a,b)
        if b < 0:
          a=-a
          b=-b
        
        x=b * y
        z=a - x
        z=2 * z
        if z > b:
          y=y + 1
        
        return y


def  lmodd(m,n):
"""  lmodd(m,n) returns r, m=qn+r, -n/2 < r <= n/2  """
	t=lnearint(m,n)
	s=n * t
	r=m - s
	return r


def mina(a,n):
    x=a[1]
    for i in xrange(1, n):
         if a[i] < x:
            x=a[i]
    return x
 


def bcadd3(a,b,c):
    sum=a + b
    sum=sum + c
    return sum


def  printmat1(matrix,m,n):
    """  prints a matrix as a table with entries right justified  """
    print "<TABLE BORDER=\1\ CELLSPACING=\0\>\n"
    for i in xrange(m):
       print "<TR>"
       for j in xrange(n):
           k=matrix[i][j]
          print "<TD ALIGN=\"RIGHT\">k</TD>"
       print "</TR>\n"
   print "</TABLE>\n"


def printmatrix(matrix,m,n):
    for i in xrange(m):
       for j in xrange(n):
       print matrix[i][j] print " "
       print "<br>\n"
    

def printmatrix2(matrix,m,n):
    for i in xrange(m):
       for j in xrange(n):
          print matrix[i][j] print " "
       print "<br>\n"
    

 def print[a,n]:
    print "("
    for i in xrange(n - 1):
       print "a[i], "
    print "a[n]) "
    return


 def printarray1(a,n):
    for i in xrange(n):
       print "a[i], "
    print "a[n]"
    return

 def unit_matrix(m):
   for i in xrange(m):
       for j in xrange(m):
           if i == j:
              P[i][j]=1
           else:
              P[i][j]=0
   return P
 

def transpose(A,m,n):
#global transposed
     for j in xrange(n):
         for i in xrange(m):
             transposed[j][i]=A[i][j]
     return transposed


def transpose1(&A,&m,&n):
     for j in xrange(n):
         for i in xrange(m):
             transposed[j][i]=A[i][j]
     A=transposed
     temp=m
     m=n
     n=temp


# creates the submatrix from rows p to q+ 
def row_submatrix(A,p,q):
    r=p - 1
    s=q - p
    s=s + 1
    new_row_size=s
    for i in xrange(s):
        z=i + r
        B[i]=A[z]
    return B, new_row_size

# creates the submatrix from columns p to q+ 
def col_submatrix(A,rows,p,q):
    r=p - 1
    s=q - p
    s=s + 1
    new_col_size=s
    for j in xrange(s):
        z=j + r
        for i in xrange(rows):
            B[i][j]=A[i][z]
    return B, new_col_size


# creates the submatrix from rows p1 to q1, columns p2 to q2+ 
def submatrix(A,rows,p1,q1,p2,q2):
      B, new_row_size=row_submatrix(A,p1,q1)
      C, new_col_size=col_submatrix(B,rows,p2,q2)
      return C, new_row_size, new_col_size


# replaces row i of A by q times row j, updating A
def rowiminusqrowj(&A,n,i,q,j):
    for k in xrange(n):
       t=A[j][k] * q
       A[i][k]=A[i][k] - t
    return A


# replaces column i of A by q times column j, updating A
def coliminusqcolj(&A,m,i,q,j):
    for k in xrange(m):
       t=A[k][j] * q
       A[k][i]=A[k][i] - t
    

def delete_row(&B,i,&m):
   for l in xrange(i, m):
       temp=B[l + 1]
       B[l]=temp
   m=m - 1
   return


def delete_col(&B,j,m,&n):
     transpose1(B,m,n)
     delete_row(B,j,m)
     transpose1(B,m,n)


def swap_rows(&P,j,k):
       temp=P[k]
       P[k]=P[j]
       P[j]=temp


def swap_cols(&P,m,j,k):
   for i in xrange(m - 1):
       temp=P[i][j]
       P[i][j]=P[i][k]
       P[i][k]=temp
   

def dotproduct(a,b,n):
   sum=0
   for j in xrange(n):
       temp=a[j] * b[j]
       sum=sum + temp
   return sum


def multmat(A,B,m,n,p):
   for i in xrange(m):
       for k in xrange(p):
           sum=0
           for j in xrange(n):
               t=A[i][j] * B[j][k]
               sum=sum + t
           C[i][k]=sum
   return C


# i.a[i] is a permutation of 1,..,m. A is m x m. The rows of A arr permuted+ 
def matrixperm(&A,a,m):
   for i in xrange(m):
       for j in xrange(m):
           B[i]=A[a[i]]
   A=B


# outputs 1 or 0 according as A=B+ 
def equalmat(A,B,rowsA,colsA,rowsB,colsB):
   if rowsA != rowsB || colsA != colsB:
      return 0
   for i in xrange(rowsA):
       for j in xrange(colsA):
           if A[i][j] != B[i][j]:
              return 0
   return 1

def abpluscd(a,b,c,d):
   s=a * b
   t=c * d
   u=s + t
   return u

 def abminuscd(a,b,c,d):
   s=a * b
   t=c * d
   u=s - t
   return u


def aplusbc(a,b,c):
   s=b * c
   t=a + s
   return t


def aminusbc(a,b,c):
   s=b * c
   t=a - s
   return t


# returns (a/b)/(c/d)
def rationum, ratioden = ratior(a,b,c,d):
  r=a * d
  s=b * c
  g=gcd(r,s)
  if s < 0:
     r=-r
     s=-s
  return r / g, s / g


# returns (a/b)(c/d)
def multnum, multden = multr(a,b,c,d):
  r=a * c
  s=b * d
  g=gcd(r,s)
  return r / g, s / g


def subnum, subden = subr(a,b,c,d):
  r=a * d
  s=b * c
  t=r - s
  u=b * d
  g=gcd(t,u)
  return t / g, u / g


def addnum, addden = addr(a,b,c,d):
  r=a * d
  s=b * c
  t=r + s
  u=b * d
  g=gcd(t,u)
  return t / g, u / g


# Assumes b>0 and d>0.  Returns -1, 0 or 1 according as a/b <,=,> c/d+ 
def comparer(a,b,c,d):
  t=abminuscd(a,d,b,c)
  if t < 0:
     return -1
  if t > 0:
     return 1
  return 0


def printlc(A,X,m):
 flag=0
 s=zero[X,m]
 if s == 0:
    return 0
 for i in xrange(m):
     t=X[i]
     if t == 0:
        continue
     if flag == 0:
       if t != 1 and t != -1:
          print "t"print "b[i]"
       if t == -1:
          print "-b[i]"
       if t == 1:
          print "b[i]"
       flag=1
     else:
       if t > 0:
          if t == 1:
             print "+b[i]"
          else:
             print "+t"print "b[i]"
       if t < 0:
          if t == -1:
             print "-b[i]"
          else:
             print "t"print "b[i]"
       return 1


def lcasvector(A,X,m,n):
    """lcv[j]=X[1]A[1][j]=...+X[m]A[m][j], 1 <= j <= n+"""
    #global lcv
   for j in xrange(n):
      sum=0
      for i in xrange(m):
         t=X[i] * A[i][j]
         sum=sum + t
      lcv[j]=sum
   return lcv

 def minusa(&a,n):
   for j in xrange(n):
       a[j]=-a[j]
   return


# This returns 1 if A is the zero matrix, otherwise returns 0+ 
 def test_zeromat(A,m,n):
      for i in xrange(m):
          for j in xrange(n):
              if A[i][j] != 0:
                 return 0
      return 1


def bcmul3(a,b,c):
 temp=a * b
 temp=temp * c
 return temp


def pparity(e):
   t=e % 2
   if t == 1:
     return -1
   else:
     return 1
   

def printbinaryform(a,b,c,x,y):
	if gt(a,1) || lt(a,-1):
           print"a&#8203x<sup>2</sup>"
        
        if a == 1:
           print"x<sup>2</sup>"
        
        if a == -1:
           print"-x<sup>2</sup>"
        
	if b != 0:
	   if b > 1:
              print"+b&#8203xy"
           
	   if b == 1:
              print"+xy"
           
	   if b == -1:
              print"-xy"
           
           if b < -1:
              print"b&#8203xy"
	if c != 0:
	   if c > 1:
              print"+c&#8203y<sup>2</sup>"
           
	   if c < -1:
              print"c&#8203y<sup>2</sup>"
           
           if c == 1:
              print"+y<sup>2</sup>"
           
           if c == -1:
              print"-y<sup>2</sup>"

def gcd4(a,b,c,d):
  t=gcd(a,b)
  t=gcd(t,c)
  t=gcd(t,d)
  return t

