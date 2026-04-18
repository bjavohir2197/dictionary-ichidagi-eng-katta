talaba = {
    "ism": "Anvar",
    "yosh": 20,
    "kurs": 3,
    "baholar": [85, 90, 78, 92, 88]
}

print("Talaba ma'lumotlari:")
for kalit, qiymat in talaba.items():
    print(f"  {kalit}: {qiymat}")

print(f"\nO'rtacha baho: {sum(talaba['baholar']) / len(talaba['baholar']):.1f}")
