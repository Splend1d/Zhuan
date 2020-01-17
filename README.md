
# 篆來篆去 -- 您的小篆學習器
# Wondering in the universe of ancient chinese characters 
### 網址連結 Website :  [篆來篆去](https://splend1d.github.io/Zhuan/ "您的小篆學習器")
### 作品介紹 Introduction
本作品為一個線上的小篆學習器，不僅提供基本的楷體對應之小篆字體搜尋，亦結合每字部件做出延伸，將含有相似部件之字體列出，讓學習者可一次學習多個相關單字。除此互動式的查詢功能之外，我們亦設計出不同的遊戲學習模式和提示型態，讓學習者能用更有趣的方式認識小篆，使學習不再局限於背誦。
實作部分，以[中研院小學堂小篆資料庫](http://xiaoxue.iis.sinica.edu.tw/xiaozhuan)為資料來源，來實作該網站。首先我們透過Python爬蟲取得中研院小學堂小篆資料庫之楷篆各項重要資料，對應與《說文》之解釋，並將每一個字的部件解析，以構成本作品主要的資料。接著，我們透過互動性網頁設計（HTML、CSS與JavaScript）將資料轉變成多種好玩的遊戲，不只為使用者帶來更好的學習效果，我們更希望透過本作品讓人文資料遊戲化，拉近大家與人文資料的距離，展現多元結合的可能性。

This website is for those who are interested in learning [Small Seal Script](https://en.wikipedia.org/wiki/Small_seal_script) characters. These characters are used in China before the Qin dynasty. The website features a query webpage where you can find small seal script character representations of modern Tranditional Chinese chatacters.It also includes mini-games to assist learning. We also picked the top 2000 most frequent nowadays characters, and listed them for users to learn efficiently.
### 創作動機 Motivation
小篆是由春秋戰國時代的秦國文字演變而來，字形規整勻稱。秦始皇統一六國後，李斯等人整理、統一撰《倉頡》篇，進行「書同文」工作，以當時的秦國小篆作為通用文字，消滅了「文字異形」現象，在漢字發展史上有重要意義。中國文字發展到小篆階段，逐漸定型，文字更加符號化。漢代時，隸書取代小篆成為主要字體，之後小篆主要用來刻印章、銘金石。《說文》是東漢許慎所編的文字工具書，全書分為540個部首、收錄9353字，收錄字體以小篆為主，也收錄古文、籀文，說解著重於本形本義，在文字學、訓詁學中有重要價值。
小篆是研究漢字演變的重要材料，識篆能直接閱讀古文物，獲得第一手資料或看懂新出土的文字資料；篆書線條單純、用筆簡單，用筆以中鋒為主，書法初學者能藉由習寫篆書鍛鍊對空間、線條質感的控制能力，並學習文字知識，因此適合書法初學者。對於設計領域的學生而言，小篆字形規整勻稱，不少店家招牌、商標使用小篆書寫，印章刻印也使用小篆，學習小篆能增加設計作品的人文思考。對普羅大眾而言，識篆、用篆能感受中國文字之美，增進人文素養。
我們觀察現有資源發現，對於中文系學生、考古學、器物學、文字學研究者、習書法者、古文物愛好者及其他欲學習識篆者，小篆的學習資源並不足。我們藉由訪談中文系學生，發現其學習小篆多是使用紙本書籍，藉由摹寫增進記憶，不僅造成查詢困難（欲找尋某一字的篆體，需翻閱大量紙本資料），抄寫背誦小篆部件的學習歷程也枯燥無效率。科技部人文及社科研究發展司人文處中文學門所撰之〈中文學門小學類文字學領域的困境與省思〉（中文學門小學專刊11.3期，2010年6月）也提到「學生抱怨文字學內容乏味，恐怕導因於教師無法廣徵博引，將文字學內容教得活潑有趣。」
因此我們推出「篆來篆去」小篆學習器，希望能改善小篆學習資源不足、學習方式枯燥無效率的現象。我們藉由三種遊戲方式幫助使用者記憶小篆各部件，同時引入許慎《說文解字》之內容，帶領使用者了解文字背後的意義及形成原因，理解與記憶雙管齊下，將達到更佳學習效果。另一方面，我們整合現有的資料庫查詢篆體功能，讓使用者能在線將現代文字轉成小篆。期待「篆來篆去」能成為小篆學習新平台，幫助使用者更有效率、系統地學習小篆、理解文字之美！

Small seal scripts are important materials for exploring the change in Chinese Characters. For calligraphy starters, small seal scripts is a great candidate because of the simplicity of it's strokes. Current difficulties in learning the small seal scripts include relying on hard copy resources, which is inefficient. Online resources developed by Academia Sinica are in the form of a database, and is not designed for systematic studying of the characters. We came to the conclusion that the fun factor can not only encourage people to dive in an unfamiliar field, but also help hardcore learners to learn more efficiently. The various modes provide suitable learning environments for all kinds of learners.

### 網站操作說明 How to use the website : 
已將說明布署於各子網頁之中
Seriously, just visit the website.

### 網頁資料概覽 Implementation detail :
A. 路徑  ./assets/src/get*.py 之檔案：為爬蟲程式，將中研院資料庫轉為pickle檔案存取
1. getbasic.py : 爬取核心資料。蒐集的資訊包含所有部首的集合，以及每一個小篆字體的核心資訊，下面顯示此爬蟲的其中一筆結果。
    >{'meaning': '《說文》：“一，惟初太始，道立於一，造分天地，化成萬物。弌，古文一。”', 'fonts': ['&0.4E00;', '&1.EFB2;', '&27.4E00;', '&27.E000;']}, 2: {'meaning': '《說文》：“元，始也。从一，从兀。”', 'fonts': ['&0.5143;', '&27.5143;']}
2. getfreq.py : 爬取小篆字體中，對應成現代漢字的常用字率的資料。此處常用字字集乃依林樹教授編著之〈中文電腦基本用字表〉所記錄之字頻排序，由高字頻排至低字頻字形。此外，門檻值設為100000時，可獲得所有常用漢字集，是在部件學習模式中所使用。在部件學習模式中，為了避免在隨機生成的題目中，答案只有不常使用的古字，題幹會事先經過篩選，答案內包含夠多的常用字時，才會被納入題目當中。
3. getimg.py (使用前需先執行getbasic.py)：從getbasic.py所獲得的核心資料中，蒐集每一個字元的相片，並建立小篆字型與楷書字型的對照表，對照表的一筆結果如下，分別對應到小篆字形，楷書字形，以及電腦漢字
['27.932E', '0.932E', '錮']
4. gettree.py (使用前需先執行getbasic.py)：從getbasic.py所獲得的核心資料中，蒐集每一個字元的衍生字以及子部件，做法為透過漢字古今資料庫的部件功能，先找出每一個字元的衍生字，就可以反向推衍出子部件。
路徑 ./assets/src/parse*.py之檔案：整理先前所爬取的資料，並將其從pickle檔轉為json檔。
5. parsemain.py : 在主要的資料裡加入部首的資料。
6. parsemajors.py：由於中研院資料庫頁面並沒有部首的資訊，需要由部首查詢來查詢正確的部首，有些字礙於utf-8的限制並無法直接用爬蟲獲得，於是以人工查找的方式補齊每個字的部首資料。
7. parsesubchars.py：中研院資料庫裡有些字元屬於籀文的範疇，因此我們把不將異體字納入資料庫內。此程式可以分出主要的字集異體字集。
8. parsetree.py：整理字的樹狀結構。針對每一個字的子部件以及衍生字進行排序，使得在顯示子部件時，會從部件數目最多的子部件，條列到部件數目最少的子部件，如下圖之結果。衍生字則正好相反，會由子部件數目少的排到子部件數目大的。
9. parsefreq.py：對常見字集進行排序。為了使學習成效更能提升，在關卡處理上，我們希望字在部件上是能夠有連貫性的，例如：「漢」這個字的部件有「水」，則在學習漢這個字之前，應該先學習水。因此，我們採用的演算法如下：
10. more on prase freq 關卡分類演算法
    - 找尋子部件只有自己的小篆單字，令此集合為x。
    - 從我們建立的子部件資料庫中，找出子部件含有x的單字，並將其子部件x暫時去除。
    - 去除後，有些單字的子部件減少，可能有符合步驟1之新的單字產生，重新做步驟1。
    - 此方法理論上可以將所有字元分類，在做完此演算法之後，我們發現有一些字詞仍然無法被分類，原因是有一些部件為彼此互為子部件，導致子部件無法被消除的情況，於是，我們增加了一條規則，來解決這種字元（2000筆中大概有100筆）。
若有字尚未被分類完成，而已經找不到新的基礎單字時，從剩下的字元中，選擇衍生字最多的字元，加到難度序列的下一個值。接著重複步驟1~3。

B. 路徑 ./assets/src/gen*.py之檔案：生成.js檔作為javascript的資料庫

C. 路徑 ./assets/db/之檔案：我們的資料庫

D. 路徑 ./*.html：網站內容
