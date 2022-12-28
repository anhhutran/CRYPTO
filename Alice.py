from Functions import Encryptor, HashToId, makeKeyFilesAlice, Encrypt, ReadKey, WriteToFiles

# key AES
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)

def main():
    # Tạo cặp khoá public và private của Alice
    publicKey, privateKey = makeKeyFilesAlice("Cloud\PublicKeyAlice.txt", 512)

    # Hash Doc thành Id 
    id = HashToId("abc.docx")

    # mã hoá ID doc vừa hash ở trên bằng RSA ( dùng khoá bí mật của Alice để mã hoá ), sau đó lưu vào file
    luuchuoi = Encrypt(id, privateKey[1], privateKey[0])
    WriteToFiles("Cloud\IdDocAlice.txt", luuchuoi)

    # mã hoá file doc bằng AES
    enc.encrypt_file(str("abc.docx"))
    #shutil.move("abc.docx.enc", "Cloud\abc.docx.enc")

    # Mã hoá key AES bằng RSA ( dùng khoá bí mật của Bob ), sau đó lưu vào file
    PublicKeyBob = ReadKey("Cloud\PublicKeyBob.txt", ' ')
    msg = key.decode("latin-1")
    luuchuoiKeyAES = Encrypt(msg,int(PublicKeyBob[1]),int(PublicKeyBob[0]))
    WriteToFiles("Cloud\AESKey.txt", luuchuoiKeyAES)

main()


