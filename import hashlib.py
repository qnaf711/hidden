import hashlib

# الهاش الذي نريد كسره
target_hash = "4ad2320ac856e3e1b0c8bc1379fe0ed23e63a91091812e918812d174bbb03d3b"  # غيّره حسب الحاجة

# مسار wordlist (أو استخدم قائمة داخلية)
wordlist_path = "wordlist.txt"  # ضع مسار ملف القائمة

# اختيار نوع التجزئة، هنا نفترض أنه SHA-1
hash_function = hashlib.sha1

# فتح قائمة الكلمات وتجربة كل كلمة
with open(wordlist_path, "r", encoding="utf-8") as file:
    for word in file:
        word = word.strip()  # إزالة المسافات البيضاء
        hashed_word = hash_function(word.encode()).hexdigest()  # توليد الهاش

        if hashed_word == target_hash:
            print(f"[+] كلمة المرور الصحيحة: {word}")
            break
    else:
        print("[-] لم يتم العثور على تطابق.")
