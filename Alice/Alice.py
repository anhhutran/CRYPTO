from Functions import Encryptor, HashToId, makeKeyFilesAlice, Encrypt, ReadKey, WriteToFiles, get_random_bytes, shutil

# random ra key AES với độ dài khoá là 32 bytes
key = get_random_bytes(32)
enc = Encryptor(key)

def main():
    # Tạo cặp khoá public và private của Alice
    publicKey, privateKey = makeKeyFilesAlice("Cloud/PublicKeyAlice.txt", 512)

    # Hash Doc thành Id 
    id = HashToId("abc.docx")
    print("\n- Quá trình Hash file Document thành ID \n====> Thành công !!!")

    # mã hoá ID doc vừa hash ở trên bằng RSA ( dùng khoá bí mật của Alice để mã hoá ), sau đó lưu vào file
    luuchuoi = Encrypt(id, privateKey[1], privateKey[0])
    WriteToFiles("Cloud/IdDocAlice.txt", luuchuoi)
    print("\n - Quá trình mã hoá ID của Document bằng RSA và lưu vào file Cloud \n====> Thành công !!!")

    # mã hoá file doc bằng AES
    enc.encrypt_file(str("abc.docx"))
    # di chuyển file doc đã mã hoá vào thư mục Cloud
    shutil.move("abc.docx.enc", "Cloud/abc.docx.enc")
    print("\n - Quá trình mã hoá Document bằng AES và lưu vào file Cloud \n====> Thành công !!!")

    # Mã hoá key AES bằng RSA ( dùng khoá công khai của Bob ), sau đó lưu vào file
    PublicKeyBob = ReadKey("Cloud/PublicKeyBob.txt", ' ')
    msg = key.decode("latin-1")
    luuchuoiKeyAES = Encrypt(msg,int(PublicKeyBob[1]),int(PublicKeyBob[0]))
    WriteToFiles("Cloud/AESKey.txt", luuchuoiKeyAES)
    print("\n - Quá trình mã hoá key AES bằng RSA ( dùng khoá công khai của Bob ) và lưu vào file Cloud \n====> Thành công !!!")

main()


