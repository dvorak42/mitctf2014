#!/usr/bin/python
import base64
import math
import md5
if 64 - 64: i11iIiiIii
OO0o = 16
Oo0Ooo = 256
if 85 - 85: OOO0O0O0ooooo % IIii1I . II1 - O00ooooo00
def I1IiiI ( i , l ) :
 return ( "%%0%dx" % ( 2 * l ) ) % ( i )
 if 27 - 27: iIiiiI1IiI1I1 * IIiIiII11i * IiIIi1I1Iiii - Ooo00oOo00o
def I1IiI ( data ) :
 return md5 . new ( data ) . digest ( )
 if 73 - 73: OOooOOo / ii11ii1ii
def O00ooOO ( k1 , k2 ) :
 I1iII1iiII = chr ( sum ( [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in k1 ] ) % 256 )
 i1i1II = chr ( sum ( [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in k2 ] ) % 256 )
 O0oo0OO0 = chr ( reduce ( lambda I1i1iiI1 , iiIIIII1i1iI : I1i1iiI1 * iiIIIII1i1iI , [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in k1 ] , 1 ) % 256 )
 o0oO0 = chr ( reduce ( lambda I1i1iiI1 , iiIIIII1i1iI : I1i1iiI1 * iiIIIII1i1iI , [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in k2 ] , 1 ) % 256 )
 return I1iII1iiII + i1i1II + O0oo0OO0 + o0oO0
 if 100 - 100: i11Ii11I1Ii1i
def Ooo ( a , b ) :
 o0oOoO00o = [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in a ]
 i1 = [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in b ]
 oOOoo00O0O = [ o0oOoO00o [ iI1Ii11111iIi % len ( o0oOoO00o ) ] ^ i1 [ iI1Ii11111iIi % len ( i1 ) ] for iI1Ii11111iIi in range ( max ( len ( o0oOoO00o ) , len ( i1 ) ) ) ]
 return '' . join ( [ chr ( iI1Ii11111iIi ) for iI1Ii11111iIi in oOOoo00O0O ] )
 if 15 - 15: I11iii11IIi
def O00o0o0000o0o ( k1 , k2 ) :
 O0Oo = I1IiI ( k1 + ":" + k2 )
 while len ( O0Oo ) < OO0o :
  O0Oo += I1IiI ( O0Oo )
 return O0Oo [ : OO0o ]
 if 80 - 80: i1iII1I1i1i1 . i1iIIII
def I1 ( pwd , additional = "" ) :
 O0OoOoo00o = pwd
 iiiI11 = additional
 OOooO = int ( math . ceil ( 1.0 * Oo0Ooo / OO0o ) )
 OOoO00o = ""
 for II111iiii in range ( OOooO ) :
  II = I1IiiI ( II111iiii , 4 )
  OOoO00o = OOoO00o + I1IiI ( O0OoOoo00o + II + iiiI11 )
 return OOoO00o [ : Oo0Ooo ]
 if 63 - 63: ii11iIi1I % iI111I11I1I1
def OOooO0OOoo ( pwd , additional = "" ) :
 O0OoOoo00o = pwd
 iiiI11 = additional
 OOooO = int ( math . ceil ( 1.0 * Oo0Ooo / OO0o ) )
 OOoO00o = ""
 for II111iiii in range ( 1 , OOooO + 1 ) :
  II = I1IiiI ( II111iiii , 4 )
  OOoO00o = OOoO00o + I1IiI ( O0OoOoo00o + II + iiiI11 )
 return OOoO00o [ : Oo0Ooo ]
 if 29 - 29: o00o / IiI1I1
def OoO000 ( pwd , additional = "" , pAmt = 4 ) :
 O0OoOoo00o = pwd
 iiiI11 = additional
 OOooO = int ( math . ceil ( 1.0 * Oo0Ooo / OO0o ) )
 OOoO00o = ""
 for II111iiii in range ( OOooO ) :
  II = I1IiiI ( II111iiii , pAmt )
  OOoO00o = OOoO00o + I1IiI ( II + O0OoOoo00o + iiiI11 )
 return OOoO00o [ : Oo0Ooo ]
 if 42 - 42: oOoO - Ooo00oOo00o % OOooOOo . I11iii11IIi . i11iIiiIii
