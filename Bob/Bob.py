from Functions import Encryptor, HashToId, makeKeyFilesBob, Decrypt, ReadKey, shutil

def main():
    # đầu tiên Bob tạo ra cặp khoá công khai và bí mật, sau đó gửi khoá công khai cho Alice
    #makeKeyFilesBob("Cloud\PublicKeyBob.txt","PrivateKeyBob.txt", 512)

    # đọc file AESKey.txt của Alice gửi sau đó dùng khoá bí mật của Bob để giải mã
    AESKey = ReadKey("Cloud/AESKey.txt",' ')
    privateKey = ReadKey("PrivateKeyBob.txt",' ')
    AESKeyDecrypt = Decrypt(AESKey, int(privateKey[1]), int(privateKey[0])).encode("latin-1")

    # sau đó dùng khoá AES vừa giải mã được cho vào class Encryptor để giải mã file abc.docx.enc
    enc = Encryptor(AESKeyDecrypt)
    shutil.move("Cloud/abc.docx.enc", "abc.docx.enc")
    enc.decrypt_file(str("abc.docx.enc"))

    # sau khi giải mã file docx ra thì dùng hàm hash để hash ID của file doc vừa giải mã ra id'
    IdDocBob = HashToId("abc.docx")

    # đọc file khoá công khai và id doc ( đã mã hoá ) được gửi từ Alice
    publicKeyAlice = ReadKey("Cloud/PublicKeyAlice.txt",' ')
    IdDocAlice = ReadKey("Cloud/IdDocAlice.txt",' ')

    # rồi dùng khoá công khai của Alice để giải mã Id doc vừa đọc được
    IdDocAlice = Decrypt(IdDocAlice, int(publicKeyAlice[1]), int(publicKeyAlice[0]))

    # cuối cùng so sánh Id' mà Bob hash ra so với Id Doc ( của Alice ) vừa giải mã ra để so sánh, nếu bằng nhau thì file Doc đúng
    print("------------------------------------------------------------------------------------------------------------------------\nId Of Doc Alice: ",IdDocAlice)
    print("Id Of Doc Bob: ",IdDocBob)
    if (IdDocBob == IdDocAlice):
        print("------------------------------------------------------------------------------------------------------------------------\n====> Bằng nhau")
        print("====> File Document này nguyên gốc")
main()