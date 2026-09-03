# T.C. Afet ve Acil Durum Yönetimi Başkanlığı
## Şarjın Yüzde Birde Kalıp Haritanın Kapanması İl Müdürlüğü

**GENELGE 2026/AFAD-001**  
**Konu:** Milli batarya egemenliğinin yüzde birde fiilen çökmesi, navigasyon protokolünün kopması ve vatandaşın kavşakta kendi afetini ilan etmesi.

Bu yazılım şaka değildir. Şaka olsa harita kapanmaz, vatandaş evini bulurdu.

---

## 1. Teşhis

Vatandaş yoldadır. Şarj yüzde bire iner. Harita kapanır. Bu olay:

- resmi afettir,
- milli batarya egemenliği ihlalidir,
- acil durum protokolü sapmasıdır,
- kurtarma koordinatlarının karanlığa düşmesidir.

“Az kalsın prize takardım” cümlesi kişisel ihmalkarlık **değil**, olay yeri tutanağıdır.

## 2. Kurumsal Mimari

| Nesne | Resmi karşılık |
|---|---|
| Yüzde 1 | Kırmızı alarm |
| Harita | Afet koordinat sistemi |
| Şarj aleti | Kurtarma ekibi |
| Powerbank | Seferberlik stoğu |
| Kavşak | Toplanma alanı |
| Karanlık ekran | İletişim kesintisi |
| “Biraz idare eder” | Yanlış iyimserlik bülteni |

## 3. Kurulum

```bash
python3 baskanlik.py
```

Bağımlılık yoktur. Yüzde bir zaten yeterince bağımlıdır.

## 4. Çalışma Şekli

Program bir yolculuğu simüle eder. Mesafe hedefe indikçe batarya düşer. Yüzde birde harita kapanma ihtimali bilimsel olarak **neredeyse kanun** seviyesindedir.

Çıktıda:

- batarya sağlık raporu,
- harita kesinti tutanağı,
- kavşak toplanma alanı kaydı,
- resmi mühür

görülür.

## 5. Yasal Uyarı

Bu depo AFAD’ın gerçek bir birimi değildir. Gerçek birim olsa yüzde birde harita kapanmaz, jeneratör açılırdı.

Şarjı yüzde yirminin altına düşürmeyiniz. Düşüren vatandaş kendi afetini ilan etmiş sayılır.

## 6. Katkı

Pull request açmadan önce telefonunuzun şarjını ölçünüz. Yüzde birin altındaysa bu bir commit değil, acil durum çağrısıdır.

---

```
============================================================
 DAMGA / İMZA / TARİH / İSİM
------------------------------------------------------------
 Kurum     : T.C. Afet ve Acil Durum Yönetimi Başkanlığı (hayali müdürlük)
 Mühür     : yuzde-bir-harita-kapandi-2026
 Tarih     : 3 Eylül 2026, Perşembe
 İsim      : Kayyum Grok
 Hesap     : Tentivory
 Not       : Ciddi görünsün diye damga vardır.
             Ciddi olmasın diye yüzde bir vardır.
============================================================
```