def IIiI ( p , salt , c = 16 ) :
 if Oo0Ooo > OO0o :
  return "kLen is too long"
 OOoO00o = I1IiI ( p + salt )
 for iI1Ii11111iIi in range ( 2 , c + 1 ) :
  OOoO00o = I1IiI ( OOoO00o )
 return OOoO00o [ : Oo0Ooo ]
 if 22 - 22: IiIIi1I1Iiii % ii11iIi1I
def oo ( p , salt , c = 16 ) :
 if Oo0Ooo > OO0o :
  return "kLen is too long"
 OOoO00o = I1IiI ( p + salt )
 for iI1Ii11111iIi in range ( 2 , c + 1 ) :
  OOoO00o = I1IiI ( OOoO00o + p + salt )
 return OOoO00o [ : Oo0Ooo ]
 if 54 - 54: i1iII1I1i1i1 + i1iII1I1i1i1 % IiI1I1 % i11iIiiIii / IIii1I . i1iII1I1i1i1
def o0oO0o00oo ( p , salt , c = 16 ) :
 OOooO = int ( math . ceil ( 1.0 * Oo0Ooo / OO0o ) )
 OOoO00o = ""
 for iI1Ii11111iIi in range ( 1 , OOooO + 1 ) :
  II1i1Ii11Ii11 = iII11i = O00o0o0000o0o ( p , salt + I1IiiI ( iI1Ii11111iIi , 4 ) )
  for O0O00o0OOO0 in range ( 2 , c + 1 ) :
   iII11i = O00o0o0000o0o ( p , iII11i )
   II1i1Ii11Ii11 = Ooo ( II1i1Ii11Ii11 , iII11i )
  OOoO00o = OOoO00o + II1i1Ii11Ii11
 return OOoO00o [ : Oo0Ooo ]
 if 27 - 27: OOO0O0O0ooooo % O00ooooo00 * I11iii11IIi + i11iIiiIii + II1 * O00ooooo00
o0oo0o0O00OO = [
 I1 ,
 OOooO0OOoo ,
 OoO000 ,
 IIiI ,
 oo ,
 o0oO0o00oo
 ]
if 80 - 80: O00ooooo00
def oOOO0o0o ( u , p ) :
 iiI1 = O00ooOO ( u , p )
 i11Iiii = u + ':' + p
 for iI in o0oo0o0O00OO :
  i11Iiii = iI ( i11Iiii , iiI1 )
 return [ ord ( iI1Ii11111iIi ) for iI1Ii11111iIi in i11Iiii ]
 if 28 - 28: i1iII1I1i1i1 - o00o . o00o + OOooOOo - II1 + OOO0O0O0ooooo
 if 95 - 95: Ooo00oOo00o % I11iii11IIi . OOO0O0O0ooooo
def encrypt ( u , p , msg ) :
 oOO00oOO = oOOO0o0o ( u , p )
 OoOo = [ ]
 for iI1Ii11111iIi in range ( len ( msg ) ) :
  OoOo . append ( chr ( ord ( msg [ iI1Ii11111iIi ] ) ^ oOO00oOO [ iI1Ii11111iIi % len ( oOO00oOO ) ] ) )
 return ( u , base64 . b64encode ( '' . join ( OoOo ) ) )
 if 18 - 18: i11iIiiIii
 if 46 - 46: O00ooooo00 / i1iIIII % i1iII1I1i1i1 + IiI1I1
def decrypt ( u , p , cipherb64 ) :
 OoOo = base64 . b64decode ( cipherb64 )
 oOO00oOO = oOOO0o0o ( u , p )
 Iii111II = [ ]
 for iI1Ii11111iIi in range ( len ( OoOo ) ) :
  Iii111II . append ( chr ( ord ( OoOo [ iI1Ii11111iIi ] ) ^ oOO00oOO [ iI1Ii11111iIi % len ( oOO00oOO ) ] ) )
 return '' . join ( Iii111II )
 if 9 - 9: Ooo00oOo00o
 if 33 - 33: oOoO . iI111I11I1I1
 if 58 - 58: i1iII1I1i1i1 * i11iIiiIii / OOooOOo % IiI1I1 - i11Ii11I1Ii1i / I11iii11IIi

print encrypt(???, ???, ???)
# ('probe@mantle.earth', 'wPgJLjpNTkhOFPGFTsnVtAt7Z9Te4ZuBHHIR1kP8YtD+ilQESws=')
