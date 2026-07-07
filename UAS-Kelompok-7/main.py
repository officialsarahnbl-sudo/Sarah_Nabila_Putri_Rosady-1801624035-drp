from tampilan_registrasi import sign_up, sign_in, regist, users
from komputasi import tampilkan_komputasi

def header():
    print("====================================================")
    print("============== Wellcome to Miss Me 📑 ==============")
    print("====================================================")   

def main():
    header()
    tampilkan_komputasi (users)

    while True:
        regist()

if __name__ == "__main__":
    main()