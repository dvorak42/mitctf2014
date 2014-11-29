
for i17 in range(256):
    for i43 in range(256):
        i00 = ord('t')
        i01 = ord('e')
        i02 = ord('s')
        i03 = ord('s')
        i04 = ord('e')
        i05 = ord('r')
        i06 = ord('a')
        i07 = ord('c')
        i08 = ord('t')
        i09 = ord('2')
        i10 = ord('0')
        i11 = ord('1')
        i12 = ord('4')
        i13 = ord('{')
        i46 = ord('}')
        i45 = i01 + i02 - i00
        i44 = i02 + i04 - i03
        i39 = i08 + i45 - i44
        i30 = i39 + i44 - i45
        i42 = i44 + i46 - i43
        i41 = i43 + i44 - i42
        i40 = i42 + i45 - i46
        i39 = i42 + i46 - i43
        i38 = i40 + i42 - i43
        i37 = i41 + i42 - i43
        i36 = i39 + i45 - i37
        i35 = i40 + i44 - i38
        i34 = i38 + i42 - i36
        i33 = i39 + i45 - i37
        i32 = i35 + i38 - i40
        i31 = i33 + i44 - i35
        i29 = i30 + i34 - i31
        i28 = i30 + i32 - i42
        i27 = i30 + i31 - i28
        i26 = i39 + i45 - i37
        i25 = i28 + i29 - i43
        i24 = i39 + i41 - i27
        i23 = i40 + i45 - i34
        i22 = i35 + i45 - i37
        i21 = i24 + i45 - i22
        i20 = i22 + i25 - i40
        i19 = i29 + i42 - i38
        i18 = i28 + i35 - i31
        i16 = i28 + i37 - i45
        i15 = i17 + i35 - i24
        i14 = i34 + i37 - i32
        valid = (i13 == i19 + i28 - i45) and (i12 == i25 + i40 - i37) and (i11 == i12 + i32 - i31) and (i10 == i11 + i42 - i28) and (i04 == i35 + i44 - i41)
        m = ""
        for i in range(47):
            v  = eval('i%02d' % i)
            if v >= 256 or v < 0:
                valid = False
                break
            m += chr(v)
        if valid:
            print m
