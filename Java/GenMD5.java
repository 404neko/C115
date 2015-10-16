package Java;

import java.io.UnsupportedEncodingException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public final class GenMD5 {
    public static String a(String str) {
        return a(str, "md5");
    }

    private static String a(String str, String str2) {
        if (str == null) {
            throw new IllegalArgumentException("\u8bf7\u8f93\u5165\u8981\u52a0\u5bc6\u7684\u5185\u5bb9");
        }
        if (str2 == null || "".equals(str2.trim())) {
            str2 = "md5";
        }
        try {
            MessageDigest instance = MessageDigest.getInstance(str2);
            instance.update(str.getBytes("UTF8"));
            return a(instance.digest());
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
            return null;
        } catch (UnsupportedEncodingException e2) {
            e2.printStackTrace();
            return null;
        }
    }

    private static String a(byte[] bArr) {
        StringBuffer stringBuffer = new StringBuffer();
        for (byte b : bArr) {
            stringBuffer.append(Integer.toHexString((b & 255) | 256).substring(1, 3));
        }
        return stringBuffer.toString();
    }
}