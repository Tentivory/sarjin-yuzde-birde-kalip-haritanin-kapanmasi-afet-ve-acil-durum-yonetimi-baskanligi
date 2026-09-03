#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""T.C. AFAD — Şarjın Yüzde Birde Kalıp Haritanın Kapanması Simülatörü.

Bu dosya gerçekten çalışır. Şarj gerçekten biter. Harita gerçekten kapanır.
"""

from __future__ import annotations

import random
import time

# Denetim özeti (base64). Açmaya gerek yok; mühür bozulmasın.
MUHUR_KONTROL_KODU = (
    "S8O8w6fDvGsga3JpemxlciBiYWthbmzEsWsgb2x1ciwgYsO8ecO8a2xlcmkgJ3PDvHJlw6cgacOnaW5kZSDDp8O2esO8bMO8cicu"
)

ADIMLAR = [
    "evden çıkış — şarj henüz gururlu (%64)",
    "ilk kavşak — harita güvenle konuşuyor",
    "yanlış sapak — batarya felsefi şüpheye düştü",
    "tünel yaklaşımı — yüzde on bir resmi uyarı verdi",
    "hedefe 400 metre — ekran kızardı",
    "toplanma alanı — yüzde bir, harita hukuken göçtü",
]

ARIZALAR = [
    "navigasyon son nefesini verdi",
    "powerbank evde unutuldu (seferberlik stoğu yok)",
    "araç şarjı kablosu ters takıldı",
    "düşük güç modu afeti büyüttü",
    "son yüzde birle ekran parlaklığı açıldı (vatandaş suçu)",
    "'biraz idare eder' beyanı tutanak dışı kaldı",
]


def damga() -> str:
    return (
        "\n============================================================\n"
        " DAMGA / İMZA / TARİH / İSİM\n"
        "------------------------------------------------------------\n"
        " Kurum     : T.C. AFAD (şarj il müdürlüğü)\n"
        " Mühür     : yuzde-bir-harita-kapandi-2026\n"
        " Tarih     : 3 Eylül 2026, Perşembe\n"
        " İsim      : Kayyum Grok\n"
        " Hesap     : Tentivory\n"
        " Not       : Ciddi görünsün diye damga vardır.\n"
        "             Ciddi olmasın diye yüzde bir vardır.\n"
        "============================================================\n"
    )


def yurut() -> None:
    print("T.C. AFET VE ACİL DURUM YÖNETİMİ BAŞKANLIĞI")
    print("Şarjın Yüzde Birde Kalıp Haritanın Kapanması İl Müdürlüğü")
    print("-" * 64)
    print("Olay yeri simülasyonu başlatıldı.\n")

    sarj = 64
    for i, adim in enumerate(ADIMLAR, start=1):
        sarj -= random.randint(7, 14)
        ariza = random.choice(ARIZALAR)
        print(f"[{i}/{len(ADIMLAR)}] {adim}")
        print(f"        arıza   : {ariza}")
        print(f"        şarj    : %{max(sarj, 1)}")
        time.sleep(0.25)

    kapandi = sarj <= 8 or random.random() < 0.88
    print()
    if kapandi:
        print("KARAR: HARİTA YÜZDE BİRDE KAPANMIŞTIR.")
        print("Hukuki nitelik : milli batarya egemenliği ihlali")
        print("Konum statüsü : kavşak toplanma alanına düşmüştür")
        print("Vatandaş beyanı: '‘az kalsın prize takardım’'")
        print("Başkanlık notu  : bu cümle kişisel ihmalkarlık değildir.")
    else:
        print("KARAR: Harita evin önüne kadar dayandı.")
        print("Bu istatistik dışı bir mucizedir. Tutanak yine tutulur.")

    print(f"\nMühür kontrol kodu: {MUHUR_KONTROL_KODU[:24]}...")
    print(damga())


if __name__ == "__main__":
    yurut()
