def sezar_sifrele(metin, anahtar):
    sifrelenmis_metin = ""
    for karakter in metin:
        if karakter.isalpha():  # Sadece harfler üzerinde işlem yap
            if karakter.islower():  # Küçük harfler
                yeni_harf = chr((ord(karakter) - ord('a') + anahtar) % 26 + ord('a'))
            elif karakter.isupper():  # Büyük harfler
                yeni_harf = chr((ord(karakter) - ord('A') + anahtar) % 26 + ord('A'))
            sifrelenmis_metin += yeni_harf
        else:
            sifrelenmis_metin += karakter  # Harf olmayan karakterleri olduğu gibi ekle
    return sifrelenmis_metin


def sezar_coz(sifrelenmis_metin, anahtar):
    cozulmus_metin = ""
    for karakter in sifrelenmis_metin:
        if karakter.isalpha():  # Sadece harfler üzerinde işlem yap
            if karakter.islower():  # Küçük harfler
                orijinal_harf = chr((ord(karakter) - ord('a') - anahtar) % 26 + ord('a'))
            elif karakter.isupper():  # Büyük harfler
                orijinal_harf = chr((ord(karakter) - ord('A') - anahtar) % 26 + ord('A'))
            cozulmus_metin += orijinal_harf
        else:
            cozulmus_metin += karakter  # Harf olmayan karakterleri olduğu gibi ekle
    return cozulmus_metin


if __name__ == "__main__":
    metin = input("Metni giriniz: ")
    anahtar = int(input("Anahtarı giriniz: "))

    sifrelenmis_metin = sezar_sifrele(metin, anahtar)
    print("Şifrelenmiş Metin:", sifrelenmis_metin)

    cozulmus_metin = sezar_coz(sifrelenmis_metin, anahtar)
    print("Çözülmüş Metin:", cozulmus_metin)
