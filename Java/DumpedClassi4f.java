package Java;

public final class DumpedClassi4f {
    public static char[] a;

    static {
        a = new char[]{'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
    }

    public static String a(String str) {
        String str2;
        String str3;
        int i;
        int i2;
        if (str == null) {
            str2 = "";
        } else {
            str2 = str;
        }
        if (str2 == null) {
            str3 = "";
        } else {
            str3 = str2;
        }
        int[] iArr = new int[(str3.length() * 8)];
        for (i = 0; i < str3.length() * 8; i += 8) {
            i2 = i >> 5;
            iArr[i2] = iArr[i2] | ((str3.charAt(i / 8) & 255) << (24 - (i % 32)));
        }
        i = 0;
        int i3 = 0;
        while (i3 < iArr.length && iArr[i3] != 0) {
            i3++;
            i++;
        }
        int[] iArr2 = new int[i];
        for (i3 = 0; i3 < i; i3++) {
            iArr2[i3] = iArr[i3];
        }
        i3 = str2.length() * 8;
        int i4 = i3 >> 5;
        int[] a = a(iArr2, i4);
        a[i4] = a[i4] | (128 << (24 - (i3 % 32)));
        i4 = (((i3 + 64) >> 9) << 4) + 15;
        int[] a2 = a(a, i4);
        a2[i4] = i3;
        int[] iArr3 = new int[80];
        int i5 = 1732584193;
        i = -271733879;
        int i6 = -1732584194;
        i2 = 271733878;
        i4 = -1009589776;
        for (i3 = 0; i3 < a2.length; i3 += 16) {
            int i7 = 0;
            int i8 = i4;
            int i9 = i;
            int i10 = i5;
            int i11 = i2;
            int i12 = i6;
            while (i7 < 80) {
                if (i7 < 16) {
                    iArr3[i7] = a2[i3 + i7];
                } else {
                    iArr3[i7] = a(((iArr3[i7 - 3] ^ iArr3[i7 - 8]) ^ iArr3[i7 - 14]) ^ iArr3[i7 - 16], 1);
                }
                int a3 = a(i10, 5);
                int i13 = i7 < 20 ? (i9 & i12) | ((i9 ^ -1) & i11) : (i7 < 40 || i7 >= 60) ? (i9 ^ i12) ^ i11 : ((i9 & i12) | (i9 & i11)) | (i12 & i11);
                a3 = b(a3, i13);
                i8 = b(i8, iArr3[i7]);
                i13 = i7 < 20 ? 1518500249 : i7 < 40 ? 1859775393 : i7 < 60 ? -1894007588 : -899497514;
                i8 = b(a3, b(i8, i13));
                i7++;
                int i14 = i11;
                i11 = i12;
                i12 = a(i9, 30);
                i9 = i10;
                i10 = i8;
                i8 = i14;
            }
            i5 = b(i10, i5);
            i = b(i9, i);
            i6 = b(i12, i6);
            i2 = b(i11, i2);
            i4 = b(i8, i4);
        }
        int[] iArr4 = new int[]{i5, i, i6, i2, i4};
        String str4 = "0123456789abcdef";
        str2 = "";
        for (i3 = 0; i3 < iArr4.length * 4; i3++) {
            str2 = str2 + new Character(str4.charAt((iArr4[i3 >> 2] >> (((3 - (i3 % 4)) * 8) + 4)) & 15)).toString() + new Character(str4.charAt((iArr4[i3 >> 2] >> ((3 - (i3 % 4)) * 8)) & 15)).toString();
        }
        return str2;
    }

    private static int a(int i, int i2) {
        return (i << i2) | (i >>> (32 - i2));
    }

    private static int b(int i, int i2) {
        int i3 = (i & 65535) + (i2 & 65535);
        return (i3 & 65535) | ((((i >> 16) + (i2 >> 16)) + (i3 >> 16)) << 16);
    }

    private static int[] a(int[] iArr, int i) {
        int i2 = 0;
        int length = iArr.length;
        if (length >= i + 1) {
            return iArr;
        }
        int[] iArr2 = new int[(i + 1)];
        for (int i3 = 0; i3 < i; i3++) {
            iArr2[i3] = 0;
        }
        while (i2 < length) {
            iArr2[i2] = iArr[i2];
            i2++;
        }
        return iArr2;
    }
}