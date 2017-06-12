# 讀取txt-班上成績 #

## 說明 ##


現在我們有某公館國中班上的數學<b>期中考</b>與<b>期末考</b>的成績檔案<br>
請讀取：<br>
1.期中考： <code>../app/MathScoreMid01.txt</code> <br>
2.期末考： <code>../app/MathScoreFinal01.txt</code> <br>

要求：<br>
1.找到每個人的平均<br>
2.找到成績不滿60分的同學<br>
3.找到期末考退步最多的學生，並列印出來<br>

<br>
ID:學生編號<br>
score:考試成績<br>
<br>

## Input Format ##

輸入兩個字串表示下列兩個檔案的名字。例如 MathScoreMid01.txt ， MathScoreFinal01.txt 。<br>
1.期中考成績.txt<br>
2.期末考成績.txt<br>
所有資料都是ID由小而大排好了。<br>

## Output Format ##

1.找到每個人的平均<br>
2.找到成績不滿60分的同學<br>
3.找到期末考退步最多的學生(不一定只有一位)<br>

## Sample Input 1 ##
```
MathScoreMid01.txt
MathScoreFinal01.txt

```

## Sample Output 1 ##
```
[Mean]
s1: 54.0
s2: 65.5
s3: 61.5
s4: 93.0
s5: 35.5
s6: 55.0
s7: 56.0
s8: 88.0
s9: 41.5
s10: 50.0
s11: 70.5
s12: 48.5
s13: 57.0
s14: 61.5
s15: 98.5
s16: 56.0
s17: 54.0
s18: 46.5
s19: 65.0
s20: 73.5
Fail: s1 & s5 & s6 & s7 & s9 & s10 & s12 & s13 & s16 & s17 & s18
BackWard: s17
```

## Hint ##

```

```
