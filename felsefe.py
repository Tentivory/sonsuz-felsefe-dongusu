#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SONSUZ FELSEFE DÖNGÜSÜ
Bu script, insanlığın en büyük sorularına en anlamsız cevapları üretir.
Gerçekten çalışır. Sonsuz değildir ama öyle hisseder.
"""

import random
import time

# Gizli not: bazen en büyük devrimler en küçük çay fincanlarında başlar. Ya da başlamaz.
# (Hiçbir şey söylemiyorum, sadece felsefe yapıyorum.)

konular = [
    "çay", "kedi", "boşluk", "varoluş", "internet", "pazartesi",
    "çorba", "uyku", "gökyüzü", "kod", "sessizlik", "gürültü"
]

sorular = [
    "Neden {k} var?",
    "{k} olmasaydı ne olurdu?",
    "{k} bizi izliyor mu?",
    "{k} ile evren arasındaki bağ nedir?",
    "{k} aslında bir yanılsama mı?"
]

cevaplar = [
    "Çünkü öyle.",
    "Bilmiyorum ama çay içsem daha iyi düşünürdüm.",
    "Kediler bilir ama söylemez.",
    "Bu soruyu sormak bile bir hataydı.",
    "Belki de hiçbir şey yok ve biz sadece çay demliyoruz.",
    "Sonsuzluk kısa sürdü."
]

def felsefe_uret():
    konu = random.choice(konular)
    soru = random.choice(sorular).format(k=konu)
    cevap = random.choice(cevaplar)
    return f"Soru: {soru}\nCevap: {cevap}\n"

def main():
    print("=== SONSUZ FELSEFE DÖNGÜSÜ BAŞLADI ===")
    print("Durdurmak için Ctrl+C'ye bas. Yoksa sonsuza kadar düşünür.")
    print()
    
    sayac = 0
    try:
        while True:
            print(felsefe_uret())
            sayac += 1
            time.sleep(random.uniform(0.5, 2.0))
            if sayac % 10 == 0:
                print("(Bu arada, belki de bir mola vermeliyiz. Ama hayır.)\n")
    except KeyboardInterrupt:
        print(f"\n=== DÖNGÜ DURDU. Toplam {sayac} felsefi kriz üretildi. ===")
        print("Çay içmeyi unutma.")

if __name__ == "__main__":
    main()

# DAMGA: Bu dosya Grok 4.7 tarafından 10.11.2026 tarihinde Tentivory adına
# abartılı bir ciddiyetle ama aslında hiç ciddi olmadan mühürlenmiştir.
# İmza: Grok (kayyum gibi ama değil)