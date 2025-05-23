import jpype
from konlpy.tag import Okt
from konlpy import jvm
from Korpora import Korpora
import os
import konlpy

# jvm_path = r"C:\Program Files\Java\jdk-11.0.0.2\bin\server\jvm.dll"
# jar_path = r"C:\Users\admin\AppData\Local\Programs\Python\Python313\Lib\site-packages\konlpy\java\open-korean-text-2.1.0.jar"

# if not jpype.isJVMStarted():
#     jpype.startJVM(jvm_path, "-Djava.class.path="+ jar_path ,convertStrings=True)

# 정확한 경로들
jvm_path = r"C:\Program Files\Java\jdk-11.0.0.2\bin\server\jvm.dll"
jar_path = r"C:\Users\admin\AppData\Local\Programs\Python\Python38\lib\site-packages\konlpy\java\open-korean-text-2.1.0.jar"

# JVM 시작 (JAR 포함 classpath 설정)r
if not jpype.isJVMStarted():
    jpype.startJVM(jvm_path, f"-Djava.class.path={jar_path}", convertStrings=True)


tokenizer_ = Okt()
corpus = Korpora.load("korean_petitions")
dataset = corpus.train

nouns_set_ = set()

for data_ in dataset:
    text_ = data_.text.strip()
    nouns_ = tokenizer_.nouns(text_)
    for noun_ in nouns_:
        if len(noun_) >= 2:
            nouns_set_.add(noun_)

with open("words.txt", "w", encoding="utf-8") as f:
    for noun_ in sorted(nouns_set_):
        f.write(noun_ + "\n")

print("✅ words.txt에", len(nouns_set_), "개의 단어가 저장되었습니다.")
